# rq.UiItemIconOpts

`since 2.21.0`

What `rq.uikit.item_icon` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `size` *(optional)* | `integer` | The tile's side in pixels. Default 100, the game's; the rank badge shrinks with it. |
| `current` *(optional)* | `boolean` | The game's yellow frame stays on, as on the status page's chosen slot. |
| `disabled` *(optional)* | `boolean` | Darkened at half, as the kit greys a skill tile. It cannot be clicked, and its tip still shows. |
| `remove` *(optional)* | `boolean` | The status page's REMOVE button at the tile's x + 100, y + 10, on the tile under the mouse or the keys' cursor, or on a `current` one. Not on an empty slot, nor on an item that cannot be taken off (`rq.item.get(ii).locked`), as the status page leaves it out (since 2.22.1). |
| `judged` *(optional)* | `boolean` | false: the tip is the game's UNIDENTIFIED card, with the icon alone. Default true. |

## Used by

[`rq.uikit.item_icon`](../api/rq.uikit.md#rquikititem_icon)
