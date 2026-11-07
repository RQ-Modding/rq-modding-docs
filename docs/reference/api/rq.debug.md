# rq.debug

`since 0.2.0`

Adds rows to the engine's F3 debug menu.

Hold F3 to show the menu. It redraws every frame and does not take normal play keys; F3 and the
keys listed on it are swallowed only so the game does not also see them. Key 6 toggles Rendering
Stats, which the engine owns. A menu holds up to 32 rows.

While F3 is held, `rqmod-ctl ui` lists the rows under `debug.actions`, so a test can press them
with `hold f3`, `key 7`, `release f3`.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.debug.action`](#rqdebugaction) | Adds a row to the F3 menu, replaces it, or removes it. |

### rq.debug.action

```lua
rq.debug.action(action) -> boolean
```

`since 0.2.0`

Adds a row to the F3 menu, replaces it, or removes it.

Pass a `rq.DebugAction` to add a row; a row with the same `id` is replaced. Pass just the id (a
string, or `{ id = id }` without label, key or onPress) to remove the row; call this when a mod
no longer needs it. Loading a mod again drops its old rows first.

Raises an error for a missing label, key or onPress, an unknown or reserved key, an id the engine
owns, a page name of 24 characters or more, or a 33rd row.

```lua
rq.debug.action({
  id = "my-toggle",
  label = "My Toggle",
  key = "7",
  onPress = function() rq.log("my-toggle") end,
})
rq.debug.action("my-toggle")  -- remove it again
```

| Parameter | Type | Description |
| --- | --- | --- |
| `action` | [`rq.DebugAction`](../types/rq.DebugAction.md) `\|string` | The row, or the id of a row to remove. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the row was added, replaced or removed. |
