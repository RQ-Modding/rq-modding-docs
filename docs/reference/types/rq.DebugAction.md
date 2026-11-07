# rq.DebugAction

A row on the F3 debug menu.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | A short token that names the row. "rendering-stats" belongs to the engine. |
| `label` | `string` | The text on the menu. |
| `key` | `string` | The key that runs it, as a pipe key name ("7", "f4", "space"). "6", "f3", "+", "-" and "m" are reserved. |
| `page` *(optional)* | `string` | The menu page. Default "Main". |
| `onPress` | `fun()` | Runs when the key goes down while F3 is held. |

## Used by

[`rq.debug.action`](../api/rq.debug.md#rqdebugaction)
