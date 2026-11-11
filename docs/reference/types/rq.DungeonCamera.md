# rq.DungeonCamera

The camera range `rq.dungeon.camera` patches.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `lock` *(optional)* | `number` | The distance the camera is locked at on a first visit. Default 35. |
| `min` *(optional)* | `number` | The nearest zoom. Default 17.5. |
| `max` *(optional)* | `number` | The farthest zoom. Default 120. |
| `fog_far` *(optional)* | `number` | Where the fog ends. Default 160. |
| `far` *(optional)* | `number` | Where the 3D view is cut: ground farther than this from the camera is not drawn. Default 200, the game's. More than 5, the near cut. Since 2.30.0. |
| `slider_steps` *(optional)* | `integer` | Steps on the zoom slider. Default 25. |

## Used by

[`rq.dungeon.camera`](../api/rq.dungeon.md#rqdungeoncamera)
