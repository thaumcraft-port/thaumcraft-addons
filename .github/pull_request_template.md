## 变更类型 / Type

- [ ] 新增模组 (add)
- [ ] 更新模组 (update)
- [ ] 移除模组 (remove)
- [ ] 脚本 / 文档 / CI

## 说明 / Description

<!-- 简要说明本次改动 -->

## 模组信息（新增 / 更新时填写）

| 项目 | 内容 |
| --- | --- |
| 模组名称 | |
| modId | |
| Minecraft 版本 | |
| 加载器 | |
| 依赖 TC4R | |
| 源码仓库 | |
| 开源许可 | |

## 自检 / Checklist

- [ ] jar 放在 `mods/<Minecraft版本>/`（实验版放 `mods/experimental/<Minecraft版本>/`）
- [ ] 已在 jar 内声明 `thaumcraft` 依赖与 `license`
- [ ] 文件名规范（ASCII、无 `(20738+)` 前缀）
- [ ] 已运行 `python scripts/add_mod.py`（或 `build.ps1`），提交了 `catalog/` 与 `README.md`
- [ ] 本地 `python scripts/validate.py --check-generated` 通过
- [ ] 我确认有权分发该二进制文件，并遵守其开源许可
