# rq.ItemDef

An item template for `rq.item.define`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The text id, such as "mymod:binoculars". It becomes a stable number from 1000 up. |
| `name` | `string` | The name. |
| `type` *(optional)* | `"weapon"\|"armor"\|"item"\|"special"\|"quest"\|"none"` | The slot: weapon (1), armor (11), item (17), special (21), quest (22), none (23, cannot be equipped). Default "item". |
| `subtype` *(optional)* | `integer` | The detailed kind (`種類詳細`); a familiar is 20. |
| `rank` *(optional)* | `integer` | The kind rank (`種類ランク`). Default 10. |
| `icon` *(optional)* | `integer\|string` | A game CG number or a file in the mod's folder (shown at 100×100, proportions kept). Default: a grey question mark (since 0.15.0). |
| `price` *(optional)* | `integer` | The price. |
| `level` *(optional)* | `integer` | The level needed to equip it (`装備ＬＶ`). |
| `rarity` *(optional)* | `integer` | The rarity (`レアランク`). |
| `classes` *(optional)* | `integer[]` | The classes that may equip it, 1 to 8. Default: all. |
| `characters` *(optional)* | `integer[]` | The characters that may equip it (`装備キャラ`). |
| `effects` *(optional)* | [`rq.ItemEffect`](rq.ItemEffect.md) `[]` | Up to five effects. |
| `info` *(optional)* | `string` | The description; `$` is a line break. |
| `locked` *(optional)* | `boolean` | Cannot be taken off (`外せません`). |
| `vanishes` *(optional)* | `boolean` | Vanishes (`消滅します`). |
| `on_create` *(optional)* | `fun(ii: integer)` | Runs when an instance is created. |

## Used by

[`rq.item.define`](../api/rq.item.md#rqitemdefine)
