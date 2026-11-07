# rq.skilllist

`since 0.2.0`

Pages the Potential Skills grid, 36 skills a page.

The engine keeps up to 144 buy-list rows (index 0 to 143) and draws Previous Page and Next Page on
that window, with the castle's skill screen buttons. Lua decides the page. Opening the menu goes back
to page 1. Known Skills is not paged. A page is 36 rows of the filtered buy list in the order they
were added, then sorted with `compSkill`.

```lua
rq.skilllist.install()
rq.skilllist.on_page(function(ctx)
  if ctx.dir == 0 then return ctx.page end
  local p = ctx.page + ctx.dir
  if p < 1 or p > ctx.pages then return false end
  return p
end)
rq.skilllist.on_buttons(function(prev, next)
  if prev > 0 then rq.agent.control("skill-page-prev", { label = "Previous Page", button = prev }) end
  if next > 0 then rq.agent.control("skill-page-next", { label = "Next Page", button = next }) end
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.skilllist.install`](#rqskilllistinstall) | Patches the buy list, the cut at 36 and the two buttons. |
| [`rq.skilllist.set_page`](#rqskilllistset_page) | Sets the page used the next time the grid is cut. |
| [`rq.skilllist.page_count`](#rqskilllistpage_count) | Returns how many pages the current filtered buy list has. |

### rq.skilllist.install

```lua
rq.skilllist.install() -> boolean
```

`since 0.2.0`

Patches the buy list, the cut at 36 and the two buttons.

Calling it again does nothing more.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

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
| [`rq.skilllist.on_buttons`](#rqskillliston_buttons) | Calls `fn` after Previous and Next were made, and again whenever the window makes them again. |

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

Calls `fn` after Previous and Next were made, and again whenever the window makes them again.

Pass the ids to `rq.agent.control` so tests can press them. Up to 16 callbacks.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(prev_id: integer, next_id: integer)` | Gets the `T_Button` ids; 0 for an arrow that was not made. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 0.23.0: Returns a remover.
