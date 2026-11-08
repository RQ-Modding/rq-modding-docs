# rq.skilllist

`since 0.2.0`

Pages the Potential Skills grid, 36 skills a page.

The engine keeps up to 144 buy-list rows (index 0 to 143) and cuts each page's 36. Lua decides the
page. Opening the menu goes back to page 1. Known Skills is not paged. A page is 36 rows of the
filtered buy list in the order they were added, then sorted with `compSkill`.

The page buttons are a mod's own: `install{ buttons = false }`, then `rq.gamebutton` entries in the
`"skill-window"` group that set the page and call `rq.skilllist.refresh`. `install()` with no
options also draws the engine's old Previous Page and Next Page, for mods made before 2.17.0;
`on_buttons` belongs to those.

```lua
rq.skilllist.install({ buttons = false })
local function step(dir)
  local p = rq.skilllist.page() + dir
  if p >= 1 and p <= rq.skilllist.page_count() then return p end
end
rq.gamebutton.add({ group = "skill-window", id = "next", label = "Next Page",
  enabled = function() return step(1) ~= nil end,
  on_click = function() rq.skilllist.set_page(step(1)); rq.skilllist.refresh() end })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.skilllist.install`](#rqskilllistinstall) | Patches the buy list and the cut at 36, and with `buttons` the engine's two page buttons. |
| [`rq.skilllist.set_page`](#rqskilllistset_page) | Sets the page used the next time the grid is cut. |
| [`rq.skilllist.page`](#rqskilllistpage) | Returns the page the grid shows, or will show when it is next cut. |
| [`rq.skilllist.refresh`](#rqskilllistrefresh) | Builds the Potential Skills list again for the character shown, as the game does after a buy. |
| [`rq.skilllist.page_count`](#rqskilllistpage_count) | Returns how many pages the current filtered buy list has. |

### rq.skilllist.install

```lua
rq.skilllist.install(opts) -> boolean
```

`since 0.2.0` `changed 2.17.0`

Patches the buy list and the cut at 36, and with `buttons` the engine's two page buttons.

Calling it again does nothing more, except that a call with `buttons` adds the engine's buttons
when an earlier call left them out.

picture.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | `{buttons?: boolean}` | `buttons = false` leaves out the engine's Previous Page and Next Page, for a mod that makes its own with `rq.gamebutton`. Default true. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

> Changed in 2.17.0: `opts.buttons`; the engine's buttons are at y 660 (were 652), under the list's

### rq.skilllist.set_page

```lua
rq.skilllist.set_page(page)
```

`since 0.2.0`

Sets the page used the next time the grid is cut.

Raises an error before `rq.skilllist.install`.

| Parameter | Type | Description |
| --- | --- | --- |
| `page` | `integer` | The page; below 1 becomes 1. |

### rq.skilllist.page

```lua
rq.skilllist.page() -> integer
```

`since 2.17.0`

Returns the page the grid shows, or will show when it is next cut.

Raises an error before `rq.skilllist.install`.

| Returns | Type | Description |
| --- | --- | --- |
| `page` | `integer` | The page, from 1. |

### rq.skilllist.refresh

```lua
rq.skilllist.refresh() -> boolean
```

`since 2.17.0`

Builds the Potential Skills list again for the character shown, as the game does after a buy.

Use it after `set_page` to show the new page at once, for example from a button's `on_click`. The
page's buttons, the window's and every mod's, are made again with it. Does nothing while the window
is closed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the list was built; false while the window is closed. |

### rq.skilllist.page_count

```lua
rq.skilllist.page_count() -> integer
```

`since 0.2.0`

Returns how many pages the current filtered buy list has.

Raises an error before `rq.skilllist.install`.

| Returns | Type | Description |
| --- | --- | --- |
| `pages` | `integer` | The page count; 1 before the menu first opens. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.skilllist.on_open`](#rqskillliston_open) | Calls `fn` when the Potential Skills menu opens, after the page is set to 1 and before the grid is built. |
| [`rq.skilllist.on_page`](#rqskillliston_page) | Calls `fn` to decide the page. |
| [`rq.skilllist.on_buttons`](#rqskillliston_buttons) | Calls `fn` after the engine's Previous and Next were made, and again whenever the window makes them again. |

### rq.skilllist.on_open

```lua
rq.skilllist.on_open(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` when the Potential Skills menu opens, after the page is set to 1 and before the grid is
built.

Up to 16 callbacks.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | Runs on open. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 0.23.0: Returns a remover.

### rq.skilllist.on_page

```lua
rq.skilllist.on_page(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` to decide the page.

It is also called once per arrow while the buttons are built: false or nil greys that arrow out, so
its click plays the game's deny sound and does not call Lua. An enabled click calls it again. The
last callback that answers (not nil) decides; all nil denies. Up to 16 callbacks.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.SkillListCtx`](../types/rq.SkillListCtx.md) `): integer\|false\|nil` | Returns the page to show, or false to deny. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs; the last answer decides.

> Changed in 0.23.0: Returns a remover.

### rq.skilllist.on_buttons

```lua
rq.skilllist.on_buttons(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` after the engine's Previous and Next were made, and again whenever the window makes them again.

Pass the ids to `rq.agent.control` so tests can press them. Only with the engine's buttons
(`install()` without `buttons = false`); a mod's own buttons are named by `rq.gamebutton`. Up to 16
callbacks.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(prev_id: integer, next_id: integer)` | Gets the `T_Button` ids; 0 for an arrow that was not made. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 0.23.0: Returns a remover.
