#!/usr/bin/env python3
"""
测试脚本 - 验证配置生成器功能
"""

import sys
import os
from pathlib import Path

# 添加 src 目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from config_generator import ConfigGenerator
from yaml_processor import YAMLProcessor
from utils import setup_logging, validate_config
import yaml


def test_config_validation():
    """测试配置验证"""
    print("🧪 测试配置验证...")
    
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    is_valid = validate_config(config)
    
    if is_valid:
        print("  ✅ 配置文件验证通过")
    else:
        print("  ❌ 配置文件验证失败")
        return False
    
    return True


def test_template_rendering():
    """测试模板渲染"""
    print("\n🧪 测试模板渲染...")
    
    try:
        generator = ConfigGenerator()
        
        # 测试渲染一个配置
        generator.generate_config(
            'main_router',
            'test_output.conf',
            '测试主路由配置'
        )
        
        output_file = generator.output_dir / 'test_output.conf'
        
        if output_file.exists():
            print(f"  ✅ 模板渲染成功: {output_file}")
            
            # 读取并显示前几行
            with open(output_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()[:10]
                print("  📄 生成的配置文件预览:")
                for line in lines:
                    print(f"    {line.rstrip()}")
            
            # 删除测试文件
            output_file.unlink()
            
            return True
        else:
            print("  ❌ 模板渲染失败: 文件未生成")
            return False
            
    except Exception as e:
        print(f"  ❌ 模板渲染失败: {e}")
        return False


def test_yaml_processor():
    """测试 YAML 处理器"""
    print("\n🧪 测试 YAML 处理器...")
    
    try:
        processor = YAMLProcessor()
        
        # 创建一个测试配置
        test_config = {
            'dns': {
                'enable': True,
                'ipv6': True,
                'enhanced-mode': 'fake-ip',
                'fake-ip-range': '198.18.0.1/16'
            },
            'proxy-groups': [
                {
                    'name': 'Proxy',
                    'type': 'select',
                    'proxies': ['DIRECT', 'REJECT']
                }
            ],
            'rules': [
                'DOMAIN,google.com,Proxy',
                'GEOIP,CN,DIRECT'
            ]
        }
        
        # 测试提取功能
        dns_config = processor.extract_dns_config(test_config)
        proxy_groups = processor.extract_proxy_groups(test_config)
        rules = processor.extract_rules(test_config)
        
        print(f"  ✅ DNS 配置: {dns_config['enhanced_mode']}")
        print(f"  ✅ 代理组数量: {len(proxy_groups)}")
        print(f"  ✅ 规则数量: {len(rules)}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ YAML 处理器测试失败: {e}")
        return False


def test_full_generation():
    """测试完整生成流程"""
    print("\n🧪 测试完整生成流程...")
    
    try:
        generator = ConfigGenerator()
        generator.generate_all()
        
        # 检查输出文件
        output_files = list(generator.output_dir.glob('*.conf'))
        
        if output_files:
            print(f"  ✅ 成功生成 {len(output_files)} 个配置文件:")
            for file in output_files:
                size = file.stat().st_size
                print(f"    📄 {file.name} ({size} bytes)")
            return True
        else:
            print("  ❌ 未生成任何配置文件")
            return False
            
    except Exception as e:
        print(f"  ❌ 完整生成测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主测试函数"""
    print("=" * 60)
    print("OpenClash Config Generator - 测试套件")
    print("=" * 60)
    
    # 设置日志
    setup_logging()
    
    tests = [
        ("配置验证", test_config_validation),
        ("YAML 处理器", test_yaml_processor),
        ("模板渲染", test_template_rendering),
        ("完整生成流程", test_full_generation),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ 测试 '{test_name}' 出现异常: {e}")
            results.append((test_name, False))
    
    # 显示测试结果摘要
    print("\n" + "=" * 60)
    print("测试结果摘要")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{status} - {test_name}")
    
    print(f"\n总计: {passed}/{total} 个测试通过")
    
    if passed == total:
        print("\n🎉 所有测试通过！")
        return 0
    else:
        print(f"\n⚠️  有 {total - passed} 个测试失败")
        return 1


if __name__ == '__main__':
    sys.exit(main())
