# Buttons in the game's menus

Since loader 2.16.0 a mod can put a way in to itself inside the game's own menus, drawn and moved
by the game itself, instead of a HUD button over the screen. Three places so far:

- the **SYSTEM menu**: one MODS row for every mod, with each mod's entries in a list;
- **Rance Castle**: a room of the mod's own;
- the **skill window** (2.17.0): buttons under the Potential Skills list;
- a character's **status page** (2.20.0): icon buttons in its title row.

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
- **`face`** (a CG number) or **`chara`** (a character number from `rq.ids.chara`: their face, while
  they are in the roster) beside the name.
- The handle's `where()` says where the room is while the castle shows it, `set{...}` changes it from
  the next time the castle opens, and `remove()` takes it out.

Make rooms in `init.lua`. There are 21 area numbers for every mod together, given in load order.

Agents see the castle as the screen `castle` (since 2.20.1), each room as the control
`room-<area>` with its name as the label and its floor as the value, so a mod's room is
`room-<handle.area()>`.

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

## Buttons on the status page

```lua
rq.gamebutton.add({
  group = "status",
  id = "notes",
  label = "Notes",
  icon = 11158,
  tip = function(chara) return "Notes on " .. rq.chara.get(chara).name end,
  enabled = function(chara) return chara ~= 1 end,
  on_click = function()
    rq.log("notes for", rq.statuspage.chara())
  end,
})
```

A character's status page has one free place: its title row, between the name and the X. The
buttons go there, right to left from the X, at x 472 and 436 (y 61), in load order. The widest
name in the game ends at x 435, so they never cover a name. There is room for two; a third is not
placed (the log says so).

- **`icon`** is a CG number, such as one from `rq.image.add`. The cell is 32 × 29: a smaller icon
  is centered, a larger one shrunk to fit. The button is the icon on the page's own background, as
  the game's own picture buttons: the yellow frame under the mouse, the icon moved down a pixel
  while pressed, the whole cell darkened while greyed.
- **Asked on every draw.** The game draws the page's card again on open, on a change of character,
  after every equip, skill or profile change, and when the skill window closes. Each time, the
  loader asks `shown(chara, mode)`, `enabled(chara)` and, when the tip opens, `tip(chara)`. A
  button with `shown` false gives its cell to the next.
- **A click** runs `on_click` with the page still open, after the game's click sound. A greyed one
  plays the deny sound.
- **The tip** is the game's comment window beside the icon, with the label as its title, on a
  greyed button too, so it can say why it is greyed. `\n` starts a line.
- **The keys.** Up from the Special slot goes to the buttons; Left and Right move between them,
  Down goes back to the Special slot, Up to SKILL SCREEN. Enter presses one.

Agents see each button as the control `<mod id>.<id>` of the `status` screen. Morurun Items' MORU
RUN button is made this way.

### The page itself: `rq.statuspage`

```lua
rq.statuspage.on_chara(function(chara, old) rq.log("now", chara, "was", old) end)

local function heal()
  local c = rq.statuspage.chara()
  rq.chara.set(c, { hp = rq.chara.get(c).hp_max })
  rq.statuspage.refresh()
end
```

- `chara()` is the character shown, nil while the page is closed; `mode()` says how it was opened:
  `"party"` (the footer's party summary), `"party-edit"` (the Party screen), `"party-store"` (its
  stored characters) or `"battle-result"` (the level-up after a fight).
- **`refresh()`** draws the card again after a mod changed the character, with no sound, as the
  game does after an equip. With the item list open beside the page, the list is built again too.
  It does nothing while the skill window covers the page (the game draws the card when it closes).
- **Events:** `on_open(chara, mode)`, `on_chara(chara, old)`, `on_update(chara)` after every draw,
  `on_close()`. Each returns a function that removes it.

For a list of items by number, such as the ones the Morurun absorbed, `rq.item.info(no)` gives an
item number's name, icon and stats line with no item in the game, as the kit's rows want them.

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
- **Not from Config.** Over Config the dialog opens under Config's screen, out of sight, and the
  dump does not list it. A page in Config's Mods tab asks on the page itself, with kit buttons, as
  Keep Donations' Set does.
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
[`rq.statuspage`](../reference/api/rq.statuspage.md), [`rq.castle`](../reference/api/rq.castle.md) and
[`rq.ui`](../reference/api/rq.ui.md) for every field.
