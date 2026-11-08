# rq.gamebutton

`since 2.16.0`

Buttons of mods in the game's own menus, made by the game itself.

One group so far, `"system-menu"`: the SYSTEM menu, from the town, a quest's map or anywhere the
game shows it. Mods add entries, not rows. While any entry exists the menu has one more row,
**MODS**, under Save (or Suspend Save), in the menu's own painted look; the keys reach it as any
row, and it is greyed while no entry is enabled. Picking it closes the menu as any row does and
lists every enabled entry in the game's choice menu (`rq.ui.choose`, 20 rows at most), in the
order they were added. Agents see the row as the control `mods` of the `system-menu` screen, and
the entries as that choice menu's rows.

```lua
rq.gamebutton.add({ id = "settings", label = "My Mod settings", tip = "Opens My Mod's page",
  on_click = function() rq.log("open my page here") end })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.gamebutton.add`](#rqgamebuttonadd) | Adds an entry to a game menu. |
| [`rq.gamebutton.groups`](#rqgamebuttongroups) | Lists the groups and their entries. |

### rq.gamebutton.add

```lua
rq.gamebutton.add(spec) -> rq.GameButtonHandle
```

`since 2.16.0`

Adds an entry to a game menu.

Raises an error for a spec that is not a table, an unknown group, no id or label, no `on_click`,
an `enabled` or `tip` of the wrong type, or an id the mod already has.

| Parameter | Type | Description |
| --- | --- | --- |
| `spec` | [`rq.GameButtonSpec`](../types/rq.GameButtonSpec.md) | The entry. |

| Returns | Type | Description |
| --- | --- | --- |
| `entry` | [`rq.GameButtonHandle`](../types/rq.GameButtonHandle.md) | The entry, to change or remove it. |

### rq.gamebutton.groups

```lua
rq.gamebutton.groups() -> rq.GameButtonGroup[]
```

`since 2.16.0`

Lists the groups and their entries.

| Returns | Type | Description |
| --- | --- | --- |
| `groups` | [`rq.GameButtonGroup`](../types/rq.GameButtonGroup.md) `[]` | One for each group. |
