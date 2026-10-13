# Thaumcraft 4R 附属模组分发仓库

<div align="center">

**Thaumcraft 4 Reconstructed (TC4R) 附属 / 联动模组的二进制分发与索引**

[![Validate](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/validate.yml/badge.svg)](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/validate.yml)
[![Release](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/release.yml/badge.svg)](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/release.yml)
[![Latest release](https://img.shields.io/github/v/release/thaumcraft-port/thaumcraft-addons?color=blue)]({{RELEASES_PAGE}})

[下载](#-下载) · [模组介绍](#-模组介绍) · [版本对照](#-tc4r-版本对照) · [贡献](#-贡献你的模组)

</div>

## 这是什么

本仓库集中分发 **Thaumcraft 4 Reconstructed（TC4R）** 生态的附属 / 联动模组的二进制文件，并自动索引每个模组所依赖的 TC4R 内核版本。

- 📦 所有 `*.jar` 都是**编译好的模组本体**，通过 [Releases]({{RELEASES_PAGE}}) 下载。
- 🧩 每个模组按 **Minecraft 版本**（当前 {{MC_VERSIONS}}）与 **加载器**（Forge / NeoForge）区分。
- 🔍 仓库自带脚本，自动读取每个模组声明的 **TC4R 依赖基线与最低构建号**。
- ✅ 每次提交 / PR 都由 GitHub Actions 自动校验（元数据、目录规范、依赖声明、README 是否最新）。

> 当前共收录 **{{TOTAL}}** 个模组文件，数据由 `catalog/mods.json` 自动生成。

## 📥 下载

所有文件都在 **[Releases]({{RELEASES_PAGE}})** 页面。点击下表即可直接下载最新版本；下载后建议核对 [SHA-256](#-校验和)。

### 正式通道

{{TABLE_STABLE}}

### 实验通道（早期测试，谨慎使用）

{{TABLE_EXPERIMENTAL}}

## 🧩 模组介绍

{{MOD_CARDS}}

## 🔧 TC4R 版本对照

下表列出每个模组要求的最低 TC4R 内核构建号，来源是模组 `mods.toml` / `neoforge.mods.toml` 中 `thaumcraft` 依赖的版本范围。

{{BUILD_MATRIX}}

## 🔐 校验和

{{CHECKSUMS}}

## 🤝 贡献你的模组

欢迎 fork 本仓库并通过 PR 添加你自己的附属模组。完整规范见 **[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)**，最简流程：

```bash
git clone https://github.com/<你的用户名>/thaumcraft-addons
cd thaumcraft-addons
python scripts/add_mod.py /路径/你的模组.jar   # 自动归档 + 重建索引
git add -A
git commit -m "add: 你的模组名"
git push
```

然后向本仓库发起 Pull Request，CI 通过后即可合并。`add_mod.py` 会自动读取元数据、把 jar 放进正确的 `mods/<Minecraft版本>/` 目录，并重新生成 `catalog/` 与 `README.md`。

## ⚖️ 声明

本仓库仅作**分发与索引**用途，所有模组版权归各自作者所有，下载与使用请遵守各模组自身的开源许可（见上表或模组内 `mods.toml` 的 `license` 字段）。仓库的脚本与文档以 MIT 许可发布。若你是某个模组的作者且不希望在此分发，请提交 Issue，我们会在第一时间移除。

---

<sub>本 README 由 `scripts/gen_readme.py` 依据 `catalog/mods.json` 自动生成，请勿手工编辑；如需修改请编辑 `README.template.md`。生成时间：{{GENERATED_AT}}</sub>
