# OpenClash 覆写配置文件

本目录包含自动生成的 OpenClash 覆写配置文件。

## 文件命名规则
- `Overwrite-external-*`: 来自外部仓库(HenryChiao/mihomo_yamls)的配置
- `Overwrite-local-*`: 来自本仓库 cleaner_config/ 目录的本地配置
- `-main.conf`: 主路由标准模式(Url-test)
- `-bypass.conf`: 旁路由模式(需设置 EN_DNS)
- `-smart.conf`: Smart智能模式

## 使用方法

1. **下载覆写文件**: 直接点击需要的 `.conf` 文件，点击右上角 "Raw" 获取原始链接
2. **在 OpenClash 中使用**:
   - 进入 OpenClash 插件设置
   - 找到 "覆写设置" -> "自定义覆写"
   - 粘贴文件 URL 或上传文件
3. **设置环境变量**:
   - 单订阅: `EN_KEY=https://your-sub-url`
   - 多订阅: `EN_KEY1=https://sub1`, `EN_KEY2=https://sub2`...
   - 旁路由模式额外需要: `EN_DNS=223.5.5.5`

## 自动更新

本目录文件每天自动从上游同步并重新生成，如需修改请编辑:
- 外部配置: 向 [HenryChiao/mihomo_yamls](https://github.com/HenryChiao/mihomo_yamls) 提交 PR
- 本地配置: 修改本仓库的 `cleaner_config/` 目录

