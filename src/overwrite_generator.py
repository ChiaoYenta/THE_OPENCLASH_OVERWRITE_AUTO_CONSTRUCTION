#!/usr/bin/env python3
"""
OpenClash Overwrite Generator - 按来源分类存储版本
Fixed Version with improvements
"""
import yaml
import json
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from jinja2 import Environment, FileSystemLoader


class OverwriteGenerator:
    def __init__(self, template_dir: Path, config_types_path: Path):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )
        self.logger = logging.getLogger(__name__)
        
        with open(config_types_path, 'r') as f:
            self.config_types = json.load(f)['config_types']

    def analyze_yaml(self, yaml_path: Path) -> Optional[Dict]:
        """分析 YAML 文件"""
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            if not config:
                return None
            
            proxy_providers = config.get('proxy-providers', {}) or {}
            providers = []
            
            for name, cfg in proxy_providers.items():
                if isinstance(cfg, dict):
                    providers.append({
                        'name': name,
                        'type': cfg.get('type', 'http'),
                        'url': cfg.get('url', ''),
                        'interval': cfg.get('interval', 86400)
                    })
            
            return {
                'proxy_providers': providers,
                'count': len(providers),
                'name': yaml_path.stem
            }
        
        except Exception as e:
            self.logger.error(f"Error analyzing {yaml_path}: {e}")
            return None

    def generate_readme(self, category_dir: Path, category_name: str, 
                       source_type: str, files_generated: List[str]):
        """为每个分类目录生成 README"""
        
        # 根据来源确定说明文字
        if source_type == 'external':
            if 'General_Config' in category_name:
                source_desc = "HenryChiao/mihomo_yamls/THEYAMLS/General_Config"
                purpose = "通用配置，适合大多数使用场景"
            elif 'Smart_Mode' in category_name:
                source_desc = "HenryChiao/mihomo_yamls/THEYAMLS/Smart_Mode"
                purpose = "Smart 智能模式专用配置，自动选择最优节点"
            else:
                source_desc = f"HenryChiao/mihomo_yamls/THEYAMLS/{category_name}"
                purpose = "外部同步配置"
        else:
            source_desc = f"本地目录 cleaner_config/{category_name}"
            purpose = "用户自定义配置"
        
        readme_content = f"""# {category_name} 覆写配置

## 📍 来源
- **路径**: `{source_desc}`
- **类型**: {'外部自动同步' if source_type == 'external' else '本地手动维护'}
- **用途**: {purpose}

## 📁 文件说明

本目录包含以下 9 种配置变体：

| 文件名 | 模式 | IPv6 | LGBM | 适用场景 |
|--------|------|------|------|----------|
| `Overwrite-*.conf` | 标准 | ✅ | ❌ | 主路由，启用 IPv6 |
| `Overwrite-noipv6-*.conf` | 标准 | ❌ | ❌ | 主路由，禁用 IPv6 |
| `Overwrite-bypass-*.conf` | 标准 | ❌ | ❌ | **旁路由**，需 EN_DNS |
| `Overwrite-smart-*.conf` | Smart | ✅ | ❌ | Smart 模式，启用 IPv6 |
| `Overwrite-smart-noipv6-*.conf` | Smart | ❌ | ❌ | Smart 模式，禁用 IPv6 |
| `Overwrite-smart-LGBM-*.conf` | Smart | ✅ | ✅ | Smart + LGBM 模型 |
| `Overwrite-smart-noipv6-LGBM-*.conf` | Smart | ❌ | ✅ | Smart + LGBM，无 IPv6 |
| `Overwrite-smart-bypass-*.conf` | Smart | ❌ | ❌ | **Smart 旁路由**，需 EN_DNS |
| `Overwrite-smart-bypass-LGBM-*.conf` | Smart | ❌ | ✅ | **Smart 旁路由 + LGBM**，需 EN_DNS |

## 🔧 环境变量

### 基础变量（所有配置）
```bash
EN_KEY=你的订阅链接

# 或（多 provider 时）
EN_KEY1=订阅1;EN_KEY2=订阅2;...
```

### 旁路由额外变量（bypass 系列）
```bash
EN_DNS=223.5.5.5,114.114.114.114
```

## 📝 生成信息
- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 配置文件数: {len(files_generated)}
- 原始 YAML: {category_name}

---
*由 GitHub Actions 自动生成*
"""
        
        readme_path = category_dir / 'README.md'
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        self.logger.info(f"Generated README: {readme_path}")

    def generate_overwrite(self, yaml_path: Path, output_path: Path, 
                          config_def: Dict, repo_url: str, category: str, 
                          source_type: str) -> bool:
        """生成单个覆写文件"""
        
        analysis = self.analyze_yaml(yaml_path)
        if not analysis or analysis['count'] == 0:
            self.logger.warning(f"No providers in {yaml_path}, skipping")
            return False
        
        # 构建下载URL（保持分类结构）- 确保使用正斜杠
        yaml_url = f"{repo_url}/processed_configs/{source_type}/{category}/{yaml_path.name}".replace('\\', '/')
        
        try:
            template = self.env.get_template('base.conf.j2')
            content = template.render(
                config_name=analysis['name'],
                source_type=source_type,
                category=category,
                provider_count=analysis['count'],
                proxy_providers=analysis['proxy_providers'],
                yaml_url=yaml_url,
                timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                smart_mode=config_def['smart_mode'],
                bypass_mode=config_def['bypass_mode'],
                enable_ipv6=config_def['enable_ipv6'],
                enable_lgbm=config_def['enable_lgbm']
            )
            
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        except Exception as e:
            self.logger.error(f"Failed to generate {output_path}: {e}")
            return False

    def process_directory(self, input_dir: Path, output_base: Path, 
                         repo_url: str, source_type: str) -> Dict:
        """处理一个来源目录（保持子目录结构）"""
        
        stats = {'categories': {}, 'total': 0, 'errors': 0}
        
        # 遍历子目录（General_Config, Smart_Mode 等）
        for category_dir in input_dir.iterdir():
            if not category_dir.is_dir():
                continue
            
            category_name = category_dir.name
            category_output = output_base / category_name
            
            self.logger.info(f"\n{'='*60}")
            self.logger.info(f"处理分类: {category_name}")
            self.logger.info(f"输出目录: {category_output}")
            
            yaml_files = list(category_dir.rglob('*.yaml'))
            files_generated = []
            
            for yaml_file in yaml_files:
                for config_def in self.config_types:
                    try:
                        # 构建文件名
                        base_name = yaml_file.stem
                        suffix = config_def['suffix']
                        
                        if suffix:
                            filename = f"Overwrite{suffix}-{base_name}.conf"
                        else:
                            filename = f"Overwrite-{base_name}.conf"
                        
                        output_path = category_output / filename
                        
                        result = self.generate_overwrite(
                            yaml_file, output_path, config_def,
                            repo_url, category_name, source_type
                        )
                        
                        if result:
                            files_generated.append(filename)
                            stats['total'] += 1
                        else:
                            stats['errors'] += 1
                    
                    except Exception as e:
                        self.logger.error(f"Error: {e}")
                        stats['errors'] += 1
            
            # 生成分类 README（即使没有文件也生成）
            self.generate_readme(category_output, category_name, 
                               source_type, files_generated)
            stats['categories'][category_name] = len(files_generated)
        
        return stats


def main():
    parser = argparse.ArgumentParser(
        description='Generate OpenClash overwrite configs from YAML files'
    )
    parser.add_argument('--input', '-i', type=Path, required=True,
                       help='输入目录（包含子目录如 General_Config/）')
    parser.add_argument('--output', '-o', type=Path, required=True,
                       help='输出基础目录')
    parser.add_argument('--templates', '-t', type=Path, 
                       default=Path('templates'))
    parser.add_argument('--config-types', '-c', type=Path,
                       default=Path('src/config_types.json'))
    parser.add_argument('--repo-url', 
                       default='https://raw.githubusercontent.com/USER/REPO/main',
                       help='Repository base URL for YAML downloads')
    parser.add_argument('--source', default='external',
                       help='来源类型: external 或 local')
    parser.add_argument('--verbose', '-v', action='store_true')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be generated without writing files')
    
    args = parser.parse_args()
    
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(levelname)s: %(message)s'
    )
    
    try:
        gen = OverwriteGenerator(args.templates, args.config_types)
        
        if args.dry_run:
            logging.info("DRY RUN MODE - No files will be written")
        
        stats = gen.process_directory(
            args.input, args.output, args.repo_url, args.source
        )
        
        print(f"\n{'='*60}")
        print(f"总计生成: {stats['total']} 个文件")
        if stats['errors'] > 0:
            print(f"⚠️  错误数: {stats['errors']}")
        print(f"分类统计:")
        for cat, count in stats['categories'].items():
            print(f"  - {cat}: {count} 个文件")
        
        return 0
    
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())
