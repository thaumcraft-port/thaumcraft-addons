# Thaumcraft 4R / 神秘工匠 1.21.1 NeoForge 原生 API 完整参考

> 适用环境：Minecraft 1.21.1、NeoForge 21.1.248、Java 21。

本文是面向附属模组作者的原生 Java API 完整符号参考。定义直接取自当前原生 API Jar；正文逐项列出其中每个公开类型，以及该类型在 JVM 公共 ABI 中可见的常量、字段、构造器和方法。

## 1. 文档范围与完整性

- 本体 API 制品：`thaumcraft-neoforge-4.2.3.5-1.21.1-port.0.1.0-20713-api.jar`，共 289 个类型。
- 神秘工匠 API 制品：`thaumic-tinkerer-neoforge-2.5-1.21.1-port.0.1.0-20713-api.jar`，共 2 个类型。
- 本文合计收录 291 个类型；详细参考没有抽样或省略类型。
- 签名块使用完全限定类名，便于区分同名类型，并完整保留泛型、数组、可变参数在字节码中的形式和 `throws` 声明。
- 编译器生成但可公开调用的记录类访问器、枚举辅助方法和桥接方法也会列出，因为它们属于实际 ABI。
- 继承但未在当前类型重新声明的方法不重复展开；应查阅其父类或接口条目。
- JVM ABI 不保存可靠的形参名称，因此方法以形参类型序列为准；含义相近的重载必须按完整签名区分。

支持的主要入口位于 `dev.tc4port.thaumcraft.api` 和 `dev.tc4port.thaumictinkerer.api`。若详细清单出现 API 根包之外的类型，它是公开签名直接要求的原生类型；除此以外不要依赖本体或神秘工匠实现包。

## 2. Gradle 接入

```groovy
dependencies {
    compileOnly files('libs/thaumcraft-neoforge-4.2.3.5-1.21.1-port.0.1.0-20713-api.jar')
    compileOnly files('libs/thaumic-tinkerer-neoforge-2.5-1.21.1-port.0.1.0-20713-api.jar')

    runtimeOnly files('libs/thaumcraft-neoforge-4.2.3.5-1.21.1-port.0.1.0-20713.jar')
    runtimeOnly files('libs/thaumic-tinkerer-neoforge-2.5-1.21.1-port.0.1.0-20713.jar')
}
```

API Jar 只放在编译类路径；游戏运行时使用完整模组 Jar。附属成品不得打包本体、神秘工匠或它们的 API 类。神秘工匠的公开定义引用本体 API 类型，因此即使只调用神秘工匠 API，也要同时提供两个 API Jar。

## 3. 通用调用规则

- 返回 `Registration` 的方法具有显式生命周期。保持句柄强引用，在扩展失效时调用 `close()`；关闭操作是幂等的。
- 会改变玩家、实体、世界、法杖、节点、研究或 Warp 状态的调用必须在权威服务端及其正确线程执行。
- 接受 `VisAction.SIMULATE`/`EXECUTE` 的方法是事务边界：模拟不得产生副作用，只有执行阶段可以扣除资源或修改状态。
- 带 `generation()` 的注册表视图是可重载快照。资源重载后重新取得视图，不要永久缓存旧快照派生出的对象。
- `api.client` 仅在客户端环境调用；公共网络和表现接口不能替代服务端权限、目标和费用校验。
- 物品、实体或方块实体 SPI 只用于附属自己拥有的类。扩展其他模组对象时使用公开注册入口，不要通过反射或注入访问实现。

## 4. 包索引

| 包 | 类型数 | 职责 |
| --- | ---: | --- |
| `dev.tc4port.thaumcraft.api` | 6 | 本体总入口、注册句柄、内容引用、标签以及跨子系统辅助方法。 |
| `dev.tc4port.thaumcraft.api.alchemy` | 3 | 炼金设备、奥术风箱和蒸馏状态接口。 |
| `dev.tc4port.thaumcraft.api.aspect` | 20 | 要素标识、数量、注册表、Vis 费用与玩家要素池。 |
| `dev.tc4port.thaumcraft.api.block` | 2 | 方块相关的公共行为与守护灵气操作。 |
| `dev.tc4port.thaumcraft.api.champion` | 11 | 冠军生物词缀定义、目录和权威分配。 |
| `dev.tc4port.thaumcraft.api.client` | 31 | 仅客户端可调用的渲染、粒子和显示接口。 |
| `dev.tc4port.thaumcraft.api.damage` | 1 | 本体伤害类型键和伤害源工厂。 |
| `dev.tc4port.thaumcraft.api.data` | 11 | 公开数据结构、装备能力、法杖部件和数据映射值。 |
| `dev.tc4port.thaumcraft.api.effect` | 1 | 状态效果相关公共契约。 |
| `dev.tc4port.thaumcraft.api.entity` | 10 | 本体实体能力、要素球、弹射物和实体分类接口。 |
| `dev.tc4port.thaumcraft.api.essentia` | 11 | Essentia 容器、传输、源搜索和原子读写。 |
| `dev.tc4port.thaumcraft.api.event` | 19 | 附属可监听或触发的公共事件契约。 |
| `dev.tc4port.thaumcraft.api.flux` | 4 | Flux 消耗、查询和结果类型。 |
| `dev.tc4port.thaumcraft.api.focus` | 20 | 核心定义、状态、升级、参数和费用目录。 |
| `dev.tc4port.thaumcraft.api.focus.action` | 14 | 核心动作注册、目标、授权、事务和表现。 |
| `dev.tc4port.thaumcraft.api.golem` | 16 | 傀儡状态、标记、家位置与空间适配。 |
| `dev.tc4port.thaumcraft.api.integration` | 1 | 与其他模组交互时可用的稳定公共契约。 |
| `dev.tc4port.thaumcraft.api.inventory` | 1 | 公共容器和物品栏操作契约。 |
| `dev.tc4port.thaumcraft.api.item` | 14 | 附属自有物品可实现的装备、修复、揭示和法术接口。 |
| `dev.tc4port.thaumcraft.api.loot` | 1 | 战利品相关公共定义与查询。 |
| `dev.tc4port.thaumcraft.api.machine` | 7 | 奥术机器和方块实体的只读视图或受控操作。 |
| `dev.tc4port.thaumcraft.api.node` | 14 | 灵气节点定义、状态、并发更新和网络消费。 |
| `dev.tc4port.thaumcraft.api.player` | 6 | 玩家 Warp、同步和只读状态。 |
| `dev.tc4port.thaumcraft.api.presentation` | 3 | 服务端确认的音画表现、受众和表现数据。 |
| `dev.tc4port.thaumcraft.api.recipe` | 12 | 奥术、坩埚、注魔及附魔配方的公共查询与变换。 |
| `dev.tc4port.thaumcraft.api.research` | 26 | 研究键、目录、完成状态、扫描、页面和研究条件。 |
| `dev.tc4port.thaumcraft.api.taint` | 2 | 腐化生物群系和腐化行为接口。 |
| `dev.tc4port.thaumcraft.api.vis` | 3 | Vis 网络、来源和消费操作。 |
| `dev.tc4port.thaumcraft.api.wand` | 16 | 法杖状态、杖柄、杖帽、充能、载体和机器上下文。 |
| `dev.tc4port.thaumcraft.api.wand.behavior` | 3 | 服务端法杖行为、使用阶段和回调。 |
| `dev.tc4port.thaumictinkerer.api.enchantment` | 2 | 神秘工匠渗透附魔台的公开注册定义。 |

## 5. 完整类型索引

以下索引用于快速确认类型是否属于本版本的公开 API；同名嵌套类型以 `外部类.嵌套类` 显示。

### `dev.tc4port.thaumcraft.api`

- `Registration`（接口，Thaumcraft 4R 本体）
- `ThaumcraftApi`（类，Thaumcraft 4R 本体）
- `ThaumcraftApiCommon`（类，Thaumcraft 4R 本体）
- `ThaumcraftApiHelper`（类，Thaumcraft 4R 本体）
- `ThaumcraftContent`（类，Thaumcraft 4R 本体）
- `ThaumcraftTags`（类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.alchemy`

- `AlembicApi`（类，Thaumcraft 4R 本体）
- `AlembicSnapshot`（记录类，Thaumcraft 4R 本体）
- `ArcaneBellowsApi`（类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.aspect`

- `AspectAmounts`（记录类，Thaumcraft 4R 本体）
- `AspectApi`（类，Thaumcraft 4R 本体）
- `AspectBlendMode`（枚举，Thaumcraft 4R 本体）
- `AspectContainerView`（接口，Thaumcraft 4R 本体）
- `AspectDefinition`（记录类，Thaumcraft 4R 本体）
- `AspectId`（记录类，Thaumcraft 4R 本体）
- `AspectItemView`（接口，Thaumcraft 4R 本体）
- `AspectList`（类，Thaumcraft 4R 本体）
- `AspectPoolApi`（类，Thaumcraft 4R 本体）
- `AspectPoolFeedback`（枚举，Thaumcraft 4R 本体）
- `AspectPoolImport`（记录类，Thaumcraft 4R 本体）
- `AspectPoolImportResult`（记录类，Thaumcraft 4R 本体）
- `AspectRegistryView`（接口，Thaumcraft 4R 本体）
- `VisAction`（枚举，Thaumcraft 4R 本体）
- `VisChannel`（枚举，Thaumcraft 4R 本体）
- `VisConsumptionContext`（枚举，Thaumcraft 4R 本体）
- `VisCost`（类，Thaumcraft 4R 本体）
- `VisPaymentResult`（记录类，Thaumcraft 4R 本体）
- `WholeVisCost`（记录类，Thaumcraft 4R 本体）
- `AspectPoolImportResult.Status`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.block`

- `WardingAuraApi`（类，Thaumcraft 4R 本体）
- `WardingAuraResult`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.champion`

- `ChampionApi`（类，Thaumcraft 4R 本体）
- `ChampionAssignmentResult`（记录类，Thaumcraft 4R 本体）
- `ChampionAssignmentStatus`（枚举，Thaumcraft 4R 本体）
- `ChampionAttributeModifier`（记录类，Thaumcraft 4R 本体）
- `ChampionCategory`（枚举，Thaumcraft 4R 本体）
- `ChampionDefinition`（记录类，Thaumcraft 4R 本体）
- `ChampionDespawnPolicy`（枚举，Thaumcraft 4R 本体）
- `ChampionId`（记录类，Thaumcraft 4R 本体）
- `ChampionRegistryView`（接口，Thaumcraft 4R 本体）
- `ChampionSettings`（记录类，Thaumcraft 4R 本体）
- `ChampionVisual`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.client`

- `ActionPresentationContext`（记录类，Thaumcraft 4R 本体）
- `ActionPresentationHandler`（接口，Thaumcraft 4R 本体）
- `ArmorReduction`（接口，Thaumcraft 4R 本体）
- `ClientBehaviorHooks`（类，Thaumcraft 4R 本体）
- `ClothingLayerHooks`（类，Thaumcraft 4R 本体）
- `FortressArmorRenderApi`（类，Thaumcraft 4R 本体）
- `HeldItemRenderContext`（类，Thaumcraft 4R 本体）
- `HudHeartHooks`（类，Thaumcraft 4R 本体）
- `HudHeartPass`（接口，Thaumcraft 4R 本体）
- `ItemTickState`（接口，Thaumcraft 4R 本体）
- `ParticleCameraFade`（记录类，Thaumcraft 4R 本体）
- `ParticlePipeline`（类，Thaumcraft 4R 本体）
- `QueuedParticleType`（接口，Thaumcraft 4R 本体）
- `ResearchRecipeRenderContext`（接口，Thaumcraft 4R 本体）
- `ResearchRecipeRendererApi`（类，Thaumcraft 4R 本体）
- `ThaumcraftClientEffectsApi`（类，Thaumcraft 4R 本体）
- `ThaumcraftClientPresentationApi`（类，Thaumcraft 4R 本体）
- `ThaumcraftClientRenderApi`（类，Thaumcraft 4R 本体）
- `ThaumcraftClientRenderApiCommon`（类，Thaumcraft 4R 本体）
- `WandRenderApi`（类，Thaumcraft 4R 本体）
- `WorldRenderBoundary`（类，Thaumcraft 4R 本体）
- `WorldRenderContext`（记录类，Thaumcraft 4R 本体）
- `WorldRenderTransforms`（类，Thaumcraft 4R 本体）
- `ClientBehaviorHooks.BiomeColor`（接口，Thaumcraft 4R 本体）
- `ClientBehaviorHooks.HandLayer`（接口，Thaumcraft 4R 本体）
- `ClothingLayerHooks.Interceptor`（接口，Thaumcraft 4R 本体）
- `HudHeartHooks.Passes`（类，Thaumcraft 4R 本体）
- `ItemTickState.Access`（接口，Thaumcraft 4R 本体）
- `ThaumcraftClientRenderApiCommon.EffectUv`（记录类，Thaumcraft 4R 本体）
- `ThaumcraftClientRenderApiCommon.WorldRenderScope`（接口，Thaumcraft 4R 本体）
- `WorldRenderContext.Stage`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.damage`

- `ThaumcraftDamageTypes`（类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.data`

- `BlockAspectDefinition`（记录类，Thaumcraft 4R 本体）
- `EquipmentAbilityDefinition`（记录类，Thaumcraft 4R 本体）
- `NativeItemStateDeclarations`（类，Thaumcraft 4R 本体）
- `PechValueDefinition`（记录类，Thaumcraft 4R 本体）
- `RelayAttunementDefinition`（记录类，Thaumcraft 4R 本体）
- `WandCapDefinition`（记录类，Thaumcraft 4R 本体）
- `WandRodDefinition`（记录类，Thaumcraft 4R 本体）
- `WarpDefinition`（记录类，Thaumcraft 4R 本体）
- `BlockAspectDefinition.Mode`（枚举，Thaumcraft 4R 本体）
- `EquipmentAbilityDefinition.RunicTrait`（枚举，Thaumcraft 4R 本体）
- `RelayAttunementDefinition.Attunement`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.effect`

- `EffectCurePolicy`（接口，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.entity`

- `AspectOrbApi`（类，Thaumcraft 4R 本体）
- `AttributeTypes`（类，Thaumcraft 4R 本体）
- `EldritchMob`（接口，Thaumcraft 4R 本体）
- `EntityAspectApi`（类，Thaumcraft 4R 本体）
- `EntityNbtCondition`（记录类，Thaumcraft 4R 本体）
- `EntityScanIdentity`（记录类，Thaumcraft 4R 本体）
- `ExplosiveOrbApi`（类，Thaumcraft 4R 本体）
- `TaintSwarmApi`（类，Thaumcraft 4R 本体）
- `TaintedMob`（接口，Thaumcraft 4R 本体）
- `WispApi`（类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.essentia`

- `EssentiaApi`（类，Thaumcraft 4R 本体）
- `EssentiaContainerApi`（类，Thaumcraft 4R 本体）
- `EssentiaJarView`（接口，Thaumcraft 4R 本体）
- `EssentiaMultiStoreView`（接口，Thaumcraft 4R 本体）
- `EssentiaSearch`（记录类，Thaumcraft 4R 本体）
- `EssentiaSource`（接口，Thaumcraft 4R 本体）
- `EssentiaSourceRef`（记录类，Thaumcraft 4R 本体）
- `EssentiaTransferMode`（枚举，Thaumcraft 4R 本体）
- `EssentiaTransport`（接口，Thaumcraft 4R 本体）
- `FilledJarEssentiaApi`（类，Thaumcraft 4R 本体）
- `FilledJarEssentiaView`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.event`

- `AttributeOperation`（枚举，Thaumcraft 4R 本体）
- `BlockHarvest`（记录类，Thaumcraft 4R 本体）
- `CancellableHook`（类，Thaumcraft 4R 本体）
- `CriticalDecision`（记录类，Thaumcraft 4R 本体）
- `Damage`（记录类，Thaumcraft 4R 本体）
- `GameplayHooks`（类，Thaumcraft 4R 本体）
- `HarvestExperiencePolicy`（接口，Thaumcraft 4R 本体）
- `HookDecision`（记录类，Thaumcraft 4R 本体）
- `JigsawSelectionHooks`（类，Thaumcraft 4R 本体）
- `NativeEntityTicks`（类，Thaumcraft 4R 本体）
- `OrderedCallbacks`（类，Thaumcraft 4R 本体）
- `PlatformIdentity`（类，Thaumcraft 4R 本体）
- `WorldBehaviorHooks`（类，Thaumcraft 4R 本体）
- `GameplayHooks.GrowthDecision`（记录类，Thaumcraft 4R 本体）
- `GameplayHooks.TeleportDecision`（记录类，Thaumcraft 4R 本体）
- `JigsawSelectionHooks.Session`（接口，Thaumcraft 4R 本体）
- `WorldBehaviorHooks.ArrowSource`（接口，Thaumcraft 4R 本体）
- `WorldBehaviorHooks.RainLevel`（接口，Thaumcraft 4R 本体）
- `WorldBehaviorHooks.TickPermission`（接口，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.flux`

- `FluxApi`（类，Thaumcraft 4R 本体）
- `FluxConsumeContext`（记录类，Thaumcraft 4R 本体）
- `FluxConsumeEvent`（类，Thaumcraft 4R 本体）
- `FluxConsumeResult`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.focus`

- `FocusApi`（类，Thaumcraft 4R 本体）
- `FocusClientPresentation`（记录类，Thaumcraft 4R 本体）
- `FocusId`（记录类，Thaumcraft 4R 本体）
- `FocusIdentityItem`（接口，Thaumcraft 4R 本体）
- `FocusInstallResult`（枚举，Thaumcraft 4R 本体）
- `FocusInventorySourceItem`（接口，Thaumcraft 4R 本体）
- `FocusInventoryView`（接口，Thaumcraft 4R 本体）
- `FocusParameterValues`（记录类，Thaumcraft 4R 本体）
- `FocusParameters`（记录类，Thaumcraft 4R 本体）
- `FocusProfileDefinition`（记录类，Thaumcraft 4R 本体）
- `FocusPropertyUpdateResult`（枚举，Thaumcraft 4R 本体）
- `FocusRegistryView`（接口，Thaumcraft 4R 本体）
- `FocusStateView`（记录类，Thaumcraft 4R 本体）
- `FocusUpgradeDefinition`（记录类，Thaumcraft 4R 本体）
- `FocusUpgradeId`（记录类，Thaumcraft 4R 本体）
- `FocusParameters.Override`（记录类，Thaumcraft 4R 本体）
- `FocusParameters.Value`（记录类，Thaumcraft 4R 本体）
- `FocusProfileDefinition.CostMode`（枚举，Thaumcraft 4R 本体）
- `FocusProfileDefinition.CostOverride`（记录类，Thaumcraft 4R 本体）
- `FocusProfileDefinition.Requirement`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.focus.action`

- `FocusActionApi`（类，Thaumcraft 4R 本体）
- `FocusActionAuthorizer`（接口，Thaumcraft 4R 本体）
- `FocusActionContext`（接口，Thaumcraft 4R 本体）
- `FocusActionHandler`（接口，Thaumcraft 4R 本体）
- `FocusActionRegistryView`（接口，Thaumcraft 4R 本体）
- `FocusActionResult`（枚举，Thaumcraft 4R 本体）
- `FocusActionSpec`（记录类，Thaumcraft 4R 本体）
- `FocusActionTarget`（接口，Thaumcraft 4R 本体）
- `FocusActivation`（枚举，Thaumcraft 4R 本体）
- `FocusAuthorization`（记录类，Thaumcraft 4R 本体）
- `FocusAuthorizationContext`（接口，Thaumcraft 4R 本体）
- `FocusCastAnimation`（枚举，Thaumcraft 4R 本体）
- `FocusActionTarget.Focus`（记录类，Thaumcraft 4R 本体）
- `FocusActionTarget.Upgrade`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.golem`

- `GolemApi`（类，Thaumcraft 4R 本体）
- `GolemControlApi`（类，Thaumcraft 4R 本体）
- `GolemControlResult`（枚举，Thaumcraft 4R 本体）
- `GolemMarkerView`（记录类，Thaumcraft 4R 本体）
- `GolemRecoveryAction`（接口，Thaumcraft 4R 本体）
- `GolemSpatialAdapter`（接口，Thaumcraft 4R 本体）
- `GolemSpatialAdapters`（类，Thaumcraft 4R 本体）
- `GolemTravelContext`（记录类，Thaumcraft 4R 本体）
- `GolemTravelFrame`（记录类，Thaumcraft 4R 本体）
- `GolemTravelTarget`（接口，Thaumcraft 4R 本体）
- `GolemView`（记录类，Thaumcraft 4R 本体）
- `GolemRecoveryAction.ControlledStep`（记录类，Thaumcraft 4R 本体）
- `GolemRecoveryAction.Path`（记录类，Thaumcraft 4R 本体）
- `GolemTravelTarget.BlockTarget`（记录类，Thaumcraft 4R 本体）
- `GolemTravelTarget.EntityTarget`（记录类，Thaumcraft 4R 本体）
- `GolemTravelTarget.PointTarget`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.integration`

- `JadeRegistration`（类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.inventory`

- `FakeSlot`（接口，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.item`

- `AuraRevealingGear`（接口，Thaumcraft 4R 本体）
- `ExtendedRepairableGear`（接口，Thaumcraft 4R 本体）
- `GogglesOverlayGear`（接口，Thaumcraft 4R 本体）
- `InfusionEquipmentApi`（类，Thaumcraft 4R 本体）
- `ItemProperties`（类，Thaumcraft 4R 本体）
- `ItemStatePlatform`（类，Thaumcraft 4R 本体）
- `RepairableGear`（接口，Thaumcraft 4R 本体）
- `RunicGear`（接口，Thaumcraft 4R 本体）
- `ScribeTools`（接口，Thaumcraft 4R 本体）
- `ThaumcraftItemApi`（类，Thaumcraft 4R 本体）
- `ToolProperties`（类，Thaumcraft 4R 本体）
- `VisDiscountGear`（接口，Thaumcraft 4R 本体）
- `WarpingGear`（接口，Thaumcraft 4R 本体）
- `WispEssenceFactory`（类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.loot`

- `LootBagTier`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.machine`

- `ArcaneBoreView`（接口，Thaumcraft 4R 本体）
- `ArcaneEarControlApi`（类，Thaumcraft 4R 本体）
- `ArcaneEarControlResult`（枚举，Thaumcraft 4R 本体）
- `ArcaneEarView`（接口，Thaumcraft 4R 本体）
- `BrainJarView`（接口，Thaumcraft 4R 本体）
- `DeconstructionTableView`（接口，Thaumcraft 4R 本体）
- `InfusionPedestal`（接口，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.node`

- `AuraNodeState`（记录类，Thaumcraft 4R 本体）
- `AuraNodeView`（接口，Thaumcraft 4R 本体）
- `NodeApi`（类，Thaumcraft 4R 本体）
- `NodeAspectProfile`（枚举，Thaumcraft 4R 本体）
- `NodeGenerationSettings`（记录类，Thaumcraft 4R 本体）
- `NodeModifierDefinition`（记录类，Thaumcraft 4R 本体）
- `NodeModifierId`（记录类，Thaumcraft 4R 本体）
- `NodeRegistryView`（接口，Thaumcraft 4R 本体）
- `NodeStateChangeResult`（枚举，Thaumcraft 4R 本体）
- `NodeTypeDefinition`（记录类，Thaumcraft 4R 本体）
- `NodeTypeId`（记录类，Thaumcraft 4R 本体）
- `NodeVis`（记录类，Thaumcraft 4R 本体）
- `VisNetworkApi`（类，Thaumcraft 4R 本体）
- `VisSource`（接口，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.player`

- `FlightAccess`（类，Thaumcraft 4R 本体）
- `NetworkPositionInterpolation`（接口，Thaumcraft 4R 本体）
- `PlayerMovementApi`（类，Thaumcraft 4R 本体）
- `PlayerWarpApi`（类，Thaumcraft 4R 本体）
- `PlayerWarpView`（记录类，Thaumcraft 4R 本体）
- `NetworkPositionInterpolation.Position`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.presentation`

- `ActionPresentationApi`（类，Thaumcraft 4R 本体）
- `ActionPresentationAudience`（枚举，Thaumcraft 4R 本体）
- `WorldEffectsApi`（类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.recipe`

- `ArcaneCraftingApi`（类，Thaumcraft 4R 本体）
- `ArcaneCraftingRecipe`（接口，Thaumcraft 4R 本体）
- `InfusionCentralTransformation`（接口，Thaumcraft 4R 本体）
- `InfusionEnchantmentApi`（类，Thaumcraft 4R 本体）
- `InfusionEnchantmentCost`（记录类，Thaumcraft 4R 本体）
- `InfusionEnchantmentRecipe`（接口，Thaumcraft 4R 本体）
- `InfusionEnchantmentScaling`（记录类，Thaumcraft 4R 本体）
- `InfusionEnchantmentStage`（记录类，Thaumcraft 4R 本体）
- `InfusionInputPatch`（接口，Thaumcraft 4R 本体）
- `InfusionInputPatchApi`（类，Thaumcraft 4R 本体）
- `InfusionEnchantmentApi.Entry`（记录类，Thaumcraft 4R 本体）
- `InfusionEnchantmentRecipe.Result`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.research`

- `ResearchApi`（类，Thaumcraft 4R 本体）
- `ResearchCategoryKey`（记录类，Thaumcraft 4R 本体）
- `ResearchCategorySummary`（记录类，Thaumcraft 4R 本体）
- `ResearchClientPage`（记录类，Thaumcraft 4R 本体）
- `ResearchClientPresentation`（记录类，Thaumcraft 4R 本体）
- `ResearchCompletionContext`（记录类，Thaumcraft 4R 本体）
- `ResearchCompletionReason`（枚举，Thaumcraft 4R 本体）
- `ResearchCompletionResult`（枚举，Thaumcraft 4R 本体）
- `ResearchCraftingExample`（记录类，Thaumcraft 4R 本体）
- `ResearchCraftingRecipe`（接口，Thaumcraft 4R 本体）
- `ResearchDifficulty`（枚举，Thaumcraft 4R 本体）
- `ResearchDiscoveryResult`（枚举，Thaumcraft 4R 本体）
- `ResearchEntryFlag`（枚举，Thaumcraft 4R 本体）
- `ResearchEntrySummary`（记录类，Thaumcraft 4R 本体）
- `ResearchKey`（记录类，Thaumcraft 4R 本体）
- `ResearchKeyPrefix`（记录类，Thaumcraft 4R 本体）
- `ResearchRecipeDisplay`（记录类，Thaumcraft 4R 本体）
- `ResearchRecipeDisplayApi`（类，Thaumcraft 4R 本体）
- `ResearchRegistryView`（接口，Thaumcraft 4R 本体）
- `ResearchRequirement`（记录类，Thaumcraft 4R 本体）
- `ResearchSelectorExclusion`（记录类，Thaumcraft 4R 本体）
- `ResearchTableApi`（类，Thaumcraft 4R 本体）
- `ScanApi`（类，Thaumcraft 4R 本体）
- `ScanHandler`（接口，Thaumcraft 4R 本体）
- `ScanPhenomenon`（记录类，Thaumcraft 4R 本体）
- `ResearchClientPage.Type`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.taint`

- `TaintBiomeApi`（类，Thaumcraft 4R 本体）
- `TaintBiomeChangeResult`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.vis`

- `OwnedVisStorageProvider`（接口，Thaumcraft 4R 本体）
- `VisStorageApi`（类，Thaumcraft 4R 本体）
- `VisStorageView`（记录类，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.wand`

- `CustomWandItem`（类，Thaumcraft 4R 本体）
- `CustomWandSpec`（记录类，Thaumcraft 4R 本体）
- `VisTransferResult`（记录类，Thaumcraft 4R 本体）
- `WandApi`（类，Thaumcraft 4R 本体）
- `WandCapSpec`（记录类，Thaumcraft 4R 本体）
- `WandCarrierItem`（类，Thaumcraft 4R 本体）
- `WandMachineContext`（记录类，Thaumcraft 4R 本体）
- `WandMaterialId`（记录类，Thaumcraft 4R 本体）
- `WandPartApi`（类，Thaumcraft 4R 本体）
- `WandPartAssemblyMode`（枚举，Thaumcraft 4R 本体）
- `WandPartChangeResult`（枚举，Thaumcraft 4R 本体）
- `WandPartLimits`（类，Thaumcraft 4R 本体）
- `WandRechargeSpec`（记录类，Thaumcraft 4R 本体）
- `WandRodSpec`（记录类，Thaumcraft 4R 本体）
- `WandView`（接口，Thaumcraft 4R 本体）
- `WandRechargeSpec.Mode`（枚举，Thaumcraft 4R 本体）

### `dev.tc4port.thaumcraft.api.wand.behavior`

- `WandBehaviorApi`（类，Thaumcraft 4R 本体）
- `WandServerBehavior`（接口，Thaumcraft 4R 本体）
- `WandServerContext`（接口，Thaumcraft 4R 本体）

### `dev.tc4port.thaumictinkerer.api.enchantment`

- `OsmoticEnchantmentApi`（类，神秘工匠）
- `OsmoticEnchantmentDefinition`（记录类，神秘工匠）

## 6. 所有公开定义

本节是完整参考主体。每个 Java 代码块对应一个原生类文件的公共声明。

## 6.1 `dev.tc4port.thaumcraft.api`

本体总入口、注册句柄、内容引用、标签以及跨子系统辅助方法。

### `dev.tc4port.thaumcraft.api.Registration`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.Registration extends java.lang.AutoCloseable {
  public abstract void close();
  public static dev.tc4port.thaumcraft.api.Registration of(java.lang.Runnable);
  public static dev.tc4port.thaumcraft.api.Registration empty();
}
```

### `dev.tc4port.thaumcraft.api.ThaumcraftApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.ThaumcraftApi extends dev.tc4port.thaumcraft.api.ThaumcraftApiCommon {
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.data.WandRodDefinition> WAND_ROD_DATA;
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.level.block.Block, dev.tc4port.thaumcraft.api.data.BlockAspectDefinition> BLOCK_ASPECT_DATA;
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.data.WandCapDefinition> WAND_CAP_DATA;
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.data.WarpDefinition> CRAFTING_WARP_DATA;
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.data.WarpDefinition> EQUIPPED_WARP_DATA;
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.data.PechValueDefinition> PECH_VALUE_DATA;
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition> EQUIPMENT_ABILITY_DATA;
  public static final net.neoforged.neoforge.registries.datamaps.DataMapType<net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition> VIS_RELAY_ATTUNEMENT_DATA;
  public static dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition equipmentAbilities(net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.data.WarpDefinition equippedWarp(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.ThaumcraftApiCommon`

归属：Thaumcraft 4R 本体；类型：类。

```java
public abstract class dev.tc4port.thaumcraft.api.ThaumcraftApiCommon {
  public static final int MAX_INFUSION_INSTABILITY = 499;
  public static final int MAX_INFUSION_COMPONENTS = 288;
  public static final net.minecraft.world.item.Tier TOOL_MATERIAL_THAUMIUM;
  public static final net.minecraft.world.item.Tier TOOL_MATERIAL_VOID;
  public static final net.minecraft.world.item.Tier TOOL_MATERIAL_ELEMENTAL;
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.item.enchantment.Enchantment> ENCHANTMENT_HASTE;
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.item.enchantment.Enchantment> ENCHANTMENT_REPAIR;
  public static dev.tc4port.thaumcraft.api.Registration registerScanHandler(dev.tc4port.thaumcraft.api.research.ScanHandler);
  public static dev.tc4port.thaumcraft.api.Registration registerEntityAspects(net.minecraft.resources.ResourceLocation, net.minecraft.world.entity.EntityType<?>, dev.tc4port.thaumcraft.api.entity.EntityScanIdentity, dev.tc4port.thaumcraft.api.aspect.AspectAmounts, dev.tc4port.thaumcraft.api.entity.EntityNbtCondition...);
  public static <T extends net.minecraft.world.entity.item.ItemEntity> dev.tc4port.thaumcraft.api.Registration registerObjectScannedEntityType(net.minecraft.world.entity.EntityType<T>);
  public static dev.tc4port.thaumcraft.api.Registration registerSmeltingBonus(net.minecraft.world.item.Item, net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.Registration registerSmeltingBonus(net.minecraft.tags.TagKey<net.minecraft.world.item.Item>, net.minecraft.world.item.ItemStack);
  public static net.minecraft.world.item.ItemStack getSmeltingBonus(net.minecraft.world.item.ItemStack);
  public static boolean hasObjectAspectDefinition(net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.Registration registerObjectAspects(net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public static dev.tc4port.thaumcraft.api.Registration registerBlockAspects(net.minecraft.world.level.block.Block, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public static dev.tc4port.thaumcraft.api.Registration registerBlockAspects(net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block>, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts blockAspects(net.minecraft.world.level.block.state.BlockState);
  public static long blockAspectGeneration();
  public static dev.tc4port.thaumcraft.api.Registration registerObjectAspects(net.minecraft.tags.TagKey<net.minecraft.world.item.Item>, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public static dev.tc4port.thaumcraft.api.Registration registerObjectScanGroup(net.minecraft.resources.ResourceLocation, java.util.List<net.minecraft.world.item.Item>);
  public static dev.tc4port.thaumcraft.api.Registration registerItemWarp(net.minecraft.world.item.Item, int);
  public static int getWarp(net.minecraft.world.item.ItemStack);
  public static boolean isPortableHoleBlacklisted(net.minecraft.world.level.block.state.BlockState);
  public static boolean areMirrorsEnabled();
  public static dev.tc4port.thaumcraft.api.Registration registerPortableHoleBlacklist(net.minecraft.world.level.block.Block...);
  public static dev.tc4port.thaumcraft.api.Registration registerLootBagItem(net.minecraft.resources.ResourceLocation, net.minecraft.world.item.ItemStack, int, dev.tc4port.thaumcraft.api.loot.LootBagTier...);
  public static dev.tc4port.thaumcraft.api.Registration registerInfusionCentralTransformation(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.recipe.InfusionCentralTransformation);
}
```

### `dev.tc4port.thaumcraft.api.ThaumcraftApiHelper`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.ThaumcraftApiHelper {
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts cullTags(dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public static boolean hasDiscoveredAspect(net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId> getDiscoveredAspectIds(net.minecraft.world.entity.player.Player);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts getAspectPools(net.minecraft.world.entity.player.Player);
  public static net.minecraft.world.item.ItemStack getStackInRowAndColumn(net.minecraft.world.item.crafting.CraftingInput, int, int);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts getObjectAspects(net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts getBonusObjectTags(net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts generateTags(net.minecraft.world.item.ItemStack);
  public static boolean areItemStackTagsEqualForCrafting(net.minecraft.world.item.ItemStack, net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.essentia.EssentiaTransport getConnectableTransport(net.minecraft.world.level.BlockGetter, net.minecraft.core.BlockPos, net.minecraft.core.Direction);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts getAllAspects(int);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts getAllCompoundAspects(int);
  public static dev.tc4port.thaumcraft.api.aspect.VisPaymentResult consumeVisFromWand(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction, dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext);
  public static dev.tc4port.thaumcraft.api.aspect.VisPaymentResult consumeVisFromWand(net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.wand.WandMachineContext, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction, dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext);
  public static dev.tc4port.thaumcraft.api.aspect.VisPaymentResult consumeExactVisFromWand(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player, java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.aspect.VisPaymentResult consumeExactVisFromWand(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.aspect.VisPaymentResult consumeVisFromInventory(net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static int consumeUpToVisFromInventory(net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.aspect.VisChannel, int);
  public static void addWarpToPlayer(net.minecraft.server.level.ServerPlayer, int, boolean);
  public static void addStickyWarpToPlayer(net.minecraft.server.level.ServerPlayer, int);
  public static net.minecraft.world.phys.BlockHitResult rayTraceIgnoringSource(net.minecraft.world.level.Level, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, boolean, boolean, boolean);
}
```

### `dev.tc4port.thaumcraft.api.ThaumcraftContent`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.ThaumcraftContent {
  public static net.minecraft.world.item.Item item(java.lang.String);
  public static net.minecraft.world.level.block.Block block(java.lang.String);
  public static net.minecraft.sounds.SoundEvent sound(java.lang.String);
  public static net.minecraft.world.level.block.entity.BlockEntityType<?> blockEntity(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.ThaumcraftTags`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.ThaumcraftTags {
  public static final net.minecraft.tags.TagKey<net.minecraft.world.item.Item> THAUMIUM_INGOTS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> INCORRECT_FOR_THAUMIUM_TOOL;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.item.Item> REPAIRABLE_ITEMS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.item.Item> CRAFTING_TRANSMUTATION_CATALYSTS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.item.Item> INFUSION_MASK_HELMETS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.item.Item> WAND_RODS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.item.Item> STAFF_CORES;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.item.Item> WAND_CAPS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> INFUSION_STABILIZERS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> PORTABLE_HOLE_BLACKLIST;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> LAMP_GROWTH_BLACKLIST;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> GOLEM_STANDARD_CROPS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> GOLEM_CLICKABLE_CROPS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> GOLEM_STACKED_CROPS;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> GREATWOOD_GROWS_ON;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> SILVERWOOD_GROWS_ON;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> NODE_GENERATION_REPLACEABLE;
  public static final net.minecraft.tags.TagKey<net.minecraft.world.level.block.Block> WARDING_AURA_SOURCES;
}
```

## 6.2 `dev.tc4port.thaumcraft.api.alchemy`

炼金设备、奥术风箱和蒸馏状态接口。

### `dev.tc4port.thaumcraft.api.alchemy.AlembicApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.alchemy.AlembicApi {
  public static java.util.Optional<dev.tc4port.thaumcraft.api.alchemy.AlembicSnapshot> snapshot(net.minecraft.world.level.Level, net.minecraft.core.BlockPos);
  public static int insertLoaded(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
}
```

### `dev.tc4port.thaumcraft.api.alchemy.AlembicSnapshot`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.alchemy.AlembicSnapshot extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.alchemy.AlembicSnapshot(dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.AspectId, int, int);
  public int remainingCapacity();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.aspect.AspectId storedAspect();
  public dev.tc4port.thaumcraft.api.aspect.AspectId filter();
  public int amount();
  public int capacity();
}
```

### `dev.tc4port.thaumcraft.api.alchemy.ArcaneBellowsApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.alchemy.ArcaneBellowsApi {
  public static boolean blowsToward(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, net.minecraft.core.BlockPos);
  public static int countAdjacentBlowingToward(net.minecraft.world.level.Level, net.minecraft.core.BlockPos);
}
```

## 6.3 `dev.tc4port.thaumcraft.api.aspect`

要素标识、数量、注册表、Vis 费用与玩家要素池。

### `dev.tc4port.thaumcraft.api.aspect.AspectAmounts`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectAmounts extends java.lang.Record {
  public static final dev.tc4port.thaumcraft.api.aspect.AspectAmounts EMPTY;
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts(java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer>);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts of(dev.tc4port.thaumcraft.api.aspect.AspectId, int);
  public int amount(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer> amounts();
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectApi {
  public static dev.tc4port.thaumcraft.api.aspect.AspectRegistryView registry();
  public static java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.AspectDefinition> definitions();
  public static java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId> primals();
  public static dev.tc4port.thaumcraft.api.aspect.AspectDefinition get(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static boolean contains(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.aspect.AspectId> combination(dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static net.minecraft.network.chat.MutableComponent tooltipName(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static net.minecraft.network.chat.MutableComponent tooltipDescription(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static net.minecraft.network.chat.MutableComponent tooltipEntry(dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.String);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.aspect.AspectAmounts> getBlockAspects(net.minecraft.world.level.block.entity.BlockEntity);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts getItemAspects(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectBlendMode`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectBlendMode extends java.lang.Enum<dev.tc4port.thaumcraft.api.aspect.AspectBlendMode> {
  public static final dev.tc4port.thaumcraft.api.aspect.AspectBlendMode ADDITIVE;
  public static final dev.tc4port.thaumcraft.api.aspect.AspectBlendMode NORMAL;
  public static dev.tc4port.thaumcraft.api.aspect.AspectBlendMode[] values();
  public static dev.tc4port.thaumcraft.api.aspect.AspectBlendMode valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectContainerView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.aspect.AspectContainerView {
  public abstract dev.tc4port.thaumcraft.api.aspect.AspectAmounts visibleAspects();
  public default java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId> visibleAspectOrder();
  public default java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId> visibleAspectFilters();
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectDefinition extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.aspect.AspectDefinition(dev.tc4port.thaumcraft.api.aspect.AspectId, int, java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId>, net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.aspect.AspectBlendMode, int, java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisChannel>);
  public boolean primal();
  public boolean isVisChannel();
  public java.lang.String name();
  public java.lang.String descriptionKey();
  public net.minecraft.network.chat.Component description();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.aspect.AspectId id();
  public int color();
  public java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId> components();
  public net.minecraft.resources.ResourceLocation texture();
  public dev.tc4port.thaumcraft.api.aspect.AspectBlendMode blendMode();
  public int naturalGenerationWeight();
  public java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisChannel> visChannel();
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectId`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectId extends java.lang.Record implements java.lang.Comparable<dev.tc4port.thaumcraft.api.aspect.AspectId> {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.aspect.AspectId> CODEC;
  public dev.tc4port.thaumcraft.api.aspect.AspectId(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.aspect.AspectId of(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.aspect.AspectId parse(java.lang.String);
  public java.lang.String serialized();
  public int compareTo(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation value();
  public int compareTo(java.lang.Object);
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectItemView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.aspect.AspectItemView {
  public abstract dev.tc4port.thaumcraft.api.aspect.AspectAmounts storedAspectData(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectList`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectList {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.aspect.AspectList> CODEC;
  public dev.tc4port.thaumcraft.api.aspect.AspectList();
  public dev.tc4port.thaumcraft.api.aspect.AspectList(java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer>);
  public dev.tc4port.thaumcraft.api.aspect.AspectList copy();
  public int size();
  public int visSize();
  public boolean contains(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public int amount(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId> aspects();
  public java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId> primalAspects();
  public java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId> aspectsSorted();
  public java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId> aspectsSortedByAmount();
  public boolean reduce(dev.tc4port.thaumcraft.api.aspect.AspectId, int);
  public dev.tc4port.thaumcraft.api.aspect.AspectList remove(dev.tc4port.thaumcraft.api.aspect.AspectId, int);
  public dev.tc4port.thaumcraft.api.aspect.AspectList remove(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public dev.tc4port.thaumcraft.api.aspect.AspectList add(dev.tc4port.thaumcraft.api.aspect.AspectId, int);
  public dev.tc4port.thaumcraft.api.aspect.AspectList merge(dev.tc4port.thaumcraft.api.aspect.AspectId, int);
  public dev.tc4port.thaumcraft.api.aspect.AspectList add(dev.tc4port.thaumcraft.api.aspect.AspectList);
  public dev.tc4port.thaumcraft.api.aspect.AspectList merge(dev.tc4port.thaumcraft.api.aspect.AspectList);
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer> asMap();
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectPoolApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectPoolApi {
  public static boolean addSilently(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.aspect.AspectId, int);
  public static int add(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static int add(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static boolean discover(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult importBatch(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.aspect.AspectPoolImport, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback extends java.lang.Enum<dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback> {
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback POOL_GAIN;
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback DISCOVER_IF_NEW;
  public static dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback[] values();
  public static dev.tc4port.thaumcraft.api.aspect.AspectPoolFeedback valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectPoolImport`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectPoolImport extends java.lang.Record {
  public static final int MAX_ASPECTS = 256;
  public dev.tc4port.thaumcraft.api.aspect.AspectPoolImport(java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId>, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId> discoveries();
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts additions();
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult(dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status, java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId>, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status status();
  public java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId> newlyDiscovered();
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts additions();
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectRegistryView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.aspect.AspectRegistryView {
  public abstract long generation();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.AspectDefinition> definitions();
  public abstract java.util.Optional<dev.tc4port.thaumcraft.api.aspect.AspectDefinition> get(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public abstract java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId> primals();
  public abstract java.util.Set<dev.tc4port.thaumcraft.api.aspect.AspectId> compounds();
  public abstract java.util.List<dev.tc4port.thaumcraft.api.aspect.VisChannel> visChannels();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer> naturalPrimalWeights();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer> naturalCompoundWeights();
  public abstract dev.tc4port.thaumcraft.api.aspect.AspectId selectNaturalPrimal(long);
  public abstract dev.tc4port.thaumcraft.api.aspect.AspectId selectNaturalCompound(long);
  public abstract java.util.Optional<dev.tc4port.thaumcraft.api.aspect.AspectId> combination(dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.AspectId);
}
```

### `dev.tc4port.thaumcraft.api.aspect.VisAction`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.aspect.VisAction extends java.lang.Enum<dev.tc4port.thaumcraft.api.aspect.VisAction> {
  public static final dev.tc4port.thaumcraft.api.aspect.VisAction SIMULATE;
  public static final dev.tc4port.thaumcraft.api.aspect.VisAction EXECUTE;
  public static dev.tc4port.thaumcraft.api.aspect.VisAction[] values();
  public static dev.tc4port.thaumcraft.api.aspect.VisAction valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.aspect.VisChannel`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.aspect.VisChannel extends java.lang.Enum<dev.tc4port.thaumcraft.api.aspect.VisChannel> {
  public static final dev.tc4port.thaumcraft.api.aspect.VisChannel AER;
  public static final dev.tc4port.thaumcraft.api.aspect.VisChannel TERRA;
  public static final dev.tc4port.thaumcraft.api.aspect.VisChannel IGNIS;
  public static final dev.tc4port.thaumcraft.api.aspect.VisChannel AQUA;
  public static final dev.tc4port.thaumcraft.api.aspect.VisChannel ORDO;
  public static final dev.tc4port.thaumcraft.api.aspect.VisChannel PERDITIO;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.aspect.VisChannel> CODEC;
  public static dev.tc4port.thaumcraft.api.aspect.VisChannel[] values();
  public static dev.tc4port.thaumcraft.api.aspect.VisChannel valueOf(java.lang.String);
  public int index();
  public dev.tc4port.thaumcraft.api.aspect.AspectId aspectId();
  public static java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisChannel> fromIndex(int);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisChannel> fromAspectId(dev.tc4port.thaumcraft.api.aspect.AspectId);
}
```

### `dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext extends java.lang.Enum<dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext> {
  public static final dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext CRAFTING;
  public static final dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext CASTING;
  public static dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext[] values();
  public static dev.tc4port.thaumcraft.api.aspect.VisConsumptionContext valueOf(java.lang.String);
  public boolean crafting();
}
```

### `dev.tc4port.thaumcraft.api.aspect.VisCost`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.VisCost {
  public static dev.tc4port.thaumcraft.api.aspect.VisCost ofCentivis(java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>);
  public static dev.tc4port.thaumcraft.api.aspect.VisCost ofWholeVis(java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>);
  public static dev.tc4port.thaumcraft.api.aspect.VisCost ofCentivis(dev.tc4port.thaumcraft.api.aspect.VisChannel, int);
  public static dev.tc4port.thaumcraft.api.aspect.VisCost ofWholeVis(dev.tc4port.thaumcraft.api.aspect.VisChannel, int);
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> amounts();
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> wholeVis();
  public boolean equals(java.lang.Object);
  public int hashCode();
  public java.lang.String toString();
}
```

### `dev.tc4port.thaumcraft.api.aspect.VisPaymentResult`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.VisPaymentResult extends java.lang.Record {
  public static final dev.tc4port.thaumcraft.api.aspect.VisPaymentResult UNAVAILABLE;
  public static final dev.tc4port.thaumcraft.api.aspect.VisPaymentResult AVAILABLE;
  public static final dev.tc4port.thaumcraft.api.aspect.VisPaymentResult CONSUMED;
  public dev.tc4port.thaumcraft.api.aspect.VisPaymentResult(boolean, boolean);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public boolean affordable();
  public boolean consumed();
}
```

### `dev.tc4port.thaumcraft.api.aspect.WholeVisCost`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.aspect.WholeVisCost extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.aspect.WholeVisCost(java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>);
  public static dev.tc4port.thaumcraft.api.aspect.WholeVisCost of(dev.tc4port.thaumcraft.api.aspect.VisChannel, int);
  public dev.tc4port.thaumcraft.api.aspect.VisCost toCentivis();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> amounts();
}
```

### `dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status extends java.lang.Enum<dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status> {
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status EXECUTED;
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status SIMULATED;
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status NO_CHANGE;
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status UNKNOWN_ASPECT;
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status OVERFLOW;
  public static final dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status OFF_SERVER_THREAD;
  public static dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status[] values();
  public static dev.tc4port.thaumcraft.api.aspect.AspectPoolImportResult$Status valueOf(java.lang.String);
}
```

## 6.4 `dev.tc4port.thaumcraft.api.block`

方块相关的公共行为与守护灵气操作。

### `dev.tc4port.thaumcraft.api.block.WardingAuraApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.block.WardingAuraApi {
  public static boolean isAura(net.minecraft.world.level.block.state.BlockState);
  public static boolean ensureAura(net.minecraft.world.level.Level, net.minecraft.core.BlockPos);
  public static dev.tc4port.thaumcraft.api.block.WardingAuraResult ensureLoadedAura(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos);
  public static void syncBlockingState(net.minecraft.world.level.Level, net.minecraft.core.BlockPos);
  public static dev.tc4port.thaumcraft.api.block.WardingAuraResult syncLoadedBlockingState(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos);
  public static net.minecraft.core.BlockPos sourcePosition(net.minecraft.world.level.BlockGetter, net.minecraft.core.BlockPos);
}
```

### `dev.tc4port.thaumcraft.api.block.WardingAuraResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.block.WardingAuraResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.block.WardingAuraResult> {
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult CREATED;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult ALREADY_PRESENT;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult UPDATED;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult UNCHANGED;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult BLOCKED;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult NOT_AURA;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult OFF_SERVER_THREAD;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult CHUNK_UNLOADED;
  public static final dev.tc4port.thaumcraft.api.block.WardingAuraResult OUT_OF_BOUNDS;
  public static dev.tc4port.thaumcraft.api.block.WardingAuraResult[] values();
  public static dev.tc4port.thaumcraft.api.block.WardingAuraResult valueOf(java.lang.String);
  public boolean successful();
}
```

## 6.5 `dev.tc4port.thaumcraft.api.champion`

冠军生物词缀定义、目录和权威分配。

### `dev.tc4port.thaumcraft.api.champion.ChampionApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionApi {
  public static dev.tc4port.thaumcraft.api.champion.ChampionRegistryView registry();
  public static java.util.Optional<dev.tc4port.thaumcraft.api.champion.ChampionId> current(net.minecraft.world.entity.Mob);
  public static dev.tc4port.thaumcraft.api.champion.ChampionAssignmentResult assign(net.minecraft.world.entity.Mob, dev.tc4port.thaumcraft.api.champion.ChampionId, dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy);
  public static dev.tc4port.thaumcraft.api.champion.ChampionAssignmentResult assignRandom(net.minecraft.world.entity.Mob, dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy);
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionAssignmentResult`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionAssignmentResult extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.champion.ChampionAssignmentResult(dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus, java.util.Optional<dev.tc4port.thaumcraft.api.champion.ChampionId>);
  public boolean applied();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus status();
  public java.util.Optional<dev.tc4port.thaumcraft.api.champion.ChampionId> assignedId();
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus extends java.lang.Enum<dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus> {
  public static final dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus APPLIED;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus CLIENT_SIDE;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus ALREADY_CHAMPION;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus UNKNOWN_DEFINITION;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus UNSUPPORTED_MOB;
  public static dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus[] values();
  public static dev.tc4port.thaumcraft.api.champion.ChampionAssignmentStatus valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionAttributeModifier`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionAttributeModifier extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.champion.ChampionAttributeModifier(net.minecraft.resources.ResourceLocation, net.minecraft.resources.ResourceLocation, double, dev.tc4port.thaumcraft.api.event.AttributeOperation);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation attribute();
  public net.minecraft.resources.ResourceLocation modifierId();
  public double amount();
  public dev.tc4port.thaumcraft.api.event.AttributeOperation operation();
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionCategory`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionCategory extends java.lang.Enum<dev.tc4port.thaumcraft.api.champion.ChampionCategory> {
  public static final dev.tc4port.thaumcraft.api.champion.ChampionCategory PASSIVE;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionCategory OFFENSIVE;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionCategory DEFENSIVE;
  public static dev.tc4port.thaumcraft.api.champion.ChampionCategory[] values();
  public static dev.tc4port.thaumcraft.api.champion.ChampionCategory valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionDefinition extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.champion.ChampionDefinition(dev.tc4port.thaumcraft.api.champion.ChampionId, java.lang.String, dev.tc4port.thaumcraft.api.champion.ChampionCategory, net.minecraft.resources.ResourceLocation, java.util.Optional<dev.tc4port.thaumcraft.api.champion.ChampionVisual>, boolean, java.util.List<dev.tc4port.thaumcraft.api.champion.ChampionAttributeModifier>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.champion.ChampionId id();
  public java.lang.String nameKey();
  public dev.tc4port.thaumcraft.api.champion.ChampionCategory category();
  public net.minecraft.resources.ResourceLocation behavior();
  public java.util.Optional<dev.tc4port.thaumcraft.api.champion.ChampionVisual> visualEffect();
  public boolean randomEligible();
  public java.util.List<dev.tc4port.thaumcraft.api.champion.ChampionAttributeModifier> attributeModifiers();
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy extends java.lang.Enum<dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy> {
  public static final dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy UNCHANGED;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy PREVENT_DESPAWN;
  public static dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy[] values();
  public static dev.tc4port.thaumcraft.api.champion.ChampionDespawnPolicy valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionId`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionId extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.champion.ChampionId> CODEC;
  public dev.tc4port.thaumcraft.api.champion.ChampionId(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.champion.ChampionId of(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.champion.ChampionId parse(java.lang.String);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation value();
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionRegistryView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.champion.ChampionRegistryView {
  public abstract long generation();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.champion.ChampionId, dev.tc4port.thaumcraft.api.champion.ChampionDefinition> definitions();
  public abstract dev.tc4port.thaumcraft.api.champion.ChampionSettings settings();
  public abstract java.util.List<dev.tc4port.thaumcraft.api.champion.ChampionId> randomPool();
  public default java.util.Optional<dev.tc4port.thaumcraft.api.champion.ChampionDefinition> get(dev.tc4port.thaumcraft.api.champion.ChampionId);
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionSettings`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionSettings extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.champion.ChampionSettings(java.util.List<dev.tc4port.thaumcraft.api.champion.ChampionAttributeModifier>, float, dev.tc4port.thaumcraft.api.champion.ChampionId);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.List<dev.tc4port.thaumcraft.api.champion.ChampionAttributeModifier> baseAttributeModifiers();
  public float initialHealHealthPoints();
  public dev.tc4port.thaumcraft.api.champion.ChampionId creeperSubstituteId();
}
```

### `dev.tc4port.thaumcraft.api.champion.ChampionVisual`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.champion.ChampionVisual extends java.lang.Enum<dev.tc4port.thaumcraft.api.champion.ChampionVisual> {
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual BOLD;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual SPINE;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual ARMOR;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual MIGHTY;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual GRIM;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual WARDED;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual WARP;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual UNDYING;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual FIERY;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual SICKLY;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual VENOMOUS;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual VAMPIRIC;
  public static final dev.tc4port.thaumcraft.api.champion.ChampionVisual INFESTED;
  public static dev.tc4port.thaumcraft.api.champion.ChampionVisual[] values();
  public static dev.tc4port.thaumcraft.api.champion.ChampionVisual valueOf(java.lang.String);
}
```

## 6.6 `dev.tc4port.thaumcraft.api.client`

仅客户端可调用的渲染、粒子和显示接口。

### `dev.tc4port.thaumcraft.api.client.ActionPresentationContext`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.client.ActionPresentationContext extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.client.ActionPresentationContext(net.minecraft.resources.ResourceLocation, net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.entity.LivingEntity, net.minecraft.world.InteractionHand, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, java.util.Optional<net.minecraft.world.entity.Entity>, double, int, long, boolean);
  public java.util.Optional<net.minecraft.world.entity.LivingEntity> optionalSource();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation presentationId();
  public net.minecraft.client.multiplayer.ClientLevel level();
  public net.minecraft.world.entity.LivingEntity source();
  public net.minecraft.world.InteractionHand hand();
  public net.minecraft.world.phys.Vec3 sourcePosition();
  public net.minecraft.world.phys.Vec3 origin();
  public net.minecraft.world.phys.Vec3 target();
  public java.util.Optional<net.minecraft.world.entity.Entity> targetEntity();
  public double detail();
  public int value();
  public long seed();
  public boolean predicted();
}
```

### `dev.tc4port.thaumcraft.api.client.ActionPresentationHandler`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ActionPresentationHandler {
  public abstract void present(dev.tc4port.thaumcraft.api.client.ActionPresentationContext);
}
```

### `dev.tc4port.thaumcraft.api.client.ArmorReduction`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ArmorReduction {
  public abstract float apply(net.minecraft.world.damagesource.DamageSource, float, float);
}
```

### `dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks {
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.util.function.Predicate<net.minecraft.client.player.AbstractClientPlayer>> CAPE;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.util.function.BiPredicate<net.minecraft.world.entity.player.Player, net.minecraft.core.BlockPos>> DESTROY_BLOCK;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks$BiomeColor> BIOME_COLOR;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.util.function.BiConsumer<net.minecraft.client.model.HumanoidModel<?>, net.minecraft.world.entity.LivingEntity>> HUMANOID_POSE;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks$HandLayer> HAND_LAYER;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.util.function.BiPredicate<net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand>> EQUIP_RESET;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.lang.Runnable> BEFORE_DRAW;
  public static boolean allowCape(net.minecraft.client.player.AbstractClientPlayer);
  public static boolean allowDestroy(net.minecraft.world.entity.player.Player, net.minecraft.core.BlockPos);
  public static int biomeColor(net.minecraft.world.level.biome.Biome, boolean, double, double, int);
  public static void pose(net.minecraft.client.model.HumanoidModel<?>, net.minecraft.world.entity.LivingEntity);
  public static boolean allowHand(net.minecraft.world.entity.LivingEntity, net.minecraft.world.item.ItemStack, net.minecraft.world.item.ItemDisplayContext, net.minecraft.world.entity.HumanoidArm);
  public static boolean allowEquipReset(net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand);
  public static void beforeDraw();
}
```

### `dev.tc4port.thaumcraft.api.client.ClothingLayerHooks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.ClothingLayerHooks {
  public static void register(dev.tc4port.thaumcraft.api.client.ClothingLayerHooks$Interceptor);
  public static <T extends net.minecraft.world.entity.LivingEntity> void render(int, net.minecraft.client.model.EntityModel<T>, net.minecraft.resources.ResourceLocation, com.mojang.blaze3d.vertex.PoseStack, net.minecraft.client.renderer.MultiBufferSource, int, T, int, java.lang.Runnable);
}
```

### `dev.tc4port.thaumcraft.api.client.FortressArmorRenderApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.FortressArmorRenderApi {
  public static net.neoforged.neoforge.client.extensions.common.IClientItemExtensions create(java.util.function.Predicate<net.minecraft.world.item.ItemStack>);
}
```

### `dev.tc4port.thaumcraft.api.client.HeldItemRenderContext`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.HeldItemRenderContext {
  public static void push(net.minecraft.world.entity.LivingEntity);
  public static void pop();
  public static net.minecraft.world.entity.LivingEntity currentEntity();
}
```

### `dev.tc4port.thaumcraft.api.client.HudHeartHooks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.HudHeartHooks {
  public static void register(java.util.function.Supplier<? extends dev.tc4port.thaumcraft.api.client.HudHeartPass>);
}
```

### `dev.tc4port.thaumcraft.api.client.HudHeartPass`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.HudHeartPass {
  public abstract void begin(float, int);
  public abstract void beforeHeart(net.minecraft.client.gui.GuiGraphics, int, int);
  public abstract void finish(net.minecraft.client.gui.GuiGraphics);
}
```

### `dev.tc4port.thaumcraft.api.client.ItemTickState`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ItemTickState {
  public abstract void beginTick(net.minecraft.world.entity.item.ItemEntity);
  public abstract void finishTick(net.minecraft.world.entity.item.ItemEntity);
  public default boolean receivePosition(net.minecraft.world.entity.item.ItemEntity, double, double, double, int);
  public static <T extends dev.tc4port.thaumcraft.api.client.ItemTickState> T get(net.minecraft.world.entity.item.ItemEntity, java.lang.String, java.util.function.Supplier<T>);
}
```

### `dev.tc4port.thaumcraft.api.client.ParticleCameraFade`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.client.ParticleCameraFade extends java.lang.Record {
  public static final dev.tc4port.thaumcraft.api.client.ParticleCameraFade NONE;
  public dev.tc4port.thaumcraft.api.client.ParticleCameraFade(float, float);
  public float visibility(double);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public float hiddenDistance();
  public float fullSizeDistance();
}
```

### `dev.tc4port.thaumcraft.api.client.ParticlePipeline`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.ParticlePipeline {
  public static void register(java.util.function.ToIntFunction<net.minecraft.client.particle.ParticleRenderType>, java.util.function.BiConsumer<net.minecraft.client.particle.ParticleRenderType, net.minecraft.client.renderer.texture.TextureManager>, java.lang.Runnable);
  public static void prepare(net.minecraft.client.particle.ParticleRenderType, net.minecraft.client.renderer.texture.TextureManager);
  public static void finish();
  public static java.util.Comparator<net.minecraft.client.particle.ParticleRenderType> comparator(java.util.List<net.minecraft.client.particle.ParticleRenderType>, java.util.Comparator<net.minecraft.client.particle.ParticleRenderType>);
}
```

### `dev.tc4port.thaumcraft.api.client.QueuedParticleType`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.QueuedParticleType extends net.minecraft.client.particle.ParticleRenderType {
}
```

### `dev.tc4port.thaumcraft.api.client.ResearchRecipeRenderContext`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ResearchRecipeRenderContext {
  public abstract net.minecraft.client.gui.GuiGraphics graphics();
  public abstract net.minecraft.client.gui.Font font();
  public abstract int x();
  public abstract int y();
  public abstract net.minecraft.world.item.ItemStack output();
  public abstract void item(net.minecraft.world.item.ItemStack, int, int, boolean);
  public abstract void ingredient(net.minecraft.world.item.crafting.Ingredient, int, int);
  public abstract boolean isHovered(int, int, int, int);
}
```

### `dev.tc4port.thaumcraft.api.client.ResearchRecipeRendererApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.ResearchRecipeRendererApi {
  public static synchronized <R extends net.minecraft.world.item.crafting.Recipe<?>> dev.tc4port.thaumcraft.api.Registration register(net.minecraft.resources.ResourceLocation, java.lang.Class<R>, java.util.function.BiConsumer<R, dev.tc4port.thaumcraft.api.client.ResearchRecipeRenderContext>);
  public static boolean render(net.minecraft.world.item.crafting.Recipe<?>, dev.tc4port.thaumcraft.api.client.ResearchRecipeRenderContext);
}
```

### `dev.tc4port.thaumcraft.api.client.ThaumcraftClientEffectsApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.ThaumcraftClientEffectsApi {
  public static final double MAX_TRAIL_DISTANCE = 256.0d;
  public static final double MAX_EFFECT_DISTANCE = 256.0d;
  public static final double MAX_EFFECT_SPEED = 16.0d;
  public static final float MAX_WISP_SIZE = 1024.0f;
  public static final float MAX_TRAIL_SCALE = 64.0f;
  public static void spawnEssentiaTrail(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, int, int, float);
  public static void spawnSparkle(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, float, int, int, float, boolean);
  public static void spawnDestinationWisp(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, float, int, boolean, float);
  public static void spawnQualitySparkle(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, float, int, float);
  public static void spawnMovingSparkle(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, float, int, int, float, boolean);
  public static void spawnCustomSparkle(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, float, float, float, float, int, int, int, float, boolean, boolean, boolean, boolean, dev.tc4port.thaumcraft.api.client.ParticleCameraFade);
  public static void spawnWispMote(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, float, float, float, float, boolean, float);
  public static void spawnBlockSparkle(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.core.BlockPos, int, int);
  public static int qualityScaledParticleCount(int);
  public static void spawnBlockRune(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, float, float, float, int, float);
  public static void spawnMovingWisp(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, float, int, boolean, float, boolean);
  public static void spawnFollowingFallingWisp(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.entity.Entity);
  public static void spawnBurst(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, float);
  public static void spawnSmokeSpiral(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, float, float, double, int);
  public static void spawnFocusLightning(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3);
  public static void spawnShockLightning(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3);
  public static void spawnNodeLightning(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3);
  public static void spawnGenericParticle(net.minecraft.client.multiplayer.ClientLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, float, float, float, float, boolean, int, int, int, int, int, float);
}
```

### `dev.tc4port.thaumcraft.api.client.ThaumcraftClientPresentationApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.ThaumcraftClientPresentationApi {
  public static dev.tc4port.thaumcraft.api.Registration register(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.client.ActionPresentationHandler);
}
```

### `dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApi extends dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon {
}
```

### `dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon`

归属：Thaumcraft 4R 本体；类型：类。

```java
public class dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon {
  public static dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$EffectUv particleAtlasUv(float, float, float, float);
  public static boolean isFocusDialAtBottom();
  public static void drawAspect(net.minecraft.client.gui.GuiGraphics, dev.tc4port.thaumcraft.api.aspect.AspectId, int, int, float);
  public static net.minecraft.client.renderer.RenderType legacyLinearAdditiveBillboard(net.minecraft.resources.ResourceLocation);
  public static net.minecraft.client.renderer.RenderType legacyLinearTranslucentBillboard(net.minecraft.resources.ResourceLocation);
  public static net.minecraft.client.renderer.RenderType legacyLinearTranslucentDepthWriteBillboard(net.minecraft.resources.ResourceLocation);
  public static <T extends net.minecraft.world.entity.Entity> net.minecraft.client.renderer.entity.EntityRenderer<T> createEldritchOrbRenderer(net.minecraft.client.renderer.entity.EntityRendererProvider$Context);
  public static net.minecraft.client.renderer.RenderType eldritchOrbRays();
  public static net.minecraft.world.entity.LivingEntity currentHeldItemEntity();
  public static dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$WorldRenderScope beginAfterLevelWorldRender(dev.tc4port.thaumcraft.api.client.WorldRenderContext, boolean);
  public static dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$WorldRenderScope beginAfterLevelWorldRender(org.joml.Matrix4f, org.joml.Matrix4f, boolean);
  public static void renderLegacyFramedWand(net.minecraft.world.item.ItemStack, com.mojang.blaze3d.vertex.PoseStack, net.minecraft.client.renderer.MultiBufferSource, int, int);
  public static void renderLegacyDirectEntityWand(net.minecraft.world.item.ItemStack, com.mojang.blaze3d.vertex.PoseStack, net.minecraft.client.renderer.MultiBufferSource, int, int);
  public static void renderInstalledFocus(net.minecraft.world.item.ItemStack, boolean, com.mojang.blaze3d.vertex.PoseStack, int, int, int);
  public static net.minecraft.world.phys.Vec3 resolveFocusCastOrigin(net.minecraft.world.entity.LivingEntity, net.minecraft.world.InteractionHand);
  public static void showFocusBeam(net.minecraft.resources.ResourceLocation, net.minecraft.world.entity.LivingEntity, net.minecraft.world.InteractionHand, net.minecraft.world.phys.Vec3, int, float, int);
}
```

### `dev.tc4port.thaumcraft.api.client.WandRenderApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.WandRenderApi {
  public static net.minecraft.client.model.HumanoidModel$ArmPose getArmPose(net.minecraft.world.entity.LivingEntity, net.minecraft.world.InteractionHand, net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.client.WorldRenderBoundary`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.WorldRenderBoundary {
  public static void beforeTranslucent(java.lang.Runnable);
  public static void dispatch();
}
```

### `dev.tc4port.thaumcraft.api.client.WorldRenderContext`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.client.WorldRenderContext extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.client.WorldRenderContext(dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage, com.mojang.blaze3d.vertex.PoseStack, org.joml.Matrix4f, org.joml.Matrix4f, float, net.minecraft.client.Camera, net.minecraft.client.renderer.culling.Frustum);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage getStage();
  public com.mojang.blaze3d.vertex.PoseStack getPoseStack();
  public org.joml.Matrix4f getModelViewMatrix();
  public org.joml.Matrix4f getProjectionMatrix();
  public float getPartialTick();
  public net.minecraft.client.Camera getCamera();
  public net.minecraft.client.renderer.culling.Frustum getFrustum();
}
```

### `dev.tc4port.thaumcraft.api.client.WorldRenderTransforms`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.WorldRenderTransforms {
  public static org.joml.Matrix4f modelViewMatrix();
  public static com.mojang.blaze3d.vertex.PoseStack$Pose cameraRelativePose(com.mojang.blaze3d.vertex.PoseStack$Pose);
  public static void cameraRelativePose(com.mojang.blaze3d.vertex.PoseStack$Pose, com.mojang.blaze3d.vertex.PoseStack$Pose);
  public static void resetWorldPose(com.mojang.blaze3d.vertex.PoseStack);
}
```

### `dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks$BiomeColor`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks$BiomeColor {
  public abstract int apply(net.minecraft.world.level.biome.Biome, boolean, double, double, int);
}
```

### `dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks$HandLayer`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ClientBehaviorHooks$HandLayer {
  public abstract boolean allow(net.minecraft.world.entity.LivingEntity, net.minecraft.world.item.ItemStack, net.minecraft.world.item.ItemDisplayContext, net.minecraft.world.entity.HumanoidArm);
}
```

### `dev.tc4port.thaumcraft.api.client.ClothingLayerHooks$Interceptor`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ClothingLayerHooks$Interceptor {
  public abstract <T extends net.minecraft.world.entity.LivingEntity> void render(int, net.minecraft.client.model.EntityModel<T>, net.minecraft.resources.ResourceLocation, com.mojang.blaze3d.vertex.PoseStack, net.minecraft.client.renderer.MultiBufferSource, int, T, int, java.lang.Runnable);
}
```

### `dev.tc4port.thaumcraft.api.client.HudHeartHooks$Passes`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.client.HudHeartHooks$Passes implements dev.tc4port.thaumcraft.api.client.HudHeartPass {
  public dev.tc4port.thaumcraft.api.client.HudHeartHooks$Passes();
  public void begin(float, int);
  public void beforeHeart(net.minecraft.client.gui.GuiGraphics, int, int);
  public void finish(net.minecraft.client.gui.GuiGraphics);
}
```

### `dev.tc4port.thaumcraft.api.client.ItemTickState$Access`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ItemTickState$Access {
  public abstract <T extends dev.tc4port.thaumcraft.api.client.ItemTickState> T platform$state(java.lang.String, java.util.function.Supplier<T>);
}
```

### `dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$EffectUv`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$EffectUv extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$EffectUv(float, float, float, float);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public float u0();
  public float u1();
  public float v0();
  public float v1();
}
```

### `dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$WorldRenderScope`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.client.ThaumcraftClientRenderApiCommon$WorldRenderScope extends java.lang.AutoCloseable {
  public abstract void close();
}
```

### `dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage extends java.lang.Enum<dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage> {
  public static final dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage AFTER_BLOCK_ENTITIES;
  public static final dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage AFTER_TRANSLUCENT_BLOCKS;
  public static final dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage AFTER_PARTICLES;
  public static final dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage AFTER_WEATHER;
  public static final dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage AFTER_LEVEL;
  public static final dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage OTHER;
  public static dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage[] values();
  public static dev.tc4port.thaumcraft.api.client.WorldRenderContext$Stage valueOf(java.lang.String);
}
```

## 6.7 `dev.tc4port.thaumcraft.api.damage`

本体伤害类型键和伤害源工厂。

### `dev.tc4port.thaumcraft.api.damage.ThaumcraftDamageTypes`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.damage.ThaumcraftDamageTypes {
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.damagesource.DamageType> FLUX_TAINT;
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.damagesource.DamageType> DISSOLVE;
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.damagesource.DamageType> TENTACLE;
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.damagesource.DamageType> AIR_ARROW;
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.damagesource.DamageType> FIRE_ARROW;
  public static final net.minecraft.resources.ResourceKey<net.minecraft.world.damagesource.DamageType> ORDER_ARROW;
  public static net.minecraft.world.damagesource.DamageSource fluxTaint(net.minecraft.world.level.Level);
  public static net.minecraft.world.damagesource.DamageSource dissolve(net.minecraft.world.level.Level);
  public static net.minecraft.world.damagesource.DamageSource tentacle(net.minecraft.world.level.Level, net.minecraft.world.entity.LivingEntity);
  public static net.minecraft.world.damagesource.DamageSource primalArrow(net.minecraft.world.level.Level, net.minecraft.resources.ResourceKey<net.minecraft.world.damagesource.DamageType>, net.minecraft.world.entity.Entity, net.minecraft.world.entity.Entity);
}
```

## 6.8 `dev.tc4port.thaumcraft.api.data`

公开数据结构、装备能力、法杖部件和数据映射值。

### `dev.tc4port.thaumcraft.api.data.BlockAspectDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.data.BlockAspectDefinition extends java.lang.Record {
  public static final int MAX_AMOUNT = 64;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.BlockAspectDefinition> CODEC;
  public dev.tc4port.thaumcraft.api.data.BlockAspectDefinition(dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
  public static dev.tc4port.thaumcraft.api.data.BlockAspectDefinition merge(dev.tc4port.thaumcraft.api.data.BlockAspectDefinition, dev.tc4port.thaumcraft.api.data.BlockAspectDefinition);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode mode();
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts aspects();
}
```

### `dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition> CODEC;
  public dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition(int, java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>, boolean, boolean, boolean, boolean, int, dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait, float, boolean);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int visDiscount();
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> aspectVisDiscounts();
  public boolean gogglesOverlay();
  public boolean auraRevealing();
  public boolean infusionGogglesReveal();
  public boolean runic();
  public int runicCharge();
  public dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait runicTrait();
  public float fallDistanceReduction();
  public boolean hoverFuelEfficiency();
}
```

### `dev.tc4port.thaumcraft.api.data.NativeItemStateDeclarations`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.data.NativeItemStateDeclarations {
  public static synchronized <T> net.minecraft.core.component.DataComponentType<T> declare(net.minecraft.resources.ResourceLocation, com.mojang.serialization.Codec<T>);
  public static synchronized <T> net.minecraft.core.component.DataComponentType<T> declare(net.minecraft.resources.ResourceLocation, com.mojang.serialization.Codec<T>, net.minecraft.network.codec.StreamCodec<net.minecraft.network.RegistryFriendlyByteBuf, T>);
  public static synchronized net.minecraft.resources.ResourceLocation id(net.minecraft.core.component.DataComponentType<?>);
  public static void register(java.lang.Object, java.util.List<? extends net.minecraft.core.component.DataComponentType<?>>);
}
```

### `dev.tc4port.thaumcraft.api.data.PechValueDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.data.PechValueDefinition extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.PechValueDefinition> CODEC;
  public dev.tc4port.thaumcraft.api.data.PechValueDefinition(int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int value();
}
```

### `dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition> CODEC;
  public dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition(dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement);
  public int relaySlot();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement attunement();
}
```

### `dev.tc4port.thaumcraft.api.data.WandCapDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.data.WandCapDefinition extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.WandCapDefinition> CODEC;
  public dev.tc4port.thaumcraft.api.data.WandCapDefinition(dev.tc4port.thaumcraft.api.wand.WandMaterialId, float, java.util.Set<dev.tc4port.thaumcraft.api.aspect.VisChannel>, float, net.minecraft.resources.ResourceLocation, int, dev.tc4port.thaumcraft.api.research.ResearchRequirement, dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode, int);
  public dev.tc4port.thaumcraft.api.data.WandCapDefinition(dev.tc4port.thaumcraft.api.wand.WandMaterialId, float, java.util.Set<dev.tc4port.thaumcraft.api.aspect.VisChannel>, float, net.minecraft.resources.ResourceLocation, int, dev.tc4port.thaumcraft.api.research.ResearchRequirement, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.wand.WandMaterialId materialId();
  public float baseCostModifier();
  public java.util.Set<dev.tc4port.thaumcraft.api.aspect.VisChannel> specialCostModifierAspects();
  public float specialCostModifier();
  public net.minecraft.resources.ResourceLocation texture();
  public int craftCost();
  public dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
  public dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode assemblyMode();
  public int order();
}
```

### `dev.tc4port.thaumcraft.api.data.WandRodDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.data.WandRodDefinition extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.WandRodDefinition> CODEC;
  public dev.tc4port.thaumcraft.api.data.WandRodDefinition(dev.tc4port.thaumcraft.api.wand.WandMaterialId, int, int, dev.tc4port.thaumcraft.api.wand.WandRechargeSpec, dev.tc4port.thaumcraft.api.research.ResearchRequirement, net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode, boolean, boolean, int);
  public dev.tc4port.thaumcraft.api.data.WandRodDefinition(dev.tc4port.thaumcraft.api.wand.WandMaterialId, int, int, dev.tc4port.thaumcraft.api.wand.WandRechargeSpec, dev.tc4port.thaumcraft.api.research.ResearchRequirement, net.minecraft.resources.ResourceLocation, boolean, boolean, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.wand.WandMaterialId materialId();
  public int capacity();
  public int craftCost();
  public dev.tc4port.thaumcraft.api.wand.WandRechargeSpec recharge();
  public dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
  public net.minecraft.resources.ResourceLocation texture();
  public dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode assemblyMode();
  public boolean glowing();
  public boolean runes();
  public int order();
}
```

### `dev.tc4port.thaumcraft.api.data.WarpDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.data.WarpDefinition extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.WarpDefinition> CODEC;
  public dev.tc4port.thaumcraft.api.data.WarpDefinition(int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int amount();
}
```

### `dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode extends java.lang.Enum<dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode> {
  public static final dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode ADD;
  public static final dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode REPLACE;
  public static dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode[] values();
  public static dev.tc4port.thaumcraft.api.data.BlockAspectDefinition$Mode valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait extends java.lang.Enum<dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait> {
  public static final dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait NONE;
  public static final dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait FASTER_RECHARGE;
  public static final dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait KINETIC;
  public static final dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait HEALING;
  public static final dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait EMERGENCY;
  public static dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait[] values();
  public static dev.tc4port.thaumcraft.api.data.EquipmentAbilityDefinition$RunicTrait valueOf(java.lang.String);
  public java.lang.String serialized();
}
```

### `dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement extends java.lang.Enum<dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement> {
  public static final dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement AIR;
  public static final dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement FIRE;
  public static final dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement WATER;
  public static final dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement EARTH;
  public static final dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement ORDER;
  public static final dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement ENTROPY;
  public static final dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement NEUTRAL;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement> CODEC;
  public static dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement[] values();
  public static dev.tc4port.thaumcraft.api.data.RelayAttunementDefinition$Attunement valueOf(java.lang.String);
  public int relaySlot();
}
```

## 6.9 `dev.tc4port.thaumcraft.api.effect`

状态效果相关公共契约。

### `dev.tc4port.thaumcraft.api.effect.EffectCurePolicy`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.effect.EffectCurePolicy {
}
```

## 6.10 `dev.tc4port.thaumcraft.api.entity`

本体实体能力、要素球、弹射物和实体分类接口。

### `dev.tc4port.thaumcraft.api.entity.AspectOrbApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.entity.AspectOrbApi {
  public static final int MAX_VALUE = 32767;
  public static java.util.Optional<net.minecraft.world.entity.Entity> spawn(net.minecraft.server.level.ServerLevel, net.minecraft.world.phys.Vec3, dev.tc4port.thaumcraft.api.aspect.AspectId, int);
}
```

### `dev.tc4port.thaumcraft.api.entity.AttributeTypes`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.entity.AttributeTypes {
  public static final net.minecraft.core.Holder<net.minecraft.world.entity.ai.attributes.Attribute> MAX_ABSORPTION;
  public dev.tc4port.thaumcraft.api.entity.AttributeTypes();
  public static float baseJumpStrength(net.minecraft.world.entity.LivingEntity);
  public static net.minecraft.core.Holder<net.minecraft.world.entity.ai.attributes.Attribute> stepHeight();
  public static double stepBase(double);
  public static net.minecraft.world.entity.ai.attributes.AttributeInstance resolve(net.minecraft.world.entity.LivingEntity, net.minecraft.resources.ResourceLocation);
}
```

### `dev.tc4port.thaumcraft.api.entity.EldritchMob`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.entity.EldritchMob {
}
```

### `dev.tc4port.thaumcraft.api.entity.EntityAspectApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.entity.EntityAspectApi {
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts resolve(net.minecraft.world.entity.Entity);
}
```

### `dev.tc4port.thaumcraft.api.entity.EntityNbtCondition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.entity.EntityNbtCondition extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.entity.EntityNbtCondition(java.lang.String, net.minecraft.nbt.Tag, java.lang.String);
  public net.minecraft.nbt.Tag expected();
  public boolean matches(net.minecraft.nbt.CompoundTag);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.lang.String name();
  public java.lang.String scanHashContribution();
}
```

### `dev.tc4port.thaumcraft.api.entity.EntityScanIdentity`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.entity.EntityScanIdentity extends java.lang.Record {
  public static final int MAX_CHARACTERS = 256;
  public dev.tc4port.thaumcraft.api.entity.EntityScanIdentity(java.lang.String);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.lang.String serialized();
}
```

### `dev.tc4port.thaumcraft.api.entity.ExplosiveOrbApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.entity.ExplosiveOrbApi {
  public static final float MAX_STRENGTH = 64.0f;
  public static java.util.Optional<net.minecraft.world.entity.Entity> spawn(net.minecraft.server.level.ServerLevel, net.minecraft.world.entity.LivingEntity, float);
  public static java.util.Optional<net.minecraft.world.entity.Entity> spawnAdvanced(net.minecraft.server.level.ServerLevel, net.minecraft.world.entity.LivingEntity, float);
}
```

### `dev.tc4port.thaumcraft.api.entity.TaintSwarmApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.entity.TaintSwarmApi {
  public static final int MIN_ATTACK_DAMAGE = 2;
  public static final int MAX_ATTACK_DAMAGE = 129;
  public static java.util.Optional<net.minecraft.world.entity.LivingEntity> spawnSummoned(net.minecraft.server.level.ServerPlayer, net.minecraft.world.entity.LivingEntity, int);
  public static java.util.Optional<net.minecraft.world.entity.LivingEntity> spawnSummoned(net.minecraft.server.level.ServerPlayer, net.minecraft.world.InteractionHand, net.minecraft.world.entity.LivingEntity, int);
}
```

### `dev.tc4port.thaumcraft.api.entity.TaintedMob`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.entity.TaintedMob {
}
```

### `dev.tc4port.thaumcraft.api.entity.WispApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.entity.WispApi {
  public static java.util.Optional<net.minecraft.world.entity.LivingEntity> spawn(net.minecraft.server.level.ServerLevel, net.minecraft.world.phys.Vec3, dev.tc4port.thaumcraft.api.aspect.AspectId);
}
```

## 6.11 `dev.tc4port.thaumcraft.api.essentia`

Essentia 容器、传输、源搜索和原子读写。

### `dev.tc4port.thaumcraft.api.essentia.EssentiaApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.essentia.EssentiaApi {
  public static java.util.Optional<dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef> findSource(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaSearch);
  public static int take(net.minecraft.world.level.Level, dev.tc4port.thaumcraft.api.essentia.EssentiaTransport, dev.tc4port.thaumcraft.api.aspect.AspectId, int, net.minecraft.core.Direction, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
  public static int add(net.minecraft.world.level.Level, dev.tc4port.thaumcraft.api.essentia.EssentiaTransport, dev.tc4port.thaumcraft.api.aspect.AspectId, int, net.minecraft.core.Direction, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef> findSource(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaSearch, java.util.function.Predicate<dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef>);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef> extract(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaSearch, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef> extract(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaSearch, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode, java.util.function.Predicate<dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef>);
  public static int extract(net.minecraft.world.level.Level, dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaContainerApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.essentia.EssentiaContainerApi {
  public static boolean isLabel(net.minecraft.world.item.ItemStack);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.aspect.AspectId> labelAspect(net.minecraft.world.item.ItemStack);
  public static net.minecraft.world.item.ItemStack withFilter(net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static int capacity(net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts contents(net.minecraft.world.item.ItemStack);
  public static int insert(net.minecraft.world.level.Level, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
  public static int extract(net.minecraft.world.level.Level, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaJarView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.essentia.EssentiaJarView extends dev.tc4port.thaumcraft.api.aspect.AspectContainerView {
  public abstract dev.tc4port.thaumcraft.api.aspect.AspectId filter();
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaMultiStoreView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.essentia.EssentiaMultiStoreView extends dev.tc4port.thaumcraft.api.aspect.AspectContainerView {
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaSearch`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.essentia.EssentiaSearch extends java.lang.Record {
  public static final int MAX_RANGE = 32;
  public dev.tc4port.thaumcraft.api.essentia.EssentiaSearch(int, net.minecraft.core.Direction);
  public static dev.tc4port.thaumcraft.api.essentia.EssentiaSearch nearby(int);
  public static dev.tc4port.thaumcraft.api.essentia.EssentiaSearch ahead(net.minecraft.core.Direction, int);
  public boolean directional();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int range();
  public net.minecraft.core.Direction direction();
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaSource`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.essentia.EssentiaSource {
  public abstract int extractEssentia(dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.essentia.EssentiaSourceRef(net.minecraft.resources.ResourceKey<net.minecraft.world.level.Level>, net.minecraft.core.BlockPos);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceKey<net.minecraft.world.level.Level> dimension();
  public net.minecraft.core.BlockPos position();
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode extends java.lang.Enum<dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode> {
  public static final dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode SIMULATE;
  public static final dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode EXECUTE;
  public static dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode[] values();
  public static dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode valueOf(java.lang.String);
  public boolean executes();
}
```

### `dev.tc4port.thaumcraft.api.essentia.EssentiaTransport`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.essentia.EssentiaTransport {
  public default dev.tc4port.thaumcraft.api.essentia.EssentiaTransport transferView();
  public abstract boolean isConnectable(net.minecraft.core.Direction);
  public abstract boolean canInputFrom(net.minecraft.core.Direction);
  public abstract boolean canOutputTo(net.minecraft.core.Direction);
  public abstract dev.tc4port.thaumcraft.api.aspect.AspectId suctionType(net.minecraft.core.Direction);
  public abstract int suctionAmount(net.minecraft.core.Direction);
  public abstract int takeEssentia(dev.tc4port.thaumcraft.api.aspect.AspectId, int, net.minecraft.core.Direction, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
  public abstract int addEssentia(dev.tc4port.thaumcraft.api.aspect.AspectId, int, net.minecraft.core.Direction, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
  public abstract dev.tc4port.thaumcraft.api.aspect.AspectId essentiaType(net.minecraft.core.Direction);
  public abstract int essentiaAmount(net.minecraft.core.Direction);
  public default dev.tc4port.thaumcraft.api.aspect.AspectId extractableAspect(net.minecraft.core.Direction);
  public default int availableEssentia(dev.tc4port.thaumcraft.api.aspect.AspectId, net.minecraft.core.Direction);
  public abstract int minimumSuction();
  public abstract boolean renderExtendedTube();
}
```

### `dev.tc4port.thaumcraft.api.essentia.FilledJarEssentiaApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.essentia.FilledJarEssentiaApi {
  public static boolean isJar(net.minecraft.world.item.ItemStack);
  public static boolean hasStoredData(net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.aspect.AspectAmounts contents(net.minecraft.world.item.ItemStack);
  public static int transferToJar(net.minecraft.server.level.ServerLevel, net.minecraft.world.item.ItemStack, net.minecraft.core.BlockPos, int);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.essentia.FilledJarEssentiaView> view(net.minecraft.world.item.ItemStack);
  public static int extract(net.minecraft.world.level.Level, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.AspectId, int, dev.tc4port.thaumcraft.api.essentia.EssentiaTransferMode);
}
```

### `dev.tc4port.thaumcraft.api.essentia.FilledJarEssentiaView`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.essentia.FilledJarEssentiaView extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.essentia.FilledJarEssentiaView(dev.tc4port.thaumcraft.api.aspect.AspectId, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.aspect.AspectId aspect();
  public int amount();
}
```

## 6.12 `dev.tc4port.thaumcraft.api.event`

附属可监听或触发的公共事件契约。

### `dev.tc4port.thaumcraft.api.event.AttributeOperation`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.event.AttributeOperation extends java.lang.Enum<dev.tc4port.thaumcraft.api.event.AttributeOperation> {
  public static final dev.tc4port.thaumcraft.api.event.AttributeOperation ADD_VALUE;
  public static final dev.tc4port.thaumcraft.api.event.AttributeOperation ADD_MULTIPLIED_BASE;
  public static final dev.tc4port.thaumcraft.api.event.AttributeOperation ADD_MULTIPLIED_TOTAL;
  public static dev.tc4port.thaumcraft.api.event.AttributeOperation[] values();
  public static dev.tc4port.thaumcraft.api.event.AttributeOperation valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.event.BlockHarvest`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.event.BlockHarvest extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.event.BlockHarvest(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, net.minecraft.world.level.block.state.BlockState, net.minecraft.world.entity.Entity, net.minecraft.world.item.ItemStack, java.util.List<net.minecraft.world.entity.item.ItemEntity>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.server.level.ServerLevel getLevel();
  public net.minecraft.core.BlockPos getPos();
  public net.minecraft.world.level.block.state.BlockState getState();
  public net.minecraft.world.entity.Entity getBreaker();
  public net.minecraft.world.item.ItemStack getTool();
  public java.util.List<net.minecraft.world.entity.item.ItemEntity> getDrops();
}
```

### `dev.tc4port.thaumcraft.api.event.CancellableHook`

归属：Thaumcraft 4R 本体；类型：类。

```java
public class dev.tc4port.thaumcraft.api.event.CancellableHook extends net.neoforged.bus.api.Event implements net.neoforged.bus.api.ICancellableEvent {
  public dev.tc4port.thaumcraft.api.event.CancellableHook();
}
```

### `dev.tc4port.thaumcraft.api.event.CriticalDecision`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.event.CriticalDecision extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.event.CriticalDecision(boolean, float);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public boolean isCriticalHit();
  public float getDamageMultiplier();
}
```

### `dev.tc4port.thaumcraft.api.event.Damage`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.event.Damage extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.event.Damage(net.minecraft.world.entity.LivingEntity, net.minecraft.world.damagesource.DamageSource, java.util.function.Supplier<java.lang.Float>, java.util.function.Consumer<java.lang.Float>, java.util.function.Consumer<java.lang.Boolean>);
  public float getAmount();
  public float getNewDamage();
  public void setAmount(float);
  public void setNewDamage(float);
  public void setCanceled(boolean);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.world.entity.LivingEntity getEntity();
  public net.minecraft.world.damagesource.DamageSource getSource();
  public java.util.function.Supplier<java.lang.Float> amount();
  public java.util.function.Consumer<java.lang.Float> update();
  public java.util.function.Consumer<java.lang.Boolean> cancellation();
}
```

### `dev.tc4port.thaumcraft.api.event.GameplayHooks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.event.GameplayHooks {
  public static net.minecraft.world.entity.SpawnGroupData finalizeMobSpawn(net.minecraft.world.entity.Mob, net.minecraft.world.level.ServerLevelAccessor, net.minecraft.world.DifficultyInstance, net.minecraft.world.entity.MobSpawnType, net.minecraft.world.entity.SpawnGroupData);
  public static void firePlayerCraftingEvent(net.minecraft.world.entity.player.Player, net.minecraft.world.item.ItemStack, net.minecraft.world.Container);
  public static net.minecraft.world.InteractionResultHolder<net.minecraft.world.item.ItemStack> onArrowNock(net.minecraft.world.item.ItemStack, net.minecraft.world.level.Level, net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand, boolean);
  public static int onArrowLoose(net.minecraft.world.item.ItemStack, net.minecraft.world.level.Level, net.minecraft.world.entity.player.Player, int, boolean);
  public static net.neoforged.neoforge.event.entity.EntityTeleportEvent$EnderEntity onEnderTeleport(net.minecraft.world.entity.LivingEntity, double, double, double);
  public static dev.tc4port.thaumcraft.api.event.HookDecision onMobSplit(net.minecraft.world.entity.Mob, java.util.List<net.minecraft.world.entity.Mob>);
  public static dev.tc4port.thaumcraft.api.event.HookDecision fireBlockBreak(net.minecraft.world.level.Level, net.minecraft.world.level.GameType, net.minecraft.server.level.ServerPlayer, net.minecraft.core.BlockPos, net.minecraft.world.level.block.state.BlockState);
  public static dev.tc4port.thaumcraft.api.event.CriticalDecision fireCriticalHit(net.minecraft.world.entity.player.Player, net.minecraft.world.entity.Entity, boolean, float);
  public static dev.tc4port.thaumcraft.api.event.GameplayHooks$GrowthDecision bonemeal(net.minecraft.world.entity.player.Player, net.minecraft.world.level.Level, net.minecraft.core.BlockPos, net.minecraft.world.level.block.state.BlockState, net.minecraft.world.item.ItemStack);
  public static dev.tc4port.thaumcraft.api.event.HookDecision rightClickBlock(net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand, net.minecraft.core.BlockPos, net.minecraft.world.phys.BlockHitResult);
  public static dev.tc4port.thaumcraft.api.event.HookDecision attackEntity(net.minecraft.world.entity.player.Player, net.minecraft.world.entity.Entity);
  public static boolean harvestCheck(net.minecraft.world.entity.player.Player, net.minecraft.world.level.block.state.BlockState, net.minecraft.world.level.BlockGetter, net.minecraft.core.BlockPos);
  public static dev.tc4port.thaumcraft.api.event.GameplayHooks$TeleportDecision teleport(net.minecraft.world.entity.Entity, double, double, double);
}
```

### `dev.tc4port.thaumcraft.api.event.HarvestExperiencePolicy`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.event.HarvestExperiencePolicy {
  public abstract int equippedFortuneExperience(int, int);
}
```

### `dev.tc4port.thaumcraft.api.event.HookDecision`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.event.HookDecision extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.event.HookDecision(boolean);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public boolean isCanceled();
}
```

### `dev.tc4port.thaumcraft.api.event.JigsawSelectionHooks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.event.JigsawSelectionHooks {
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.util.function.Function<net.minecraft.util.RandomSource, dev.tc4port.thaumcraft.api.event.JigsawSelectionHooks$Session>> SELECTORS;
  public static java.util.List<dev.tc4port.thaumcraft.api.event.JigsawSelectionHooks$Session> begin(net.minecraft.util.RandomSource);
}
```

### `dev.tc4port.thaumcraft.api.event.NativeEntityTicks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.event.NativeEntityTicks {
  public static void onTick(java.util.function.Predicate<net.minecraft.world.entity.Entity>, java.util.function.Consumer<net.minecraft.world.entity.Entity>);
  public static void onTick(java.util.function.Consumer<net.minecraft.world.entity.Entity>);
}
```

### `dev.tc4port.thaumcraft.api.event.OrderedCallbacks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.event.OrderedCallbacks<T> {
  public dev.tc4port.thaumcraft.api.event.OrderedCallbacks();
  public synchronized void register(int, java.lang.String, T);
  public java.util.List<T> values();
}
```

### `dev.tc4port.thaumcraft.api.event.PlatformIdentity`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.event.PlatformIdentity {
  public static final java.lang.String NAMESPACE = "thaumcraft";
}
```

### `dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks {
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$ArrowSource> ARROW_SOURCE;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$TickPermission> TICK;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.util.function.Predicate<net.minecraft.world.entity.Entity>> STEP;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$RainLevel> RAIN;
  public static final dev.tc4port.thaumcraft.api.event.OrderedCallbacks<java.util.function.Predicate<net.minecraft.resources.ResourceKey<net.minecraft.world.level.Level>>> SPIN_MAP;
  public static net.minecraft.world.damagesource.DamageSource arrowSource(net.minecraft.world.entity.projectile.AbstractArrow, net.minecraft.world.entity.Entity, net.minecraft.world.damagesource.DamageSource);
  public static boolean allowTick(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, boolean, boolean);
  public static boolean allowStep(net.minecraft.world.entity.Entity);
  public static float rain(net.minecraft.world.level.Level, float, float);
  public static boolean spinMap(net.minecraft.resources.ResourceKey<net.minecraft.world.level.Level>);
}
```

### `dev.tc4port.thaumcraft.api.event.GameplayHooks$GrowthDecision`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.event.GameplayHooks$GrowthDecision extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.event.GameplayHooks$GrowthDecision(boolean, boolean);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public boolean isCanceled();
  public boolean isSuccessful();
}
```

### `dev.tc4port.thaumcraft.api.event.GameplayHooks$TeleportDecision`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.event.GameplayHooks$TeleportDecision extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.event.GameplayHooks$TeleportDecision(boolean, net.minecraft.world.phys.Vec3);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public boolean isCanceled();
  public net.minecraft.world.phys.Vec3 getTarget();
}
```

### `dev.tc4port.thaumcraft.api.event.JigsawSelectionHooks$Session`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.event.JigsawSelectionHooks$Session {
  public abstract void filter(net.minecraft.world.level.levelgen.structure.pools.StructureTemplatePool, java.util.List<net.minecraft.world.level.levelgen.structure.pools.StructurePoolElement>, java.util.List<? super net.minecraft.world.level.levelgen.structure.PoolElementStructurePiece>, net.minecraft.util.RandomSource);
}
```

### `dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$ArrowSource`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$ArrowSource {
  public abstract net.minecraft.world.damagesource.DamageSource apply(net.minecraft.world.entity.projectile.AbstractArrow, net.minecraft.world.entity.Entity, net.minecraft.world.damagesource.DamageSource);
}
```

### `dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$RainLevel`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$RainLevel {
  public abstract float apply(net.minecraft.world.level.Level, float, float);
}
```

### `dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$TickPermission`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.event.WorldBehaviorHooks$TickPermission {
  public abstract boolean allow(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, boolean, boolean);
}
```

## 6.13 `dev.tc4port.thaumcraft.api.flux`

Flux 消耗、查询和结果类型。

### `dev.tc4port.thaumcraft.api.flux.FluxApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.flux.FluxApi {
  public static final int MAXIMUM_RANGE = 32;
  public static int consume(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, int, dev.tc4port.thaumcraft.api.flux.FluxConsumeContext, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.flux.FluxConsumeResult consumeNearby(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, int, int, dev.tc4port.thaumcraft.api.flux.FluxConsumeContext, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

### `dev.tc4port.thaumcraft.api.flux.FluxConsumeContext`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.flux.FluxConsumeContext extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.flux.FluxConsumeContext(net.minecraft.resources.ResourceLocation, net.minecraft.core.BlockPos, java.util.Optional<net.minecraft.server.level.ServerPlayer>);
  public static dev.tc4port.thaumcraft.api.flux.FluxConsumeContext machine(net.minecraft.resources.ResourceLocation, net.minecraft.core.BlockPos);
  public static dev.tc4port.thaumcraft.api.flux.FluxConsumeContext player(net.minecraft.resources.ResourceLocation, net.minecraft.server.level.ServerPlayer);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation source();
  public net.minecraft.core.BlockPos origin();
  public java.util.Optional<net.minecraft.server.level.ServerPlayer> actor();
}
```

### `dev.tc4port.thaumcraft.api.flux.FluxConsumeEvent`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.flux.FluxConsumeEvent extends dev.tc4port.thaumcraft.api.event.CancellableHook {
  public dev.tc4port.thaumcraft.api.flux.FluxConsumeEvent(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, net.minecraft.world.level.block.state.BlockState, int, dev.tc4port.thaumcraft.api.flux.FluxConsumeContext, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public net.minecraft.server.level.ServerLevel level();
  public net.minecraft.core.BlockPos position();
  public net.minecraft.world.level.block.state.BlockState state();
  public int quanta();
  public dev.tc4port.thaumcraft.api.flux.FluxConsumeContext context();
  public dev.tc4port.thaumcraft.api.aspect.VisAction action();
}
```

### `dev.tc4port.thaumcraft.api.flux.FluxConsumeResult`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.flux.FluxConsumeResult extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.flux.FluxConsumeResult(int, int, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int requestedQuanta();
  public int consumedQuanta();
  public int affectedBlocks();
}
```

## 6.14 `dev.tc4port.thaumcraft.api.focus`

核心定义、状态、升级、参数和费用目录。

### `dev.tc4port.thaumcraft.api.focus.FocusApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusApi {
  public static final int MAX_PROPERTIES = 32;
  public static final int MAX_PROPERTY_VALUE_LENGTH = 512;
  public static final int MAX_PROPERTY_ENCODED_BYTES = 4096;
  public static void requireParameters(dev.tc4port.thaumcraft.api.focus.FocusId, java.util.Set<java.lang.String>);
  public static void requireActionCosts(dev.tc4port.thaumcraft.api.focus.FocusId, java.util.Set<java.lang.String>);
  public static dev.tc4port.thaumcraft.api.focus.FocusRegistryView registry();
  public static double parameter(dev.tc4port.thaumcraft.api.focus.FocusStateView, java.lang.String);
  public static double parameter(net.minecraft.world.item.ItemStack, java.lang.String);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.focus.FocusStateView> installedState(net.minecraft.world.item.ItemStack);
  public static int upgradeLevel(net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.focus.FocusUpgradeId);
  public static void appendFocusTooltip(net.minecraft.world.item.ItemStack, java.util.List<net.minecraft.network.chat.Component>);
  public static void appendFocusInformation(net.minecraft.world.item.ItemStack, java.util.List<net.minecraft.network.chat.Component>);
  public static dev.tc4port.thaumcraft.api.focus.FocusInstallResult install(net.minecraft.server.level.ServerPlayer, net.minecraft.world.InteractionHand, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult updateInstalledProperties(net.minecraft.server.level.ServerPlayer, net.minecraft.world.InteractionHand, java.util.Map<net.minecraft.resources.ResourceLocation, java.lang.String>, java.util.Set<net.minecraft.resources.ResourceLocation>, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusClientPresentation`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusClientPresentation extends java.lang.Record {
  public static final int MAX_DEPTH_FRAMES = 256;
  public static final dev.tc4port.thaumcraft.api.focus.FocusClientPresentation NONE;
  public dev.tc4port.thaumcraft.api.focus.FocusClientPresentation(java.util.Optional<net.minecraft.resources.ResourceLocation>, int, java.util.List<java.lang.Integer>, java.util.Optional<net.minecraft.resources.ResourceLocation>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Optional<net.minecraft.resources.ResourceLocation> depthTexture();
  public int depthFrameCount();
  public java.util.List<java.lang.Integer> depthFrameSequence();
  public java.util.Optional<net.minecraft.resources.ResourceLocation> ornamentTexture();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusId`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusId extends java.lang.Record {
  public static final int MAX_LENGTH = 256;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.focus.FocusId> CODEC;
  public dev.tc4port.thaumcraft.api.focus.FocusId(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.focus.FocusId of(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.focus.FocusId parse(java.lang.String);
  public java.lang.String serialized();
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation value();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusIdentityItem`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.FocusIdentityItem {
  public static final int MAX_SELECTION_DISCRIMINATOR_LENGTH = 512;
  public abstract dev.tc4port.thaumcraft.api.focus.FocusId focusId(net.minecraft.world.item.ItemStack);
  public default java.lang.String focusSelectionDiscriminator(net.minecraft.world.item.ItemStack);
  public default dev.tc4port.thaumcraft.api.focus.FocusStateView focusState(net.minecraft.world.item.ItemStack);
  public default net.minecraft.world.item.ItemStack withFocusState(net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.focus.FocusStateView);
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusInstallResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusInstallResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.focus.FocusInstallResult> {
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult INSTALLED;
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult WOULD_INSTALL;
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult NOT_A_WAND;
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult NOT_A_FOCUS;
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult UNKNOWN_PROFILE;
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult INVALID_STATE;
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult NO_RETURN_SPACE;
  public static final dev.tc4port.thaumcraft.api.focus.FocusInstallResult DENIED;
  public static dev.tc4port.thaumcraft.api.focus.FocusInstallResult[] values();
  public static dev.tc4port.thaumcraft.api.focus.FocusInstallResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusInventorySourceItem`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.FocusInventorySourceItem {
  public abstract dev.tc4port.thaumcraft.api.focus.FocusInventoryView focusInventory(net.minecraft.world.item.ItemStack);
  public default dev.tc4port.thaumcraft.api.focus.FocusInventoryView focusInventory(net.minecraft.server.level.ServerPlayer, net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusInventoryView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.FocusInventoryView {
  public abstract java.util.List<net.minecraft.world.item.ItemStack> snapshot();
  public abstract boolean insert(net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public abstract net.minecraft.world.item.ItemStack extract(int, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public abstract long version();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusParameterValues`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusParameterValues extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.FocusParameterValues(java.util.Map<java.lang.String, java.lang.Double>);
  public double get(java.lang.String);
  public static dev.tc4port.thaumcraft.api.focus.FocusParameterValues resolve(dev.tc4port.thaumcraft.api.focus.FocusId, java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public net.minecraft.nbt.CompoundTag save();
  public static dev.tc4port.thaumcraft.api.focus.FocusParameterValues load(net.minecraft.nbt.CompoundTag);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Map<java.lang.String, java.lang.Double> values();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusParameters`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusParameters extends java.lang.Record {
  public static final int MAX_ENTRIES = 128;
  public static final double LIMIT = 1000000.0d;
  public static final dev.tc4port.thaumcraft.api.focus.FocusParameters EMPTY;
  public dev.tc4port.thaumcraft.api.focus.FocusParameters(java.util.Map<java.lang.String, dev.tc4port.thaumcraft.api.focus.FocusParameters$Value>, java.util.List<dev.tc4port.thaumcraft.api.focus.FocusParameters$Override>);
  public double value(java.lang.String, java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public double minimum(java.lang.String);
  public double maximum(java.lang.String);
  public void validate(java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Map<java.lang.String, dev.tc4port.thaumcraft.api.focus.FocusParameters$Value> values();
  public java.util.List<dev.tc4port.thaumcraft.api.focus.FocusParameters$Override> overrides();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition extends java.lang.Record {
  public static final int RANK_COUNT = 5;
  public dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition(dev.tc4port.thaumcraft.api.focus.FocusId, int, boolean, dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode, java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisCost>, java.util.List<dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride>, java.util.List<java.util.List<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>>, java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$Requirement>, dev.tc4port.thaumcraft.api.focus.FocusClientPresentation, dev.tc4port.thaumcraft.api.focus.FocusParameters, java.util.Map<java.lang.String, dev.tc4port.thaumcraft.api.aspect.VisCost>);
  public java.util.Optional<dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride> matchingCostOverride(java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisCost> fixedCost(java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public boolean displaysPerTickCost(java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.focus.FocusId focusId();
  public int color();
  public boolean displaysPerTickCost();
  public dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode costMode();
  public java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisCost> baseCost();
  public java.util.List<dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride> costOverrides();
  public java.util.List<java.util.List<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>> ranks();
  public java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$Requirement> requirements();
  public dev.tc4port.thaumcraft.api.focus.FocusClientPresentation clientPresentation();
  public dev.tc4port.thaumcraft.api.focus.FocusParameters parameters();
  public java.util.Map<java.lang.String, dev.tc4port.thaumcraft.api.aspect.VisCost> actionCosts();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult> {
  public static final dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult UPDATED;
  public static final dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult WOULD_UPDATE;
  public static final dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult UNCHANGED;
  public static final dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult NO_FOCUS;
  public static final dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult INVALID_PROPERTIES;
  public static final dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult READ_ONLY_CARRIER;
  public static final dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult DENIED;
  public static dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult[] values();
  public static dev.tc4port.thaumcraft.api.focus.FocusPropertyUpdateResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusRegistryView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.FocusRegistryView {
  public abstract long generation();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, dev.tc4port.thaumcraft.api.focus.FocusUpgradeDefinition> upgrades();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusId, dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition> profiles();
  public default java.util.Optional<dev.tc4port.thaumcraft.api.focus.FocusUpgradeDefinition> upgrade(dev.tc4port.thaumcraft.api.focus.FocusUpgradeId);
  public default java.util.Optional<dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition> profile(dev.tc4port.thaumcraft.api.focus.FocusId);
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusStateView`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusStateView extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.FocusStateView(dev.tc4port.thaumcraft.api.focus.FocusId, java.util.List<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>);
  public dev.tc4port.thaumcraft.api.focus.FocusStateView(dev.tc4port.thaumcraft.api.focus.FocusId, java.util.List<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, java.util.Map<net.minecraft.resources.ResourceLocation, java.lang.String>);
  public int level(dev.tc4port.thaumcraft.api.focus.FocusUpgradeId);
  public java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer> upgradeLevels();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.focus.FocusId focusId();
  public java.util.List<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> upgradeSlots();
  public java.util.Map<net.minecraft.resources.ResourceLocation, java.lang.String> properties();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusUpgradeDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusUpgradeDefinition extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.FocusUpgradeDefinition(dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, net.minecraft.resources.ResourceLocation, java.lang.String, java.lang.String, dev.tc4port.thaumcraft.api.aspect.AspectAmounts, int, java.util.List<java.lang.Integer>, java.util.List<java.lang.Integer>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.focus.FocusUpgradeId id();
  public net.minecraft.resources.ResourceLocation icon();
  public java.lang.String nameKey();
  public java.lang.String descriptionKey();
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts aspects();
  public int maxLevel();
  public java.util.List<java.lang.Integer> rankVis();
  public java.util.List<java.lang.Integer> rankXp();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusUpgradeId`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusUpgradeId extends java.lang.Record {
  public static final int MAX_LENGTH = 256;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> CODEC;
  public dev.tc4port.thaumcraft.api.focus.FocusUpgradeId(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.focus.FocusUpgradeId of(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.focus.FocusUpgradeId parse(java.lang.String);
  public java.lang.String serialized();
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation value();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusParameters$Override`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusParameters$Override extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.FocusParameters$Override(java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, java.util.Map<java.lang.String, dev.tc4port.thaumcraft.api.focus.FocusParameters$Value>);
  public boolean matches(java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> requireAll();
  public java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> rejectAny();
  public java.util.Map<java.lang.String, dev.tc4port.thaumcraft.api.focus.FocusParameters$Value> values();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusParameters$Value`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusParameters$Value extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.FocusParameters$Value(double, java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Double>, double, double);
  public double evaluate(java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public double base();
  public java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Double> perLevel();
  public double min();
  public double max();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode extends java.lang.Enum<dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode> {
  public static final dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode FIXED;
  public static final dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode PRIMAL_RANDOM;
  public static dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode[] values();
  public static dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostMode valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride(java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, dev.tc4port.thaumcraft.api.aspect.VisCost, java.util.Optional<java.lang.Boolean>);
  public dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride(dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, dev.tc4port.thaumcraft.api.aspect.VisCost);
  public dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride(java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, dev.tc4port.thaumcraft.api.aspect.VisCost);
  public dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$CostOverride(java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, dev.tc4port.thaumcraft.api.aspect.VisCost, boolean);
  public dev.tc4port.thaumcraft.api.focus.FocusUpgradeId upgradeId();
  public boolean matches(java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> requiredUpgrades();
  public dev.tc4port.thaumcraft.api.aspect.VisCost cost();
  public java.util.Optional<java.lang.Boolean> perTickDisplayOverride();
}
```

### `dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$Requirement`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$Requirement extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.FocusProfileDefinition$Requirement(java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId>, dev.tc4port.thaumcraft.api.research.ResearchRequirement);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> requireAny();
  public java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> requireAll();
  public java.util.Set<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId> rejectIfAll();
  public dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
}
```

## 6.15 `dev.tc4port.thaumcraft.api.focus.action`

核心动作注册、目标、授权、事务和表现。

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusActionApi {
  public static dev.tc4port.thaumcraft.api.Registration register(dev.tc4port.thaumcraft.api.focus.action.FocusActionSpec, dev.tc4port.thaumcraft.api.focus.action.FocusActionHandler);
  public static dev.tc4port.thaumcraft.api.Registration register(dev.tc4port.thaumcraft.api.focus.action.FocusActionSpec, dev.tc4port.thaumcraft.api.focus.action.FocusActionHandler, dev.tc4port.thaumcraft.api.focus.action.FocusActionAuthorizer);
  public static dev.tc4port.thaumcraft.api.focus.action.FocusActionRegistryView registry();
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionAuthorizer`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.action.FocusActionAuthorizer {
  public abstract dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization authorize(dev.tc4port.thaumcraft.api.focus.action.FocusAuthorizationContext);
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionContext`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.action.FocusActionContext {
  public abstract net.minecraft.server.level.ServerPlayer player();
  public abstract net.minecraft.world.InteractionHand hand();
  public abstract net.minecraft.world.item.ItemStack wand();
  public abstract dev.tc4port.thaumcraft.api.focus.FocusStateView installedFocus();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer> installedUpgrades();
  public default double parameter(java.lang.String);
  public default dev.tc4port.thaumcraft.api.aspect.VisCost configuredCost();
  public default dev.tc4port.thaumcraft.api.aspect.VisCost configuredCost(java.lang.String);
  public abstract dev.tc4port.thaumcraft.api.focus.action.FocusActivation activation();
  public abstract net.minecraft.world.phys.HitResult authoritativeHit();
  public abstract int useTicks();
  public default net.minecraft.world.phys.Vec3 castOrigin();
  public default dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization authorization();
  public abstract void present(net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, net.minecraft.world.entity.Entity, double, int, dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience);
  public abstract dev.tc4port.thaumcraft.api.aspect.VisPaymentResult pay(dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public abstract void setCooldown(int);
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionHandler`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.action.FocusActionHandler {
  public abstract dev.tc4port.thaumcraft.api.focus.action.FocusActionResult handle(dev.tc4port.thaumcraft.api.focus.action.FocusActionContext, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionRegistryView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.action.FocusActionRegistryView {
  public abstract long generation();
  public abstract java.util.List<dev.tc4port.thaumcraft.api.focus.action.FocusActionSpec> actions();
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusActionResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.focus.action.FocusActionResult> {
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActionResult PASS;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActionResult SUCCESS;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActionResult START_USING;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActionResult STOP_USING;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActionResult FAILED;
  public static dev.tc4port.thaumcraft.api.focus.action.FocusActionResult[] values();
  public static dev.tc4port.thaumcraft.api.focus.action.FocusActionResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionSpec`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusActionSpec extends java.lang.Record {
  public static final int HARD_MAXIMUM_RANGE = 128;
  public dev.tc4port.thaumcraft.api.focus.action.FocusActionSpec(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget, java.util.Set<dev.tc4port.thaumcraft.api.focus.action.FocusActivation>, dev.tc4port.thaumcraft.api.research.ResearchRequirement, int, int, dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation, dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation actionId();
  public dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget target();
  public java.util.Set<dev.tc4port.thaumcraft.api.focus.action.FocusActivation> activations();
  public dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
  public int maximumRange();
  public int priority();
  public dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation castAnimation();
  public dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience presentation();
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget {
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActivation`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusActivation extends java.lang.Enum<dev.tc4port.thaumcraft.api.focus.action.FocusActivation> {
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActivation USE_AIR;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActivation USE_BLOCK;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActivation USE_ENTITY;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActivation USING_TICK;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusActivation STOP_USING;
  public static dev.tc4port.thaumcraft.api.focus.action.FocusActivation[] values();
  public static dev.tc4port.thaumcraft.api.focus.action.FocusActivation valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization(boolean, java.util.Optional<net.minecraft.world.phys.Vec3>);
  public static dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization allow();
  public static dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization allow(net.minecraft.world.phys.Vec3);
  public static dev.tc4port.thaumcraft.api.focus.action.FocusAuthorization deny();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public boolean authorized();
  public java.util.Optional<net.minecraft.world.phys.Vec3> target();
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusAuthorizationContext`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.focus.action.FocusAuthorizationContext {
  public abstract net.minecraft.server.level.ServerPlayer player();
  public abstract net.minecraft.world.InteractionHand hand();
  public abstract net.minecraft.world.item.ItemStack wand();
  public abstract dev.tc4port.thaumcraft.api.focus.FocusStateView installedFocus();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.focus.FocusUpgradeId, java.lang.Integer> installedUpgrades();
  public default double parameter(java.lang.String);
  public abstract dev.tc4port.thaumcraft.api.focus.action.FocusActivation activation();
  public abstract net.minecraft.world.phys.HitResult authoritativeHit();
  public abstract int useTicks();
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation extends java.lang.Enum<dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation> {
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation NONE;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation INSTANT;
  public static final dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation CONTINUOUS;
  public static dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation[] values();
  public static dev.tc4port.thaumcraft.api.focus.action.FocusCastAnimation valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget$Focus`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget$Focus extends java.lang.Record implements dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget {
  public dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget$Focus(dev.tc4port.thaumcraft.api.focus.FocusId);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.focus.FocusId id();
}
```

### `dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget$Upgrade`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget$Upgrade extends java.lang.Record implements dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget {
  public dev.tc4port.thaumcraft.api.focus.action.FocusActionTarget$Upgrade(dev.tc4port.thaumcraft.api.focus.FocusUpgradeId);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.focus.FocusUpgradeId id();
}
```

## 6.16 `dev.tc4port.thaumcraft.api.golem`

傀儡状态、标记、家位置与空间适配。

### `dev.tc4port.thaumcraft.api.golem.GolemApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemApi {
  public static boolean isGolem(net.minecraft.world.entity.Entity);
  public static net.minecraft.core.Direction homeSide(net.minecraft.world.entity.Entity);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.golem.GolemView> view(net.minecraft.world.entity.Entity);
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemControlApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemControlApi {
  public static final int MAX_MARKERS = 64;
  public static dev.tc4port.thaumcraft.api.golem.GolemControlResult setHome(net.minecraft.server.level.ServerLevel, net.minecraft.world.entity.Entity, net.minecraft.core.GlobalPos, net.minecraft.core.Direction);
  public static dev.tc4port.thaumcraft.api.golem.GolemControlResult replaceMarkers(net.minecraft.server.level.ServerLevel, net.minecraft.world.entity.Entity, java.util.List<dev.tc4port.thaumcraft.api.golem.GolemMarkerView>);
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemControlResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemControlResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.golem.GolemControlResult> {
  public static final dev.tc4port.thaumcraft.api.golem.GolemControlResult UPDATED;
  public static final dev.tc4port.thaumcraft.api.golem.GolemControlResult UNCHANGED;
  public static final dev.tc4port.thaumcraft.api.golem.GolemControlResult NOT_A_GOLEM;
  public static final dev.tc4port.thaumcraft.api.golem.GolemControlResult WRONG_LEVEL;
  public static final dev.tc4port.thaumcraft.api.golem.GolemControlResult INVALID_TARGET;
  public static final dev.tc4port.thaumcraft.api.golem.GolemControlResult OFF_SERVER_THREAD;
  public static dev.tc4port.thaumcraft.api.golem.GolemControlResult[] values();
  public static dev.tc4port.thaumcraft.api.golem.GolemControlResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemMarkerView`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemMarkerView extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.golem.GolemMarkerView(net.minecraft.core.GlobalPos, net.minecraft.core.Direction, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.core.GlobalPos position();
  public net.minecraft.core.Direction side();
  public int color();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction {
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemSpatialAdapter`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.golem.GolemSpatialAdapter {
  public abstract net.minecraft.resources.ResourceLocation id();
  public default int priority();
  public abstract java.util.Optional<dev.tc4port.thaumcraft.api.golem.GolemTravelFrame> resolve(dev.tc4port.thaumcraft.api.golem.GolemTravelContext);
  public default java.util.Optional<dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction> recover(dev.tc4port.thaumcraft.api.golem.GolemTravelContext, dev.tc4port.thaumcraft.api.golem.GolemTravelFrame, int);
  public default java.util.OptionalDouble distanceSquared(net.minecraft.server.level.ServerLevel, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3);
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemSpatialAdapters`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemSpatialAdapters {
  public static dev.tc4port.thaumcraft.api.Registration register(dev.tc4port.thaumcraft.api.golem.GolemSpatialAdapter);
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemTravelContext`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemTravelContext extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.golem.GolemTravelContext(net.minecraft.server.level.ServerLevel, net.minecraft.world.entity.Entity, dev.tc4port.thaumcraft.api.golem.GolemTravelTarget, double, double);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.server.level.ServerLevel level();
  public net.minecraft.world.entity.Entity golem();
  public dev.tc4port.thaumcraft.api.golem.GolemTravelTarget target();
  public double acceptedDistanceSqr();
  public double speed();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemTravelFrame`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemTravelFrame extends java.lang.Record {
  public static final int MAX_PATH_TARGETS = 64;
  public dev.tc4port.thaumcraft.api.golem.GolemTravelFrame(long, net.minecraft.world.phys.Vec3, net.minecraft.core.BlockPos, java.util.Set<net.minecraft.core.BlockPos>, double);
  public static dev.tc4port.thaumcraft.api.golem.GolemTravelFrame simple(long, net.minecraft.world.phys.Vec3, net.minecraft.core.BlockPos, double);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public long routeRevision();
  public net.minecraft.world.phys.Vec3 interactionPoint();
  public net.minecraft.core.BlockPos navigationTarget();
  public java.util.Set<net.minecraft.core.BlockPos> pathTargets();
  public double distanceSqr();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemTravelTarget`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.golem.GolemTravelTarget {
  public abstract net.minecraft.world.phys.Vec3 fallbackInteractionPoint();
  public static dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$BlockTarget block(net.minecraft.core.BlockPos);
  public static dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$BlockTarget block(net.minecraft.core.BlockPos, net.minecraft.core.Direction);
  public static dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$BlockTarget block(net.minecraft.core.BlockPos, net.minecraft.core.Direction, net.minecraft.world.phys.Vec3);
  public static dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$PointTarget point(net.minecraft.world.phys.Vec3);
  public static dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$EntityTarget entity(net.minecraft.world.entity.Entity);
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemView`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemView extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.golem.GolemView(java.lang.String, java.util.Optional<net.minecraft.resources.ResourceLocation>, java.util.Optional<net.minecraft.core.GlobalPos>, java.util.List<dev.tc4port.thaumcraft.api.golem.GolemMarkerView>, net.minecraft.resources.ResourceLocation, net.minecraft.world.phys.Vec3, float, float);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.lang.String decorations();
  public java.util.Optional<net.minecraft.resources.ResourceLocation> coreId();
  public java.util.Optional<net.minecraft.core.GlobalPos> home();
  public java.util.List<dev.tc4port.thaumcraft.api.golem.GolemMarkerView> markers();
  public net.minecraft.resources.ResourceLocation type();
  public net.minecraft.world.phys.Vec3 position();
  public float health();
  public float maximumHealth();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction$ControlledStep`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction$ControlledStep extends java.lang.Record implements dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction {
  public dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction$ControlledStep(net.minecraft.world.phys.Vec3, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.world.phys.Vec3 target();
  public int maxTicks();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction$Path`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction$Path extends java.lang.Record implements dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction {
  public dev.tc4port.thaumcraft.api.golem.GolemRecoveryAction$Path(java.util.Set<net.minecraft.core.BlockPos>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Set<net.minecraft.core.BlockPos> targets();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$BlockTarget`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$BlockTarget extends java.lang.Record implements dev.tc4port.thaumcraft.api.golem.GolemTravelTarget {
  public dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$BlockTarget(net.minecraft.core.BlockPos, net.minecraft.core.Direction, net.minecraft.world.phys.Vec3);
  public net.minecraft.world.phys.Vec3 fallbackInteractionPoint();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.core.BlockPos pos();
  public net.minecraft.core.Direction face();
  public net.minecraft.world.phys.Vec3 interactionPoint();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$EntityTarget`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$EntityTarget extends java.lang.Record implements dev.tc4port.thaumcraft.api.golem.GolemTravelTarget {
  public dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$EntityTarget(net.minecraft.world.entity.Entity);
  public net.minecraft.world.phys.Vec3 fallbackInteractionPoint();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.world.entity.Entity entity();
}
```

### `dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$PointTarget`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$PointTarget extends java.lang.Record implements dev.tc4port.thaumcraft.api.golem.GolemTravelTarget {
  public dev.tc4port.thaumcraft.api.golem.GolemTravelTarget$PointTarget(net.minecraft.world.phys.Vec3);
  public net.minecraft.world.phys.Vec3 fallbackInteractionPoint();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.world.phys.Vec3 point();
}
```

## 6.17 `dev.tc4port.thaumcraft.api.integration`

与其他模组交互时可用的稳定公共契约。

### `dev.tc4port.thaumcraft.api.integration.JadeRegistration`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.integration.JadeRegistration {
  public dev.tc4port.thaumcraft.api.integration.JadeRegistration();
  public static void client(snownee.jade.api.IWailaClientRegistration);
  public static void blockData(snownee.jade.api.IWailaCommonRegistration, snownee.jade.api.IServerDataProvider<snownee.jade.api.BlockAccessor>, java.lang.Class<? extends net.minecraft.world.level.block.Block>);
}
```

## 6.18 `dev.tc4port.thaumcraft.api.inventory`

公共容器和物品栏操作契约。

### `dev.tc4port.thaumcraft.api.inventory.FakeSlot`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.inventory.FakeSlot {
  public abstract boolean isFake();
}
```

## 6.19 `dev.tc4port.thaumcraft.api.item`

附属自有物品可实现的装备、修复、揭示和法术接口。

### `dev.tc4port.thaumcraft.api.item.AuraRevealingGear`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.AuraRevealingGear {
  public abstract boolean revealsThaumcraftAura(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player);
}
```

### `dev.tc4port.thaumcraft.api.item.ExtendedRepairableGear`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.ExtendedRepairableGear extends dev.tc4port.thaumcraft.api.item.RepairableGear {
  public abstract boolean beforeThaumcraftRepair(net.minecraft.world.item.ItemStack, net.minecraft.server.level.ServerPlayer, int);
}
```

### `dev.tc4port.thaumcraft.api.item.GogglesOverlayGear`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.GogglesOverlayGear {
  public abstract boolean showsThaumcraftGogglesOverlay(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player);
}
```

### `dev.tc4port.thaumcraft.api.item.InfusionEquipmentApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.item.InfusionEquipmentApi {
  public static boolean hasGoggles(net.minecraft.world.item.ItemStack);
  public static java.util.OptionalInt mask(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.item.ItemProperties`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.item.ItemProperties {
  public static net.minecraft.network.chat.Component customName(net.minecraft.world.item.ItemStack);
  public static net.minecraft.world.item.Item$Properties unbreakable(net.minecraft.world.item.Item$Properties);
  public static void bind(net.minecraft.world.item.Item, net.minecraft.world.item.Item$Properties);
  public static net.minecraft.world.item.Item$Properties movementTool(net.minecraft.world.item.Item$Properties, net.minecraft.world.item.Tier, float, float, net.minecraft.resources.ResourceLocation, double);
  public static net.minecraft.world.item.Item$Properties container(net.minecraft.world.item.Item$Properties);
  public static int hashItemAndData(net.minecraft.world.item.ItemStack);
  public static net.minecraft.world.level.block.state.BlockState blockState(net.minecraft.world.item.ItemStack, net.minecraft.world.level.block.state.BlockState);
}
```

### `dev.tc4port.thaumcraft.api.item.ItemStatePlatform`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.item.ItemStatePlatform {
  public static final com.mojang.serialization.Codec<net.minecraft.world.item.ItemStack> OPTIONAL_STACK_CODEC;
  public static <T> net.minecraft.world.item.Item$Properties withDefault(net.minecraft.world.item.Item$Properties, net.minecraft.core.component.DataComponentType<T>, T);
  public static void bindDefaults(net.minecraft.world.item.Item, net.minecraft.world.item.Item$Properties);
  public static boolean hasStackChanges(net.minecraft.world.item.ItemStack);
  public static <T> net.minecraft.core.component.DataComponentType<T> type(net.minecraft.core.component.DataComponentType<T>);
  public static <T> T get(net.minecraft.world.item.ItemStack, net.minecraft.core.component.DataComponentType<T>);
  public static boolean has(net.minecraft.world.item.ItemStack, net.minecraft.core.component.DataComponentType<?>);
  public static <T> T set(net.minecraft.world.item.ItemStack, net.minecraft.core.component.DataComponentType<T>, T);
  public static <T> T remove(net.minecraft.world.item.ItemStack, net.minecraft.core.component.DataComponentType<T>);
  public static java.lang.Object contentsForHash(net.minecraft.world.item.ItemStack);
  public static void register(java.lang.Object, java.util.List<? extends net.minecraft.core.component.DataComponentType<?>>);
}
```

### `dev.tc4port.thaumcraft.api.item.RepairableGear`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.RepairableGear {
}
```

### `dev.tc4port.thaumcraft.api.item.RunicGear`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.RunicGear {
  public static final int MAX_CHARGE = 255;
  public abstract int thaumcraftRunicCharge(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.item.ScribeTools`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.ScribeTools {
  public default boolean hasInk(net.minecraft.world.item.ItemStack);
  public default void consumeInk(net.minecraft.world.item.ItemStack);
  public static boolean isUsable(net.minecraft.world.item.ItemStack);
  public static void consume(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.item.ThaumcraftItemApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.item.ThaumcraftItemApi {
  public static final int MAX_WISP_ASPECT_TYPES = 64;
  public static final int MAX_WISP_TOTAL_ASPECTS = 16384;
  public static final int MAX_WISP_ENCODED_BYTES = 4096;
  public static net.minecraft.world.item.ItemStack createCrystalEssence(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static net.minecraft.world.item.ItemStack createWispEssence(dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
}
```

### `dev.tc4port.thaumcraft.api.item.ToolProperties`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.item.ToolProperties {
  public dev.tc4port.thaumcraft.api.item.ToolProperties();
  public static net.minecraft.world.item.Item$Properties apply(net.minecraft.world.item.Item$Properties, net.minecraft.world.item.Tier, float, float);
}
```

### `dev.tc4port.thaumcraft.api.item.VisDiscountGear`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.VisDiscountGear {
  public abstract int thaumcraftVisDiscount(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.aspect.VisChannel);
}
```

### `dev.tc4port.thaumcraft.api.item.WarpingGear`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.item.WarpingGear {
  public abstract int thaumcraftWarp(net.minecraft.world.item.ItemStack, java.util.Optional<net.minecraft.world.entity.player.Player>);
}
```

### `dev.tc4port.thaumcraft.api.item.WispEssenceFactory`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.item.WispEssenceFactory {
  public static final int MAX_WISP_ASPECT_TYPES = 64;
  public static final int MAX_WISP_TOTAL_ASPECTS = 16384;
  public static final int MAX_WISP_ENCODED_BYTES = 4096;
  public static net.minecraft.world.item.ItemStack create(dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
}
```

## 6.20 `dev.tc4port.thaumcraft.api.loot`

战利品相关公共定义与查询。

### `dev.tc4port.thaumcraft.api.loot.LootBagTier`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.loot.LootBagTier extends java.lang.Enum<dev.tc4port.thaumcraft.api.loot.LootBagTier> {
  public static final dev.tc4port.thaumcraft.api.loot.LootBagTier COMMON;
  public static final dev.tc4port.thaumcraft.api.loot.LootBagTier UNCOMMON;
  public static final dev.tc4port.thaumcraft.api.loot.LootBagTier RARE;
  public static dev.tc4port.thaumcraft.api.loot.LootBagTier[] values();
  public static dev.tc4port.thaumcraft.api.loot.LootBagTier valueOf(java.lang.String);
}
```

## 6.21 `dev.tc4port.thaumcraft.api.machine`

奥术机器和方块实体的只读视图或受控操作。

### `dev.tc4port.thaumcraft.api.machine.ArcaneBoreView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.machine.ArcaneBoreView {
  public abstract boolean hasPickaxe();
  public abstract boolean hasFocus();
  public abstract boolean isPickaxeBroken();
  public abstract boolean isWorking();
  public abstract int radius();
  public abstract int speed();
  public abstract boolean hasNativeClusters();
  public abstract int fortune();
  public abstract boolean hasSilkTouch();
}
```

### `dev.tc4port.thaumcraft.api.machine.ArcaneEarControlApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.machine.ArcaneEarControlApi {
  public static dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult setNote(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, int);
}
```

### `dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult> {
  public static final dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult UPDATED;
  public static final dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult UNCHANGED;
  public static final dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult NOT_AN_ARCANE_EAR;
  public static final dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult TARGET_UNLOADED;
  public static final dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult OFF_SERVER_THREAD;
  public static dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult[] values();
  public static dev.tc4port.thaumcraft.api.machine.ArcaneEarControlResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.machine.ArcaneEarView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.machine.ArcaneEarView {
  public abstract int note();
}
```

### `dev.tc4port.thaumcraft.api.machine.BrainJarView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.machine.BrainJarView {
  public abstract int experience();
}
```

### `dev.tc4port.thaumcraft.api.machine.DeconstructionTableView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.machine.DeconstructionTableView {
  public abstract boolean hasItem();
  public abstract java.util.Optional<dev.tc4port.thaumcraft.api.aspect.AspectId> currentAspect();
}
```

### `dev.tc4port.thaumcraft.api.machine.InfusionPedestal`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.machine.InfusionPedestal {
  public abstract net.minecraft.world.item.ItemStack item();
  public abstract void setItem(int, net.minecraft.world.item.ItemStack);
  public abstract void clearContent();
}
```

## 6.22 `dev.tc4port.thaumcraft.api.node`

灵气节点定义、状态、并发更新和网络消费。

### `dev.tc4port.thaumcraft.api.node.AuraNodeState`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.node.AuraNodeState extends java.lang.Record {
  public static final dev.tc4port.thaumcraft.api.node.AuraNodeState EMPTY;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.node.AuraNodeState> CODEC;
  public dev.tc4port.thaumcraft.api.node.AuraNodeState(java.util.Optional<java.util.UUID>, dev.tc4port.thaumcraft.api.node.NodeTypeId, dev.tc4port.thaumcraft.api.node.NodeModifierId, dev.tc4port.thaumcraft.api.node.NodeVis, dev.tc4port.thaumcraft.api.node.NodeVis);
  public dev.tc4port.thaumcraft.api.node.AuraNodeState withInstanceId(java.util.Optional<java.util.UUID>);
  public dev.tc4port.thaumcraft.api.node.AuraNodeState withType(dev.tc4port.thaumcraft.api.node.NodeTypeId);
  public dev.tc4port.thaumcraft.api.node.AuraNodeState withCurrentVis(dev.tc4port.thaumcraft.api.node.NodeVis);
  public dev.tc4port.thaumcraft.api.node.AuraNodeState withVis(dev.tc4port.thaumcraft.api.node.NodeVis, dev.tc4port.thaumcraft.api.node.NodeVis);
  public dev.tc4port.thaumcraft.api.node.AuraNodeState withState(dev.tc4port.thaumcraft.api.node.NodeTypeId, dev.tc4port.thaumcraft.api.node.NodeModifierId, dev.tc4port.thaumcraft.api.node.NodeVis, dev.tc4port.thaumcraft.api.node.NodeVis);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Optional<java.util.UUID> instanceId();
  public dev.tc4port.thaumcraft.api.node.NodeTypeId type();
  public dev.tc4port.thaumcraft.api.node.NodeModifierId modifier();
  public dev.tc4port.thaumcraft.api.node.NodeVis baseVis();
  public dev.tc4port.thaumcraft.api.node.NodeVis currentVis();
}
```

### `dev.tc4port.thaumcraft.api.node.AuraNodeView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.node.AuraNodeView extends dev.tc4port.thaumcraft.api.aspect.AspectContainerView {
  public abstract dev.tc4port.thaumcraft.api.node.AuraNodeState nodeState();
  public default dev.tc4port.thaumcraft.api.aspect.AspectAmounts inspectionAspects();
  public default dev.tc4port.thaumcraft.api.aspect.AspectAmounts visibleAspects();
  public default java.util.List<dev.tc4port.thaumcraft.api.aspect.AspectId> visibleAspectOrder();
}
```

### `dev.tc4port.thaumcraft.api.node.NodeApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeApi {
  public static dev.tc4port.thaumcraft.api.node.NodeRegistryView registry();
  public static dev.tc4port.thaumcraft.api.node.NodeStateChangeResult replaceLoadedState(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.node.AuraNodeState, dev.tc4port.thaumcraft.api.node.AuraNodeState, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.node.NodeStateChangeResult replaceLoadedStates(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.node.AuraNodeState, dev.tc4port.thaumcraft.api.node.AuraNodeState, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.node.AuraNodeState, dev.tc4port.thaumcraft.api.node.AuraNodeState, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

### `dev.tc4port.thaumcraft.api.node.NodeAspectProfile`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeAspectProfile extends java.lang.Enum<dev.tc4port.thaumcraft.api.node.NodeAspectProfile> {
  public static final dev.tc4port.thaumcraft.api.node.NodeAspectProfile NORMAL;
  public static final dev.tc4port.thaumcraft.api.node.NodeAspectProfile HUNGRY;
  public static final dev.tc4port.thaumcraft.api.node.NodeAspectProfile PURE;
  public static final dev.tc4port.thaumcraft.api.node.NodeAspectProfile DARK;
  public static dev.tc4port.thaumcraft.api.node.NodeAspectProfile[] values();
  public static dev.tc4port.thaumcraft.api.node.NodeAspectProfile valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.node.NodeGenerationSettings`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeGenerationSettings extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.node.NodeGenerationSettings(dev.tc4port.thaumcraft.api.node.NodeTypeId, dev.tc4port.thaumcraft.api.node.NodeModifierId, dev.tc4port.thaumcraft.api.node.NodeTypeId, dev.tc4port.thaumcraft.api.node.NodeTypeId, dev.tc4port.thaumcraft.api.node.NodeTypeId, int, int, float, int, int, int, int, int, int, int, int, int, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.node.NodeTypeId defaultType();
  public dev.tc4port.thaumcraft.api.node.NodeModifierId defaultModifier();
  public dev.tc4port.thaumcraft.api.node.NodeTypeId silverwoodType();
  public dev.tc4port.thaumcraft.api.node.NodeTypeId eerieType();
  public dev.tc4port.thaumcraft.api.node.NodeTypeId taintedType();
  public int modifierRarityDivisor();
  public int smallAuraDivisor();
  public float taintedAuraMultiplier();
  public int extraAspectAttempts();
  public int environmentRadius();
  public int waterThreshold();
  public int lavaThreshold();
  public int stoneThreshold();
  public int foliageThreshold();
  public int strongSpreadMinimum();
  public int strongSpreadRange();
  public int ordinarySpreadMinimum();
  public int ordinarySpreadRange();
}
```

### `dev.tc4port.thaumcraft.api.node.NodeModifierDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeModifierDefinition extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.node.NodeModifierDefinition(dev.tc4port.thaumcraft.api.node.NodeModifierId, int, int, float, float, float, boolean, int, boolean);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.node.NodeModifierId id();
  public int generationWeight();
  public int rechargeIntervalTicks();
  public float energizedOutputMultiplier();
  public float renderAlphaMultiplier();
  public float renderAlphaPulse();
  public boolean shiny();
  public int dischargeIntervalTicks();
  public boolean halfDischargeChance();
}
```

### `dev.tc4port.thaumcraft.api.node.NodeModifierId`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeModifierId extends java.lang.Record implements java.lang.Comparable<dev.tc4port.thaumcraft.api.node.NodeModifierId> {
  public static final dev.tc4port.thaumcraft.api.node.NodeModifierId NONE;
  public static final dev.tc4port.thaumcraft.api.node.NodeModifierId BRIGHT;
  public static final dev.tc4port.thaumcraft.api.node.NodeModifierId PALE;
  public static final dev.tc4port.thaumcraft.api.node.NodeModifierId FADING;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.node.NodeModifierId> CODEC;
  public dev.tc4port.thaumcraft.api.node.NodeModifierId(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.node.NodeModifierId of(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.node.NodeModifierId parse(java.lang.String);
  public java.lang.String serialized();
  public int compareTo(dev.tc4port.thaumcraft.api.node.NodeModifierId);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation value();
  public int compareTo(java.lang.Object);
}
```

### `dev.tc4port.thaumcraft.api.node.NodeRegistryView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.node.NodeRegistryView {
  public abstract long generation();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.node.NodeTypeId, dev.tc4port.thaumcraft.api.node.NodeTypeDefinition> types();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.node.NodeModifierId, dev.tc4port.thaumcraft.api.node.NodeModifierDefinition> modifiers();
  public abstract dev.tc4port.thaumcraft.api.node.NodeGenerationSettings settings();
  public default java.util.Optional<dev.tc4port.thaumcraft.api.node.NodeTypeDefinition> get(dev.tc4port.thaumcraft.api.node.NodeTypeId);
  public default java.util.Optional<dev.tc4port.thaumcraft.api.node.NodeModifierDefinition> get(dev.tc4port.thaumcraft.api.node.NodeModifierId);
}
```

### `dev.tc4port.thaumcraft.api.node.NodeStateChangeResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeStateChangeResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.node.NodeStateChangeResult> {
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult OFF_SERVER_THREAD;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult DUPLICATE_POSITION;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult CHUNK_UNLOADED;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult NOT_A_MUTABLE_NODE;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult NOT_AN_ORDINARY_NODE;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult STALE_EXPECTED_STATE;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult IDENTITY_CHANGE_DENIED;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult UNCHANGED;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult WOULD_REPLACE;
  public static final dev.tc4port.thaumcraft.api.node.NodeStateChangeResult REPLACED;
  public static dev.tc4port.thaumcraft.api.node.NodeStateChangeResult[] values();
  public static dev.tc4port.thaumcraft.api.node.NodeStateChangeResult valueOf(java.lang.String);
  public boolean successful();
  public boolean changed();
}
```

### `dev.tc4port.thaumcraft.api.node.NodeTypeDefinition`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeTypeDefinition extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.node.NodeTypeDefinition(dev.tc4port.thaumcraft.api.node.NodeTypeId, dev.tc4port.thaumcraft.api.node.NodeAspectProfile, int, boolean, boolean, int, boolean, boolean, float);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.node.NodeTypeId id();
  public dev.tc4port.thaumcraft.api.node.NodeAspectProfile initialAspectProfile();
  public int generationWeight();
  public boolean shiny();
  public boolean darkRender();
  public int renderLayer();
  public boolean fixedRotation();
  public boolean volatileOutput();
  public float coreScale();
}
```

### `dev.tc4port.thaumcraft.api.node.NodeTypeId`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeTypeId extends java.lang.Record implements java.lang.Comparable<dev.tc4port.thaumcraft.api.node.NodeTypeId> {
  public static final dev.tc4port.thaumcraft.api.node.NodeTypeId NORMAL;
  public static final dev.tc4port.thaumcraft.api.node.NodeTypeId UNSTABLE;
  public static final dev.tc4port.thaumcraft.api.node.NodeTypeId DARK;
  public static final dev.tc4port.thaumcraft.api.node.NodeTypeId TAINTED;
  public static final dev.tc4port.thaumcraft.api.node.NodeTypeId HUNGRY;
  public static final dev.tc4port.thaumcraft.api.node.NodeTypeId PURE;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.node.NodeTypeId> CODEC;
  public dev.tc4port.thaumcraft.api.node.NodeTypeId(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.node.NodeTypeId of(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.node.NodeTypeId parse(java.lang.String);
  public java.lang.String serialized();
  public int compareTo(dev.tc4port.thaumcraft.api.node.NodeTypeId);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation value();
  public int compareTo(java.lang.Object);
}
```

### `dev.tc4port.thaumcraft.api.node.NodeVis`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.node.NodeVis extends java.lang.Record {
  public static final int MAX_ASPECTS = 256;
  public static final dev.tc4port.thaumcraft.api.node.NodeVis EMPTY;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.node.NodeVis> CODEC;
  public dev.tc4port.thaumcraft.api.node.NodeVis(java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer>);
  public int amount(dev.tc4port.thaumcraft.api.aspect.AspectId);
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts positiveAmounts();
  public boolean equals(java.lang.Object);
  public int hashCode();
  public final java.lang.String toString();
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer> amounts();
}
```

### `dev.tc4port.thaumcraft.api.node.VisNetworkApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.node.VisNetworkApi {
  public static int drain(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.VisChannel, int, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.Registration registerProvider(net.minecraft.resources.ResourceLocation, java.util.function.Function<net.minecraft.world.level.block.entity.BlockEntity, java.util.List<? extends dev.tc4port.thaumcraft.api.node.VisSource>>);
  public static void registerSource(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos);
  public static void removeSource(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos);
  public static int drainRelay(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.VisChannel, int, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static net.minecraft.core.BlockPos facingRelay(net.minecraft.world.level.Level, net.minecraft.core.BlockPos, net.minecraft.core.Direction);
}
```

### `dev.tc4port.thaumcraft.api.node.VisSource`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.node.VisSource {
  public abstract boolean canSupplyVis();
  public abstract net.minecraft.core.BlockPos networkEndpoint();
  public default java.lang.Object simulationIdentity();
  public abstract int takeVis(dev.tc4port.thaumcraft.api.aspect.VisChannel, int, dev.tc4port.thaumcraft.api.aspect.VisAction, int);
}
```

## 6.23 `dev.tc4port.thaumcraft.api.player`

玩家 Warp、同步和只读状态。

### `dev.tc4port.thaumcraft.api.player.FlightAccess`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.player.FlightAccess {
  public dev.tc4port.thaumcraft.api.player.FlightAccess();
  public static void grant(net.minecraft.world.entity.player.Player, net.minecraft.resources.ResourceLocation);
  public static boolean revoke(net.minecraft.world.entity.player.Player, net.minecraft.resources.ResourceLocation);
  public static boolean owns(net.minecraft.world.entity.player.Player, net.minecraft.resources.ResourceLocation);
  public static boolean mayFly(net.minecraft.world.entity.player.Player);
}
```

### `dev.tc4port.thaumcraft.api.player.NetworkPositionInterpolation`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.player.NetworkPositionInterpolation {
  public abstract boolean platform$queuePosition(dev.tc4port.thaumcraft.api.player.NetworkPositionInterpolation$Position);
}
```

### `dev.tc4port.thaumcraft.api.player.PlayerMovementApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.player.PlayerMovementApi {
  public static final double MAX_SYNCED_VELOCITY = 3.9d;
  public static void resetFloatingCounter(net.minecraft.server.level.ServerPlayer);
  public static void setVelocityAndSync(net.minecraft.server.level.ServerPlayer, net.minecraft.world.phys.Vec3);
  public static void setPredictedVelocity(net.minecraft.world.entity.Entity, net.minecraft.world.phys.Vec3);
  public static void scalePredictedVerticalVelocity(net.minecraft.world.entity.Entity, double);
  public static void addPredictedVelocity(net.minecraft.world.entity.Entity, net.minecraft.world.phys.Vec3);
}
```

### `dev.tc4port.thaumcraft.api.player.PlayerWarpApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.player.PlayerWarpApi {
  public static dev.tc4port.thaumcraft.api.player.PlayerWarpView view(net.minecraft.world.entity.player.Player);
}
```

### `dev.tc4port.thaumcraft.api.player.PlayerWarpView`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.player.PlayerWarpView extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.player.PlayerWarpView(int, int, int);
  public long total();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int permanent();
  public int sticky();
  public int temporary();
}
```

### `dev.tc4port.thaumcraft.api.player.NetworkPositionInterpolation$Position`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.player.NetworkPositionInterpolation$Position extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.player.NetworkPositionInterpolation$Position(double, double, double, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public double x();
  public double y();
  public double z();
  public int steps();
}
```

## 6.24 `dev.tc4port.thaumcraft.api.presentation`

服务端确认的音画表现、受众和表现数据。

### `dev.tc4port.thaumcraft.api.presentation.ActionPresentationApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.presentation.ActionPresentationApi {
  public static void present(net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand, net.minecraft.resources.ResourceLocation, net.minecraft.world.phys.Vec3);
  public static void present(net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand, net.minecraft.resources.ResourceLocation, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, net.minecraft.world.entity.Entity, double, int);
  public static void present(net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand, net.minecraft.resources.ResourceLocation, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, net.minecraft.world.entity.Entity, double, int, dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience);
  public static void presentAt(net.minecraft.server.level.ServerLevel, net.minecraft.resources.ResourceLocation, net.minecraft.world.phys.Vec3, net.minecraft.world.phys.Vec3, net.minecraft.world.entity.Entity, double, int);
}
```

### `dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience extends java.lang.Enum<dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience> {
  public static final dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience NONE;
  public static final dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience LOCAL_ONLY;
  public static final dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience PREDICTED;
  public static final dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience CONFIRMED_ALL;
  public static final dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience CONFIRMED_OBSERVERS;
  public static dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience[] values();
  public static dev.tc4port.thaumcraft.api.presentation.ActionPresentationAudience valueOf(java.lang.String);
  public boolean predictsLocally();
  public boolean sendsConfirmation();
}
```

### `dev.tc4port.thaumcraft.api.presentation.WorldEffectsApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.presentation.WorldEffectsApi {
  public static void blockSparkle(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos, double, int, int);
}
```

## 6.25 `dev.tc4port.thaumcraft.api.recipe`

奥术、坩埚、注魔及附魔配方的公共查询与变换。

### `dev.tc4port.thaumcraft.api.recipe.ArcaneCraftingApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.ArcaneCraftingApi {
  public static java.util.List<net.minecraft.world.item.crafting.RecipeHolder<dev.tc4port.thaumcraft.api.recipe.ArcaneCraftingRecipe>> recipes(net.minecraft.world.level.Level);
  public static java.util.Optional<net.minecraft.world.item.crafting.RecipeHolder<dev.tc4port.thaumcraft.api.recipe.ArcaneCraftingRecipe>> byId(net.minecraft.world.level.Level, net.minecraft.resources.ResourceLocation);
}
```

### `dev.tc4port.thaumcraft.api.recipe.ArcaneCraftingRecipe`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.recipe.ArcaneCraftingRecipe extends net.minecraft.world.item.crafting.Recipe<net.minecraft.world.item.crafting.CraftingInput> {
  public abstract dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> vis();
  public default java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> vis(net.minecraft.world.item.crafting.CraftingInput);
  public default java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey> requiredResearch(net.minecraft.world.item.crafting.CraftingInput);
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionCentralTransformation`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.recipe.InfusionCentralTransformation {
  public default boolean matches(net.minecraft.world.item.ItemStack);
  public abstract net.minecraft.world.item.ItemStack transform(net.minecraft.world.item.ItemStack, net.minecraft.core.HolderLookup$Provider);
  public default int instability(net.minecraft.world.item.ItemStack, int);
  public default dev.tc4port.thaumcraft.api.aspect.AspectAmounts aspects(net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.AspectAmounts);
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentApi {
  public static java.util.List<dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentApi$Entry> recipes(net.minecraft.world.level.Level);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentApi$Entry> byId(net.minecraft.world.level.Level, net.minecraft.resources.ResourceLocation);
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentCost`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentCost extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentCost(dev.tc4port.thaumcraft.api.aspect.AspectAmounts, int, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts aspects();
  public int instability();
  public int experienceLevels();
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe {
  public abstract dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
  public abstract net.minecraft.core.Holder<net.minecraft.world.item.enchantment.Enchantment> enchantment();
  public abstract java.util.List<net.minecraft.world.item.crafting.Ingredient> pedestalComponents();
  public abstract java.util.List<dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentStage> stages();
  public abstract dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentScaling costScaling();
  public abstract dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentCost costAtLevel(int);
  public abstract java.util.Optional<dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe$Result> resolve(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentScaling`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentScaling extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentScaling> CODEC;
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentScaling(float, float, float, float);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public float xpPerLevel();
  public float aspectsPerLevel();
  public float aspectsPerOtherLevel();
  public float instabilityPerLevel();
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentStage`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentStage extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentStage> CODEC;
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentStage(int, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int from();
  public int to();
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionInputPatch`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.recipe.InfusionInputPatch {
  public abstract void validate(int, int);
  public abstract void apply(net.minecraft.world.item.ItemStack, int, net.minecraft.core.HolderLookup$Provider);
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionInputPatchApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.InfusionInputPatchApi {
  public static dev.tc4port.thaumcraft.api.Registration register(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.recipe.InfusionInputPatch);
  public static void validate(net.minecraft.resources.ResourceLocation, int, int);
  public static void apply(net.minecraft.resources.ResourceLocation, net.minecraft.world.item.ItemStack, int, net.minecraft.core.HolderLookup$Provider);
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentApi$Entry`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentApi$Entry extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentApi$Entry(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation id();
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe recipe();
}
```

### `dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe$Result`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe$Result extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentRecipe$Result(dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentStage, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentCost);
  public net.minecraft.world.item.ItemStack output();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentStage stage();
  public dev.tc4port.thaumcraft.api.recipe.InfusionEnchantmentCost cost();
}
```

## 6.26 `dev.tc4port.thaumcraft.api.research`

研究键、目录、完成状态、扫描、页面和研究条件。

### `dev.tc4port.thaumcraft.api.research.ResearchApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchApi {
  public static dev.tc4port.thaumcraft.api.research.ResearchRegistryView registry();
  public static dev.tc4port.thaumcraft.api.research.ResearchDifficulty difficulty();
  public static boolean canPurchase(net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static void requestPurchase(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static boolean purchase(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static boolean isComplete(net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static boolean isDiscovered(net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult discover(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static int warp(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchClientPresentation> clientPresentation(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static dev.tc4port.thaumcraft.api.Registration registerWarp(dev.tc4port.thaumcraft.api.research.ResearchKey, int);
  public static dev.tc4port.thaumcraft.api.Registration registerSelectorExclusion(net.minecraft.resources.ResourceLocation, net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.research.ResearchSelectorExclusion);
  public static dev.tc4port.thaumcraft.api.research.ResearchCompletionResult complete(net.minecraft.server.level.ServerPlayer, dev.tc4port.thaumcraft.api.research.ResearchKey, dev.tc4port.thaumcraft.api.research.ResearchCompletionContext);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchCategoryKey`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchCategoryKey extends java.lang.Record implements java.lang.Comparable<dev.tc4port.thaumcraft.api.research.ResearchCategoryKey> {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.research.ResearchCategoryKey> CODEC;
  public dev.tc4port.thaumcraft.api.research.ResearchCategoryKey(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public static dev.tc4port.thaumcraft.api.research.ResearchCategoryKey parse(java.lang.String);
  public java.lang.String serialized();
  public java.lang.String nameTranslationKey();
  public int compareTo(dev.tc4port.thaumcraft.api.research.ResearchCategoryKey);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.research.ResearchKey value();
  public int compareTo(java.lang.Object);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchCategorySummary`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchCategorySummary extends java.lang.Record {
  public static final int DEFAULT_SORT_ORDER = 1000;
  public dev.tc4port.thaumcraft.api.research.ResearchCategorySummary(dev.tc4port.thaumcraft.api.research.ResearchCategoryKey, java.util.Optional<net.minecraft.resources.ResourceLocation>, java.util.Optional<net.minecraft.resources.ResourceLocation>, int, int, int, int, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>);
  public dev.tc4port.thaumcraft.api.research.ResearchCategorySummary(dev.tc4port.thaumcraft.api.research.ResearchCategoryKey, java.util.Optional<net.minecraft.resources.ResourceLocation>, java.util.Optional<net.minecraft.resources.ResourceLocation>, int, int, int, int, int, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.research.ResearchCategoryKey key();
  public java.util.Optional<net.minecraft.resources.ResourceLocation> icon();
  public java.util.Optional<net.minecraft.resources.ResourceLocation> background();
  public int sortOrder();
  public int minimumColumn();
  public int minimumRow();
  public int maximumColumn();
  public int maximumRow();
  public java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey> entries();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchClientPage`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchClientPage extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.research.ResearchClientPage(dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type, java.lang.String, java.util.Optional<java.net.URI>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type type();
  public java.lang.String translationKey();
  public java.util.Optional<java.net.URI> externalLink();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchClientPresentation`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchClientPresentation extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.research.ResearchClientPresentation(java.util.List<dev.tc4port.thaumcraft.api.research.ResearchClientPage>);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.List<dev.tc4port.thaumcraft.api.research.ResearchClientPage> pages();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchCompletionContext`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchCompletionContext extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.research.ResearchCompletionContext(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.research.ResearchCompletionReason);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation source();
  public dev.tc4port.thaumcraft.api.research.ResearchCompletionReason reason();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchCompletionReason`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchCompletionReason extends java.lang.Enum<dev.tc4port.thaumcraft.api.research.ResearchCompletionReason> {
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionReason GAMEPLAY_REWARD;
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionReason SHARED_KNOWLEDGE;
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionReason ADMIN_COMMAND;
  public static dev.tc4port.thaumcraft.api.research.ResearchCompletionReason[] values();
  public static dev.tc4port.thaumcraft.api.research.ResearchCompletionReason valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchCompletionResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchCompletionResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.research.ResearchCompletionResult> {
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionResult COMPLETED;
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionResult ALREADY_COMPLETE;
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionResult UNKNOWN_RESEARCH;
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionResult MISSING_PREREQUISITE;
  public static final dev.tc4port.thaumcraft.api.research.ResearchCompletionResult DENIED;
  public static dev.tc4port.thaumcraft.api.research.ResearchCompletionResult[] values();
  public static dev.tc4port.thaumcraft.api.research.ResearchCompletionResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchCraftingExample`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchCraftingExample extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.research.ResearchCraftingExample(int, java.util.List<net.minecraft.world.item.ItemStack>, net.minecraft.world.item.ItemStack);
  public java.util.List<net.minecraft.world.item.ItemStack> inputs();
  public net.minecraft.world.item.ItemStack output();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public int width();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchCraftingRecipe`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.research.ResearchCraftingRecipe {
  public abstract dev.tc4port.thaumcraft.api.research.ResearchCraftingExample researchCraftingExample(long);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchDifficulty`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchDifficulty extends java.lang.Enum<dev.tc4port.thaumcraft.api.research.ResearchDifficulty> {
  public static final dev.tc4port.thaumcraft.api.research.ResearchDifficulty EASY;
  public static final dev.tc4port.thaumcraft.api.research.ResearchDifficulty NORMAL;
  public static final dev.tc4port.thaumcraft.api.research.ResearchDifficulty HARD;
  public static dev.tc4port.thaumcraft.api.research.ResearchDifficulty[] values();
  public static dev.tc4port.thaumcraft.api.research.ResearchDifficulty valueOf(java.lang.String);
  public int legacyValue();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult> {
  public static final dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult DISCOVERED;
  public static final dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult ALREADY_DISCOVERED;
  public static final dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult ALREADY_COMPLETE;
  public static final dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult OFF_SERVER_THREAD;
  public static dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult[] values();
  public static dev.tc4port.thaumcraft.api.research.ResearchDiscoveryResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchEntryFlag`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchEntryFlag extends java.lang.Enum<dev.tc4port.thaumcraft.api.research.ResearchEntryFlag> {
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag SPECIAL;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag STUB;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag LOST;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag CONCEALED;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag HIDDEN;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag VIRTUAL;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag AUTO_UNLOCK;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag ROUND;
  public static final dev.tc4port.thaumcraft.api.research.ResearchEntryFlag SECONDARY;
  public static dev.tc4port.thaumcraft.api.research.ResearchEntryFlag[] values();
  public static dev.tc4port.thaumcraft.api.research.ResearchEntryFlag valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchEntrySummary`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchEntrySummary extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.research.ResearchEntrySummary(dev.tc4port.thaumcraft.api.research.ResearchKey, dev.tc4port.thaumcraft.api.research.ResearchCategoryKey, dev.tc4port.thaumcraft.api.aspect.AspectAmounts, int, int, int, java.util.Set<dev.tc4port.thaumcraft.api.research.ResearchEntryFlag>, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>, int, java.util.Set<net.minecraft.resources.ResourceLocation>);
  public dev.tc4port.thaumcraft.api.research.ResearchEntrySummary(dev.tc4port.thaumcraft.api.research.ResearchKey, dev.tc4port.thaumcraft.api.research.ResearchCategoryKey, dev.tc4port.thaumcraft.api.aspect.AspectAmounts, int, int, int, java.util.Set<dev.tc4port.thaumcraft.api.research.ResearchEntryFlag>, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>, java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey>, int);
  public boolean hasFlag(dev.tc4port.thaumcraft.api.research.ResearchEntryFlag);
  public boolean hasLabel(net.minecraft.resources.ResourceLocation);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.research.ResearchKey key();
  public dev.tc4port.thaumcraft.api.research.ResearchCategoryKey category();
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts aspects();
  public int displayColumn();
  public int displayRow();
  public int complexity();
  public java.util.Set<dev.tc4port.thaumcraft.api.research.ResearchEntryFlag> flags();
  public java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey> parents();
  public java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey> hiddenParents();
  public java.util.List<dev.tc4port.thaumcraft.api.research.ResearchKey> siblings();
  public int warp();
  public java.util.Set<net.minecraft.resources.ResourceLocation> labels();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchKey`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchKey extends java.lang.Record implements java.lang.Comparable<dev.tc4port.thaumcraft.api.research.ResearchKey> {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.research.ResearchKey> CODEC;
  public dev.tc4port.thaumcraft.api.research.ResearchKey(java.lang.String, java.lang.String);
  public static dev.tc4port.thaumcraft.api.research.ResearchKey of(java.lang.String, java.lang.String);
  public static dev.tc4port.thaumcraft.api.research.ResearchKey parse(java.lang.String);
  public java.lang.String serialized();
  public java.lang.String nameTranslationKey();
  public java.lang.String descriptionTranslationKey();
  public int compareTo(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.lang.String namespace();
  public java.lang.String path();
  public int compareTo(java.lang.Object);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchKeyPrefix`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchKeyPrefix extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.research.ResearchKeyPrefix> CODEC;
  public dev.tc4port.thaumcraft.api.research.ResearchKeyPrefix(java.lang.String, java.lang.String);
  public static dev.tc4port.thaumcraft.api.research.ResearchKeyPrefix parse(java.lang.String);
  public boolean matches(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public java.lang.String serialized();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.lang.String namespace();
  public java.lang.String pathPrefix();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchRecipeDisplay`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchRecipeDisplay extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.research.ResearchRecipeDisplay(net.minecraft.network.chat.Component, net.minecraft.world.item.crafting.Ingredient, net.minecraft.world.item.ItemStack, net.minecraft.world.item.crafting.Ingredient, net.minecraft.network.chat.Component);
  public net.minecraft.network.chat.Component title();
  public net.minecraft.world.item.ItemStack workstation();
  public net.minecraft.network.chat.Component cost();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.world.item.crafting.Ingredient input();
  public net.minecraft.world.item.crafting.Ingredient catalyst();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchRecipeDisplayApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchRecipeDisplayApi {
  public static synchronized <R extends net.minecraft.world.item.crafting.Recipe<?>> dev.tc4port.thaumcraft.api.Registration register(net.minecraft.resources.ResourceLocation, java.lang.Class<R>, java.util.function.Function<R, dev.tc4port.thaumcraft.api.research.ResearchRecipeDisplay>);
  public static synchronized boolean supports(net.minecraft.world.item.crafting.Recipe<?>);
  public static synchronized java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchRecipeDisplay> describe(net.minecraft.world.item.crafting.Recipe<?>);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchRegistryView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.research.ResearchRegistryView {
  public abstract long generation();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.research.ResearchCategoryKey, dev.tc4port.thaumcraft.api.research.ResearchCategorySummary> categories();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.research.ResearchKey, dev.tc4port.thaumcraft.api.research.ResearchEntrySummary> entries();
  public default java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchEntrySummary> get(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public default java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchCategorySummary> get(dev.tc4port.thaumcraft.api.research.ResearchCategoryKey);
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchRequirement`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchRequirement extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.research.ResearchRequirement(java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchKey>);
  public static dev.tc4port.thaumcraft.api.research.ResearchRequirement none();
  public static dev.tc4port.thaumcraft.api.research.ResearchRequirement required(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public boolean isRequired();
  public static com.mojang.serialization.MapCodec<dev.tc4port.thaumcraft.api.research.ResearchRequirement> optionalFieldOf(java.lang.String);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchKey> key();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchSelectorExclusion`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchSelectorExclusion extends java.lang.Record {
  public static final int MAX_NAMESPACES = 64;
  public static final int MAX_KEY_PREFIXES = 128;
  public static final int MAX_KEYS = 256;
  public dev.tc4port.thaumcraft.api.research.ResearchSelectorExclusion(java.util.Set<java.lang.String>, java.util.Set<dev.tc4port.thaumcraft.api.research.ResearchKeyPrefix>, java.util.Set<dev.tc4port.thaumcraft.api.research.ResearchKey>);
  public static dev.tc4port.thaumcraft.api.research.ResearchSelectorExclusion empty();
  public boolean excludes(dev.tc4port.thaumcraft.api.research.ResearchKey);
  public dev.tc4port.thaumcraft.api.research.ResearchSelectorExclusion merge(dev.tc4port.thaumcraft.api.research.ResearchSelectorExclusion);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Set<java.lang.String> namespaces();
  public java.util.Set<dev.tc4port.thaumcraft.api.research.ResearchKeyPrefix> keyPrefixes();
  public java.util.Set<dev.tc4port.thaumcraft.api.research.ResearchKey> keys();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchTableApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchTableApi {
  public static void requestPlaceAspect(net.minecraft.core.BlockPos, int, int, dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static void requestEraseAspect(net.minecraft.core.BlockPos, int, int);
  public static void requestCombine(net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static void requestDuplicate(net.minecraft.core.BlockPos);
  public static boolean placeAspect(net.minecraft.server.level.ServerPlayer, net.minecraft.core.BlockPos, int, int, dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static boolean eraseAspect(net.minecraft.server.level.ServerPlayer, net.minecraft.core.BlockPos, int, int);
  public static boolean combine(net.minecraft.server.level.ServerPlayer, net.minecraft.core.BlockPos, dev.tc4port.thaumcraft.api.aspect.AspectId, dev.tc4port.thaumcraft.api.aspect.AspectId);
  public static boolean duplicate(net.minecraft.server.level.ServerPlayer, net.minecraft.core.BlockPos);
}
```

### `dev.tc4port.thaumcraft.api.research.ScanApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.research.ScanApi {
  public static boolean isObjectScanned(net.minecraft.world.entity.player.Player, net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.research.ScanHandler`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.research.ScanHandler {
  public abstract java.util.Optional<dev.tc4port.thaumcraft.api.research.ScanPhenomenon> scan(net.minecraft.server.level.ServerPlayer, net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.research.ScanPhenomenon`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.research.ScanPhenomenon extends java.lang.Record {
  public static final int MAX_ID_LENGTH = 256;
  public static final int MAX_DISPLAY_JSON_LENGTH = 4096;
  public static final int MAX_ASPECTS = 64;
  public dev.tc4port.thaumcraft.api.research.ScanPhenomenon(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.aspect.AspectAmounts, net.minecraft.network.chat.Component);
  public net.minecraft.network.chat.Component displayName();
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation id();
  public dev.tc4port.thaumcraft.api.aspect.AspectAmounts aspects();
}
```

### `dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type extends java.lang.Enum<dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type> {
  public static final dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type LORE;
  public static final dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type EXTERNAL_LINK;
  public static dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type[] values();
  public static dev.tc4port.thaumcraft.api.research.ResearchClientPage$Type valueOf(java.lang.String);
}
```

## 6.27 `dev.tc4port.thaumcraft.api.taint`

腐化生物群系和腐化行为接口。

### `dev.tc4port.thaumcraft.api.taint.TaintBiomeApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.taint.TaintBiomeApi {
  public static dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult taintLoadedColumn(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos);
}
```

### `dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult> {
  public static final dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult APPLIED;
  public static final dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult CHUNK_UNLOADED;
  public static final dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult OFF_SERVER_THREAD;
  public static dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult[] values();
  public static dev.tc4port.thaumcraft.api.taint.TaintBiomeChangeResult valueOf(java.lang.String);
}
```

## 6.28 `dev.tc4port.thaumcraft.api.vis`

Vis 网络、来源和消费操作。

### `dev.tc4port.thaumcraft.api.vis.OwnedVisStorageProvider`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.vis.OwnedVisStorageProvider {
  public abstract dev.tc4port.thaumcraft.api.vis.VisStorageView view(net.minecraft.world.item.ItemStack);
  public abstract dev.tc4port.thaumcraft.api.wand.VisTransferResult extract(net.minecraft.server.level.ServerPlayer, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

### `dev.tc4port.thaumcraft.api.vis.VisStorageApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.vis.VisStorageApi {
  public static dev.tc4port.thaumcraft.api.Registration registerItem(net.minecraft.world.item.Item, dev.tc4port.thaumcraft.api.vis.OwnedVisStorageProvider);
  public static long generation();
}
```

### `dev.tc4port.thaumcraft.api.vis.VisStorageView`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.vis.VisStorageView extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.vis.VisStorageView(java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>, java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>, long);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> currentCentivis();
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> capacityCentivis();
  public long version();
}
```

## 6.29 `dev.tc4port.thaumcraft.api.wand`

法杖状态、杖柄、杖帽、充能、载体和机器上下文。

### `dev.tc4port.thaumcraft.api.wand.CustomWandItem`

归属：Thaumcraft 4R 本体；类型：类。

```java
public class dev.tc4port.thaumcraft.api.wand.CustomWandItem extends dev.tc4port.thaumcraft.api.wand.WandCarrierItem {
  public dev.tc4port.thaumcraft.api.wand.CustomWandItem(net.minecraft.world.item.Item$Properties, dev.tc4port.thaumcraft.api.wand.CustomWandSpec);
  public final dev.tc4port.thaumcraft.api.wand.CustomWandSpec thaumcraftWandSpec();
  public boolean requiresBothHands(net.minecraft.world.item.ItemStack);
  public net.minecraft.world.InteractionResultHolder<net.minecraft.world.item.ItemStack> use(net.minecraft.world.level.Level, net.minecraft.world.entity.player.Player, net.minecraft.world.InteractionHand);
  public net.minecraft.world.InteractionResult onItemUseFirst(net.minecraft.world.item.ItemStack, net.minecraft.world.item.context.UseOnContext);
  public net.minecraft.world.InteractionResult useOn(net.minecraft.world.item.context.UseOnContext);
  public net.minecraft.world.InteractionResult interactLivingEntity(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player, net.minecraft.world.entity.LivingEntity, net.minecraft.world.InteractionHand);
  public void appendHoverText(net.minecraft.world.item.ItemStack, net.minecraft.world.item.Item$TooltipContext, java.util.List<net.minecraft.network.chat.Component>, net.minecraft.world.item.TooltipFlag);
  public void onUseTick(net.minecraft.world.level.Level, net.minecraft.world.entity.LivingEntity, net.minecraft.world.item.ItemStack, int);
  public int getUseDuration(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.LivingEntity);
  public net.minecraft.world.item.UseAnim getUseAnimation(net.minecraft.world.item.ItemStack);
  public boolean shouldCauseReequipAnimation(net.minecraft.world.item.ItemStack, net.minecraft.world.item.ItemStack, boolean);
  public void inventoryTick(net.minecraft.world.item.ItemStack, net.minecraft.world.level.Level, net.minecraft.world.entity.Entity, int, boolean);
  public void onStopUsing(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.LivingEntity, int);
  public final int adjustedCooldownTicks(int);
}
```

### `dev.tc4port.thaumcraft.api.wand.CustomWandSpec`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.wand.CustomWandSpec extends java.lang.Record {
  public static final int MAX_CAPACITY_CENTIVIS = 10000000;
  public dev.tc4port.thaumcraft.api.wand.CustomWandSpec(dev.tc4port.thaumcraft.api.wand.WandMaterialId, dev.tc4port.thaumcraft.api.wand.WandMaterialId, int, boolean, boolean, boolean, float, float, int, float);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.wand.WandMaterialId rod();
  public dev.tc4port.thaumcraft.api.wand.WandMaterialId cap();
  public int capacityCentivis();
  public boolean staffPower();
  public boolean requiresBothHands();
  public boolean supportsArcaneCrafting();
  public float capCostDivisor();
  public float frugalDiscountDivisor();
  public int continuousIterations();
  public float cooldownMultiplier();
}
```

### `dev.tc4port.thaumcraft.api.wand.VisTransferResult`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.wand.VisTransferResult extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.wand.VisTransferResult(dev.tc4port.thaumcraft.api.aspect.VisCost, java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>, boolean);
  public int transferred(dev.tc4port.thaumcraft.api.aspect.VisChannel);
  public boolean complete();
  public static dev.tc4port.thaumcraft.api.wand.VisTransferResult none(dev.tc4port.thaumcraft.api.aspect.VisCost);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.aspect.VisCost requested();
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> transferredCentivis();
  public boolean mutated();
}
```

### `dev.tc4port.thaumcraft.api.wand.WandApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandApi {
  public static boolean isBuiltinWand(net.minecraft.world.item.ItemStack);
  public static java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> craftingCost(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player, java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer>);
  public static float craftingModifier(net.minecraft.world.item.ItemStack, net.minecraft.world.entity.player.Player, dev.tc4port.thaumcraft.api.aspect.VisChannel);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.wand.WandView> view(net.minecraft.world.item.ItemStack);
  public static boolean supportsArcaneCrafting(net.minecraft.world.item.ItemStack);
  public static boolean requiresBothHands(net.minecraft.world.item.ItemStack);
  public static int cooldownTicks(net.minecraft.world.item.ItemStack, int);
  public static net.minecraft.world.item.ItemStack create(dev.tc4port.thaumcraft.api.wand.WandMaterialId, dev.tc4port.thaumcraft.api.wand.WandMaterialId);
  public static net.minecraft.world.item.ItemStack createFullyCharged(dev.tc4port.thaumcraft.api.wand.WandMaterialId, dev.tc4port.thaumcraft.api.wand.WandMaterialId);
  public static dev.tc4port.thaumcraft.api.wand.VisTransferResult extract(net.minecraft.server.level.ServerPlayer, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.wand.VisTransferResult insert(net.minecraft.server.level.ServerPlayer, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.wand.VisTransferResult extract(dev.tc4port.thaumcraft.api.wand.WandMachineContext, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.wand.VisTransferResult insert(dev.tc4port.thaumcraft.api.wand.WandMachineContext, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public static dev.tc4port.thaumcraft.api.wand.WandPartChangeResult replaceRod(net.minecraft.server.level.ServerPlayer, net.minecraft.world.item.ItemStack, dev.tc4port.thaumcraft.api.wand.WandMaterialId, dev.tc4port.thaumcraft.api.wand.WandMaterialId, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

### `dev.tc4port.thaumcraft.api.wand.WandCapSpec`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandCapSpec extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.wand.WandCapSpec(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.wand.WandMaterialId, float, java.util.Set<dev.tc4port.thaumcraft.api.aspect.VisChannel>, float, net.minecraft.resources.ResourceLocation, int, dev.tc4port.thaumcraft.api.research.ResearchRequirement, dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode, int);
  public dev.tc4port.thaumcraft.api.wand.WandCapSpec(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.wand.WandMaterialId, float, java.util.Set<dev.tc4port.thaumcraft.api.aspect.VisChannel>, float, net.minecraft.resources.ResourceLocation, int, dev.tc4port.thaumcraft.api.research.ResearchRequirement, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation itemId();
  public dev.tc4port.thaumcraft.api.wand.WandMaterialId materialId();
  public float baseCostModifier();
  public java.util.Set<dev.tc4port.thaumcraft.api.aspect.VisChannel> specialCostModifierAspects();
  public float specialCostModifier();
  public net.minecraft.resources.ResourceLocation texture();
  public int craftCost();
  public dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
  public dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode assemblyMode();
  public int order();
}
```

### `dev.tc4port.thaumcraft.api.wand.WandCarrierItem`

归属：Thaumcraft 4R 本体；类型：类。

```java
public abstract class dev.tc4port.thaumcraft.api.wand.WandCarrierItem extends net.minecraft.world.item.Item {
  public abstract boolean requiresBothHands(net.minecraft.world.item.ItemStack);
}
```

### `dev.tc4port.thaumcraft.api.wand.WandMachineContext`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandMachineContext extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.wand.WandMachineContext(net.minecraft.server.level.ServerLevel, net.minecraft.core.BlockPos);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.server.level.ServerLevel level();
  public net.minecraft.core.BlockPos position();
}
```

### `dev.tc4port.thaumcraft.api.wand.WandMaterialId`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandMaterialId extends java.lang.Record implements java.lang.Comparable<dev.tc4port.thaumcraft.api.wand.WandMaterialId> {
  public static final dev.tc4port.thaumcraft.api.wand.WandMaterialId WOOD;
  public static final dev.tc4port.thaumcraft.api.wand.WandMaterialId IRON;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.wand.WandMaterialId> CODEC;
  public dev.tc4port.thaumcraft.api.wand.WandMaterialId(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.wand.WandMaterialId of(net.minecraft.resources.ResourceLocation);
  public static dev.tc4port.thaumcraft.api.wand.WandMaterialId parse(java.lang.String);
  public java.lang.String serialized();
  public int compareTo(dev.tc4port.thaumcraft.api.wand.WandMaterialId);
  public java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation value();
  public int compareTo(java.lang.Object);
}
```

### `dev.tc4port.thaumcraft.api.wand.WandPartApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandPartApi {
  public static final int MAX_CRAFT_COST = 3783;
  public static dev.tc4port.thaumcraft.api.Registration registerRod(dev.tc4port.thaumcraft.api.wand.WandRodSpec);
  public static dev.tc4port.thaumcraft.api.Registration registerCap(dev.tc4port.thaumcraft.api.wand.WandCapSpec);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.wand.WandRodSpec> rod(net.minecraft.world.item.ItemStack);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.wand.WandCapSpec> cap(net.minecraft.world.item.ItemStack);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.wand.WandRodSpec> rod(dev.tc4port.thaumcraft.api.wand.WandMaterialId);
  public static java.util.Optional<dev.tc4port.thaumcraft.api.wand.WandCapSpec> cap(dev.tc4port.thaumcraft.api.wand.WandMaterialId);
  public static java.util.List<dev.tc4port.thaumcraft.api.wand.WandRodSpec> rods();
  public static java.util.List<dev.tc4port.thaumcraft.api.wand.WandCapSpec> caps();
  public static int maximumCentivis(dev.tc4port.thaumcraft.api.wand.WandMaterialId, boolean);
}
```

### `dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode extends java.lang.Enum<dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode> {
  public static final dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode NORMAL;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode HIDDEN;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode RUNTIME_ONLY;
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode> CODEC;
  public static dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode[] values();
  public static dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode valueOf(java.lang.String);
  public boolean assemblyAllowed();
  public boolean recipeViewerVisible();
  public java.lang.String serialized();
}
```

### `dev.tc4port.thaumcraft.api.wand.WandPartChangeResult`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandPartChangeResult extends java.lang.Enum<dev.tc4port.thaumcraft.api.wand.WandPartChangeResult> {
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult CHANGED;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult WOULD_CHANGE;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult UNCHANGED;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult NOT_A_WAND;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult STALE_EXPECTED_ROD;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult UNKNOWN_REPLACEMENT_ROD;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult INCOMPATIBLE_CAPACITY;
  public static final dev.tc4port.thaumcraft.api.wand.WandPartChangeResult OFF_SERVER_THREAD;
  public static dev.tc4port.thaumcraft.api.wand.WandPartChangeResult[] values();
  public static dev.tc4port.thaumcraft.api.wand.WandPartChangeResult valueOf(java.lang.String);
}
```

### `dev.tc4port.thaumcraft.api.wand.WandPartLimits`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandPartLimits {
  public static final int MAX_CRAFT_COST = 3783;
}
```

### `dev.tc4port.thaumcraft.api.wand.WandRechargeSpec`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandRechargeSpec extends java.lang.Record {
  public static final com.mojang.serialization.Codec<dev.tc4port.thaumcraft.api.wand.WandRechargeSpec> CODEC;
  public dev.tc4port.thaumcraft.api.wand.WandRechargeSpec(dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode, java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisChannel>);
  public static dev.tc4port.thaumcraft.api.wand.WandRechargeSpec none();
  public static dev.tc4port.thaumcraft.api.wand.WandRechargeSpec any();
  public static dev.tc4port.thaumcraft.api.wand.WandRechargeSpec aspect(dev.tc4port.thaumcraft.api.aspect.VisChannel);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode mode();
  public java.util.Optional<dev.tc4port.thaumcraft.api.aspect.VisChannel> aspect();
}
```

### `dev.tc4port.thaumcraft.api.wand.WandRodSpec`

归属：Thaumcraft 4R 本体；类型：记录类。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandRodSpec extends java.lang.Record {
  public dev.tc4port.thaumcraft.api.wand.WandRodSpec(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.wand.WandMaterialId, int, int, dev.tc4port.thaumcraft.api.wand.WandRechargeSpec, dev.tc4port.thaumcraft.api.research.ResearchRequirement, net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode, boolean, boolean, boolean, int);
  public dev.tc4port.thaumcraft.api.wand.WandRodSpec(net.minecraft.resources.ResourceLocation, dev.tc4port.thaumcraft.api.wand.WandMaterialId, int, int, dev.tc4port.thaumcraft.api.wand.WandRechargeSpec, dev.tc4port.thaumcraft.api.research.ResearchRequirement, net.minecraft.resources.ResourceLocation, boolean, boolean, boolean, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceLocation itemId();
  public dev.tc4port.thaumcraft.api.wand.WandMaterialId materialId();
  public int capacity();
  public int craftCost();
  public dev.tc4port.thaumcraft.api.wand.WandRechargeSpec recharge();
  public dev.tc4port.thaumcraft.api.research.ResearchRequirement research();
  public net.minecraft.resources.ResourceLocation texture();
  public dev.tc4port.thaumcraft.api.wand.WandPartAssemblyMode assemblyMode();
  public boolean staff();
  public boolean glowing();
  public boolean runes();
  public int order();
}
```

### `dev.tc4port.thaumcraft.api.wand.WandView`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.wand.WandView {
  public abstract dev.tc4port.thaumcraft.api.wand.WandMaterialId rod();
  public abstract dev.tc4port.thaumcraft.api.wand.WandMaterialId cap();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> visCentivis();
  public abstract java.util.Map<dev.tc4port.thaumcraft.api.aspect.VisChannel, java.lang.Integer> capacityCentivis();
  public abstract java.util.Optional<dev.tc4port.thaumcraft.api.focus.FocusStateView> installedFocus();
  public abstract boolean staff();
  public abstract long definitionGeneration();
}
```

### `dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode`

归属：Thaumcraft 4R 本体；类型：枚举。

```java
public final class dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode extends java.lang.Enum<dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode> {
  public static final dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode NONE;
  public static final dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode ANY;
  public static final dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode ASPECT;
  public static dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode[] values();
  public static dev.tc4port.thaumcraft.api.wand.WandRechargeSpec$Mode valueOf(java.lang.String);
}
```

## 6.30 `dev.tc4port.thaumcraft.api.wand.behavior`

服务端法杖行为、使用阶段和回调。

### `dev.tc4port.thaumcraft.api.wand.behavior.WandBehaviorApi`

归属：Thaumcraft 4R 本体；类型：类。

```java
public final class dev.tc4port.thaumcraft.api.wand.behavior.WandBehaviorApi {
  public static dev.tc4port.thaumcraft.api.Registration register(dev.tc4port.thaumcraft.api.wand.WandMaterialId, dev.tc4port.thaumcraft.api.wand.behavior.WandServerBehavior);
  public static long generation();
}
```

### `dev.tc4port.thaumcraft.api.wand.behavior.WandServerBehavior`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.wand.behavior.WandServerBehavior {
  public abstract void serverTick(dev.tc4port.thaumcraft.api.wand.behavior.WandServerContext);
}
```

### `dev.tc4port.thaumcraft.api.wand.behavior.WandServerContext`

归属：Thaumcraft 4R 本体；类型：接口。

```java
public interface dev.tc4port.thaumcraft.api.wand.behavior.WandServerContext {
  public abstract net.minecraft.server.level.ServerPlayer player();
  public abstract net.minecraft.world.InteractionHand hand();
  public abstract net.minecraft.world.item.ItemStack wand();
  public abstract dev.tc4port.thaumcraft.api.wand.WandView view();
  public abstract dev.tc4port.thaumcraft.api.wand.VisTransferResult extract(dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
  public abstract dev.tc4port.thaumcraft.api.wand.VisTransferResult insert(dev.tc4port.thaumcraft.api.aspect.VisCost, dev.tc4port.thaumcraft.api.aspect.VisAction);
}
```

## 6.31 `dev.tc4port.thaumictinkerer.api.enchantment`

神秘工匠渗透附魔台的公开注册定义。

### `dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentApi`

归属：神秘工匠；类型：类。

```java
public final class dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentApi {
  public static synchronized void register(dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition);
  public static synchronized java.util.List<dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition> registeredAddons();
}
```

### `dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition`

归属：神秘工匠；类型：记录类。

```java
public final class dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition extends java.lang.Record {
  public static final int DEFAULT_SORT_ORDER = 1000;
  public dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition(net.minecraft.resources.ResourceKey<net.minecraft.world.item.enchantment.Enchantment>, java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer>, java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchKey>, net.minecraft.resources.ResourceLocation, java.util.function.BooleanSupplier);
  public dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition(net.minecraft.resources.ResourceKey<net.minecraft.world.item.enchantment.Enchantment>, java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer>, java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchKey>, net.minecraft.resources.ResourceLocation, int);
  public dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition(net.minecraft.resources.ResourceKey<net.minecraft.world.item.enchantment.Enchantment>, java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer>, java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchKey>, net.minecraft.resources.ResourceLocation);
  public dev.tc4port.thaumictinkerer.api.enchantment.OsmoticEnchantmentDefinition(net.minecraft.resources.ResourceKey<net.minecraft.world.item.enchantment.Enchantment>, java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer>, java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchKey>, net.minecraft.resources.ResourceLocation, java.util.function.BooleanSupplier, int);
  public final java.lang.String toString();
  public final int hashCode();
  public final boolean equals(java.lang.Object);
  public net.minecraft.resources.ResourceKey<net.minecraft.world.item.enchantment.Enchantment> enchantment();
  public java.util.Map<dev.tc4port.thaumcraft.api.aspect.AspectId, java.lang.Integer> baseCost();
  public java.util.Optional<dev.tc4port.thaumcraft.api.research.ResearchKey> research();
  public net.minecraft.resources.ResourceLocation icon();
  public java.util.function.BooleanSupplier enabled();
  public int sortOrder();
}
```

## 7. 使用前核对清单

1. 依赖的 API Jar、完整运行 Jar、Minecraft 和加载器目标必须完全一致。
2. 只导入本文完整清单中的类型，不因某个实现类恰好是 `public` 就把它当作 API。
3. 检查目标方法的完整重载签名、逻辑侧、线程和模拟/执行约束。
4. 保存 `Registration`，并在配置关闭、模组卸载式清理或测试复位时关闭它。
5. 不缓存跨资源重载的注册表快照。
6. 发布前在只含 API Jar 的编译类路径上重新编译附属，并在匹配完整模组 Jar 的运行环境中做链接验证。
