# rq.UiFilterState

`since 2.8.0`

A filter state for `rq.uikit.filters` and `rq.uikit.item_filter`: what the vault's filter column
has picked. 0 or nil is "all".

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `type` *(optional)* | `integer` | The category: 21 special, 1 weapon, 11 armor, 17 item and other. |
| `sub` *(optional)* | `integer` | The category's sub-filter, by its place from the right: weapons 1 daggers to 7 staves and 8 others; armor 1 leather to 4 gi and 5 others; special items 1 rank C to 4 rank S and 5 others. |
| `class` *(optional)* | `integer` | The class that may equip it, 1 to 8, in the column's order (Fighter, Guard, Gunner, Sorcerer, Healer, Ranger, Brawler, Civilian). |
| `lock` *(optional)* | `integer` | 1 locked, 2 unlocked. |
| `equip` *(optional)* | `integer` | 1 equippable, 2 unequippable by `chara`. Since 2.9.0. |
| `chara` *(optional)* | `integer` | The character `equip` is about (its roster slot, iic); without it `equip` keeps all. Since 2.9.0. |

## Used by

[`rq.uikit.filters`](../api/rq.uikit.md#rquikitfilters), [`rq.uikit.item_filter`](../api/rq.uikit.md#rquikititem_filter)
