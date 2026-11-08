# rq.UiItemRow

`since 2.8.0`

An item row's data, as `rq.uikit.item_data` reads it from the game. A table of your own with the
same fields draws a made-up row.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` *(optional)* | `integer` | The instance; nil for a made-up row. |
| `name` *(optional)* | `string` | The name (`アイテム_名前`). |
| `level` *(optional)* | `string` | The level line on the red bar (`アイテム_実装条件`), or "" for no bar. |
| `info` *(optional)* | `string` | The stats line with the game's marks (`アイテム_情報`): `$` starts a line, numbers draw white, text between two `\|` is white and between two backquotes stays yellow. |
| `icon` *(optional)* | `integer` | The icon CG (`アイテム_ＣＧ番号`), drawn 100 by 100. |
| `rank` *(optional)* | `integer` | The enhancement rank (`アイテム_レアランク`); its badge (CG 11420 + rank) shows on the icon when above 0. |
| `kind` *(optional)* | `integer` | The game's item kind (`アイテム_種類`): 1 weapon, 11 armor, 21 special, 17 item. Its mark shows at the top of a row without buttons. |
| `locked` *(optional)* | `boolean` | Locked in the vault (`アイテム_ＬＯＣＫ中`): LOCKED shows (not in the shop style), the lock button reads UNDO LOCK, and SELL and DONATE do not show. |
| `price` *(optional)* | `integer` | The price (`アイテム_価格`); the shop style shows it in gold digits. |
| `place` *(optional)* | `integer` | Where it is (`アイテム_存在`): 7 the vault, 11 the storage, 6 a shop, 8 quest storage, or the owner's roster slot while equipped. |
| `classes` *(optional)* | `integer[]` | The classes that may equip it, 1 to 8 (`アイテム_装備職業`); their icons show at the bottom. |
| `discard` *(optional)* | `boolean` | The game lets it go: it can be sold or donated (`アイテム_破棄可能`; false for quest items). Since 2.9.0. |
| `disabled` *(optional)* | `boolean` | In a list: the row is greyed out and cannot be picked. |

## Used by

[`rq.uikit.item_data`](../api/rq.uikit.md#rquikititem_data), [`rq.uikit.item_dropped`](../api/rq.uikit.md#rquikititem_dropped), [`rq.uikit.item_filter`](../api/rq.uikit.md#rquikititem_filter), [`rq.uikit.item_list`](../api/rq.uikit.md#rquikititem_list), [`rq.uikit.item_row`](../api/rq.uikit.md#rquikititem_row), [`rq.uikit.item_sort`](../api/rq.uikit.md#rquikititem_sort)
