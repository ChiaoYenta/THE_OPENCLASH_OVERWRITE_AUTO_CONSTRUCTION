#!/usr/bin/env python3
"""
YAML Stripper - 提取並精簡 Mihomo YAML 配置文件
只保留: rule-providers, rules, proxy-groups, proxy-providers 和锚点
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List, Any, Set
import logging


class YAMLStripper:
    """YAML 配置精簡處理器"""

    # 需要保留的頂級鍵
    KEEP_KEYS = {
        'proxy-providers',
        'proxy-groups',
        'rule-providers',
        'rules'
    }

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.anchors = {}  # 存儲提取的锚點

    def extract_anchors(self, yaml_content: str) -> Dict[str, str]:
        """
        提取 YAML 文件中的锚點定義
        """
        anchors = {}
        anchor_pattern = r'^(\s*)&(\w+)\s*(.+)$'

        for line in yaml_content.split('\n'):
            match = re.match(anchor_pattern, line)
            if match:
                indent, anchor_name, content = match.groups()
                anchors[anchor_name] = f"{indent}&{anchor_name} {content}"
                self.logger.debug(f"Found anchor: {anchor_name}")

        return anchors

    def find_referenced_anchors(self, content: Dict) -> Set[str]:
        """
        查找被引用的锚點
        """
        referenced = set()
        content_str = yaml.dump(content)

        ref_pattern = r'\*(\w+)'
        matches = re.findall(ref_pattern, content_str)

        referenced.update(matches)
        return referenced

    def strip_yaml(self, yaml_path: Path) -> Dict[str, Any]:
        """
        精簡 YAML 文件，只保留必要部分
        """
        self.logger.info(f"Processing: {yaml_path.name}")

        with open(yaml_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()

        # 提取锚點
        self.anchors = self.extract_anchors(raw_content)

        # 解析 YAML
        try:
            full_config = yaml.safe_load(raw_content)
        except yaml.YAMLError as e:
            self.logger.error(f"Failed to parse YAML: {e}")
            return {}

        # 只保留指定鍵
        stripped_config = {}
        for key in self.KEEP_KEYS:
            if key in full_config:
                stripped_config[key] = full_config[key]

        # 查找被引用的锚點
        referenced_anchors = self.find_referenced_anchors(stripped_config)

        # 保存被引用的锚點
        stripped_config['_anchors'] = {
            name: self.anchors[name]
            for name in referenced_anchors
            if name in self.anchors
        }

        return stripped_config

    def count_providers(self, config: Dict) -> Dict[str, int]:
        """
        統計 provider 數量
        """
        counts = {
            'proxy_providers': len(config.get('proxy-providers', {})),
            'rule_providers': len(config.get('rule-providers', {})),
            'proxy_groups': len(config.get('proxy-groups', [])),
            'rules': len(config.get('rules', []))
        }
        return counts

    def save_stripped_yaml(self, config: Dict, output_path: Path,
                           include_anchors: bool = True) -> None:
        """
        保存精簡後的 YAML 文件
        """
        save_config = {k: v for k, v in config.items() if k != '_anchors'}

        yaml_content = yaml.dump(
            save_config,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False
        )

        if include_anchors and '_anchors' in config:
            anchor_lines = [
                "# ============================================================================",
                "# 锚點定義 (Anchors)",
                "# ============================================================================"
            ]
            anchor_lines.extend(config['_anchors'].values())
            anchor_lines.append("")

            yaml_content = '\n'.join(anchor_lines) + '\n' + yaml_content

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(yaml_content)

        self.logger.info(f"Saved stripped YAML to: {output_path}")

    def process_directory(self, input_dir: Path, output_dir: Path) -> List[Dict]:
        """
        批量處理目錄中的所有 YAML 文件
        """
        results = []
        output_dir.mkdir(parents=True, exist_ok=True)

        for yaml_file in input_dir.glob('*.yaml'):
            try:
                stripped_config = self.strip_yaml(yaml_file)

                if not stripped_config:
                    self.logger.warning(f"Skipped empty config: {yaml_file.name}")
                    continue

                counts = self.count_providers(stripped_config)

                output_file = output_dir / yaml_file.name
                self.save_stripped_yaml(stripped_config, output_file)

                results.append({
                    'filename': yaml_file.name,
                    'counts': counts,
                    'output': str(output_file)
                })

            except Exception as e:
                self.logger.error(f"Failed to process {yaml_file.name}: {e}")

        return results


def setup_logging(level=logging.INFO):
    """設置日誌"""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Strip Mihomo YAML configs')
    parser.add_argument('input_dir', type=Path, help='Input directory')
    parser.add.add_argument('output_dir', type=Path, help='Output directory')
    parser.add_argument('--verbose', action='store_true', help='Verbose logging')

    args = parser.parse_args()

    setup_logging(logging.DEBUG if args.verbose else logging.INFO)

    stripper = YAMLStripper()
    results = stripper.process_directory(args.input_dir, args.output_dir)

    print("\n" + "=" * 60)
    print("Processing Results")
    print("=" * 60)

    for result in results:
        print(f"\n📄 {result['filename']}")
        print(f"   Proxy Providers: {result['counts']['proxy_providers']}")
        print(f"   Rule Providers: {result['counts']['rule_providers']}")
        print(f"   Proxy Groups: {result['counts']['proxy_groups']}")
        print(f"   Rules: {result['counts']['rules']}")

    print(f"\n✅ Total processed: {len(results)} files")
