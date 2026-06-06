# General_Config/Mitchell 覆写配置

## 📍 来源
- **路径**: `HenryChiao/mihomo_yamls/THEYAMLS/General_Config/Mitchell`
- **类型**: 外部自动同步
- **用途**: 通用配置 - Mitchell 作者维护

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
- 生成时间: 2026-06-06 08:29:14
- 配置文件数: 9

---
*由 GitHub Actions 自动生成*
