# 贡献指南 / Contributing

感谢你为本仓库贡献 Thaumcraft 4R 附属模组！本仓库用于**分发与索引**编译好的模组文件，一切通过 Pull Request 合并，并由 GitHub Actions 自动校验。

## 一分钟上手

```bash
git clone https://github.com/<你的用户名>/thaumcraft-addons
cd thaumcraft-addons
python scripts/add_mod.py /路径/你的模组.jar   # 自动归档 + 重建索引 + 重建 README
git add -A
git commit -m "add: <模组名> <版本>"
git push
```

然后在 GitHub 上发起 Pull Request。CI 变绿、维护者 review 通过后即可合并。

`add_mod.py` 会自动：

1. 读取 jar 内的 `mods.toml` / `neoforge.mods.toml` / `fabric.mod.json`；
2. 判断它的 Minecraft 版本与加载器；
3. 把 jar 复制到 `mods/<Minecraft版本>/`（或 `mods/experimental/<Minecraft版本>/`）；
4. 重新生成 `catalog/mods.json`、`catalog/SHA256SUMS` 与 `README.md`。

## 仓库结构

```
mods/
  1.20.1/            # 正式通道，按 Minecraft 版本分目录
  1.21.1/
  experimental/      # 实验 / 早期测试通道，同样按 MC 版本分目录
    1.20.1/
catalog/             # 自动生成的索引（不要手工编辑）
  mods.json
  SHA256SUMS
docs/                # 文档与 TC4R API 参考
scripts/             # 自动化脚本
```

## 硬性规范（CI 会检查，违反即失败）

| 规则 | 说明 |
| --- | --- |
| **目录 = 版本** | jar 必须放在 `mods/<MC版本>/`（或 `mods/experimental/<MC版本>/`），且目录名必须与 jar 内声明的 Minecraft 版本一致。 |
| **声明 TC4R 依赖** | `mods.toml` 中必须存在 `thaumcraft` 依赖项，脚本据此索引内核构建号。 |
| **文件名规范** | 仅使用 ASCII 字符；不带历史遗留的 `(20738+)` / `(20737-)` 前缀。推荐格式 `<modId>-<MC版本>-<模组版本>.jar`。 |
| **无重复** | 同一 `(modId, MC 版本, 模组版本)` 只能出现一次；更新请替换旧文件。 |
| **唯一版本** | 同一模组在同一 MC 版本下只保留**最新稳定版**；开发中版本请放 `experimental/`。 |
| **索引一致** | `catalog/` 与 `README.md` 必须是脚本生成的**最新**状态（先跑 `add_mod.py` 或 `build.py` 再提交）。 |
| **许可** | jar 内必须声明 `license`；不得上传你无权分发的二进制。 |

## 手动流程（等价于 add_mod.py）

1. 把 jar 放进 `mods/<MC版本>/`；
2. 运行 `python scripts/build_catalog.py`；
3. 运行 `python scripts/gen_readme.py`；
4. 提交 jar + `catalog/` + `README.md`。

任意平台一键完成（含校验）：

```bash
python scripts/build.py --validate
```

## 提交信息规范

- 新增：`add: <模组名> <版本>`
- 更新：`update: <模组名> <旧版本> -> <新版本>`
- 删除：`remove: <模组名>`
- 文档/脚本：`docs:` / `chore:` / `ci:`

## 校验脚本

在本地复现 CI 的检查：

```bash
python scripts/validate.py --check-generated
```

它会依次核对：元数据可读性、目录与 MC 版本一致性、TC4R 依赖、文件名、重复项，以及 `catalog/`、`README.md` 是否最新。

## Review 与合并

1. 提交 PR 后，`validate` workflow 会跑上述校验；
2. 维护者确认元数据与许可无误；
3. 合并到 `main`；
4. 维护者打 tag（如 `v2026.10.14`），`release` workflow 会打包并发布到 [Releases](https://github.com/thaumcraft-port/thaumcraft-addons/releases)。

## 版权与移除

所有模组版权归原作者所有。本仓库仅作分发索引。如果你是某个模组的作者并希望停止分发，请提交 Issue，我们会删除对应文件。
