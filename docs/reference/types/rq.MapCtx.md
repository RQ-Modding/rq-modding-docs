# rq.MapCtx

What `rq.dungeon.on_map` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest being entered (its `Ｑ` index). |
| `cleared` | `boolean` | The quest was cleared before. |
| `map` | `integer` | The map number. |
| `party` | `integer[]` | The party's roster slots. |

## Used by

[`rq.dungeon.on_map`](../api/rq.dungeon.md#rqdungeonon_map)
