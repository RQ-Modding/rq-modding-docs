# rq.UiQuestStorage

`since 2.47.0` `changed 2.56.0`

What `rq.ui.quest_storage` returns.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `mode` | `"view"\|"give-up"\|"failure"` | Why it shows: `"view"` from the map panel's button (its close and erase buttons), `"give-up"` from Give Up (Yes and No; the items go with the quest). `"failure"` is the game's call at a failed quest's end (a party defeat or a give-up, `Ｒ８クエスト倉庫(2)`), which never shows a window: the quest's end has deleted every Quest Storage item before it, so it finds none and opens nothing. It is listed as the game has it; a mod never sees it. |
| `z` | `integer` | The window's z (`rq.sprite.scene`'s numbers). |
| `tiles` | [`rq.UiQuestStorageTile`](rq.UiQuestStorageTile.md) `[]` | The tiles with an item, in the window's order. |
| `dialog` | `boolean` | true while the game's question shows over it (the erase button's, Give Up's). |

## Used by

[`rq.ui.quest_storage`](../api/rq.ui.md#rquiquest_storage)
