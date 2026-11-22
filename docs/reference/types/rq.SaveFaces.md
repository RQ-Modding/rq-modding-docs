# rq.SaveFaces

What `rq.saves.faces` returns: the folders of the character creator's faces.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `path` | `string` | The `Face CG` folder of the save in use, the one the game reads: `<save folder>\Face CG`, so a profile's own (`Profiles\<id>\save\Face CG`). Backslashes on Windows. |
| `exists` | `boolean` | That folder exists. The game makes it at its start, with a copy of the faces in the game's own `Face CG` folder. |
| `count` | `integer` | The `.png` and `.bmp` files in it. |
| `vanilla` *(optional)* | `string` | The vanilla game's `Face CG` folder (`Documents\AliceSoft\<game>\SaveData\Face CG`), nil when it does not exist. |
| `vanilla_count` *(optional)* | `integer` | The `.png` and `.bmp` files in the vanilla folder, with `vanilla`. |
| `missing` | `integer` | The vanilla folder's files the save's folder has no file of that name for: what `rq.saves.import_faces` would copy. 0 without a vanilla folder. |

## Used by

[`rq.saves.faces`](../api/rq.saves.md#rqsavesfaces)
