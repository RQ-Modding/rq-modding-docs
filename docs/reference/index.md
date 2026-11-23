# API reference

Loader version 2.66.2.

## Namespaces

| Namespace | Summary |
| --- | --- |
| [`rq`](api/rq.md) | The global table every mod uses to reach the game. |
| [`rq.agent`](api/rq.agent.md) | Lets the test pipe (`rqmod-ctl`) see and press a mod's controls. |
| [`rq.ain`](api/rq.ain.md) | Reaches into the game's own code (the AIN): call, hook and patch its functions, and read and write its globals. |
| [`rq.battle`](api/rq.battle.md) | Hooks into fights: events, ally skill select, marks and buffs on the cards, faces, states, drops, and scripted fights. |
| [`rq.castle`](api/rq.castle.md) | Reads the castle: whether it is open, its rooms and who is in them. |
| [`rq.chara`](api/rq.chara.md) | Reads and changes characters: their skills, stats, the skill buy list, and the roster. |
| [`rq.chest`](api/rq.chest.md) | The chance of opening a red chest. |
| [`rq.combat`](api/rq.combat.md) | Changes physical damage, accuracy and criticals. |
| [`rq.config`](api/rq.config.md) | A Mods tab in the game's Config screen. |
| [`rq.counter`](api/rq.counter.md) | Lets the Counter skill (259) work after Ally Guard. |
| [`rq.debug`](api/rq.debug.md) | Adds rows to the engine's F3 debug menu. |
| [`rq.dungeon`](api/rq.dungeon.md) | Reads and changes the dungeon: the map, the player's place, objects on it, and the camera. |
| [`rq.encounters`](api/rq.encounters.md) | Random fights on a quest's map. |
| [`rq.game`](api/rq.game.md) | The player's money and charisma, as the system bar shows them. |
| [`rq.gamebutton`](api/rq.gamebutton.md) | Buttons of mods in the game's own menus, made by the game itself. |
| [`rq.hud`](api/rq.hud.md) | Draws text, boxes and CGs over the game, and reads clicks on them. |
| [`rq.ids`](api/rq.ids.md) | The game's numbers by name: characters, items, monsters, quests, skills, and the small lists the game names (classes, states, races, character types, elements, item kinds, skill targets). |
| [`rq.image`](api/rq.image.md) | Images from a mod's folder, shown by the game as CGs. |
| [`rq.input`](api/rq.input.md) | Reads the mouse and keyboard, and drives them for the game. |
| [`rq.item`](api/rq.item.md) | Defines, gives and changes items. |
| [`rq.items`](api/rq.items.md) | Lists the item instances the player owns. |
| [`rq.knownskills`](api/rq.knownskills.md) | More known skills than the game's 17, shown 17 at a time on the status page and in the skill window. |
| [`rq.loot`](api/rq.loot.md) | Chest loot: what the pools roll, and the items the player will find, known in advance. |
| [`rq.mod`](api/rq.mod.md) | Finds out about other mods, and reaches what they share. |
| [`rq.monster`](api/rq.monster.md) | The game's list of monsters: read a monster's data, change it each time the game builds it, and change each enemy a fight builds. A mod's own monsters, enemy groups and models. |
| [`rq.music`](api/rq.music.md) | Music from a mod's own file, in place of one of the game's tracks. |
| [`rq.orb`](api/rq.orb.md) | The blue Recovery Spring on the map (`回復の泉`, object 203). |
| [`rq.party`](api/rq.party.md) | Reads and changes who is in the party. |
| [`rq.quests`](api/rq.quests.md) | Lists the quests and follows them: clears, endings, quest moments and state. |
| [`rq.random`](api/rq.random.md) | Controls the random number generator the game and the loader share. |
| [`rq.savedata`](api/rq.savedata.md) | Each mod's data that follows the game's save. |
| [`rq.saves`](api/rq.saves.md) | Save profiles: whole save folders the player can switch between. |
| [`rq.scene`](api/rq.scene.md) | Plays scenes with the game's own commands, so a mod can do anything a game scene does. |
| [`rq.shop`](api/rq.shop.md) | Adds stock to Frostbuy, the item shop, and reports purchases. |
| [`rq.skill`](api/rq.skill.md) | Reads, defines and patches skills, and rewrites their hover text. |
| [`rq.skilllist`](api/rq.skilllist.md) | Pages the Potential Skills grid, 36 skills a page. |
| [`rq.sound`](api/rq.sound.md) | Plays sounds: a game sound number, a file in the mod folder, or a sound inside a game Flash file. |
| [`rq.speed`](api/rq.speed.md) | Runs the game clock faster or slower than real time. |
| [`rq.sprite`](api/rq.sprite.md) | Sprites a mod makes once and changes later, drawn among the game's own in z order. |
| [`rq.status`](api/rq.status.md) | Battle states made by mods, such as a burn, a bleed, a regeneration, a freeze or a weaken, that live beside the game's poison, stun and ▲▼, in one registry every mod shares. |
| [`rq.statuspage`](api/rq.statuspage.md) | A character's status page, for mods. |
| [`rq.store`](api/rq.store.md) | Small key and value storage for each mod and each save profile. |
| [`rq.store.global`](api/rq.store.global.md) | The same calls as `rq.store`, in one file for every save profile. |
| [`rq.ui`](api/rq.ui.md) | Reads what is on the screen and saves screenshots. |
| [`rq.uikit`](api/rq.uikit.md) | Widgets in the look of the game's Config screen and, since 2.6.0, of its hub. |
| [`rq.units`](api/rq.units.md) | Lists the recruited characters. |
| [`rq.world`](api/rq.world.md) | The world and the game's world transfer. |

## Types

| Type | Summary |
| --- | --- |
| [`rq.AccuracyCtx`](types/rq.AccuracyCtx.md) | What `rq.combat.on_accuracy` gets for one accuracy check. |
| [`rq.AgentOpts`](types/rq.AgentOpts.md) | How `rq.agent.control` finds a control: a game button, or a rectangle a mod draws. |
| [`rq.AgentWidget`](types/rq.AgentWidget.md) | A control a mod drew on this update, for `rqmod-ctl ui`. |
| [`rq.AinHookCtx`](types/rq.AinHookCtx.md) | What an `rq.ain.hook` callback gets. |
| [`rq.AinHookOpts`](types/rq.AinHookOpts.md) | What `rq.ain.hook` takes. |
| [`rq.AreaCtx`](types/rq.AreaCtx.md) | What `rq.dungeon.on_area` gets. |
| [`rq.BagInfo`](types/rq.BagInfo.md) | One enemy in `rq.battle.bags`. |
| [`rq.BattleActor`](types/rq.BattleActor.md) | The ally whose turn it is, from `rq.battle.actor`. |
| [`rq.BattleDownCtx`](types/rq.BattleDownCtx.md) | What `rq.battle.on_down` gets. |
| [`rq.BattleEndCtx`](types/rq.BattleEndCtx.md) | What `rq.battle.on_end` gets. |
| [`rq.BattleFamiliar`](types/rq.BattleFamiliar.md) | The familiar of a fight, as `rq.battle.familiar` returns it. |
| [`rq.BattleForecastCtx`](types/rq.BattleForecastCtx.md) | What `rq.battle.on_forecast` gets for one forecast line. |
| [`rq.BattleHitCtx`](types/rq.BattleHitCtx.md) | What `rq.battle.on_hit` gets for one hit. |
| [`rq.BattleLogCtx`](types/rq.BattleLogCtx.md) | What `rq.battle.on_log` gets for one line of the battle log. |
| [`rq.BattleOrderAfterCtx`](types/rq.BattleOrderAfterCtx.md) | What `rq.battle.on_order_after` gets after the game built the turn list. |
| [`rq.BattleOrderCtx`](types/rq.BattleOrderCtx.md) | What `rq.battle.on_order` gets before the game builds the turn list. |
| [`rq.BattleSelectKeyCtx`](types/rq.BattleSelectKeyCtx.md) | What `rq.battle.on_select_key` gets. |
| [`rq.BattleSnap`](types/rq.BattleSnap.md) | What `rq.battle.snapshot` returns: a copy of the fight screen. |
| [`rq.BattleStartCtx`](types/rq.BattleStartCtx.md) | What `rq.battle.on_start` gets. |
| [`rq.BattleStates`](types/rq.BattleStates.md) | Every state of a character, from `rq.battle.states`. |
| [`rq.BattleSupportCtx`](types/rq.BattleSupportCtx.md) | What `rq.battle.on_support` gets. |
| [`rq.BattleSwitchCtx`](types/rq.BattleSwitchCtx.md) | What `rq.battle.on_switch` gets for one rank. |
| [`rq.BattleTurnCtx`](types/rq.BattleTurnCtx.md) | What `rq.battle.on_turn` gets: the character whose turn starts, and what can change it. |
| [`rq.BattleUseEvent`](types/rq.BattleUseEvent.md) | What `rq.battle.on_use` gets. |
| [`rq.BoostRow`](types/rq.BoostRow.md) | One Boost, from `rq.chara.boosts`. |
| [`rq.BuffDef`](types/rq.BuffDef.md) | A mod's buff on a card, for `rq.battle.set_buff` and `set_rank_buff`. |
| [`rq.BuffInfo`](types/rq.BuffInfo.md) | One mark a card shows, from `rq.battle.buffs`. |
| [`rq.BuyCtx`](types/rq.BuyCtx.md) | What an `rq.shop.on_buy` callback gets. |
| [`rq.CanBuyCtx`](types/rq.CanBuyCtx.md) | What an `rq.shop.on_can_buy` callback gets. |
| [`rq.CanEquipCtx`](types/rq.CanEquipCtx.md) | What `rq.item.on_can_equip` gets for one item and one character. |
| [`rq.CapCtx`](types/rq.CapCtx.md) | What `rq.combat.on_cap` gets for one hit. |
| [`rq.Castle`](types/rq.Castle.md) | The castle's state, from `rq.castle()`. |
| [`rq.CastleRoom`](types/rq.CastleRoom.md) | A castle room, from `rq.castle()`. |
| [`rq.CastleRoomHandle`](types/rq.CastleRoomHandle.md) | A mod's room, from `rq.castle.room`. |
| [`rq.CastleRoomInfo`](types/rq.CastleRoomInfo.md) | A mod's room, as `rq.castle.rooms` lists it. |
| [`rq.CastleRoomPlace`](types/rq.CastleRoomPlace.md) | Where a mod's room is this time, from a room's `where()`. |
| [`rq.CastleRoomSpec`](types/rq.CastleRoomSpec.md) | A mod's room in Rance Castle, for `rq.castle.room`. |
| [`rq.CharaDef`](types/rq.CharaDef.md) | A character template for `rq.chara.define`. |
| [`rq.CharaEdit`](types/rq.CharaEdit.md) | A patch for `rq.chara.edit`. `level`, `level_max`, `skills` and `lines` do not apply. |
| [`rq.CharaFields`](types/rq.CharaFields.md) | The fields `rq.chara.define` and `rq.chara.edit` share. |
| [`rq.CharaInit`](types/rq.CharaInit.md) | Stat bonuses that each recalculation adds, in `rq.CharaFields.init`. |
| [`rq.CharaSkillGrant`](types/rq.CharaSkillGrant.md) | A skill a character gets, in `rq.CharaFields.skills` and `rq.CharaEdit.learn`. |
| [`rq.CharaSlot`](types/rq.CharaSlot.md) | One row of a character's skill list, from `rq.chara.slots`. |
| [`rq.CharaState`](types/rq.CharaState.md) | Everything `rq.chara.get` returns about a character. `rq.chara.set` takes the same names. |
| [`rq.ChestAttemptResult`](types/rq.ChestAttemptResult.md) | What `rq.chest.on_attempt` may return instead of a number. |
| [`rq.ChestInfo`](types/rq.ChestInfo.md) | What `rq.chest.on_attempt` and `on_result` get for a red chest. |
| [`rq.ChooseCtx`](types/rq.ChooseCtx.md) | What `rq.battle.on_choose` gets on an enemy's or the familiar's turn. |
| [`rq.ChooseSkill`](types/rq.ChooseSkill.md) | A skill in `rq.ChooseCtx.skills`: one slot of the actor's list as it is now. |
| [`rq.CombatRules`](types/rq.CombatRules.md) | What a skill can do in a fight, from `rq.combat.rules`. |
| [`rq.ConfigPage`](types/rq.ConfigPage.md) | A page in the Mods tab of the game's Config screen. |
| [`rq.CounterCtx`](types/rq.CounterCtx.md) | What `rq.combat.on_counter` gets after a hit. |
| [`rq.CounterGuardCtx`](types/rq.CounterGuardCtx.md) | What `rq.counter.on_guard_counter` gets. |
| [`rq.CreateCtx`](types/rq.CreateCtx.md) | What `rq.chara.on_create` gets. |
| [`rq.CritCtx`](types/rq.CritCtx.md) | What `rq.combat.on_crit` gets where the game rolls a critical. |
| [`rq.DebugAction`](types/rq.DebugAction.md) | A row on the F3 debug menu. |
| [`rq.DungeonArea`](types/rq.DungeonArea.md) | One area of `rq.dungeon.areas()`. |
| [`rq.DungeonCamera`](types/rq.DungeonCamera.md) | The camera range `rq.dungeon.camera` patches. |
| [`rq.DungeonInfo`](types/rq.DungeonInfo.md) | Where the party is in a dungeon, from `rq.dungeon.info()`. |
| [`rq.ElementCtx`](types/rq.ElementCtx.md) | What `rq.combat.on_element` gets for one physical hit. |
| [`rq.EncounterCtx`](types/rq.EncounterCtx.md) | What `rq.encounters.on_encounter` callbacks get. |
| [`rq.EncounterInfo`](types/rq.EncounterInfo.md) | What `rq.encounters.info` returns. |
| [`rq.EquipCtx`](types/rq.EquipCtx.md) | What `rq.item.on_equip` gets. |
| [`rq.EscapeCtx`](types/rq.EscapeCtx.md) | What `rq.combat.on_escape` gets. |
| [`rq.FightBackground`](types/rq.FightBackground.md) | One of the game's fight backgrounds. |
| [`rq.FightOpts`](types/rq.FightOpts.md) | What `rq.battle.start` takes. Only `enemies` is needed. |
| [`rq.FightResult`](types/rq.FightResult.md) | How a fight from `rq.battle.start` ended, its second value. |
| [`rq.FlashBitmap`](types/rq.FlashBitmap.md) | One bitmap of a game Flash file, as `rq.image.flash_bitmaps` lists it. |
| [`rq.FlashBitmapOpts`](types/rq.FlashBitmapOpts.md) | Options for `rq.image.flash_bitmap`. |
| [`rq.FlashInfo`](types/rq.FlashInfo.md) | What `rq.image.flash_info` returns. |
| [`rq.FlashSound`](types/rq.FlashSound.md) | A sound inside a Flash file, from `rq.sound.flash_info`. |
| [`rq.ForgetCtx`](types/rq.ForgetCtx.md) | What `rq.chara.on_forget` gets. |
| [`rq.GameButtonGroup`](types/rq.GameButtonGroup.md) | A group, from `rq.gamebutton.groups`. |
| [`rq.GameButtonHandle`](types/rq.GameButtonHandle.md) | An entry, from `rq.gamebutton.add`. |
| [`rq.GameButtonInfo`](types/rq.GameButtonInfo.md) | An entry, as `rq.gamebutton.groups` lists it. |
| [`rq.GameButtonList`](types/rq.GameButtonList.md) | The status page's MODS button and its list, as `rq.gamebutton.groups` gives them. |
| [`rq.GameButtonSpec`](types/rq.GameButtonSpec.md) | An entry for `rq.gamebutton.add`. |
| [`rq.GifInfo`](types/rq.GifInfo.md) | What `rq.image.gif_info` returns. |
| [`rq.GifOpts`](types/rq.GifOpts.md) | Options for `rq.image.add_gif`. |
| [`rq.GoHomeCtx`](types/rq.GoHomeCtx.md) | What an `rq.party.on_go_home` callback gets. |
| [`rq.HasSkillCtx`](types/rq.HasSkillCtx.md) | What `rq.chara.on_has_skill` gets for one check. |
| [`rq.HealCtx`](types/rq.HealCtx.md) | What `rq.combat.on_heal` gets for one heal; `amount` is writable. |
| [`rq.HpEvent`](types/rq.HpEvent.md) | What `rq.battle.on_hp` gets. |
| [`rq.HudCgOpts`](types/rq.HudCgOpts.md) | How `rq.hud.cg` draws a CG. |
| [`rq.HudTextStyle`](types/rq.HudTextStyle.md) | How `rq.hud.text` draws text. |
| [`rq.ImageInfo`](types/rq.ImageInfo.md) | What `rq.image.info` returns. |
| [`rq.ImageLayer`](types/rq.ImageLayer.md) | One layer of `rq.image.compose`: a part of a CG, a fill, or text. |
| [`rq.ImageOpts`](types/rq.ImageOpts.md) | Options for `rq.image.add` and `rq.image.replace`. |
| [`rq.Item`](types/rq.Item.md) | An owned item instance, from `rq.items()`. |
| [`rq.ItemDef`](types/rq.ItemDef.md) | An item template for `rq.item.define`. |
| [`rq.ItemEffect`](types/rq.ItemEffect.md) | One of an item's effects: the game's own code and amount. |
| [`rq.ItemFindOpts`](types/rq.ItemFindOpts.md) | What `rq.item.find` and `rq.item.count` take. |
| [`rq.ItemInfo`](types/rq.ItemInfo.md) | What `rq.item.info` returns: an item number's row data, as `rq.uikit.item_data` gives it for an instance, without the fields that belong to one instance (`ii`, `locked`, `place`). The kit's item lists take it as a row. |
| [`rq.LearnableRow`](types/rq.LearnableRow.md) | One row of the skill buy list, from `rq.chara.learnable`. |
| [`rq.LearnCtx`](types/rq.LearnCtx.md) | What `rq.chara.on_learn` gets for one purchase. |
| [`rq.LevelUpCtx`](types/rq.LevelUpCtx.md) | What `rq.chara.on_level_up` callbacks get. |
| [`rq.LootAdd`](types/rq.LootAdd.md) | An item for `rq.loot.add`. |
| [`rq.LootItem`](types/rq.LootItem.md) | An item the player will find, from `rq.loot.list`. |
| [`rq.MagicCtx`](types/rq.MagicCtx.md) | What `rq.combat.on_magic` gets for one spell. |
| [`rq.MapCtx`](types/rq.MapCtx.md) | What `rq.dungeon.on_map` gets. |
| [`rq.MapObject`](types/rq.MapObject.md) | An object on the current map, from `rq.dungeon.objects()`. |
| [`rq.MarkDef`](types/rq.MarkDef.md) | How `rq.battle.set_mark` shows one of the game's marks. |
| [`rq.ModelDef`](types/rq.ModelDef.md) | What `rq.monster.model` takes. |
| [`rq.ModelInfo`](types/rq.ModelInfo.md) | A model in the game's model table, as `rq.monster.models` lists it. |
| [`rq.Monster`](types/rq.Monster.md) | A monster's data, as `rq.monster.get` returns it. The names are `rq.chara.get`'s. |
| [`rq.MonsterCapture`](types/rq.MonsterCapture.md) | A mod's monster's capture (`rq.MonsterDef.capture`): what the game's capture skills (the two Capture skills, 166 and 451, and Capture Thread, 531) give when they catch it. |
| [`rq.MonsterCreateCtx`](types/rq.MonsterCreateCtx.md) | What `rq.monster.on_create` callbacks get. Fields marked writable change the enemy in its slot. |
| [`rq.MonsterDef`](types/rq.MonsterDef.md) | What `rq.monster.define` takes: a game monster to start from, then any field of `rq.MonsterEdit` for the mod's monster. |
| [`rq.MonsterDrop`](types/rq.MonsterDrop.md) | An item a monster may leave after a won fight (`rq.MonsterEdit.drops`). |
| [`rq.MonsterEdit`](types/rq.MonsterEdit.md) | What `rq.monster.edit` changes. Every field is optional; the numbers are whole and 0 or more. |
| [`rq.MonsterGroup`](types/rq.MonsterGroup.md) | A mod's enemy group, as `rq.monster.group` takes it. |
| [`rq.MonsterSkill`](types/rq.MonsterSkill.md) | A skill in a monster's list (`rq.Monster.skills`). |
| [`rq.MonsterSkillEdit`](types/rq.MonsterSkillEdit.md) | A skill's fields in `rq.MonsterEdit.skills`: the ones given replace the list's. |
| [`rq.MusicInfo`](types/rq.MusicInfo.md) | What `rq.music.info` tells about a track. |
| [`rq.MusicListOpts`](types/rq.MusicListOpts.md) | What `rq.uikit.music_list` takes. |
| [`rq.MusicMoment`](types/rq.MusicMoment.md) | A moment a pack names on its Config page, with a switch the player turns on and off. |
| [`rq.MusicNow`](types/rq.MusicNow.md) | What `rq.music.current` gives: the track that plays now. |
| [`rq.MusicOpts`](types/rq.MusicOpts.md) | How `rq.music.replace` and `ctx:file` play a file. |
| [`rq.MusicPageOpts`](types/rq.MusicPageOpts.md) | What `rq.music.page` takes. |
| [`rq.MusicPlayCtx`](types/rq.MusicPlayCtx.md) | What `rq.music.on_play` gets: a track the game is about to play. |
| [`rq.NewThisRun`](types/rq.NewThisRun.md) | What `rq.quests.new_this_run` returns. |
| [`rq.ObjectCtx`](types/rq.ObjectCtx.md) | What an `rq.dungeon.on_object` function gets. |
| [`rq.Offer`](types/rq.Offer.md) | A row `rq.chara.on_offer` adds to the skill buy list. |
| [`rq.OfferCtx`](types/rq.OfferCtx.md) | What `rq.chara.on_offer` gets for the character whose buy list the game just filled. |
| [`rq.OfferRow`](types/rq.OfferRow.md) | A row of the skill buy list, from `rq.chara.offers`. |
| [`rq.OrbMember`](types/rq.OrbMember.md) | A roster member, from `rq.orb.roster`. `rq.party.roster` gives the same with `hp_max` and `status`. |
| [`rq.OrderUnit`](types/rq.OrderUnit.md) | One unit of a fight, as `rq.battle.on_order` lists it. |
| [`rq.PartyMember`](types/rq.PartyMember.md) | A recruited character, from `rq.party.roster`. |
| [`rq.PhysicalCtx`](types/rq.PhysicalCtx.md) | What `rq.combat.on_physical` gets for one physical hit. |
| [`rq.PlayFlashOpts`](types/rq.PlayFlashOpts.md) | Options for `rq.image.play_flash`: the sprite's (`rq.SpriteOpts`, such as `x`, `y`, `z`, `scale`, `attach` and `sound`) and the play's. |
| [`rq.PoisonCtx`](types/rq.PoisonCtx.md) | What `rq.combat.on_poison` gets where the game works out a poison. |
| [`rq.Quest`](types/rq.Quest.md) | A quest, from `rq.quests()`. |
| [`rq.QuestArea`](types/rq.QuestArea.md) | An area of a mod's quest's map, in `rq.QuestMap.areas`. |
| [`rq.QuestAreaCtx`](types/rq.QuestAreaCtx.md) | What an area's `setup` gets (`rq.QuestArea.setup`). |
| [`rq.QuestBonus`](types/rq.QuestBonus.md) | A quest bonus in `rq.QuestRun.bonuses`. |
| [`rq.QuestClearCtx`](types/rq.QuestClearCtx.md) | What an `rq.quests.on_clear` callback gets. |
| [`rq.QuestCondition`](types/rq.QuestCondition.md) | A condition to take part in a quest, from `rq.QuestData.conditions` and for `rq.quests.edit`. |
| [`rq.QuestData`](types/rq.QuestData.md) | A quest's data as the quest list shows it, from `rq.quests.get`. |
| [`rq.QuestDef`](types/rq.QuestDef.md) | What `rq.quests.define` takes: a quest of the mod's own, with a map or with none. |
| [`rq.QuestEdit`](types/rq.QuestEdit.md) | A patch for `rq.quests.edit`: the fields to change; one left out keeps the game's. |
| [`rq.QuestEndCtx`](types/rq.QuestEndCtx.md) | What an `rq.quests.on_end` callback gets. |
| [`rq.QuestEvent`](types/rq.QuestEvent.md) | What `rq.quests.on_event` and `on_event_after` callbacks get. |
| [`rq.QuestMap`](types/rq.QuestMap.md) | A mod's quest's map, in `rq.QuestDef.map`. |
| [`rq.QuestMapShape`](types/rq.QuestMapShape.md) | The shape of a mod's quest's map, in `rq.QuestData.map`. |
| [`rq.QuestObject`](types/rq.QuestObject.md) | An object of a mod's quest's area, in `rq.QuestArea.objects`. |
| [`rq.QuestRun`](types/rq.QuestRun.md) | The quest being played, from `rq.quests.run`. |
| [`rq.QuestRunCtx`](types/rq.QuestRunCtx.md) | What a quest's `run` gets (`rq.QuestDef.run`). |
| [`rq.QuestRunEdit`](types/rq.QuestRunEdit.md) | What `rq.quests.set_run` writes; a field left out stays. |
| [`rq.RecruitOpts`](types/rq.RecruitOpts.md) | Options for `rq.chara.recruit`. |
| [`rq.RevealOpts`](types/rq.RevealOpts.md) | Options for `rq.battle.reveal_weakness`. |
| [`rq.RewardAlly`](types/rq.RewardAlly.md) | One ally in `rq.battle.on_reward`'s `ctx.allies`. |
| [`rq.RewardCtx`](types/rq.RewardCtx.md) | What `rq.battle.on_reward` callbacks get. Fields marked writable change what the game gives. |
| [`rq.SaveCtx`](types/rq.SaveCtx.md) | What `rq.saves.on_save` and `on_load` callbacks get. |
| [`rq.SaveFaces`](types/rq.SaveFaces.md) | What `rq.saves.faces` returns: the folders of the character creator's faces. |
| [`rq.SaveMod`](types/rq.SaveMod.md) | A mod, as a profile records it. |
| [`rq.SaveProfile`](types/rq.SaveProfile.md) | A save profile, from `rq.saves.list`. |
| [`rq.SaveSummary`](types/rq.SaveSummary.md) | What a profile's save holds, read from its file. |
| [`rq.SceneChoice`](types/rq.SceneChoice.md) | One row of `rq.scene.choice`. |
| [`rq.SceneCtx`](types/rq.SceneCtx.md) | What a scene file's function gets first (`rq.scene.functions`). |
| [`rq.SceneFile`](types/rq.SceneFile.md) | A scene file from `rq.scene.file`. Pass it to `rq.scene.play`, `once` or `start`, or call it with a scene's `s` in a scene that plays already. |
| [`rq.SceneFileOpts`](types/rq.SceneFileOpts.md) | How `rq.scene.file` starts a file. |
| [`rq.SceneRow`](types/rq.SceneRow.md) | One row of `rq.sprite.scene`. |
| [`rq.SceneTextOpts`](types/rq.SceneTextOpts.md) | How `rq.scene.say`, `think` and `narrate` show a line. |
| [`rq.Settings`](types/rq.Settings.md) | A settings page's values, from `rq.config.settings`. |
| [`rq.SettingsOpts`](types/rq.SettingsOpts.md) | What `rq.config.settings` takes. |
| [`rq.SettingsRow`](types/rq.SettingsRow.md) | One row of a settings page, for `rq.config.settings`. |
| [`rq.ShopCopy`](types/rq.ShopCopy.md) | What `rq.shop.next` gives for each copy: `rq.item.info`'s row data and the copy's shop level. |
| [`rq.SkillBrief`](types/rq.SkillBrief.md) | A skill as `rq.units()` lists it. |
| [`rq.SkillInfo`](types/rq.SkillInfo.md) | What `rq.skill.get` returns. |
| [`rq.SkillLevel`](types/rq.SkillLevel.md) | A skill and its level, as `rq.chara.base_skills` lists them and `edit`'s `learn` takes them. |
| [`rq.SkillListCtx`](types/rq.SkillListCtx.md) | What `rq.skilllist.on_page` gets. |
| [`rq.SkillPatch`](types/rq.SkillPatch.md) | Fields for `rq.skill.patch`, named after the game's. |
| [`rq.SkillResetCtx`](types/rq.SkillResetCtx.md) | What `rq.chara.on_skill_reset` gets. |
| [`rq.SkillSpec`](types/rq.SkillSpec.md) | A new skill for `rq.skill.define`. |
| [`rq.SkillStep`](types/rq.SkillStep.md) | A step for `rq.chara.learnable`'s `after`: a skill set to a level. |
| [`rq.SoundOpts`](types/rq.SoundOpts.md) | How `rq.sound.play` and `play_flash` play a sound. |
| [`rq.SpawnHandle`](types/rq.SpawnHandle.md) | What `rq.spawn` returns, to follow or stop the job. |
| [`rq.Sprite`](types/rq.Sprite.md) | A mod sprite among the game's own, made by `rq.sprite.new`. |
| [`rq.SpriteAttach`](types/rq.SpriteAttach.md) | What an attached sprite follows. Give one of these. |
| [`rq.SpriteMotion`](types/rq.SpriteMotion.md) | The values `Sprite:to` moves to, and how. |
| [`rq.SpriteOpts`](types/rq.SpriteOpts.md) | Options for `rq.sprite.new` and `Sprite:set`. |
| [`rq.StatusDef`](types/rq.StatusDef.md) | What `rq.status.define` takes. |
| [`rq.StatusImmune`](types/rq.StatusImmune.md) | Who cannot take a state, for `rq.StatusDef.immune`. Any one field that matches is enough. |
| [`rq.StatusInfo`](types/rq.StatusInfo.md) | What `rq.status.info` gives about a definition. |
| [`rq.StatusInstance`](types/rq.StatusInstance.md) | A state on one character, from `rq.status.add`, `get` and `list`. |
| [`rq.StepsCtx`](types/rq.StepsCtx.md) | What `rq.encounters.on_steps` callbacks get. |
| [`rq.StudyCtx`](types/rq.StudyCtx.md) | What `rq.battle.on_study` gets for one Study that fired. |
| [`rq.StunCtx`](types/rq.StunCtx.md) | What `rq.combat.on_stun` gets where the game works out a stun. |
| [`rq.TakeContext`](types/rq.TakeContext.md) | What an `rq.quests.on_take` callback gets. |
| [`rq.TextureColors`](types/rq.TextureColors.md) | Colors by numbers on a texture, as `rq.image.texture` takes them. At least one field. |
| [`rq.TextureInfo`](types/rq.TextureInfo.md) | One texture of a game model, as `rq.image.textures` lists it. |
| [`rq.TransferContext`](types/rq.TransferContext.md) | What `rq.world.on_transfer` and `on_transfer_after` callbacks get. |
| [`rq.TrapCtx`](types/rq.TrapCtx.md) | What an `rq.dungeon.on_trap` callback gets. |
| [`rq.TrapWeights`](types/rq.TrapWeights.md) | The weights of the trap kinds, from `rq.dungeon.traps()`: each 0 to 10. |
| [`rq.TryEquipCtx`](types/rq.TryEquipCtx.md) | What `rq.item.on_try_equip` gets. |
| [`rq.UiAskRow`](types/rq.UiAskRow.md) | One row of `rq.ui.ask`. |
| [`rq.UiBarOpts`](types/rq.UiBarOpts.md) | What `rq.uikit.bar` takes. |
| [`rq.UiBox`](types/rq.UiBox.md) | A row or column for `rq.uikit.row` and `col`. |
| [`rq.UiButtonStyle`](types/rq.UiButtonStyle.md) | A button style of the hub theme: two states of a grey button and its text. |
| [`rq.UiChoice`](types/rq.UiChoice.md) | One row of `rq.ui.choose`. |
| [`rq.UiCommentOpts`](types/rq.UiCommentOpts.md) | What `rq.uikit.comment` takes besides the text. |
| [`rq.UiFilterState`](types/rq.UiFilterState.md) | A filter state for `rq.uikit.filters` and `rq.uikit.item_filter`: what the vault's filter column has picked. 0 or nil is "all". |
| [`rq.UiInputOpts`](types/rq.UiInputOpts.md) | What `rq.uikit.input` takes. |
| [`rq.UiItemIconOpts`](types/rq.UiItemIconOpts.md) | What `rq.uikit.item_icon` takes. |
| [`rq.UiItemRow`](types/rq.UiItemRow.md) | An item row's data, as `rq.uikit.item_data` reads it from the game. A table of your own with the same fields draws a made-up row. |
| [`rq.UiItemWindowEntry`](types/rq.UiItemWindowEntry.md) | An entry of `rq.uikit.item_window`'s list, when a tile needs more than the item. |
| [`rq.UiItemWindowOpts`](types/rq.UiItemWindowOpts.md) | Options for `rq.uikit.item_window`. |
| [`rq.UiMenuItem`](types/rq.UiMenuItem.md) | One entry of `rq.uikit.menu`. |
| [`rq.UiOptionRow`](types/rq.UiOptionRow.md) | One row of `rq.uikit.options`. |
| [`rq.UiPiece`](types/rq.UiPiece.md) | A part of a CG drawn at any size: the edges stay as they are, the middle stretches. |
| [`rq.UiPlace`](types/rq.UiPlace.md) | Where a widget goes. |
| [`rq.UiQuestStorage`](types/rq.UiQuestStorage.md) | What `rq.ui.quest_storage` returns. |
| [`rq.UiQuestStorageTile`](types/rq.UiQuestStorageTile.md) | A tile of the game's Quest Storage window, from `rq.ui.quest_storage`. |
| [`rq.UiScrollPieces`](types/rq.UiScrollPieces.md) | The pieces of the game's scroll bar. |
| [`rq.UiSkillOpts`](types/rq.UiSkillOpts.md) | What `rq.uikit.skill_button` takes. |
| [`rq.UiStepperOpts`](types/rq.UiStepperOpts.md) | What `rq.uikit.stepper` takes. |
| [`rq.UiTabsStyle`](types/rq.UiTabsStyle.md) | A tabs style of the hub theme. |
| [`rq.UiTheme`](types/rq.UiTheme.md) | A look for the kit: pieces, text styles, colors and sounds. |
| [`rq.UiTip`](types/rq.UiTip.md) | A widget's tip: what `rq.uikit.comment` shows, and where. |
| [`rq.UnequipCtx`](types/rq.UnequipCtx.md) | What `rq.item.on_unequip` gets. |
| [`rq.Unit`](types/rq.Unit.md) | A recruited character, from `rq.units()`. |
| [`rq.VanillaSave`](types/rq.VanillaSave.md) | What `rq.saves.vanilla` returns. |

## Aliases

| Alias | Type |
| --- | --- |
| `rq.ImageFit` | `"stretch"\|"contain"\|"cover"\|"none"` |
| `rq.GameButtonState` | `"button"\|"row"\|"aside"\|"hidden"` |
| `rq.StatusPageMode` | `"party"\|"party-edit"\|"party-store"\|"battle-result"` |
