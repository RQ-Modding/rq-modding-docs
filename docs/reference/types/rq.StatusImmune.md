# rq.StatusImmune

`since 2.26.0`

Who cannot take a state, for `rq.StatusDef.immune`. Any one field that matches is enough.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `boss` *(optional)* | `boolean` | A boss. |
| `barrier` *(optional)* | `boolean` | A character behind a barrier, as a barrier blocks the game's poison and stun. |
| `races` *(optional)* | `integer[]` | These races (`rq.ids.race`). |
| `types` *(optional)* | `integer[]` | These types (`rq.ids.chara_type`). |
| `charas` *(optional)* | `integer[]` | These character numbers (`rq.CharaState.no`). |

## Used by

[`rq.StatusDef`](rq.StatusDef.md), [`rq.StatusInfo`](rq.StatusInfo.md)
