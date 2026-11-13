# rq.GoHomeCtx

`since 2.47.0`

What an `rq.party.on_go_home` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `no` | `integer` | The character's number (`rq.ids.chara`). |
| `reason` | `"aten"\|"item"` | `"aten"`: Aten's Go Home (skill 369), with her in a party of two or more. `"item"`: the wearer of item 209, in a party of two or more. |
| `item` *(optional)* | `integer` | The item, for `"item"`: 209. |
| `chance` | `integer` | The chance the character leaves, in percent: 20 for Aten, 100 for the item; a callback before this one may have changed it. |

## Used by

[`rq.party.on_go_home`](../api/rq.party.md#rqpartyon_go_home)
