# rq.gamebutton

`since 2.16.0` `changed 2.17.0` `changed 2.20.0` `changed 2.32.0` `changed 2.58.0` `changed 2.59.0`

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
were added; a fifth is not placed (`placed` false, and the log says so). The window makes them again on each build of its list (open, a buy, a
character change, `rq.skilllist.refresh`), asking `enabled` each time. A greyed button is the
game's inactive look and plays the deny sound. The arrow keys reach them: Down from a column's last
skill goes to the button under it (a greyed one is skipped); from a button Up goes to that column's
last skill, Down to its first, Left and Right to the other button of the row. Agents see each one
as the control `<mod id>.<id>` of the `skill-shop` screen.

`"status"` (2.20.0): icon buttons in a character's status page's title row, the only free room on
the page. The cells are right to left from the X: x 472 and 436, y 61, 32 × 29 each, in the order
entries were added; the widest name in the game ends at x 435. Entries with `shown` false give their
cell to the next; a third shown entry brings the MODS list (below). The
button is the icon on the page's own background, as the game's CG buttons: the yellow frame under
the mouse, the icon moved 1 pixel right and down while pressed, the whole cell darkened while
greyed. `shown`, `enabled` and a function `tip` are asked on every draw of the card (open, another
character, a change, `rq.statuspage.refresh`). The arrow keys reach the buttons: Up from the Special
slot (or its REMOVE) goes to the first button not greyed; from a button Left and Right go to the
other, Down to the Special slot, Up to SKILL SCREEN. Agents see each one as the control
`<mod id>.<id>` of the `status` screen. See `rq.statuspage` for the page itself.

**MODS** (2.59.0): when more than two title entries are shown on a draw of the card and one of them
may go in a list (`list` not false), or when a shown entry has `list = true`, the title row has one
button instead of the cells: **MODS**, over both cells (x 436, y 62, 68 × 27), the look of the
page's SKILL SCREEN button. Its click (or Enter on it) opens a list under it: one row per entry
that may go in it, in the order they were added, 30 high from y 91, right edges at x 504, as wide
as the widest row (68 to 320), up to 16 rows (more are left out, and the log says so). A row is the
map tabs' grey bar with the entry's icon at its left and its `text` beside it, the yellow frame
under the mouse or the keys, darkened while `enabled` is false. Under the mouse a row shows its tip
right of the list, with the label as its title. A click on a row closes the list and runs its
`on_click`, with the page still there (from the frame's update, as a kit widget's click, not from
the page's own loop); a darkened row plays the deny sound and the list stays. A click off the list
(MODS too), the right button or Esc only close the list; so do another character, the page
closing and a draw where the list is no longer wanted. While the list is open the page takes no
mouse and no keys: the arrows move between the rows and Enter clicks one. An entry with
`list = false` has no button while MODS shows; its `on_state` and the handle's `state` say so
(`"aside"`), and it shows its button another way or does something else. Whether MODS shows is
decided on every draw of the card, from the entries shown on that draw: it may come and go between
characters and between the ways the page opens. Up from the Special slot reaches MODS, Down from it
the Special slot, Up SKILL SCREEN; its tip lists the rows' labels. Agents see MODS as the control
`status-mods` of the `status` screen, and while the list is open each row as the kit's button
`button-<mod id>-<id>` (as `rq.uikit.icon_button` names it; the cells' own controls are gone then).

With `spot = "left"` (2.58.0), a `"status"` entry is an icon, not a button: it says something about
the character shown, as a mark. The left spot is the page's top left, at the left end of the LV row
under the class icon: two cells, x 20 and 56, y 90, 32 × 26 each, in the order those entries were
added, apart from the title row's two (a third shown left entry is not placed, and the log says so).
An icon has no `on_click`: no press, no sound, and the keys pass it by. Under the mouse it lights up
as the title buttons do, and its tip shows with the label as its title; `enabled` false darkens
it; `shown` false gives its cell to the next left entry. A mark that changes with the character
(faded or full, say) gives `icon` as a function.

`"map"` (2.32.0): tabs on a quest's map, on the 3D view's right edge against the map panel, under
the area map (AREA DISPLAY) and above the Magnum gauge, the only free room there. The tabs are
40 × 44 at x 768, from y 129, 47 apart, in the order entries were added; entries with `shown`
false give their cell to the next, and a fifth shown entry is not placed (`placed` false, and the
log says so). Each tab is a button of the panel itself (`T_MapParts`, ids 700101 to 700104): the
game's plain grey bar (CG 11009) with the icon on it, the yellow frame under the mouse, the icon
moved 1 pixel right and down while pressed, the whole tab darkened while greyed. So it hides
with the panel (a dialog, a fight, a menu, an event) and comes back with it, and the panel makes
it again for each area. `shown` and `enabled` are asked every 200 ms while the map shows, and at
once after `set`; a change in the shown tabs makes them again. The tip is the game's comment
window with the label as its title, left of the tab. In the map's key mode (Space turns it on and
off, as for the panel's own buttons) the arrow keys reach the tabs: Left from AREA DISPLAY goes to
the first tab not greyed; from a tab Up and Down go to the next one, Right back to AREA DISPLAY,
and Enter presses it. `on_click` runs with the map still there; to show a window of your own, draw
it from `rq.on_frame` (`rq.uikit.item_window` is the game's Quest Storage window). Agents see each
tab as the control `<mod id>.<id>` with its `button`, while the map takes input (not while the
Quest Storage screen shows over the panel, which stays drawn under it).

```lua
rq.gamebutton.add({ id = "settings", label = "My Mod settings", tip = "Opens My Mod's page",
  on_click = function() rq.log("open my page here") end })
-- A mark on the status page: full for a character in the mod's list, faded for the others.
local FULL = rq.image.compose("my-mod:mark", { { cg = 6247, w = 26, h = 26 } }, { w = 26, h = 26 })
local FADED = rq.image.compose("my-mod:mark-faded", { { cg = 6247, w = 26, h = 26, alpha = 90 } },
  { w = 26, h = 26 })
local marked = {}
rq.gamebutton.add({ group = "status", spot = "left", id = "mark", label = "My Mark",
  icon = function(chara) return marked[chara] and FULL or FADED end,
  tip = function(chara) return marked[chara] and "Marked." or "Not marked yet." end })
rq.gamebutton.add({ group = "skill-window", id = "plan", label = "Plan Skills",
  on_click = function() rq.log("the skill window is still open") end })
rq.gamebutton.add({ group = "status", id = "notes", label = "Notes", icon = 11158,
  tip = function(chara) return "Notes on " .. rq.chara.get(chara).name end,
  on_click = function() rq.log("notes for", rq.statuspage.chara()) end })
-- Always in the MODS list, as a row of words (no icon needed).
rq.gamebutton.add({ group = "status", id = "journal", label = "Journal", list = true,
  text = function(chara) return "Journal of " .. rq.chara.get(chara).name end,
  on_click = function() rq.log("journal") end })
-- Never in it: while MODS shows, this mod has no button and says so in its own way.
rq.gamebutton.add({ group = "status", id = "quick", label = "Quick", icon = 11158, list = false,
  on_state = function(state) rq.log("quick is", state) end,
  on_click = function() rq.log("quick") end })
local open = false
rq.gamebutton.add({ group = "map", id = "bag", label = "My Bag", icon = 11329,
  tip = "What is in my bag.", enabled = function() return rq.dungeon.exploring() end,
  on_click = function() open = true end })
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

`since 2.16.0` `changed 2.20.0` `changed 2.32.0` `changed 2.58.0` `changed 2.59.0`

Adds an entry to a game menu.

Raises an error for a spec that is not a table, an unknown group, no id or label, no `on_click`
(or one on a `"left"` entry), an `enabled`, `tip` or `shown` of the wrong type, a `"status"` or
`"map"` entry with no `icon` (a `"status"` entry with `list = true` may have a `text` instead), a
`spot` other than `"title"` or `"left"` or outside `"status"`, a `list` or `text` outside
`"status"`'s title spot or of the wrong type, an `on_state` outside `"status"` or not a function,
or an id the mod already has.

| Parameter | Type | Description |
| --- | --- | --- |
| `spec` | [`rq.GameButtonSpec`](../types/rq.GameButtonSpec.md) | The entry. |

| Returns | Type | Description |
| --- | --- | --- |
| `entry` | [`rq.GameButtonHandle`](../types/rq.GameButtonHandle.md) | The entry, to change or remove it. |

> Changed in 2.20.0: The group `"status"`, with `icon` and `shown`.

> Changed in 2.32.0: The group `"map"`, with `icon` and `shown`.

> Changed in 2.58.0: `spot` in `"status"`, and `icon` as a function there.

> Changed in 2.59.0: `list`, `text` and `on_state` in `"status"`.

### rq.gamebutton.groups

```lua
rq.gamebutton.groups() -> rq.GameButtonGroup[]
```

`since 2.16.0`

Lists the groups and their entries.

| Returns | Type | Description |
| --- | --- | --- |
| `groups` | [`rq.GameButtonGroup`](../types/rq.GameButtonGroup.md) `[]` | One for each group. |
