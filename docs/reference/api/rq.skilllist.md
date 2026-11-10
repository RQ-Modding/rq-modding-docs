# rq.skilllist

`since 0.2.0` `changed 2.18.0` `changed 2.22.1`

Pages the Potential Skills grid, 36 skills a page.

The game keeps the skills a character can buy in rows 1 to 60 of three arrays (`取得可能スキル`,
`取得可能スキルポイント`, `取得不可能スキル説明`) and shows the first 36. With `install`, the arrays
hold rows 1 to 144 and the list shows them 36 at a time. A page is 36 rows of the game's own
filtered list (no panel color 104, none the character holds) in the order they were added, then
sorted with `compSkill` as the game sorts. Opening the window goes back to page 1, and so does
another character in it (the window's scroll bar or the wheel over it). Known Skills is not paged.

It is Lua over the game's own code (`src/lua/skilllist.lua`): the arrays are made longer with
`rq.ain.set_global_len` whenever the game fills them, `スキルポン` stops at row 145 instead of 54,
and while the window builds its list `取得可能スキル_数` and `取得可能スキル_番号` answer the page's
rows. The buy is the game's own. Rows 61 to 144 are emptied when the window closes, so a save holds
only what the game's 60 rows would.

The page buttons are a mod's own: `install{ buttons = false }`, then `rq.gamebutton` entries in the
`"skill-window"` group that set the page and call `rq.skilllist.refresh`. `install()` with no
options adds two such entries for the mod, Previous Page and Next Page (`<mod id>.skilllist-prev`
and `-next`), for mods made before 2.17.0; `on_page` greys them and `on_buttons` gets their ids.

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
| [`rq.skilllist.install`](#rqskilllistinstall) | Turns the paged list on, and with `buttons` adds Previous Page and Next Page. |
| [`rq.skilllist.set_page`](#rqskilllistset_page) | Sets the page used the next time the grid is cut. |
| [`rq.skilllist.page`](#rqskilllistpage) | Returns the page the grid shows, or will show when it is next cut. |
| [`rq.skilllist.refresh`](#rqskilllistrefresh) | Builds the Potential Skills list again for the character shown, as the game does after a buy. |
| [`rq.skilllist.page_count`](#rqskilllistpage_count) | Returns how many pages the current filtered buy list has. |

### rq.skilllist.install

```lua
rq.skilllist.install(opts) -> boolean
```

`since 0.2.0` `changed 2.17.0` `changed 2.18.0`

Turns the paged list on, and with `buttons` adds Previous Page and Next Page.

Calling it again does nothing more, except that a call with `buttons` adds the two buttons when an
earlier call left them out.

Raises an error for `opts` that is not a table, or when `スキルポン`'s stop at 54 is not found.

entries were added (before, they always took the first row).

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | `{buttons?: boolean}` | `buttons = false` leaves out Previous Page and Next Page, for a mod that makes its own with `rq.gamebutton`. Default true. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

> Changed in 2.17.0: `opts.buttons`; the buttons are at y 660 (were 652), under the list's picture.

> Changed in 2.18.0: The buttons are the calling mod's `"skill-window"` entries, placed in the order

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
| [`rq.skilllist.on_buttons`](#rqskillliston_buttons) | Calls `fn` after each build of the list, with the ids of the Previous and Next that `install()` added. |

### rq.skilllist.on_open

```lua
rq.skilllist.on_open(fn) -> fun()
```

`since 0.2.0` `changed 2.18.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` when the Potential Skills menu opens, after the page is set to 1 and before the grid is
built.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | Runs on open. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.18.0: No limit on the number of callbacks (was 16).

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 0.23.0: Returns a remover.

### rq.skilllist.on_page

```lua
rq.skilllist.on_page(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 2.18.0` `changed 0.23.0`

Calls `fn` to decide the page.

It is also called once per arrow while the buttons are built: false or nil greys that arrow out, so
its click plays the game's deny sound and does not call Lua. An enabled click calls it again. The
last callback that answers (not nil) decides; all nil denies. With no callback, the page moves while it
stays between 1 and the page count.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.SkillListCtx`](../types/rq.SkillListCtx.md) `): integer\|false\|nil` | Returns the page to show, or false to deny. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs; the last answer decides.

> Changed in 2.18.0: No limit on the number of callbacks (was 16).

> Changed in 0.23.0: Returns a remover.

### rq.skilllist.on_buttons

```lua
rq.skilllist.on_buttons(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 2.18.0` `changed 0.23.0`

Calls `fn` after each build of the list, with the ids of the Previous and Next that `install()` added.

Pass the ids to `rq.agent.control` so tests can press them. Only with those buttons (`install()`
without `buttons = false`); they are also agent controls already, `<mod id>.skilllist-prev` and
`-next`, as every `rq.gamebutton` entry.

200038); no limit on the number of callbacks (was 16).

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(prev_id: integer, next_id: integer)` | Gets the `T_Button` ids; 0 for an arrow that was not made. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 2.18.0: The ids are those of `"skill-window"` cells, 200101 to 200104 (were 200037 and

> Changed in 0.23.0: Returns a remover.
