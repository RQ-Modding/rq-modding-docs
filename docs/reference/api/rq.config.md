# rq.config

`since 1.8.0`

A Mods tab in the game's Config screen.

Once a mod adds a page, Config gets a tab after Other 2, with a list of the pages on the left and the
chosen page on the right, drawn with `rq.uikit`. Config's own tabs, its buttons, the X and the right
click work as in the game. The tab has no key (F1 to F7 are the other tabs). Keep settings in
`rq.store.global` when they hold for every profile, or in `rq.store` for one save. Check that
`rq.config` is there, so the mod still runs on an older loader.

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
