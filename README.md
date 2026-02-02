# OpenClash Config Generator

[![Build Status](https://img.shields.io/github/actions/workflow/status/your-username/openclash-config-generator/build.yml?branch=main)](https://github.com/your-username/openclash-config-generator/actions)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

🤖 自动化生成 OpenClash 覆写配置文件的 Python 项目

基于 [HenryChiao/mihomo_yamls](https://github.com/HenryChiao/mihomo_yamls) 的配置文件，自动生成类似 [OpenClash_Overwrite](https://github.com/Giveupmoon/OpenClash_Overwrite) 的 `.conf` 覆写模块。

---

## ✨ 特性

- 🔄 **自动化构建**: 通过 GitHub Actions 每日自动同步上游配置
- 🐍 **纯 Python 实现**: 无需 Ruby 脚本，全部使用 Python 生成配置
- 📦 **多场景支持**: 主路由/旁路由、IPv6/无IPv6、Smart/Url-test 等多种模式
- 🎯 **模板驱动**: 基于 Jinja2 模板引擎，易于定制和扩展
- 📝 **完整文档**: 包含详细的使用说明和配置示例

---

## 📂 项目结构

```
openclash_config_generator/
├── .github/
│   └── workflows/
│       └── build.yml           # GitHub Actions 工作流
├── src/
│   ├── config_generator.py     # 主配置生成器
│   ├── yaml_processor.py       # YAML 配置处理器
│   └── utils.py               # 工具函数
├── templates/
│   ├── base.conf.j2           # 基础配置模板
│   ├── main_router.conf.j2    # 主路由配置模板
│   ├── bypass_router.conf.j2  # 旁路由配置模板
│   └── smart.conf.j2          # Smart 模式配置模板
├── output/                    # 生成的配置文件输出目录
├── configs/                   # 从上游同步的 YAML 配置
├── requirements.txt           # Python 依赖
├── config.yaml               # 项目配置文件
└── README.md                 # 项目文档
```

---

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 基本使用

```bash
# 生成所有配置文件
python src/config_generator.py

# 生成特定类型的配置
python src/config_generator.py --type main_router
python src/config_generator.py --type bypass_router
python src/config_generator.py --type smart
```

### 使用生成的配置

1. 在 OpenClash 管理界面，进入 **配置文件订阅** → **覆写设置**
2. 点击 **新增覆写模块**
3. 配置参数：
   - **文件名**: 自定义（如 `auto-config`）
   - **类型**: `http`
   - **订阅链接**: 使用本项目生成的 raw 链接
4. 配置环境变量：`EN_KEY=你的机场订阅链接`
5. 保存并应用配置

---

## 📋 配置说明

### config.yaml 配置文件

```yaml
# 上游配置源
upstream:
  repo: "HenryChiao/mihomo_yamls"
  branch: "main"
  sync_interval: "0 2 * * *"  # 每天凌晨2点同步

# 输出配置
output:
  directory: "output"
  formats:
    - main_router
    - main_router_noipv6
    - bypass_router
    - bypass_router_noipv6
    - smart
    - smart_lgbm

# OpenClash 参数配置
openclash:
  core_type: "Smart"
  dns:
    enable_redirect: 1
    enable_custom: 0
    store_fakeip: 1
    fakeip_range: "198.18.0.1/16"
  
  ipv6:
    enable: 1
    dns: 1
    mode: 0
  
  proxy:
    mode: "fake-ip"
    enable_udp: 1
    router_self_proxy: 1
  
  smart:
    auto_switch: 1
    strategy: "sticky-sessions"
    enable_lgbm: 0
    policy_priority: "Premium:0.9;SG:1.3;HK:1.5"
    collect: 1
    collect_size: 500
```

---

## 🔧 生成的配置类型

| 配置类型 | 文件名 | 说明 |
|---------|--------|------|
| 主路由 Url-test | `Overwrite-main.conf` | 自动选择最快节点 |
| 主路由 Smart | `Overwrite-main-smart.conf` | 智能分流模式 |
| 主路由 Smart-LGBM | `Overwrite-main-smart-lgbm.conf` | 启用 LightGBM 模型 |
| 主路由无IPv6 | `Overwrite-main-noipv6.conf` | 禁用 IPv6 |
| 旁路由 | `Overwrite-bypass.conf` | 旁路网关模式 |
| 旁路由 Smart | `Overwrite-bypass-smart.conf` | 旁路由智能模式 |

---

## 🤖 GitHub Actions 自动化

项目使用 GitHub Actions 实现以下自动化任务：

1. **每日同步**: 自动从 HenryChiao/mihomo_yamls 同步最新配置
2. **自动构建**: 生成所有类型的 .conf 配置文件
3. **版本发布**: 自动创建 Release 并附带生成的文件
4. **文件托管**: 配置文件可通过 GitHub Pages 或 Raw 链接访问

### 工作流触发条件

- 每天凌晨 2 点 (UTC) 自动运行
- 手动触发 (workflow_dispatch)
- 代码推送到 main 分支

---

## 📖 技术文档

### 配置生成流程

```
1. 从上游仓库同步 YAML 配置
   ↓
2. 解析 YAML 配置文件
   ↓
3. 提取核心配置参数 (DNS, 代理组, 规则等)
   ↓
4. 使用 Jinja2 模板渲染 .conf 文件
   ↓
5. 生成不同场景的配置变体
   ↓
6. 输出到 output/ 目录
```

### Python 模块说明

#### config_generator.py

主配置生成器，负责：
- 读取项目配置
- 调用 YAML 处理器
- 渲染 Jinja2 模板
- 输出最终 .conf 文件

#### yaml_processor.py

YAML 配置处理器，负责：
- 解析 Mihomo YAML 配置
- 提取 DNS 配置
- 提取代理组配置
- 提取规则配置
- 转换为 OpenClash 参数

#### utils.py

工具函数模块，包含：
- 文件读写操作
- Git 操作封装
- 配置验证函数
- 日志记录

---

## 🔗 相关项目

- [OpenClash](https://github.com/vernesong/OpenClash) - OpenWrt 的 Clash 客户端
- [HenryChiao/mihomo_yamls](https://github.com/HenryChiao/mihomo_yamls) - Mihomo 配置文件集合
- [OpenClash_Overwrite](https://github.com/Giveupmoon/OpenClash_Overwrite) - 原始覆写项目

---

## 📜 许可证

本项目采用 GPL-3.0 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- [HenryChiao](https://github.com/HenryChiao) - mihomo_yamls 项目作者
- [Giveupmoon](https://github.com/Giveupmoon) - OpenClash_Overwrite 项目作者
- [vernesong](https://github.com/vernesong) - OpenClash 项目作者

---

## 📮 反馈与支持

如果你在使用过程中遇到问题或有建议：

- 📝 [提交 Issue](https://github.com/your-username/openclash-config-generator/issues)
- 🌟 给项目点个 Star
- 🍴 Fork 并提交 Pull Request

---

**注意**: 本项目仅用于学习和研究目的，请遵守当地法律法规。
