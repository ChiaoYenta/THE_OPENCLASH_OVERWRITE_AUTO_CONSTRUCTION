#!/usr/bin/env python3
"""
YAML Processor - 处理和精简 YAML 配置文件
支持本地和外部配置的统一管理
"""

import yaml
import re
import json
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Any, Set, Optional


class YAMLProcessor:
    """YAML 配置处理器"""
    
    # OpenClash 运行所需的关键键
    KEEP_KEYS = {
        'proxy-providers',
        'proxy-groups', 
        'rule-providers',
        'rules'
    }

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.anchors = {}

    def extract_anchors(self, content: str) -> Dict[str, str]:
        """提取 YAML 锚点定义"""
        anchors = {}
        pattern = r'^(\s*)&(\w+)\s+(.+)$'
        
        for line in content.split('\n'):
            match = re.match(pattern, line)
            if match:
                indent, name, value = match.groups()
                anchors[name] = f"{indent}&{name} {value}"
        return anchors

    def find_referenced_anchors(self, content: Any) -> Set[str]:
        """查找内容中引用的锚点"""
        text = yaml.dump(content, allow_unicode=True)
        return set(re.findall(r'\*(\w+)', text))

    def strip_config(self, yaml_path: Path) -> Optional[Dict]:
        """精简 YAML 配置"""
        self.logger.info(f"Processing: {yaml_path}")
        
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                raw_content = f.read()
            
            self.anchors = self.extract_anchors(raw_content)
            config = yaml.safe_load(raw_content)
            
            if not config:
                return None

            # 只保留必要键
            stripped = {k: config[k] for k in self.KEEP_KEYS if k in config}
            
            if not stripped:
                self.logger.warning(f"No valid keys in {yaml_path}")
                return None

            # 处理锚点
            referenced = self.find_referenced_anchors(stripped)
            if referenced:
                stripped['_anchors'] = {
                    name: self.anchors[name]
                    for name in referenced if name in self.anchors
                }

            # 添加元数据
            stripped['_meta'] = {
                'source': str(yaml_path),
                'proxy_providers_count': len(stripped.get('proxy-providers', {})),
                'rule_providers_count': len(stripped.get('rule-providers', {}))
            }
            
            return stripped
            
        except Exception as e:
            self.logger.error(f"Error processing {yaml_path}: {e}")
            return None

    def save_config(self, config: Dict, output_path: Path):
        """保存配置"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 分离元数据和配置
        meta = config.pop('_meta', {})
        anchors = config.pop('_anchors', {})
        
        # 写入锚点
        lines = []
        if anchors:
            lines.extend([
                "# ============================================================================",
                "# Anchors Definition",
                "# ============================================================================"
            ])
            for name in sorted(anchors.keys()):
                lines.append(anchors[name])
            lines.append("")
        
        # 写入配置
        yaml_content = yaml.dump(
            config, 
            default_flow_style=False, 
            allow_unicode=True,
            sort_keys=False
        )
        
        with open(output_path, 'w', encoding='utf-8') as f:
            if lines:
                f.write('\n'.join(lines) + '\n')
            f.write(yaml_content)
        
        self.logger.info(f"Saved: {output_path}")

    def process_directory(self, input_dir: Path, output_dir: Path, 
                         recursive: bool = False) -> List[Dict]:
        """处理目录"""
        results = []
        pattern = '**/*.yaml' if recursive else '*.yaml'
        
        for yaml_file in input_dir.glob(pattern):
            if yaml_file.is_file():
                rel_path = yaml_file.relative_to(input_dir)
                output_file = output_dir / rel_path
                
                config = self.strip_config(yaml_file)
                if config:
                    self.save_config(config, output_file)
                    results.append({
                        'input': str(yaml_file),
                        'output': str(output_file),
                        'meta': config.get('_meta', {})
                    })
        
        return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=Path, required=True)
    parser.add_argument('--output', '-o', type=Path, required=True)
    parser.add_argument('--strip', action='store_true', help='Strip unnecessary keys')
    parser.add_argument('--recursive', '-r', action='store_true')
    parser.add_argument('--verbose', '-v', action='store_true')
    
    args = parser.parse_args()
    
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    processor = YAMLProcessor()
    results = processor.process_directory(args.input, args.output, args.recursive)
    
    print(f"\n✅ Processed {len(results)} files")
    return 0


if __name__ == '__main__':
    exit(main())
