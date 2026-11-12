# rq.QuestRun

The quest being played, from `rq.quests.run`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest number. |
| `progress` | `integer` | The progress bar, 0 to 100 (it blinks from 90). |
| `fights` | `integer` | The fights of this run. |
| `fights_here` | `integer` | The fights in this area. |
| `enemies_beaten` | `integer` | The placed enemies beaten in this run. |
| `exp` | `integer` | The EXP of this run's fights so far; the reserve gets a share of it at the end (skill 263). |
| `fame` | `integer` | The fame a clear gives now, before skill 269 doubles it. A run that does not clear gives none. |
| `fee` | `integer` | The appraisal fee per item at the end, in gold. |
| `gold_base` | `integer` | The base of a gold object: each gives a roll up to three times this. |
| `exp_bonus` | `integer` | The EXP bonus, a percent added to each fight's EXP, 0 to 50. It starts at 5 per earlier clear (20 at most) and each EXP object adds 3. |
| `bonuses` | `{feats?:` [`rq.QuestBonus`](rq.QuestBonus.md) `, level_ups?:` [`rq.QuestBonus`](rq.QuestBonus.md) `, enemies?:` [`rq.QuestBonus`](rq.QuestBonus.md) `}` | The quest's bonuses; one the quest does not have is nil. |
| `party_change` | `"normal"\|"none"\|"free"` | The party changes during the quest: as many as the fame rank gives, none, or as many as wanted. |
| `no_area_map` | `boolean` | The quest hides AREA DISPLAY. |
| `no_warp` | `{north: boolean, south: boolean, east: boolean, west: boolean}` | The warps closed that way. |

## Used by

[`rq.quests.run`](../api/rq.quests.md#rqquestsrun)
