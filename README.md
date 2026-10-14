# Thaumcraft 4R 附属模组分发仓库

<div align="center">

**Thaumcraft 4 Reconstructed (TC4R) 附属 / 联动模组的二进制分发与索引**

[![Validate](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/validate.yml/badge.svg)](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/validate.yml)
[![Release](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/release.yml/badge.svg)](https://github.com/thaumcraft-port/thaumcraft-addons/actions/workflows/release.yml)
[![Latest release](https://img.shields.io/github/v/release/thaumcraft-port/thaumcraft-addons?color=blue)](https://github.com/thaumcraft-port/thaumcraft-addons/releases)

[下载](#-下载) · [模组介绍](#-模组介绍) · [版本对照](#-tc4r-版本对照) · [贡献](#-贡献你的模组)

</div>

## 这是什么

本仓库集中分发 **Thaumcraft 4 Reconstructed（TC4R）** 生态的附属 / 联动模组的二进制文件，并自动索引每个模组所依赖的 TC4R 内核版本。

- 📦 所有 `*.jar` 都是**编译好的模组本体**，通过 [Releases](https://github.com/thaumcraft-port/thaumcraft-addons/releases) 下载。
- 🧩 每个模组按 **Minecraft 版本**（当前 1.20.1 · 1.21.1）与 **加载器**（Forge / NeoForge）区分。
- 🔍 仓库自带脚本，自动读取每个模组声明的 **TC4R 依赖基线与最低构建号**。
- ✅ 每次提交 / PR 都由 GitHub Actions 自动校验（元数据、目录规范、依赖声明、README 是否最新）。

> 当前共收录 **18** 个模组文件，数据由 `catalog/mods.json` 自动生成。

## 📥 下载

所有文件都在 **[Releases](https://github.com/thaumcraft-port/thaumcraft-addons/releases)** 页面。点击下表即可直接下载最新版本；下载后建议核对 [SHA-256](#-校验和)。

### 正式通道

#### Minecraft 1.20.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Forgotten Relics | `forgottenrelics` | `1.7.3-beta-1.20.1-port.0.1.0` | Forge | ≥ 0.1.0 | 403.6 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forgottenrelics-1.20.1-1.7.3-beta-1.20.1-port.0.1.0.jar) |
| Nodal Mechanics | `nodalmechanics` | `1.0.7-port.0.1.0-20739` | Forge | ≥ 4.2.3.5 (build 20739) | 154.8 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-forge-1.0.7-port.0.1.0-20739.jar) |
| Pollution Unofficial | `pollution` | `1.0.0-1.20.1-port.0.1.0` | Forge | ≥ 0.1.0 | 9.9 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/pollution-1.20.1-1.0.0-1.20.1-port.0.1.0.jar) |
| Technomancy Unofficial | `technom` | `0.1.0-dev` | Forge | ≥ 4.2.3.5 (build 20721) | 1.6 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.20.1-0.1.0-dev.jar) |
| Thaumic Horizons | `isorropia` | `0.1.0-dev` | Forge | ≥ 4.2.3.5 (build 20732) | 4.1 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.20.1-0.1.0-dev.jar) |
| ThaumicEnergistics | `thaumicenergistics` | `2.3.17-forge-alpha` | Forge | ≥ 4.2.3.5 | 1.4 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-2.3.17-forge-alpha.jar) |
| Warp Theory | `warptheory` | `1.5.8-GTNH-1.20.1-port.0.1.0-20739` | Forge | ≥ 4.2.3.5 (build 20739) | 586.7 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-forge-1.5.8-GTNH-1.20.1-port.0.1.0-20739.jar) |
| 秽玄天工 | `zmod` | `1.30.12` | Forge | ≥ 4.2 | 1.5 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-forge-1.20.1-1.30.12.jar) |

#### Minecraft 1.21.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Nodal Mechanics | `nodalmechanics` | `1.0.7-port.0.1.0-20739` | NeoForge | ≥ 4.2.3.5 (build 20739) | 78.4 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-neoforge-1.0.7-port.0.1.0-20739.jar) |
| Technomancy Unofficial | `technom` | `0.1.0-dev` | NeoForge | ≥ 4.2.3.5 (build 20736) | 1.5 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.21.1-neoforge-0.1.0-dev.jar) |
| Thaumic Horizons | `isorropia` | `0.1.0-dev` | NeoForge | ≥ 4.2.3.5 (build 20736) | 4.0 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.21.1-0.1.0-dev.jar) |
| ThaumicEnergistics | `tc_energy` | `2.4.17-alpha` | NeoForge | ≥ 4.2.3.5 | 1.4 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-1.21.1-neo-2.4.18-alpha.jar) |
| Warp Theory | `warptheory` | `1.5.8-GTNH-1.21.1-port.0.1.0-20739` | NeoForge | ≥ 4.2.3.5 (build 20739) | 492.0 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-neoforge-1.5.8-GTNH-1.21.1-port.0.1.0-20739.jar) |
| 秽玄天工 | `zmod` | `1.30.26` | NeoForge | ≥ 4.2.3.5 (build 20738) | 4.6 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-neoforge-1.21.1-1.30.26.jar) |

### 实验通道（早期测试，谨慎使用）

#### Minecraft 1.20.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.20.1-port.0.1.0-9470460a` | Forge | ≥ 4.2.3.5 (build 20738) | 2.9 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-9470460a.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.20.1-port.0.1.0-ebf949bf` | Forge | ≥ 4.2.3.5 (build 20732) | 2.9 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-ebf949bf.jar) |

#### Minecraft 1.21.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.21.1-port.0.1.0-9470460a` | NeoForge | ≥ 4.2.3.5 (build 20738) | 2.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-9470460a.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.21.1-port.0.1.0-ebf949bf` | NeoForge | ≥ 4.2.3.5 (build 20732) | 2.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-ebf949bf.jar) |

## 🧩 模组介绍

### Forgotten Relics (`forgottenrelics`)

> A reconstruction of Forgotten Relics for Thaumcraft 4R on Minecraft 1.20.1. Adds a variety of powerful endgame relics, mostly oriented at expanding the horizons of mid- and endgame.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.7.3-beta-1.20.1-port.0.1.0` · 需要 ≥ 0.1.0 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forgottenrelics-1.20.1-1.7.3-beta-1.20.1-port.0.1.0.jar)

### Nodal Mechanics (`nodalmechanics`)

> Craft aura nodes through attunement and infusion using the Thaumcraft Universal API.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.0.7-port.0.1.0-20739` · 需要 ≥ 4.2.3.5 (build 20739) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-forge-1.0.7-port.0.1.0-20739.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.0.7-port.0.1.0-20739` · 需要 ≥ 4.2.3.5 (build 20739) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-neoforge-1.0.7-port.0.1.0-20739.jar)

### Pollution Unofficial (`pollution`)

> Unofficial 1.20.1 port of Pollution: connects GregTech CEu Modern industrial pollution with Thaumcraft 4R flux, aura and warp systems.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.0.0-1.20.1-port.0.1.0` · 需要 ≥ 0.1.0 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/pollution-1.20.1-1.0.0-1.20.1-port.0.1.0.jar)

### Technomancy Unofficial (`technom`)

> Unofficial Technomancy port for Minecraft 1.20.1. Development scaffold; gameplay migration is in progress.

- **Minecraft 1.20.1** · Forge · 模组版本 `0.1.0-dev` · 需要 ≥ 4.2.3.5 (build 20721) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.20.1-0.1.0-dev.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `0.1.0-dev` · 需要 ≥ 4.2.3.5 (build 20736) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.21.1-neoforge-0.1.0-dev.jar)

### Thaumic Horizons (`isorropia`)

> Thaumic Horizons (Isorropia) for Thaumcraft 4 Reborn on Minecraft 1.20.1 Forge and 1.21.1 NeoForge. / ç¥ç§è§çï¼ä¸ºç¥ç§æ¶ä»£4éççå¸¦æ¥çç©æ³¨é­ãæºè´¨æºæ¢°ä¸å£è¢ä½é¢ã

- **Minecraft 1.20.1** · Forge · 模组版本 `0.1.0-dev` · 需要 ≥ 4.2.3.5 (build 20732) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.20.1-0.1.0-dev.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `0.1.0-dev` · 需要 ≥ 4.2.3.5 (build 20736) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.21.1-0.1.0-dev.jar)

### ThaumicEnergistics (`tc_energy` / `thaumicenergistics`)

> Bridges Thaumcraft Essentia with Applied Energistics 2 ME networks (Forge 1.20.1 port).

- **Minecraft 1.20.1** · Forge · 模组版本 `2.3.17-forge-alpha` · 需要 ≥ 4.2.3.5 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-2.3.17-forge-alpha.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `2.4.17-alpha` · 需要 ≥ 4.2.3.5 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-1.21.1-neo-2.4.18-alpha.jar)

### Warp Theory (`warptheory`)

> GTNH Warp Theory for Thaumcraft 4 Reconstructed.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.5.8-GTNH-1.20.1-port.0.1.0-20739` · 需要 ≥ 4.2.3.5 (build 20739) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-forge-1.5.8-GTNH-1.20.1-port.0.1.0-20739.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.5.8-GTNH-1.21.1-port.0.1.0-20739` · 需要 ≥ 4.2.3.5 (build 20739) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-neoforge-1.5.8-GTNH-1.21.1-port.0.1.0-20739.jar)

### 秽玄天工 (`zmod`)

> 秽玄天工 1.20.1 Forge 移植版

- **Minecraft 1.20.1** · Forge · 模组版本 `1.30.12` · 需要 ≥ 4.2 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-forge-1.20.1-1.30.12.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.30.26` · 需要 ≥ 4.2.3.5 (build 20738) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-neoforge-1.21.1-1.30.26.jar)

## 🔧 TC4R 版本对照

下表列出每个模组要求的最低 TC4R 内核构建号，来源是模组 `mods.toml` / `neoforge.mods.toml` 中 `thaumcraft` 依赖的版本范围。

| 模组 | MC | 加载器 | 模组版本 | TC4R 基线 | 最低构建号 | 通道 |
| --- | --- | --- | --- | --- | --- | --- |
| Forgotten Relics | 1.20.1 | Forge | `1.7.3-beta-1.20.1-port.0.1.0` | 0.1.0 | 任意 | 正式 |
| Nodal Mechanics | 1.20.1 | Forge | `1.0.7-port.0.1.0-20739` | 4.2.3.5 | 20739 | 正式 |
| Pollution Unofficial | 1.20.1 | Forge | `1.0.0-1.20.1-port.0.1.0` | 0.1.0 | 任意 | 正式 |
| Technomancy Unofficial | 1.20.1 | Forge | `0.1.0-dev` | 4.2.3.5 | 20721 | 正式 |
| Thaumic Bases | 1.20.1 | Forge | `1.3.1710.4-1.20.1-port.0.1.0-9470460a` | 4.2.3.5 | 20738 | 实验 |
| Thaumic Bases | 1.20.1 | Forge | `1.3.1710.4-1.20.1-port.0.1.0-ebf949bf` | 4.2.3.5 | 20732 | 实验 |
| Thaumic Horizons | 1.20.1 | Forge | `0.1.0-dev` | 4.2.3.5 | 20732 | 正式 |
| ThaumicEnergistics | 1.20.1 | Forge | `2.3.17-forge-alpha` | 4.2.3.5 | 任意 | 正式 |
| Warp Theory | 1.20.1 | Forge | `1.5.8-GTNH-1.20.1-port.0.1.0-20739` | 4.2.3.5 | 20739 | 正式 |
| 秽玄天工 | 1.20.1 | Forge | `1.30.12` | 4.2 | 任意 | 正式 |
| Nodal Mechanics | 1.21.1 | NeoForge | `1.0.7-port.0.1.0-20739` | 4.2.3.5 | 20739 | 正式 |
| Technomancy Unofficial | 1.21.1 | NeoForge | `0.1.0-dev` | 4.2.3.5 | 20736 | 正式 |
| Thaumic Bases | 1.21.1 | NeoForge | `1.3.1710.4-1.21.1-port.0.1.0-9470460a` | 4.2.3.5 | 20738 | 实验 |
| Thaumic Bases | 1.21.1 | NeoForge | `1.3.1710.4-1.21.1-port.0.1.0-ebf949bf` | 4.2.3.5 | 20732 | 实验 |
| Thaumic Horizons | 1.21.1 | NeoForge | `0.1.0-dev` | 4.2.3.5 | 20736 | 正式 |
| ThaumicEnergistics | 1.21.1 | NeoForge | `2.4.17-alpha` | 4.2.3.5 | 任意 | 正式 |
| Warp Theory | 1.21.1 | NeoForge | `1.5.8-GTNH-1.21.1-port.0.1.0-20739` | 4.2.3.5 | 20739 | 正式 |
| 秽玄天工 | 1.21.1 | NeoForge | `1.30.26` | 4.2.3.5 | 20738 | 正式 |

## 🔐 校验和

<details>
<summary>点击展开全部 SHA-256 校验和</summary>

| 文件 | SHA-256 |
| --- | --- |
| `thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-9470460a.jar` | `5c7b565e60116a47373514a8ca42649ead14175a42fa73b3ea7e60f2d80ac50d` |
| `thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-ebf949bf.jar` | `e48b6db8b990f0bc872e4b5c85b457b453ae0ca1fd690db5723fda65840b2204` |
| `forgottenrelics-1.20.1-1.7.3-beta-1.20.1-port.0.1.0.jar` | `28974bf373c83a4ee40397e3cb07a639f69b77297f6422a805011c35ff6c5ad8` |
| `isorropia-1.20.1-0.1.0-dev.jar` | `cbe6124dfe0d31aafba107e949ebf103db0ad1a8cd8a1fabd610bf4e2e33c027` |
| `nodal-mechanics-forge-1.0.7-port.0.1.0-20739.jar` | `78ea010a08a0fb4aa9348ad0cc9b5cd71d6a8fc7a965eee873e9d93d460fb3aa` |
| `pollution-1.20.1-1.0.0-1.20.1-port.0.1.0.jar` | `a47c6c2ef4b7c3a2db53a58a2b0e71fd8071042848f9b9e80270e31d237d678a` |
| `technom-1.20.1-0.1.0-dev.jar` | `6824dbc9592c7c919c1d3c4a18c328383488ef8df5e75681eca6f40c211ac50d` |
| `thaumicenergistics-2.3.17-forge-alpha.jar` | `1faacd6f7f2bcff1fed182caff97187ea7d8e2999cc38388465fcf48a2a4c35f` |
| `warp-theory-forge-1.5.8-GTNH-1.20.1-port.0.1.0-20739.jar` | `e019943968cb24c6813a5c7c3c389892c3b05ce6a9d3adfa36f9fd1e02310450` |
| `huixuantiangong-forge-1.20.1-1.30.12.jar` | `54c9d9c997c1dacaa0a19f7fdef8480f867923f7373b2ca800d6e027841746ff` |
| `thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-9470460a.jar` | `8ed6299663195abcdde4fccc3d58f2e2028d7decf0d1c844f6f128edfc814d05` |
| `thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-ebf949bf.jar` | `ce190dadbb3d28d25ff709b7a7c09177328abb1f1bd2afe014b5b6e3e909270e` |
| `isorropia-1.21.1-0.1.0-dev.jar` | `f2112f95c3be63a3422f935f2af9f0a5bb0dd083dc20b3bb3fff478f47500584` |
| `nodal-mechanics-neoforge-1.0.7-port.0.1.0-20739.jar` | `831abcb1794b7536feaec9d5fcac017d0daadd4bd297ed3cc2f653b4c9cf1120` |
| `thaumicenergistics-1.21.1-neo-2.4.18-alpha.jar` | `b270a26ccf3707308c8a03252d47af98543338c94a1370c00c984a94c71b071c` |
| `technom-1.21.1-neoforge-0.1.0-dev.jar` | `8ca10b90ac3c3efd5969d31f4b0afb9b899848f22db0b090076150f5d33265a7` |
| `warp-theory-neoforge-1.5.8-GTNH-1.21.1-port.0.1.0-20739.jar` | `59b39a23b2b282de069c6eb14c0ec0bd8f12fb052266cb0248b8b9a123f1804c` |
| `huixuantiangong-neoforge-1.21.1-1.30.26.jar` | `2dffb4e134b61568bdd3a5d1ca8bc6de57dd91c4c816046ac8b8b3291665122e` |

</details>

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

<sub>本 README 由 `scripts/gen_readme.py` 依据 `catalog/mods.json` 自动生成，请勿手工编辑；如需修改请编辑 `README.template.md`。生成时间：2026-10-14T05:35:16Z</sub>
