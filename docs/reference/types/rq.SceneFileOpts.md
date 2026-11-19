# rq.SceneFileOpts

How `rq.scene.file` starts a file.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `vars` *(optional)* | `table<string, any>` | The variables at the start, by name, for `{name}` in the lines and the `var` condition. Default none. |
| `from` *(optional)* | `string` | Where the file starts, in place of its first step: a label's name, or a step's place as the problems name it, such as `"steps[4]"` or `"steps[2].choice[0].steps[1]"` (from 0; 2.61.0). Default the first step. |

## Used by

[`rq.scene.file`](../api/rq.scene.md#rqscenefile)
