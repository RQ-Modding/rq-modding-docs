# rq.SceneFileOpts

How `rq.scene.file` starts a file.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `vars` *(optional)* | `table<string, any>` | The variables at the start, by name, for `{name}` in the lines and the `var` condition. Default none. |
| `from` *(optional)* | `string` | A label of the file to start at, in place of its first step. Default the first step. |

## Used by

[`rq.scene.file`](../api/rq.scene.md#rqscenefile)
