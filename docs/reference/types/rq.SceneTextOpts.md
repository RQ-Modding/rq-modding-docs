# rq.SceneTextOpts

How `rq.scene.say`, `think` and `narrate` show a line.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` *(optional)* | `string` | The name plate. Default: the face's registered name. |
| `face` *(optional)* | `boolean` | false hides the face. Default true. |
| `page` *(optional)* | `boolean` | Uses the game's E variant of the frame. |
| `paper` *(optional)* | `boolean` | `narrate` only: the paper frame. |
| `wait` *(optional)* | `boolean` | false shows the text without waiting for a click, as for a question above a choice. Default true. |

## Used by

[`rq.scene.narrate`](../api/rq.scene.md#rqscenenarrate), [`rq.scene.say`](../api/rq.scene.md#rqscenesay), [`rq.scene.think`](../api/rq.scene.md#rqscenethink)
