# OpenClash Config Builder

🤖 **自动化 OpenClash 覆写配置生成器**

从 [HenryChiao/mihomo_yamls](https://github.com/HenryChiao/mihomo_yamls) 提取配置，精简处理后生成 OpenClash .conf 覆写文件，并根据 proxy-provider 数量动态生成环境变量。

[![Build](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/build.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)

---

## ✨ 核心特性

- 🔄 **自动同步**: 每日从上游自动拉取最新配置
- ✂️ **智能精简**: 只保留 `proxy-providers`, `proxy-groups`, `rule-providers`, `rules` 和锚点
- 🎯 **动态变量**: 根据 provider 数量自动生成对应的环境变量 (`EN_KEY`, `EN_KEY1`, `EN_KEY2`, ...)
- 📦 **多场景支持**: 主路由、旁路由、Smart 智能模式
- 🤖 **全自动化**: GitHub Actions 每日构建，无需手动操作

---

## 🎯 工作原理

```
HenryChiao/mihomo_yamls (上游)
         ↓
    [同步 YAML 文件]
         ↓
    [精简处理]
    - 删除: port, external-controller, dns, tun 等非必要配置
    - 保留: proxy-providers, proxy-groups, rule-providers, rules, 锚点
         ↓
    [分析 Provider 数量]
    - 1 个 provider → EN_KEY
    - 2 个 providers → EN_KEY1, EN_KEY2
    - N 个 providers → EN_KEY1...EN_KEYN
         ↓
    [生成 .conf 文件]
    - 主路由版
    - 旁路由版  
    - Smart 版
         ↓
    [发布 Release]
```

---

## 📂 项目结构

```
clash-config-builder/
├── src/
│   ├── yaml_stripper.py      # YAML 精简处理器
│   └── conf_generator.py     # .conf 文件生成器
├── templates/
│   ├── main.conf.j2          # 主路由模板
│   ├── bypass.conf.j2        # 旁路由模板
│   └── smart.conf.j2         # Smart 模式模板
├── processed_configs/         # 精简后的 YAML 文件
├── output/                    # 生成的 .conf 文件
├── .github/workflows/
│   └── build.yml             # GitHub Actions 工作流
└── README.md
```

---

## 🚀 使用方法

### 方式一：直接使用生成的配置 (推荐)

1. **前往 [Releases](https://github.com/YOUR_USERNAME/YOUR_REPO/releases) 页面**

2. **选择最新的 Release**，找到你需要的 .conf 文件

3. **复制 Raw 链接**，例如：
   ```
   https://github.com/YOUR_USERNAME/YOUR_REPO/releases/download/v2026-02-02/配置名.conf
   ```

4. **在 OpenClash 中添加覆写模块**：
   - 文件名：自定义
   - 类型：`http`
   - 订阅链接：上面复制的 URL

5. **配置环境变量**（根据文件内的说明）：
   
   **单订阅配置**（1 个 provider）:
   ```
   EN_KEY=你的机场订阅链接
   ```
   
   **多订阅配置**（多个 providers）:
   ```
   EN_KEY1=订阅链接1;EN_KEY2=订阅链接2;EN_KEY3=订阅链接3
   ```
   
   **旁路由**（额外需要）:
   ```
   EN_DNS=114.114.114.114
   ```

6. **保存并重启 OpenClash**

### 方式二：自己构建

```bash
# 克隆项目
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd clash-config-builder

# 安装依赖
pip install PyYAML Jinja2

# 1. 同步上游配置
git clone https://github.com/HenryChiao/mihomo_yamls.git upstream
cp upstream/General_Config/*.yaml raw_configs/

# 2. 精简 YAML 文件
python src/yaml_stripper.py raw_configs processed_configs

# 3. 生成 .conf 文件
python src/conf_generator.py processed_configs output --templates templates

# 4. 查看生成的文件
ls output/
```

---

## 📋 配置文件说明

### 文件命名规则

| 文件名 | 适用场景 | Provider 变量 |
|--------|---------|--------------|
| `配置名.conf` | 主路由标准 | 自动生成 |
| `配置名-bypass_router.conf` | 旁路由 | 自动生成 + EN_DNS |
| `配置名-smart.conf` | Smart 智能模式 | 自动生成 |

### Provider 变量说明

配置文件会自动根据 `proxy-providers` 数量生成环境变量：

```python
1 个 provider  → EN_KEY
2 个 providers → EN_KEY1, EN_KEY2
3 个 providers → EN_KEY1, EN_KEY2, EN_KEY3
...
```

**示例**：

如果配置文件中有 3 个 proxy-providers:
```yaml
proxy-providers:
  provider1:
    ...
  provider2:
    ...
  provider3:
    ...
```

那么环境变量应该设置为:
```
EN_KEY1=订阅链接1;EN_KEY2=订阅链接2;EN_KEY3=订阅链接3
```

---

## 🔧 精简规则

### 保留的内容

✅ `proxy-providers` - 代理提供者  
✅ `proxy-groups` - 策略组  
✅ `rule-providers` - 规则提供者  
✅ `rules` - 规则列表  
✅ **锚点** (YAML anchors) - 如 `&anchor_name`

### 删除的内容

❌ `port`, `socks-port`, `mixed-port` - 端口配置  
❌ `external-controller` - 外部控制器  
❌ `dns` - DNS 配置（由 OpenClash 管理）  
❌ `tun` - TUN 配置（由 OpenClash 管理）  
❌ `allow-lan`, `mode`, `log-level` 等基础配置  
❌ 其他非核心配置

---

## 🤖 GitHub Actions 自动化

项目包含完整的 CI/CD 流程：

### 触发条件

- ⏰ **定时触发**: 每天凌晨 2 点 (UTC)
- 🖱️ **手动触发**: 在 Actions 页面点击 "Run workflow"
- 📝 **代码推送**: 推送到 `main` 分支时

### 工作流程

1. 克隆上游仓库 `HenryChiao/mihomo_yamls`
2. 提取所有 YAML 配置文件
3. 精简处理（只保留核心部分）
4. 生成 .conf 文件（主路由/旁路由/Smart）
5. 创建 Release 并上传文件
6. 提交更改到仓库

---

## 📊 支持的上游配置

目前自动同步以下目录：

- ✅ `General_Config/` - 通用配置
- ✅ `Smart_Mode/` - Smart 模式配置

---

## 🛠️ 开发说明

### Python 模块

#### yaml_stripper.py

负责精简 YAML 文件：

```python
from src.yaml_stripper import YAMLStripper

stripper = YAMLStripper()
config = stripper.strip_yaml(Path('input.yaml'))
stripper.save_stripped_yaml(config, Path('output.yaml'))
```

#### conf_generator.py

负责生成 .conf 文件：

```python
from src.conf_generator import ConfGenerator

generator = ConfGenerator(Path('templates'))
generator.generate_conf(
    yaml_path=Path('config.yaml'),
    output_path=Path('output.conf'),
    config_type='main_router'
)
```

### 添加新模板

1. 在 `templates/` 目录创建新的 `.j2` 文件
2. 使用 Jinja2 语法编写模板
3. 在 `conf_generator.py` 中添加对应的配置类型

---

## 📝 示例配置

### 单订阅示例

```ini
[General]
CONFIG_FILE = /etc/openclash/config/MyConfig.yaml
...

[Overwrite]
ruby_map_edit "$CONFIG_FILE" "['proxy-providers']" "provider" "['url']" "$EN_KEY"
```

**环境变量**:
```
EN_KEY=https://example.com/sub
```

### 多订阅示例

```ini
[General]
CONFIG_FILE = /etc/openclash/config/MultiSub.yaml
...

[Overwrite]
ruby_edit "$CONFIG_FILE" "['proxy-providers']['provider1']['url']" "$EN_KEY1"
ruby_edit "$CONFIG_FILE" "['proxy-providers']['provider2']['url']" "$EN_KEY2"
```

**环境变量**:
```
EN_KEY1=https://example.com/sub1;EN_KEY2=https://example.com/sub2
```

---

## ⚠️ 注意事项

1. **环境变量必须正确设置**，否则订阅无法更新
2. **旁路由用户**必须额外设置 `EN_DNS` 变量
3. 精简后的 YAML 文件会自动下载到路由器的 `/etc/openclash/config/` 目录
4. 所有配置默认启用 Smart 内核，如需 Meta 内核请手动修改
5. 请确保 OpenClash 版本 ≥ v0.47.006

---

## 🔗 相关链接

- [OpenClash 项目](https://github.com/vernesong/OpenClash)
- [HenryChiao/mihomo_yamls](https://github.com/HenryChiao/mihomo_yamls) - 上游配置源
- [Mihomo 文档](https://wiki.metacubex.one/)

---

## 📜 许可证

本项目采用 GPL-3.0 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- [HenryChiao](https://github.com/HenryChiao) - mihomo_yamls 项目作者
- [vernesong](https://github.com/vernesong) - OpenClash 项目作者
- 所有为开源社区贡献的开发者

---

**如果这个项目对你有帮助，请给个 ⭐ Star！**
