# Buttons in the game's menus

Since loader 2.16.0 a mod can put a way in to itself inside the game's own menus, drawn and moved
by the game itself, instead of a HUD button over the screen. Three places so far:

- the **SYSTEM menu**: one MODS row for every mod, with each mod's entries in a list;
- **Rance Castle**: a room of the mod's own;
- the **skill window** (2.17.0): buttons under the Potential Skills list.

## An entry in the SYSTEM menu

```lua
rq.gamebutton.add({
  id = "settings",
  label = "My Mod settings",
  tip = "Opens My Mod's page",
  on_click = function()
    rq.log("open my page here")
  end,
})
```

While any mod has an entry, the SYSTEM menu has one more row, **MODS**, under Save (Suspend Save
during a quest). It is in the menu's own painted look, and the arrow keys reach it as any row.
Picking it closes the menu, as every row does, and opens the game's choice menu with every mod's
entries, in load order. `tip` is the game's comment beside the list while the mouse is on the row.
`on_click` runs after the menus close, so a mod can open a page, ask a question or start a scene
there.

The menu is the way in from everywhere the SYSTEM button is: the town and a quest's map. Mods do not
add rows of their own: with many mods the menu would not fit the screen.

- `enabled = false`, or a function that returns false, leaves the entry out of the list. With no
  entry enabled, the MODS row is greyed, as the game greys Save during a quest.
- The handle's `set{label, enabled, tip}` changes the entry, and `remove()` takes it out. With no
  entry left, the MODS row goes as well.
- `rq.gamebutton.groups()` lists the entries, for a debug page or an agent.

Agents see the row as the control `mods` of the `system-menu` screen, and the entries as the rows of
the choice menu (`select-<label>`).

## A room in Rance Castle

```lua
rq.castle.room({
  id = "workshop",
  name = "Workshop",
  floor = "B2F",
  new = function() return not rq.store.get("workshop_seen") end,
  on_enter = function(room)
    rq.store.set("workshop_seen", true)
    rq.ui.choose({ "Craft", "Repair" }, function(id) rq.log("picked", id) end)
  end,
})
```

The castle rolls its rooms each time it opens: which rooms, which characters, how many. Two rooms
are there every time, Gal monsters and the Poster room, because the game shows them on a rule, not
on a roll. A mod's room works as they do. It is one of the game's own areas, numbers 30 to 50,
which the game leaves free, so the game draws its button with the name in the castle's font, the
face and the NEW mark, and moves the keys to it.

- **Where.** Each floor has three cells. The room goes in a free cell of its `floor` (default B2F,
  beside the Poster room). When that floor is full that time, it goes to the nearest floor with a
  free cell. The game's own rooms never move.
- **A click** runs `on_enter` instead of the game's room code. The castle stays open (a character's
  room closes it for cleaning; a mod's room does not), and the game goes back to the town's tabs.
- **`shown`** is asked each time the castle opens; false leaves the room out that time.
- **`face`** (a CG number) or **`chara`** (a character's face) beside the name.
- The handle's `where()` says where the room is while the castle shows it, `set{...}` changes it from
  the next time the castle opens, and `remove()` takes it out.

Make rooms in `init.lua`. There are 21 area numbers for every mod together, given in load order.

## Buttons in the skill window

```lua
rq.gamebutton.add({
  group = "skill-window",
  id = "plan",
  label = "Plan Skills",
  tip = "Opens My Mod's skill planner",
  on_click = function()
    rq.log("the skill window is still open")
  end,
})
```

The Potential Skills list (a character's status, then Skills) gets buttons under its picture, in
the look of the castle's buttons: the game's grey plate with the label in its font, shrunk to fit.
They are two to a row, at x 531 and 745, y 660 and 692, in load order; there is room for four, and a
fifth is not placed (the log says so).

- The window makes its buttons again each time it builds the list: on open, after a buy, on a
  character change. `enabled` is asked each time; false greys the button in the game's own way, and
  a click on it plays the deny sound.
- **A click** runs `on_click` with the window still open, after the game's click sound. To show
  something new in the list, change it and call `rq.skilllist.refresh()`, which builds the list
  again as the game does after a buy.
- **The keys.** Down from the last skill of a column goes to the button under it (a greyed one is
  skipped); from a button, Up goes back to the list, and Left and Right to the other button of the
  row. Enter presses it.
- **`tip`** is the game's skill comment, with the label as its title, under the button.

Potential Skill Pages makes its Previous Page and Next Page this way, with
`rq.skilllist.install{ buttons = false }`, `rq.skilllist.page()` and `refresh()`. Agents see each
button as the control `<mod id>.<id>` of the `skill-shop` screen.

## The game's dialogs

Since loader 2.19.0 a mod asks the player with the game's own dialog window, the one of its Save?,
Sell? and Take Quest? questions:

```lua
if rq.ui.confirm("Swap the absorbed item?\nThe old one goes back to the vault.") then
  swap()
end
rq.ui.notice("The vault cannot take " .. name .. ".")
local pick = rq.ui.ask("What now?", { { id = "trade", text = "Trade a Jewel" }, { id = "no", text = "No" } })
```

- **They wait for the answer**, as the game's own questions do: `confirm` gives true or false,
  `notice` true once OK is pressed, `ask` the picked row's `id`. So they can answer inside the
  game's flow, from an `rq.ain.hook` callback that must set `h.result`, or from a kit button's
  click. `rq.ui.choose` stays the way to open a menu at the next update with a callback.
- **One dialog at a time.** The game keeps one list of rows for all its dialogs, so a call made
  while another dialog is being built or shows draws nothing and gives nil.
- **The text.** Only `\n` starts a line. The window wraps the rest at its width, and every 3 lines
  get a row of their own. `@` and `$`, where the game's own texts break, are drawn as `＠` and `＄`;
  pass `game = true` for a text that comes from the game, such as `h.args[2]` of its question.
  The dialog does not scroll: the rows and the lines of text together are at most 20.
- **"Don't ask again"**: `confirm(text, { remember = "swap", remember_label = "Swapping" })` adds
  the game's row. Once the player turns it off, `confirm` gives true without asking, in every save.
  The question is then listed on a **Confirmations** page in Config's Mods tab, where the player
  can turn it back on, and Resetting in Config's Confirmations tab turns it back on too.
  `remember = 14` (1 to 99) uses the game's own switch instead, here "Selling items".
- **Agents** see the screen `select`: `confirm`'s buttons are `yes` and `no`, `notice`'s is `yes`,
  `ask`'s rows are `select-<label>`, and `select.message` holds the text.

Morurun Items and Gem Lady Trade ask this way.

See [`rq.gamebutton`](../reference/api/rq.gamebutton.md), [`rq.skilllist`](../reference/api/rq.skilllist.md),
[`rq.castle`](../reference/api/rq.castle.md) and [`rq.ui`](../reference/api/rq.ui.md) for every field.
