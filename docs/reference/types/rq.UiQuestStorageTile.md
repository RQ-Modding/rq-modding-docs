# rq.UiQuestStorageTile

`since 2.47.0`

A tile of the game's Quest Storage window, from `rq.ui.quest_storage`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `index` | `integer` | The tile's place in the window, 1 to 15: the control `item-<index>`. |
| `ii` | `integer` | The item instance. |
| `x` | `integer` | The tile's left edge, in game pixels. |
| `y` | `integer` | The tile's top edge, in game pixels. |
| `w` | `integer` | The tile's width, 100. |
| `h` | `integer` | The tile's height, 100. |
| `identified` | `boolean` | false for an unidentified item. |

## Used by

[`rq.UiQuestStorage`](rq.UiQuestStorage.md)
