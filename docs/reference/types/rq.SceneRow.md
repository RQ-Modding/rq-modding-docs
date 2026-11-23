# rq.SceneRow

`since 1.9.0` `changed 2.67.0`

One row of `rq.sprite.scene`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `"sprite"\|"part"\|"mod"\|"other"` | What it is: a game sprite, a game part, a mod sprite. |
| `no` | `integer` | The sprite or part number; a mod sprite's id. |
| `z` | `integer` | Its z. |
| `z2` | `integer` | Its second z. |
| `x` | `integer` | Left edge, in game pixels. |
| `y` | `integer` | Top edge, in game pixels. |
| `w` | `integer` | Width. |
| `h` | `integer` | Height. |
| `cg` | `integer` | The CG it shows; 0 for none. |
| `part` *(optional)* | `string` | A part's kind: cg, text, flash and so on. |
| `mod` *(optional)* | `string` | The mod of a mod sprite. |
| `plugin` *(optional)* | `string` | What draws a game sprite's picture, when it is not a CG: "ReignEngine" for a 3D view. |

## Used by

[`rq.sprite.scene`](../api/rq.sprite.md#rqspritescene)
