# rq.gamebutton

`since 2.16.0` `changed 2.17.0`

Buttons of mods in the game's own menus, made by the game itself.

`"system-menu"`: the SYSTEM menu, from the town, a quest's map or anywhere the game shows it. Mods
add entries, not rows. While any entry exists the menu has one more row, **MODS**, under Save (or
Suspend Save), in the menu's own painted look; the keys reach it as any row, and it is greyed while
no entry is enabled. Picking it closes the menu as any row does and lists every enabled entry in the
game's choice menu (`rq.ui.choose`, 20 rows at most), in the order they were added. Agents see the
row as the control `mods` of the `system-menu` screen, and the entries as that choice menu's rows.

`"skill-window"` (2.17.0): buttons under the Potential Skills list (status, then Skills), in the
look of the castle's buttons (CG 11153, 206 × 30, the label in the game's font, shrunk to fit).
They sit two to a row under the list's picture: x 531 and 745, y 660 and 692, in the order they
were added; a fifth is not placed (`placed` false, and the log says so). With the engine's own page
buttons (`rq.skilllist.install()` without `buttons = false`) they take the first row, and entries
start on the second. The window makes them again on each build of its list (open, a buy, a
character change, `rq.skilllist.refresh`), asking `enabled` each time. A greyed button is the
game's inactive look and plays the deny sound. The arrow keys reach them: Down from a column's last
skill goes to the button under it (a greyed one is skipped); from a button Up goes to that column's
last skill, Down to its first, Left and Right to the other button of the row. Agents see each one
as the control `<mod id>.<id>` of the `skill-shop` screen.

```lua
rq.gamebutton.add({ id = "settings", label = "My Mod settings", tip = "Opens My Mod's page",
  on_click = function() rq.log("open my page here") end })
rq.gamebutton.add({ group = "skill-window", id = "plan", label = "Plan Skills",
  on_click = function() rq.log("the skill window is still open") end })
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
