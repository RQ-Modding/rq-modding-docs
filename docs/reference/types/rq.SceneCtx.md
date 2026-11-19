# rq.SceneCtx

What a scene file's function gets first (`rq.scene.functions`).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `vars` | `table<string, any>` | The file's variables. A change here shows in the file's `{name}` and `var`. |
| `path` | `string` | The file's path in the mod's folder. |
| `step` | `string` | The step's place in the file, such as "steps[4].then[1]". |
| `mod` | `string` | The mod's id. |

## Used by

[`rq.scene.functions`](../api/rq.scene.md#rqscenefunctions)
