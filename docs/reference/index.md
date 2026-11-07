# API reference

Loader version 2.5.0.

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
| [`rq.hud`](api/rq.hud.md) | Draws text, boxes and CGs over the game, and reads clicks on them. |
| [`rq.ids`](api/rq.ids.md) | The game's numbers by name: characters, items, monsters, quests, skills, and the small lists the game names (classes, states, races, character types, elements, item kinds, skill targets). |
| [`rq.image`](api/rq.image.md) | Images from a mod's folder, shown by the game as CGs. |
| [`rq.input`](api/rq.input.md) | Reads the mouse and keyboard, and drives them for the game. |
| [`rq.item`](api/rq.item.md) | Defines, gives and changes items. |
| [`rq.items`](api/rq.items.md) | Lists the item instances the player owns. |
| [`rq.loot`](api/rq.loot.md) | Chest loot: what the pools roll, and the items the player will find, known in advance. |
| [`rq.mod`](api/rq.mod.md) | Finds out about other mods, and reaches what they share. |
| [`rq.music`](api/rq.music.md) | Music from a mod's own file, in place of one of the game's tracks. |
| [`rq.orb`](api/rq.orb.md) | The blue Recovery Spring on the map (`回復の泉`, object 203). |
| [`rq.party`](api/rq.party.md) | Reads and changes who is in the party. |
| [`rq.quests`](api/rq.quests.md) | Lists the quests and follows them: clears, endings, quest moments and state. |
| [`rq.random`](api/rq.random.md) | Controls the random number generator the game and the loader share. |
| [`rq.saves`](api/rq.saves.md) | Save profiles: whole save folders the player can switch between. |
| [`rq.scene`](api/rq.scene.md) | Plays scenes with the game's own commands, so a mod can do anything a game scene does. |
| [`rq.shop`](api/rq.shop.md) | Adds stock to Frostbuy, the item shop, and reports purchases. |
| [`rq.skill`](api/rq.skill.md) | Reads, defines and patches skills, and rewrites their hover text. |
| [`rq.skilllist`](api/rq.skilllist.md) | Pages the Potential Skills grid, 36 skills a page. |
| [`rq.sound`](api/rq.sound.md) | Plays sounds: a game sound number, a file in the mod folder, or a sound inside a game Flash file. |
| [`rq.speed`](api/rq.speed.md) | Runs the game clock faster or slower than real time. |
| [`rq.sprite`](api/rq.sprite.md) | Sprites a mod makes once and changes later, drawn among the game's own in z order. |
| [`rq.status`](api/rq.status.md) | Battle states made by mods, such as a burn, a bleed, a regeneration, a freeze or a weaken, that live beside the game's poison, stun and ▲▼, in one registry every mod shares. |
| [`rq.store`](api/rq.store.md) | Small key and value storage for each mod and each save. |
| [`rq.store.global`](api/rq.store.global.md) | The same calls as `rq.store`, in one file for every save profile. |
| [`rq.ui`](api/rq.ui.md) | Reads what is on the screen and saves screenshots. |
| [`rq.uikit`](api/rq.uikit.md) | Widgets in the look of the game's Config screen. |
| [`rq.units`](api/rq.units.md) | Lists the recruited characters. |

## Types

| Type | Summary |
| --- | --- |
| [`rq.AccuracyCtx`](types/rq.AccuracyCtx.md) | What `rq.combat.on_accuracy` gets for one accuracy check. |
| [`rq.AgentOpts`](types/rq.AgentOpts.md) | How `rq.agent.control` finds a control: a game button, or a rectangle a mod draws. |
| [`rq.AgentWidget`](types/rq.AgentWidget.md) | A control a mod drew on this update, for `rqmod-ctl ui`. |
| [`rq.AinHookCtx`](types/rq.AinHookCtx.md) | What an `rq.ain.hook` callback gets. |
| [`rq.BattleActor`](types/rq.BattleActor.md) | The ally whose turn it is, from `rq.battle.actor`. |
| [`rq.BattleDownCtx`](types/rq.BattleDownCtx.md) | What `rq.battle.on_down` gets. |
| [`rq.BattleEndCtx`](types/rq.BattleEndCtx.md) | What `rq.battle.on_end` gets. |
| [`rq.BattleHitCtx`](types/rq.BattleHitCtx.md) | What `rq.battle.on_hit` gets for one hit. |
| [`rq.BattleSelectKeyCtx`](types/rq.BattleSelectKeyCtx.md) | What `rq.battle.on_select_key` gets. |
| [`rq.BattleSnap`](types/rq.BattleSnap.md) | What `rq.battle.snapshot` returns: a copy of the fight screen. |
| [`rq.BattleStartCtx`](types/rq.BattleStartCtx.md) | What `rq.battle.on_start` gets. |
| [`rq.BattleStates`](types/rq.BattleStates.md) | Every state of a character, from `rq.battle.states`. |
| [`rq.BattleSupportCtx`](types/rq.BattleSupportCtx.md) | What `rq.battle.on_support` gets. |
| [`rq.BattleSwitchCtx`](types/rq.BattleSwitchCtx.md) | What `rq.battle.on_switch` gets for one rank. |
| [`rq.BattleTurnCtx`](types/rq.BattleTurnCtx.md) | What `rq.battle.on_turn` gets: the character whose turn starts, and what can change it. |
| [`rq.BattleUseEvent`](types/rq.BattleUseEvent.md) | What `rq.battle.on_use` gets. |
| [`rq.BuffDef`](types/rq.BuffDef.md) | A mod's buff on a card, for `rq.battle.set_buff` and `set_rank_buff`. |
| [`rq.BuffInfo`](types/rq.BuffInfo.md) | One mark a card shows, from `rq.battle.buffs`. |
| [`rq.BuyCtx`](types/rq.BuyCtx.md) | What an `rq.shop.on_buy` callback gets. |
| [`rq.Castle`](types/rq.Castle.md) | The castle's state, from `rq.castle()`. |
| [`rq.CastleRoom`](types/rq.CastleRoom.md) | A castle room, from `rq.castle()`. |
| [`rq.CharaDef`](types/rq.CharaDef.md) | A character template for `rq.chara.define`. |
| [`rq.CharaEdit`](types/rq.CharaEdit.md) | A patch for `rq.chara.edit`. `level`, `level_max`, `skills` and `lines` do not apply. |
| [`rq.CharaFields`](types/rq.CharaFields.md) | The fields `rq.chara.define` and `rq.chara.edit` share. |
| [`rq.CharaInit`](types/rq.CharaInit.md) | Stat bonuses that each recalculation adds, in `rq.CharaFields.init`. |
| [`rq.CharaSkillGrant`](types/rq.CharaSkillGrant.md) | A skill a character gets, in `rq.CharaFields.skills` and `rq.CharaEdit.learn`. |
| [`rq.CharaSlot`](types/rq.CharaSlot.md) | One row of a character's skill list, from `rq.chara.slots`. |
| [`rq.CharaState`](types/rq.CharaState.md) | Everything `rq.chara.get` returns about a character. `rq.chara.set` takes the same names. |
| [`rq.ChestAttemptResult`](types/rq.ChestAttemptResult.md) | What `rq.chest.on_attempt` may return instead of a number. |
| [`rq.ChestInfo`](types/rq.ChestInfo.md) | What `rq.chest.on_attempt` and `on_result` get for a red chest. |
| [`rq.ConfigPage`](types/rq.ConfigPage.md) | A page in the Mods tab of the game's Config screen. |
| [`rq.CounterGuardCtx`](types/rq.CounterGuardCtx.md) | What `rq.counter.on_guard_counter` gets. |
| [`rq.CreateCtx`](types/rq.CreateCtx.md) | What `rq.chara.on_create` gets. |
| [`rq.CritCtx`](types/rq.CritCtx.md) | What `rq.combat.on_crit` gets where the game rolls a critical. |
| [`rq.DebugAction`](types/rq.DebugAction.md) | A row on the F3 debug menu. |
| [`rq.DungeonCamera`](types/rq.DungeonCamera.md) | The camera range `rq.dungeon.camera` patches. |
| [`rq.DungeonInfo`](types/rq.DungeonInfo.md) | Where the party is in a dungeon, from `rq.dungeon.info()`. |
| [`rq.FlashSound`](types/rq.FlashSound.md) | A sound inside a Flash file, from `rq.sound.flash_info`. |
| [`rq.ForgetCtx`](types/rq.ForgetCtx.md) | What `rq.chara.on_forget` gets. |
| [`rq.GifInfo`](types/rq.GifInfo.md) | What `rq.image.gif_info` returns. |
| [`rq.GifOpts`](types/rq.GifOpts.md) | Options for `rq.image.add_gif`. |
| [`rq.HpEvent`](types/rq.HpEvent.md) | What `rq.battle.on_hp` gets. |
| [`rq.HudCgOpts`](types/rq.HudCgOpts.md) | How `rq.hud.cg` draws a CG. |
| [`rq.HudTextStyle`](types/rq.HudTextStyle.md) | How `rq.hud.text` draws text. |
| [`rq.ImageInfo`](types/rq.ImageInfo.md) | What `rq.image.info` returns. |
| [`rq.ImageLayer`](types/rq.ImageLayer.md) | One layer of `rq.image.compose`: a part of a CG, a fill, or text. |
| [`rq.ImageOpts`](types/rq.ImageOpts.md) | Options for `rq.image.add` and `rq.image.replace`. |
| [`rq.Item`](types/rq.Item.md) | An owned item instance, from `rq.items()`. |
| [`rq.ItemDef`](types/rq.ItemDef.md) | An item template for `rq.item.define`. |
| [`rq.ItemEffect`](types/rq.ItemEffect.md) | One of an item's effects: the game's own code and amount. |
| [`rq.ItemInfo`](types/rq.ItemInfo.md) | What `rq.item.get` returns. |
| [`rq.LootAdd`](types/rq.LootAdd.md) | An item for `rq.loot.add`. |
| [`rq.LootItem`](types/rq.LootItem.md) | An item the player will find, from `rq.loot.list`. |
| [`rq.MagicCtx`](types/rq.MagicCtx.md) | What `rq.combat.on_magic` gets for one spell. |
| [`rq.MapCtx`](types/rq.MapCtx.md) | What `rq.dungeon.on_map` gets. |
| [`rq.MarkDef`](types/rq.MarkDef.md) | How `rq.battle.set_mark` shows one of the game's marks. |
| [`rq.MusicInfo`](types/rq.MusicInfo.md) | What `rq.music.info` tells about a track. |
| [`rq.MusicNow`](types/rq.MusicNow.md) | What `rq.music.current` gives: the track that plays now. |
| [`rq.MusicOpts`](types/rq.MusicOpts.md) | How `rq.music.replace` and `ctx:file` play a file. |
| [`rq.MusicPlayCtx`](types/rq.MusicPlayCtx.md) | What `rq.music.on_play` gets: a track the game is about to play. |
| [`rq.NewThisRun`](types/rq.NewThisRun.md) | What `rq.quests.new_this_run` returns. |
| [`rq.Offer`](types/rq.Offer.md) | A row `rq.chara.on_offer` adds to the skill buy list. |
| [`rq.OfferCtx`](types/rq.OfferCtx.md) | What `rq.chara.on_offer` gets for the character whose buy list the game just filled. |
| [`rq.OfferRow`](types/rq.OfferRow.md) | A row of the skill buy list, from `rq.chara.offers`. |
| [`rq.OrbMember`](types/rq.OrbMember.md) | A roster member, from `rq.orb.roster`. |
| [`rq.PhysicalCtx`](types/rq.PhysicalCtx.md) | What `rq.combat.on_physical` gets for one physical hit. |
| [`rq.Quest`](types/rq.Quest.md) | A quest, from `rq.quests()`. |
| [`rq.QuestClearCtx`](types/rq.QuestClearCtx.md) | What an `rq.quests.on_clear` callback gets. |
| [`rq.QuestEndCtx`](types/rq.QuestEndCtx.md) | What an `rq.quests.on_end` callback gets. |
| [`rq.QuestEvent`](types/rq.QuestEvent.md) | What `rq.quests.on_event` and `on_event_after` callbacks get. |
| [`rq.RecruitOpts`](types/rq.RecruitOpts.md) | Options for `rq.chara.recruit`. |
| [`rq.SaveMod`](types/rq.SaveMod.md) | A mod, as a profile records it. |
| [`rq.SaveProfile`](types/rq.SaveProfile.md) | A save profile, from `rq.saves.list`. |
| [`rq.SaveSummary`](types/rq.SaveSummary.md) | What a profile's save holds, read from its file. |
| [`rq.SceneChoice`](types/rq.SceneChoice.md) | One row of `rq.scene.choice`. |
| [`rq.SceneRow`](types/rq.SceneRow.md) | One row of `rq.sprite.scene`. |
| [`rq.SceneTextOpts`](types/rq.SceneTextOpts.md) | How `rq.scene.say`, `think` and `narrate` show a line. |
| [`rq.SkillBrief`](types/rq.SkillBrief.md) | A skill as `rq.units()` lists it. |
| [`rq.SkillInfo`](types/rq.SkillInfo.md) | What `rq.skill.get` returns. |
| [`rq.SkillListCtx`](types/rq.SkillListCtx.md) | What `rq.skilllist.on_page` gets. |
| [`rq.SkillPatch`](types/rq.SkillPatch.md) | Fields for `rq.skill.patch`, named after the game's. |
| [`rq.SkillSpec`](types/rq.SkillSpec.md) | A new skill for `rq.skill.define`. |
| [`rq.SoundOpts`](types/rq.SoundOpts.md) | How `rq.sound.play` and `play_flash` play a sound. |
| [`rq.Sprite`](types/rq.Sprite.md) | A mod sprite among the game's own, made by `rq.sprite.new`. |
| [`rq.SpriteAttach`](types/rq.SpriteAttach.md) | What an attached sprite follows. Give one of these. |
| [`rq.SpriteMotion`](types/rq.SpriteMotion.md) | The values `Sprite:to` moves to, and how. |
| [`rq.SpriteOpts`](types/rq.SpriteOpts.md) | Options for `rq.sprite.new` and `Sprite:set`. |
| [`rq.StatusDef`](types/rq.StatusDef.md) | What `rq.status.define` takes. |
| [`rq.StatusInfo`](types/rq.StatusInfo.md) | What `rq.status.info` gives about a definition. |
| [`rq.StatusInstance`](types/rq.StatusInstance.md) | A state on one character, from `rq.status.add`, `get` and `list`. |
| [`rq.UiBox`](types/rq.UiBox.md) | A row or column for `rq.uikit.row` and `col`. |
| [`rq.UiMenuItem`](types/rq.UiMenuItem.md) | One entry of `rq.uikit.menu`. |
| [`rq.UiPiece`](types/rq.UiPiece.md) | A part of a CG drawn at any size: the edges stay as they are, the middle stretches. |
| [`rq.UiPlace`](types/rq.UiPlace.md) | Where a widget goes. |
| [`rq.UiTheme`](types/rq.UiTheme.md) | A look for the kit: pieces, text styles, colors and sounds. |
| [`rq.Unit`](types/rq.Unit.md) | A recruited character, from `rq.units()`. |
| [`rq.VanillaSave`](types/rq.VanillaSave.md) | What `rq.saves.vanilla` returns. |

## Aliases

| Alias | Type |
| --- | --- |
| `rq.ImageFit` | `"stretch"\|"contain"\|"cover"\|"none"` |
