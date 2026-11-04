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

> 当前共收录 **35** 个模组文件，数据由 `catalog/mods.json` 自动生成。

## 📥 下载

所有文件都在 **[Releases](https://github.com/thaumcraft-port/thaumcraft-addons/releases)** 页面。点击下表即可直接下载最新版本；下载后建议核对 [SHA-256](#-校验和)。

### 正式通道

#### Minecraft 1.20.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Forbidden Magic | `forbidden_magic` | `0.574-1.20.1-port.0.1.0-20759` | Forge | ≥ 4.2.3.5 (build 20754) | 1.2 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forbidden-magic-forge-0.574-1.20.1-port.0.1.0-20759.jar) |
| Forgotten Relics | `forgottenrelics` | `1.7.3-beta-1.20.1-port.0.1.0` | Forge | ≥ 0.1.0 | 403.6 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forgottenrelics-1.20.1-1.7.3-beta-1.20.1-port.0.1.0.jar) |
| Middle-earth Thaumaturgy | `mett` | `0.8.0-1.20.1` | Forge | ≥ 4.2.3.5 (build 20759) | 715.5 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/mett-1.20.1-0.8.0-1.20.1.jar) |
| Nodal Mechanics | `nodalmechanics` | `1.0.7-port.0.1.0-20759` | Forge | ≥ 4.2.3.5 (build 20759) | 141.2 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-forge-1.0.7-port.0.1.0-20759.jar) |
| Pollution Unofficial | `pollution` | `1.0.0-1.20.1-port.0.1.0` | Forge | ≥ 4.2.3.5 (build 20759) | 10.0 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/pollution-1.20.1-1.0.0-1.20.1-port.0.1.0.jar) |
| Tainted Magic | `tainted_magic` | `8.1.1-1.20.1-port.0.1.0-20759` | Forge | ≥ 4.2.3.5 (build 20759) | 3.8 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/tainted-magic-forge-8.1.1-1.20.1-port.0.1.0-20759.jar) |
| Technomancy Unofficial | `technom` | `0.1.0-dev` | Forge | ≥ 4.2.3.5 (build 20753) | 1.6 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.20.1-0.1.0-dev.jar) |
| Thaumcraft Client Tweaks | `tc4tweaks` | `1.1.5` | Forge | ≥ 4.2.3.5 (build 20740) | 480.1 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumcraft-client-tweaks-forge-1.1.5.jar) |
| Thaumic Additions: Reconstructed (Port) | `thaumadds` | `0.1.0` | Forge | ≥ 4.2.3.5 (build 20759) | 4.8 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumadds-1.20.1-0.1.0.jar) |
| Thaumic Horizons | `isorropia` | `1.0.7-alpha` | Forge | ≥ 4.2.3.5 (build 20759) | 4.1 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.20.1-1.0.7-alpha.jar) |
| Thaumic Tinkerer | `thaumictinkerer` | `2.5-1.20.1-port.0.1.0-20759` | Forge | ≥ 4.2.3.5 (build 20759) | 2.9 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-tinkerer-forge-2.5-1.20.1-port.0.1.0-20759.jar) |
| Thaumic WarpFX | `warpfx` | `0.1.0` | Forge | ≥ 4.2.3.5 (build 20739) | 67.6 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warpfx-1.20.1-forge-0.1.0.jar) |
| ThaumicEnergistics | `thaumicenergistics` | `2.3.17-forge-alpha` | Forge | ≥ 4.2.3.5 | 1.4 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-2.3.17-forge-alpha.jar) |
| Warp Theory | `warptheory` | `1.5.8-GTNH-1.20.1-port.0.1.0-20759` | Forge | ≥ 4.2.3.5 (build 20759) | 593.3 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-forge-1.5.8-GTNH-1.20.1-port.0.1.0-20759.jar) |
| 秽玄天工 | `zmod` | `1.30.12` | Forge | ≥ 4.2 | 1.5 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-forge-1.20.1-1.30.12.jar) |

#### Minecraft 1.21.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Forbidden Magic | `forbidden_magic` | `0.574-1.21.1-port.0.1.0-20759` | NeoForge | ≥ 4.2.3.5 (build 20756) | 1.0 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forbidden-magic-neoforge-0.574-1.21.1-port.0.1.0-20759.jar) |
| Nodal Mechanics | `nodalmechanics` | `1.0.7-port.0.1.0-20759` | NeoForge | ≥ 4.2.3.5 (build 20759) | 62.8 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-neoforge-1.0.7-port.0.1.0-20759.jar) |
| Tainted Magic | `tainted_magic` | `8.1.1-1.21.1-port.0.1.0-20759` | NeoForge | ≥ 4.2.3.5 (build 20759) | 3.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/tainted-magic-neoforge-8.1.1-1.21.1-port.0.1.0-20759.jar) |
| Technomancy Unofficial | `technom` | `0.1.0-dev` | NeoForge | ≥ 4.2.3.5 (build 20753) | 1.5 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.21.1-0.1.0-dev.jar) |
| Thaumcraft Client Tweaks | `tc4tweaks` | `1.1.5` | NeoForge | ≥ 4.2.3.5 (build 20740) | 461.5 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumcraft-client-tweaks-neoforge-1.1.5.jar) |
| Thaumic Additions: Reconstructed (Port) | `thaumadds` | `0.1.0` | NeoForge | ≥ 4.2.3.5 (build 20759) | 4.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumadds-1.21.1-0.1.0.jar) |
| Thaumic Horizons | `isorropia` | `1.0.7-alpha` | NeoForge | ≥ 4.2.3.5 (build 20759) | 4.1 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.21.1-1.0.7-alpha.jar) |
| Thaumic Tinkerer | `thaumictinkerer` | `2.5-1.21.1-port.0.1.0-20759` | NeoForge | ≥ 4.2.3.5 (build 20759) | 2.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-tinkerer-neoforge-2.5-1.21.1-port.0.1.0-20759.jar) |
| Thaumic WarpFX | `warpfx` | `0.1.0` | NeoForge | ≥ 4.2.3.5 (build 20739) | 66.6 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warpfx-1.21.1-neoforge-0.1.0.jar) |
| ThaumicEnergistics | `tc_energy` | `2.4.17-alpha` | NeoForge | ≥ 4.2.3.5 | 1.4 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-1.21.1-neo-2.4.18-alpha.jar) |
| Warp Theory | `warptheory` | `1.5.8-GTNH-1.21.1-port.0.1.0-20759` | NeoForge | ≥ 4.2.3.5 (build 20759) | 486.7 KB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-neoforge-1.5.8-GTNH-1.21.1-port.0.1.0-20759.jar) |
| 秽玄天工 | `zmod` | `1.30.26` | NeoForge | ≥ 4.2.3.5 (build 20738) | 4.6 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-neoforge-1.21.1-1.30.26.jar) |

### 实验通道（早期测试，谨慎使用）

#### Minecraft 1.20.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.20.1-port.0.1.0-20759` | Forge | ≥ 4.2.3.5 (build 20759) | 2.5 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-20759.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.20.1-port.0.1.0-26c67473` | Forge | ≥ 4.2.3.5 | 2.9 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-26c67473.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.20.1-port.0.1.0-9470460a` | Forge | ≥ 4.2.3.5 (build 20738) | 2.9 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-9470460a.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.20.1-port.0.1.0-ebf949bf` | Forge | ≥ 4.2.3.5 (build 20732) | 2.9 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-ebf949bf.jar) |

#### Minecraft 1.21.1

| 模组 | modId | 版本 | 加载器 | TC4R 要求 | 大小 | 下载 |
| --- | --- | --- | --- | --- | --- | --- |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.21.1-port.0.1.0-20759` | NeoForge | ≥ 4.2.3.5 (build 20759) | 2.3 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-20759.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.21.1-port.0.1.0-26c67473` | NeoForge | ≥ 4.2.3.5 | 2.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-26c67473.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.21.1-port.0.1.0-9470460a` | NeoForge | ≥ 4.2.3.5 (build 20738) | 2.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-9470460a.jar) |
| Thaumic Bases | `thaumicbases` | `1.3.1710.4-1.21.1-port.0.1.0-ebf949bf` | NeoForge | ≥ 4.2.3.5 (build 20732) | 2.7 MB | [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-ebf949bf.jar) |

## 🧩 模组介绍

### Forbidden Magic (`forbidden_magic`)

> Explore the forbidden side of Thaumcraft 4R with sinister research, powerful artifacts, and unconventional tools for the adventurous thaumaturge.

- **Minecraft 1.20.1** · Forge · 模组版本 `0.574-1.20.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20754) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forbidden-magic-forge-0.574-1.20.1-port.0.1.0-20759.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `0.574-1.21.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20756) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forbidden-magic-neoforge-0.574-1.21.1-port.0.1.0-20759.jar)

### Forgotten Relics (`forgottenrelics`)

> A reconstruction of Forgotten Relics for Thaumcraft 4R on Minecraft 1.20.1. Adds a variety of powerful endgame relics, mostly oriented at expanding the horizons of mid- and endgame.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.7.3-beta-1.20.1-port.0.1.0` · 需要 ≥ 0.1.0 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/forgottenrelics-1.20.1-1.7.3-beta-1.20.1-port.0.1.0.jar)

### Middle-earth Thaumaturgy (`mett`)

> Unofficial 1.20.1 port of MiddleEarth-Thaumaturgy: LotR-themed aspects, faction wands, summoning foci and compressed essentia jars for Thaumcraft 4R and Middle-earth.

- **Minecraft 1.20.1** · Forge · 模组版本 `0.8.0-1.20.1` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/mett-1.20.1-0.8.0-1.20.1.jar)

### Nodal Mechanics (`nodalmechanics`)

> Create your own aura nodes in Thaumcraft 4R. Attune node matrices with essentia, then bring them to life through infusion.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.0.7-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-forge-1.0.7-port.0.1.0-20759.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.0.7-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/nodal-mechanics-neoforge-1.0.7-port.0.1.0-20759.jar)

### Pollution Unofficial (`pollution`)

> Unofficial 1.20.1 port of Pollution: connects GregTech CEu Modern industrial pollution with Thaumcraft 4R flux, aura and warp systems.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.0.0-1.20.1-port.0.1.0` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/pollution-1.20.1-1.0.0-1.20.1-port.0.1.0.jar)

### Tainted Magic (`tainted_magic`)

> Harness darker powers in Thaumcraft 4R. Forge Shadow Metal equipment, craft powerful wand foci, and uncover new possibilities in taint and thaumaturgy.

- **Minecraft 1.20.1** · Forge · 模组版本 `8.1.1-1.20.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/tainted-magic-forge-8.1.1-1.20.1-port.0.1.0-20759.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `8.1.1-1.21.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/tainted-magic-neoforge-8.1.1-1.21.1-port.0.1.0-20759.jar)

### Technomancy Unofficial (`technom`)

> Unofficial Technomancy port: essentia-powered machinery, node engineering, rituals, and a shared FE/EU energy system.

- **Minecraft 1.20.1** · Forge · 模组版本 `0.1.0-dev` · 需要 ≥ 4.2.3.5 (build 20753) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.20.1-0.1.0-dev.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `0.1.0-dev` · 需要 ≥ 4.2.3.5 (build 20753) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/technom-1.21.1-0.1.0-dev.jar)

### Thaumcraft Client Tweaks (`tc4tweaks`)

> Client-side Thaumonomicon search, navigation, layout, optional research-table interface and aura-node visual improvements.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.1.5` · 需要 ≥ 4.2.3.5 (build 20740) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumcraft-client-tweaks-forge-1.1.5.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.1.5` · 需要 ≥ 4.2.3.5 (build 20740) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumcraft-client-tweaks-neoforge-1.1.5.jar)

### Thaumic Additions: Reconstructed (Port) (`thaumadds`)

> Port of Thaumic Additions: Reconstructed onto Thaumcraft 4: Reconstructed (1.20.1 Forge / 1.21.1 NeoForge).

- **Minecraft 1.20.1** · Forge · 模组版本 `0.1.0` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumadds-1.20.1-0.1.0.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `0.1.0` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumadds-1.21.1-0.1.0.jar)

### Thaumic Horizons (`isorropia`)

> Thaumic Horizons (Isorropia) for Thaumcraft 4 Reborn on Minecraft 1.20.1 Forge and 1.21.1 NeoForge. / 神秘视界：为神秘时代4重生版带来生物注魔、源质机械与口袋位面。

- **Minecraft 1.20.1** · Forge · 模组版本 `1.0.7-alpha` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.20.1-1.0.7-alpha.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.0.7-alpha` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/isorropia-1.21.1-1.0.7-alpha.jar)

### Thaumic Tinkerer (`thaumictinkerer`)

> Expand Thaumcraft 4R with inventive magical tools, advanced enchantments, and arcane devices. Discover new ways to shape your world through thaumaturgy.

- **Minecraft 1.20.1** · Forge · 模组版本 `2.5-1.20.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-tinkerer-forge-2.5-1.20.1-port.0.1.0-20759.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `2.5-1.21.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumic-tinkerer-neoforge-2.5-1.21.1-port.0.1.0-20759.jar)

### Thaumic WarpFX (`warpfx`)

> EnhancedVisuals client effects for TC4R warp events and Warp Theory events.

- **Minecraft 1.20.1** · Forge · 模组版本 `0.1.0` · 需要 ≥ 4.2.3.5 (build 20739) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warpfx-1.20.1-forge-0.1.0.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `0.1.0` · 需要 ≥ 4.2.3.5 (build 20739) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warpfx-1.21.1-neoforge-0.1.0.jar)

### ThaumicEnergistics (`tc_energy` / `thaumicenergistics`)

> Bridges Thaumcraft Essentia with Applied Energistics 2 ME networks (Forge 1.20.1 port).

- **Minecraft 1.20.1** · Forge · 模组版本 `2.3.17-forge-alpha` · 需要 ≥ 4.2.3.5 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-2.3.17-forge-alpha.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `2.4.17-alpha` · 需要 ≥ 4.2.3.5 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/thaumicenergistics-1.21.1-neo-2.4.18-alpha.jar)

### Warp Theory (`warptheory`)

> Experience the unpredictable consequences of warp in Thaumcraft 4R, with strange events, unsettling hallucinations, and new ways to keep warp in check.

- **Minecraft 1.20.1** · Forge · 模组版本 `1.5.8-GTNH-1.20.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-forge-1.5.8-GTNH-1.20.1-port.0.1.0-20759.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.5.8-GTNH-1.21.1-port.0.1.0-20759` · 需要 ≥ 4.2.3.5 (build 20759) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/warp-theory-neoforge-1.5.8-GTNH-1.21.1-port.0.1.0-20759.jar)

### 秽玄天工 (`zmod`)

> 秽玄天工 1.20.1 Forge 移植版

- **Minecraft 1.20.1** · Forge · 模组版本 `1.30.12` · 需要 ≥ 4.2 · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-forge-1.20.1-1.30.12.jar)
- **Minecraft 1.21.1** · NeoForge · 模组版本 `1.30.26` · 需要 ≥ 4.2.3.5 (build 20738) · [下载](https://github.com/thaumcraft-port/thaumcraft-addons/releases/latest/download/huixuantiangong-neoforge-1.21.1-1.30.26.jar)

## 🔧 TC4R 版本对照

下表列出每个模组要求的最低 TC4R 内核构建号，来源是模组 `mods.toml` / `neoforge.mods.toml` 中 `thaumcraft` 依赖的版本范围。

| 模组 | MC | 加载器 | 模组版本 | TC4R 基线 | 最低构建号 | 通道 |
| --- | --- | --- | --- | --- | --- | --- |
| Forbidden Magic | 1.20.1 | Forge | `0.574-1.20.1-port.0.1.0-20759` | 4.2.3.5 | 20754 | 正式 |
| Forgotten Relics | 1.20.1 | Forge | `1.7.3-beta-1.20.1-port.0.1.0` | 0.1.0 | 任意 | 正式 |
| Middle-earth Thaumaturgy | 1.20.1 | Forge | `0.8.0-1.20.1` | 4.2.3.5 | 20759 | 正式 |
| Nodal Mechanics | 1.20.1 | Forge | `1.0.7-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| Pollution Unofficial | 1.20.1 | Forge | `1.0.0-1.20.1-port.0.1.0` | 4.2.3.5 | 20759 | 正式 |
| Tainted Magic | 1.20.1 | Forge | `8.1.1-1.20.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| Technomancy Unofficial | 1.20.1 | Forge | `0.1.0-dev` | 4.2.3.5 | 20753 | 正式 |
| Thaumcraft Client Tweaks | 1.20.1 | Forge | `1.1.5` | 4.2.3.5 | 20740 | 正式 |
| Thaumic Additions: Reconstructed (Port) | 1.20.1 | Forge | `0.1.0` | 4.2.3.5 | 20759 | 正式 |
| Thaumic Bases | 1.20.1 | Forge | `1.3.1710.4-1.20.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 实验 |
| Thaumic Bases | 1.20.1 | Forge | `1.3.1710.4-1.20.1-port.0.1.0-26c67473` | 4.2.3.5 | 任意 | 实验 |
| Thaumic Bases | 1.20.1 | Forge | `1.3.1710.4-1.20.1-port.0.1.0-9470460a` | 4.2.3.5 | 20738 | 实验 |
| Thaumic Bases | 1.20.1 | Forge | `1.3.1710.4-1.20.1-port.0.1.0-ebf949bf` | 4.2.3.5 | 20732 | 实验 |
| Thaumic Horizons | 1.20.1 | Forge | `1.0.7-alpha` | 4.2.3.5 | 20759 | 正式 |
| Thaumic Tinkerer | 1.20.1 | Forge | `2.5-1.20.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| Thaumic WarpFX | 1.20.1 | Forge | `0.1.0` | 4.2.3.5 | 20739 | 正式 |
| ThaumicEnergistics | 1.20.1 | Forge | `2.3.17-forge-alpha` | 4.2.3.5 | 任意 | 正式 |
| Warp Theory | 1.20.1 | Forge | `1.5.8-GTNH-1.20.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| 秽玄天工 | 1.20.1 | Forge | `1.30.12` | 4.2 | 任意 | 正式 |
| Forbidden Magic | 1.21.1 | NeoForge | `0.574-1.21.1-port.0.1.0-20759` | 4.2.3.5 | 20756 | 正式 |
| Nodal Mechanics | 1.21.1 | NeoForge | `1.0.7-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| Tainted Magic | 1.21.1 | NeoForge | `8.1.1-1.21.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| Technomancy Unofficial | 1.21.1 | NeoForge | `0.1.0-dev` | 4.2.3.5 | 20753 | 正式 |
| Thaumcraft Client Tweaks | 1.21.1 | NeoForge | `1.1.5` | 4.2.3.5 | 20740 | 正式 |
| Thaumic Additions: Reconstructed (Port) | 1.21.1 | NeoForge | `0.1.0` | 4.2.3.5 | 20759 | 正式 |
| Thaumic Bases | 1.21.1 | NeoForge | `1.3.1710.4-1.21.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 实验 |
| Thaumic Bases | 1.21.1 | NeoForge | `1.3.1710.4-1.21.1-port.0.1.0-26c67473` | 4.2.3.5 | 任意 | 实验 |
| Thaumic Bases | 1.21.1 | NeoForge | `1.3.1710.4-1.21.1-port.0.1.0-9470460a` | 4.2.3.5 | 20738 | 实验 |
| Thaumic Bases | 1.21.1 | NeoForge | `1.3.1710.4-1.21.1-port.0.1.0-ebf949bf` | 4.2.3.5 | 20732 | 实验 |
| Thaumic Horizons | 1.21.1 | NeoForge | `1.0.7-alpha` | 4.2.3.5 | 20759 | 正式 |
| Thaumic Tinkerer | 1.21.1 | NeoForge | `2.5-1.21.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| Thaumic WarpFX | 1.21.1 | NeoForge | `0.1.0` | 4.2.3.5 | 20739 | 正式 |
| ThaumicEnergistics | 1.21.1 | NeoForge | `2.4.17-alpha` | 4.2.3.5 | 任意 | 正式 |
| Warp Theory | 1.21.1 | NeoForge | `1.5.8-GTNH-1.21.1-port.0.1.0-20759` | 4.2.3.5 | 20759 | 正式 |
| 秽玄天工 | 1.21.1 | NeoForge | `1.30.26` | 4.2.3.5 | 20738 | 正式 |

## 🔐 校验和

<details>
<summary>点击展开全部 SHA-256 校验和</summary>

| 文件 | SHA-256 |
| --- | --- |
| `thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-20759.jar` | `8223a817c0092ef44f4cc1f1f03aed4d72c49512feede49fbad37218bd5d0db7` |
| `thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-26c67473.jar` | `7c6742eef8c011d010bff742f51530189227793a94336a7f6f5c3d3ddc269d8d` |
| `thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-9470460a.jar` | `5c7b565e60116a47373514a8ca42649ead14175a42fa73b3ea7e60f2d80ac50d` |
| `thaumic-bases-forge-1.3.1710.4-1.20.1-port.0.1.0-ebf949bf.jar` | `e48b6db8b990f0bc872e4b5c85b457b453ae0ca1fd690db5723fda65840b2204` |
| `forbidden-magic-forge-0.574-1.20.1-port.0.1.0-20759.jar` | `742b5c6449e6e9db3fff254e2e376fe7f0b3bb69c9c5f7e858a0379c39ab8063` |
| `forgottenrelics-1.20.1-1.7.3-beta-1.20.1-port.0.1.0.jar` | `28974bf373c83a4ee40397e3cb07a639f69b77297f6422a805011c35ff6c5ad8` |
| `isorropia-1.20.1-1.0.7-alpha.jar` | `88399117851681be7c095380f995a245e488cb79a615cb99c35976c7f95d19b8` |
| `mett-1.20.1-0.8.0-1.20.1.jar` | `b48026853c6cc81faaf74867baac7bcfe0e886856170a7c7115dfa27fe59c552` |
| `nodal-mechanics-forge-1.0.7-port.0.1.0-20759.jar` | `2518b6d3ae498bd44937f6516896fef5e726e18f9100f1bd15880dde937eea83` |
| `pollution-1.20.1-1.0.0-1.20.1-port.0.1.0.jar` | `4cf4ce00a5d695d527bfb6460f403c2126c75bf81cd2649334fe188e9360e6e7` |
| `tainted-magic-forge-8.1.1-1.20.1-port.0.1.0-20759.jar` | `e2e2f0fea477e51f4912e09c0d670022fd768906391d3e8bb9edf89b99857832` |
| `thaumcraft-client-tweaks-forge-1.1.5.jar` | `4d858adc7580cc804fa0b5363f6badfc3d68c5585d83568fe68600205408fce2` |
| `technom-1.20.1-0.1.0-dev.jar` | `02319ac8687299d6209c087a73060d2bb92b7c261c74741a166bdb93cc5e6a5e` |
| `thaumadds-1.20.1-0.1.0.jar` | `221db801f3699ad0fc039929f51bafbc72576394eff3e2a9945feeece52bfc7a` |
| `thaumicenergistics-2.3.17-forge-alpha.jar` | `1faacd6f7f2bcff1fed182caff97187ea7d8e2999cc38388465fcf48a2a4c35f` |
| `thaumic-tinkerer-forge-2.5-1.20.1-port.0.1.0-20759.jar` | `d3ceb2ce7a129450f5cdb44e43a326648576841730053e3e80074b7fe501bcfc` |
| `warpfx-1.20.1-forge-0.1.0.jar` | `9742a59cc2fa5725045ade274ad975d849ba436087539383fec28e5d3be513fb` |
| `warp-theory-forge-1.5.8-GTNH-1.20.1-port.0.1.0-20759.jar` | `de06056d89ecd8bee4c27c28558c372315dd3f829fb4399080bfc0b3d8cc133d` |
| `huixuantiangong-forge-1.20.1-1.30.12.jar` | `54c9d9c997c1dacaa0a19f7fdef8480f867923f7373b2ca800d6e027841746ff` |
| `thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-20759.jar` | `e98d2769b8b81637d806bf2919be2a12b215a6aed42f2908983eea8ccd67a0d4` |
| `thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-26c67473.jar` | `2d2a98dc9b74352a9c77a7c702d19d74669fbcc0ceffc3b29f0e2cbfeced6cc1` |
| `thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-9470460a.jar` | `8ed6299663195abcdde4fccc3d58f2e2028d7decf0d1c844f6f128edfc814d05` |
| `thaumic-bases-neoforge-1.3.1710.4-1.21.1-port.0.1.0-ebf949bf.jar` | `ce190dadbb3d28d25ff709b7a7c09177328abb1f1bd2afe014b5b6e3e909270e` |
| `forbidden-magic-neoforge-0.574-1.21.1-port.0.1.0-20759.jar` | `34aa54f65fd883059cc353bc04e891548480f5d7553ea4e16b85df7f16c0b5fc` |
| `isorropia-1.21.1-1.0.7-alpha.jar` | `1318a49d954934263e8d5fc733cd9aa8b6ab58e86bd48bd83c98ba6db3e358f0` |
| `nodal-mechanics-neoforge-1.0.7-port.0.1.0-20759.jar` | `92815dc25aa45302f0ec4083ec89dbe8b472654cafdac0febf7b4b45950d62f6` |
| `tainted-magic-neoforge-8.1.1-1.21.1-port.0.1.0-20759.jar` | `36130033048d5a0d0b745dc4a264311b7691ca010b52bcaa8b7ec633652e8709` |
| `thaumcraft-client-tweaks-neoforge-1.1.5.jar` | `2f9f5e60bb6f5caa64211d0dc52a0e1b90c287d90da1b2ca7660b4d77905df79` |
| `thaumicenergistics-1.21.1-neo-2.4.18-alpha.jar` | `b270a26ccf3707308c8a03252d47af98543338c94a1370c00c984a94c71b071c` |
| `technom-1.21.1-0.1.0-dev.jar` | `37eaed7dee38bc4f5aa9ba5d33344df865b3ced29b35c56ecbe0aa37135a7775` |
| `thaumadds-1.21.1-0.1.0.jar` | `75df27727c19d8456ed654cb91e0d90f9e3baa1e4d82843d1509e6b0ead588e1` |
| `thaumic-tinkerer-neoforge-2.5-1.21.1-port.0.1.0-20759.jar` | `0c88ca4214a09c3066c42588e6dada94f4cb3295525685242bd7539067a10fd3` |
| `warpfx-1.21.1-neoforge-0.1.0.jar` | `9595306fe6ba624abc94eb7911ae18078488cba989b1f010a3059921e941c913` |
| `warp-theory-neoforge-1.5.8-GTNH-1.21.1-port.0.1.0-20759.jar` | `5a661087fb0bef9566a957cfdbba3cbb28793c3e0a73e3609ecf7ca4c1f64abf` |
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

<sub>本 README 由 `scripts/gen_readme.py` 依据 `catalog/mods.json` 自动生成，请勿手工编辑；如需修改请编辑 `README.template.md`。生成时间：2026-11-04T05:40:14Z</sub>
