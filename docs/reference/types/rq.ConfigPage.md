# rq.ConfigPage

`since 1.8.0`

A page in the Mods tab of the game's Config screen.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` *(optional)* | `string` | Keeps the page across reloads. Default: the title. |
| `title` | `string` | Its row in the list and its heading. |
| `draw` | `fun(ui:` [`rq.uikit`](../api/rq.uikit.md) `, box: {x: integer, y: integer, w: integer, h: integer})` | Runs on every update the page shows, inside a column at `box` (738 by 531, under the title). An error is logged once and shown at the bottom of the page. |
| `on_open` *(optional)* | `fun()` | The page came on screen. |
| `on_close` *(optional)* | `fun()` | It went away: another page, another tab, Config closed. |

## Used by

[`rq.config.page`](../api/rq.config.md#rqconfigpage)
