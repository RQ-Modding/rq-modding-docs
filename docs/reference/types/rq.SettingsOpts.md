# rq.SettingsOpts

`since 2.35.0`

What `rq.config.settings` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `rows` | [`rq.SettingsRow`](rq.SettingsRow.md) `[]` | The rows, top to bottom. |
| `id` *(optional)* | `string` | The page's id (`rq.config.show`). Default the mod's id. |
| `title` *(optional)* | `string` | The page's row in the list and its heading. Default the mod's name. |
| `keep` *(optional)* | `"global"\|"profile"\|"save"` | Where the values are kept: "global" (default) in `rq.store.global`, the same for every profile; "profile" in `rq.store`, the profile's; "save" in `rq.savedata`, the save's, and the page asks to load a save first while none is loaded. |
| `reset` *(optional)* | `boolean` | false leaves out the Reset button, which puts every row back to its default. |
| `label_w` *(optional)* | `integer` | The width of the labels' column in pixels. Default the widest label, 120 to 420. |
| `draw` *(optional)* | `fun(ui:` [`rq.uikit`](../api/rq.uikit.md) `, box: {x: integer, y: integer, w: integer, h: integer})` | Draws more after the rows and the Reset button, as a page's own `draw` does. |
| `on_open` *(optional)* | `fun()` | The page came on screen. |
| `on_close` *(optional)* | `fun()` | It went away. |

## Used by

[`rq.config.settings`](../api/rq.config.md#rqconfigsettings)
