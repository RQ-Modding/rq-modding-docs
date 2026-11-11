# rq.config

`since 1.8.0` `changed 2.35.0`

A Mods tab in the game's Config screen.

Once a mod adds a page, Config gets a tab after Other 2, with a list of the pages on the left and the
chosen page on the right, drawn with `rq.uikit`. Config's own tabs, its buttons, the X and the right
click work as in the game. The tab has no key (F1 to F7 are the other tabs). Keep settings in
`rq.store.global` when they hold for every profile, or in `rq.store` for one save. Check that
`rq.config` is there, so the mod still runs on an older loader.

For a page of settings, `rq.config.settings` builds it from a list of rows and keeps the values;
`page` with a `draw` of its own is for a page that is more than settings.

```lua
if rq.config then
  local on = rq.store.global.get("on", false)
  rq.config.page({
    id = "my-mod",
    title = "My Mod",
    draw = function(ui, box)
      local v, changed = ui.checkbox(on, "Turn it on", { id = "on" })
      if changed then
        on = v
        rq.store.global.set("on", on)
      end
    end,
  })
end
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.config.page`](#rqconfigpage) | Adds a page, or replaces the one with the same id. |
| [`rq.config.is_open`](#rqconfigis_open) | Returns whether the Mods page is on screen. |
| [`rq.config.pages`](#rqconfigpages) | Returns the page shown and every page's id. |
| [`rq.config.show`](#rqconfigshow) | Shows a page, now or the next time the Mods tab opens. |
| [`rq.config.settings`](#rqconfigsettings) | Adds a page of settings to the Mods tab, built from a list of rows. |

### rq.config.page

```lua
rq.config.page(page) -> string
```

`since 1.8.0`

Adds a page, or replaces the one with the same id.

| Parameter | Type | Description |
| --- | --- | --- |
| `page` | [`rq.ConfigPage`](../types/rq.ConfigPage.md) | The page. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string` | The page's id. |

### rq.config.is_open

```lua
rq.config.is_open() -> boolean
```

`since 1.8.0`

Returns whether the Mods page is on screen.

| Returns | Type | Description |
| --- | --- | --- |
| `open` | `boolean` | true while the page shows and no game dialog (going to the title, quitting) is over it. |

### rq.config.pages

```lua
rq.config.pages() -> string|nil, string[]
```

`since 1.8.0`

Returns the page shown and every page's id.

| Returns | Type | Description |
| --- | --- | --- |
| `current` | `string\|nil` | The id of the page shown, or nil. |
| `ids` | `string[]` | Every page's id, in the list's order. |

### rq.config.show

```lua
rq.config.show(id) -> boolean
```

`since 1.8.0`

Shows a page, now or the next time the Mods tab opens.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The page's id. |

| Returns | Type | Description |
| --- | --- | --- |
| `found` | `boolean` | false when no page has that id. |

### rq.config.settings

```lua
rq.config.settings(opts) -> rq.Settings
```

`since 2.35.0`

Adds a page of settings to the Mods tab, built from a list of rows.

Each row is a widget with its label, and the loader keeps its value: in `rq.store.global` (default),
`rq.store` or `rq.savedata`, under the row's `key`, for the mod. A Reset button closes the page.
The page needs no `draw`; `draw` adds more after the rows. The object it returns reads and writes
the values, and tells when one changes.

The page is `rq.config.page`'s, with the same id rules: calling it again with the same id replaces
the page, and its object keeps working on the same keys.

Raises an error for a row that is not one of the kinds, a value row with no key or a key used
twice, a default the row cannot take, or a `keep` that is not one of the three; and when called
from no mod's code.

```lua
local settings = rq.config.settings({
  title = "My Mod",
  rows = {
    { kind = "checkbox", key = "on", label = "Turn it on", default = true },
    { kind = "stepper", key = "count", label = "Count", min = 1, max = 99, default = 10,
      note = "How many each time." },
    { kind = "choice", key = "speed", label = "Speed", options = { "Slow", "Fast" },
      values = { 0.5, 2 }, disabled = function() return not settings.get("on") end },
  },
})
settings.on_change(function(key, value) rq.log(key, "is now", value) end)
if settings.get("on") then rq.log("count:", settings.get("count")) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.SettingsOpts`](../types/rq.SettingsOpts.md) | The page and its rows. |

| Returns | Type | Description |
| --- | --- | --- |
| `settings` | [`rq.Settings`](../types/rq.Settings.md) | The values. |

See also: [`rq.config.page`](rq.config.md#rqconfigpage)
