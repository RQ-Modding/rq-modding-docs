# rq.agent

`since 0.2.0`

Lets the test pipe (`rqmod-ctl`) see and press a mod's controls.

Agents and test scripts drive the game through `rqmod-ctl` (`ui`, `hover`, `press`). The game's
own buttons are listed automatically; a mod lists what it adds with these calls.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.agent.control`](#rqagentcontrol) | Registers a control under a stable id for `rqmod-ctl ui`, `hover` and `press`. |
| [`rq.agent.widgets`](#rqagentwidgets) | Lists the controls a mod's HUD drew on this update. |

### rq.agent.control

```lua
rq.agent.control(id, opts) -> boolean|nil
```

`since 0.2.0`

Registers a control under a stable id for `rqmod-ctl ui`, `hover` and `press`.

With `opts.button`, the control is a game `T_Button`; it is listed only while that button is
shown, and drops out when the game deletes it. With `x`, `y`, `w`, `h` it is a rectangle a mod
draws with `rq.hud`: register it on every update it is on screen and remove it when it is not.
`press` on a rectangle also sends Enter. Calling again with the same id updates the row. Pass no
`opts` to remove the registration at once.

Raises an error when the id or the button is rejected, or when `opts` has neither a button nor a
full rectangle.

```lua
rq.on_frame(function()
  rq.hud.rect(20, 20, 120, 32, 40, 40, 40, 220)
  rq.agent.control("my-button", { label = "My button", x = 20, y = 20, w = 120, h = 32 })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The pipe id: ASCII, no spaces. |
| `opts` *(optional)* | [`rq.AgentOpts`](../types/rq.AgentOpts.md) | The button or rectangle; nil removes the registration. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean\|nil` | true when registered; nothing when removed. |

### rq.agent.widgets

```lua
rq.agent.widgets(list) -> integer
```

`since 1.8.0`

Lists the controls a mod's HUD drew on this update.

They show in `rqmod-ctl ui` in the section `"kit"`, and `press` clicks the middle of a control's
box. Each call replaces the previous list; `{}` clears it. `rq.uikit` lists its own widgets, so
call this only for a HUD of your own.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | [`rq.AgentWidget`](../types/rq.AgentWidget.md) `[]` | Everything drawn on this update. |

| Returns | Type | Description |
| --- | --- | --- |
| `listed` | `integer` | How many controls were listed. |
