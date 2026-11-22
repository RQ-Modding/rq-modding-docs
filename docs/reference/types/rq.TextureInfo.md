# rq.TextureInfo

`since 2.64.0`

One texture of a game model, as `rq.image.textures` lists it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | The texture's file name, as the model names it, such as "gokiburi.png". |
| `path` | `string` | Its full path in the game's archive with `/`, as `rq.image.texture` takes it. For a mod's model, the path in its base's folder. |
| `kind` | `"color"\|"alpha"\|"light"\|"normal"\|"specular"` | How the model uses it: "color" when any material draws its colours from it, else its other use. Rance Quest's models use colour, alpha and light maps; a model may also name a map its archive lacks (see `missing`). |
| `alpha_map` | `boolean` | True when a material also uses this colour file as its own alpha map. It matters only where `alpha` is false: the game's red then keeps cutting the model's holes whatever picture is put there. Where `alpha` is true, the picture's alpha decides, as on any texture with alpha. |
| `frames` | `integer` | For a colour texture the game animates, its frames (`face.png`, `face[1].png` and `face[2].png` are 3); otherwise 1. |
| `missing` | `boolean` | True when the game's archive lacks the file. Such a texture cannot be changed and has no `w`, `h` or `alpha`. |
| `w` *(optional)* | `integer` | The game's picture's width, in pixels. |
| `h` *(optional)* | `integer` | The game's picture's height, in pixels. |
| `alpha` *(optional)* | `boolean` | Whether the game's picture has alpha. |
| `mod` *(optional)* | `string` | When a mod changed it: that mod's id. |
| `picture` *(optional)* | `string\|string[]` | When a mod put a picture on it: the PNG, or the list of PNGs, as the mod gave them (a copy). |
| `colors` *(optional)* | [`rq.TextureColors`](rq.TextureColors.md) | When a mod changed its colors: the numbers, with the defaults filled in. |
| `own` *(optional)* | `boolean` | When a mod changed it: true for a mod's model's own texture, from `rq.monster.model`. |
| `used` *(optional)* | `integer` | When a mod changed it: how many times a model's material was loaded with the change since it was made. 0 means nothing has drawn it yet; frames do not count apart. |

## Used by

[`rq.image.textures`](../api/rq.image.md#rqimagetextures)
