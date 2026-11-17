# Buttons in the game's menus

Since loader 2.16.0 a mod can put a way in to itself inside the game's own menus, drawn and moved
by the game itself, instead of a HUD button over the screen. The places so far:

- the **SYSTEM menu**: one MODS row for every mod, with each mod's entries in a list;
- **Rance Castle**: a room of the mod's own;
- the **skill window** (2.17.0): buttons under the Potential Skills list;
- a character's **status page** (2.20.0): icon buttons in its title row;
- a quest's **map** (2.32.0): tabs against the map panel, under the area map;
- Config's **Mods tab** (1.8.0): a page of the mod's own, and since 2.35.0 a page of settings built
  from a list.

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

## More known skills

```lua
rq.knownskills.install({ most = 34 })
```

A character knows at most 17 skills and the item effect skill: the game keeps them in rows 1 to 18 of
the character's skill list, and both the status page and the skill window show those 18.
`rq.knownskills.install` raises the most (17 to 102) and shows the known skills 17 at a time.

- **The rows.** Every character's list grows to `most` + 4 rows, and the game's own code walks them
  all: fights, the hotbar, passives and Boosts in the stats, refills, the check for a free row before
  a buy, Skill Again. `rq.chara.slots`, `skill_room`, `learnable` and `learn` count the new rows.
  Call `install` from `init.lua`: mods load before the game makes its characters, so they are made
  with the longer list.
- **The pages.** The page's 17 skills are sorted as the game sorts the list (panel color, then
  number), with the item effect skill last. REMOVE and the upgrade buttons act on the skill shown.
  The status page opens on page 1, and so does another character.
- **The controls.** A slim scroll bar between the status page's skills and the equipment (and the
  wheel over the skills), and the game's left and right arrows beside the skill window's KNOWN SKILLS.
  `install{ controls = false }` leaves them out for a mod that makes its own and turns pages with
  `rq.knownskills.set_page`.
- **The save** stays the game's own, 18 rows a character. The rows past them are kept in the
  loader's [data beside the save](save-data.md) and come back after the save and after a load. A
  smaller `most` than a character holds keeps the rows that do not fit there until a row is free.
  Without the mod, the first save drops them; Skill Again gives the points back.

Agents see the controls `scrollbar-known-pages` (`status` screen), `button-known-prev` and
`button-known-next` (`skill-shop`), and `knownPage` and `knownPages` in `status` and `skillShop`.
Known Skill Pages installs it with a Config setting for `most`.

## Tabs on a quest's map

```lua
local open = false
rq.gamebutton.add({
  group = "map",
  id = "previews",
  label = "Item Previews",
  icon = rq.image.compose("my-mod:pouch", { { cg = 11329, src = { 18, 0, 64, 54 } } }, { w = 64, h = 54 }),
  tip = "What the chests of this room hold.",
  on_click = function() open = true end,
})
rq.on_frame(function()
  if not open then return end
  open = rq.uikit.item_window(my_items(), { id = "loot", title = "Item Previews" })
end)
```

The map panel at the right of a quest's map has no free room, and the 3D view's top holds the
encounter bar. The free place is the 3D view's right edge, against the panel, between the area map
(AREA DISPLAY) and the Magnum gauge. The tabs go there: 40 × 44 at x 768, from y 129, 47 apart, in
load order. There is room for four; a fifth is not placed (the log says so).

- **The panel's own buttons.** Each tab is a button of the panel, the game's plain grey bar with the
  `icon` on it (a CG number, fitted in 32 × 34). So it hides with the panel when a dialog, a fight,
  a menu or an event takes the screen, and comes back with it; the panel makes it again for each
  area. Under the mouse it gets the game's yellow frame, the icon moves down a pixel while pressed,
  and a greyed tab is darkened and plays the deny sound.
- **Asked every 200 ms** while the map shows: `shown()` and `enabled()`, with no argument. A tab
  with `shown` false gives its cell to the next; the handle's `set{...}` asks again at once.
- **A click** runs `on_click` with the map still there, after the game's click sound. To show
  something, draw it from `rq.on_frame`: `rq.uikit.item_window` is the game's Quest Storage window,
  which Loot Preview opens with the room's items.
- **The tip** is the game's comment window, with the label as its title, left of the tab. `tip`
  may be a function, asked when the tip opens. `
` starts a line.
- **The keys.** In the map's key mode (Space turns it on and off, as for the panel's own buttons),
  Left from AREA DISPLAY goes to the first tab not greyed; Up and Down move between the tabs, Right
  goes back to AREA DISPLAY. Enter presses one.

Agents see each tab as the control `<mod id>.<id>`, with its `button`, while the map takes input. The
game keeps the panel drawn under its Quest Storage screen, so the tabs show there too, but agents do
not see them and a click does nothing.
Loot Preview's Item Previews tab is made this way.

### The game's Quest Storage window

The map panel's Quest Storage button opens the game's own window of the quest's items.
[`rq.ui.quest_storage()`](../reference/api/rq.ui.md#rquiquest_storage) (2.47.0) gives it while it
shows: its `mode` (`"view"` from the panel's button, `"give-up"` from Give Up; `"failure"` is the
game's call at a failed quest's end, which never shows a window, as the quest's end has already
deleted the items), whether the game's question is over it (`dialog`), and each tile with an item:
its place in the window, the instance and its box (100 × 100). A mod draws on the tiles from
`rq.on_frame`; the game gets no mouse over a kit widget, and a click on a tile does nothing in the
game anyway. [`rq.uikit.icon_button`](../reference/api/rq.uikit.md#rquikiticon_button) is a picture
as a button, the size of a corner. After moving items in or out (`rq.item.set(ii, { place = ... })`,
8 is the quest storage), `rq.ui.quest_storage_refresh()` builds the window again.

Return Bonsai puts a button on each tile that moves the item into its own window, made with
`rq.uikit.item_window` and its `capacity` (2.47.0): the cells past it are locked, with the vault's
lock mark.

```lua
local ICON = rq.image.add("my-mod:button", "icons/bonsai.webp", { fit = "contain", w = 22, h = 24 })
local kept, cap = {}, 4
rq.on_frame(function()
  local qs = rq.ui.quest_storage()
  if not qs or qs.mode ~= "view" or qs.dialog then return end
  local moved = false
  for _, tile in ipairs(qs.tiles) do
    if rq.uikit.icon_button(ICON, { x = tile.x + 72, y = tile.y + 2, w = 26, h = 28,
        id = "keep-" .. tile.index, label = "Keep", tip = "Keep this one.", disabled = #kept >= cap }) then
      rq.item.set(tile.ii, { place = 11 })
      kept[#kept + 1] = tile.ii
      moved = true
    end
  end
  if moved then rq.ui.quest_storage_refresh() end
end)
-- and in the tab's window:
-- open = rq.uikit.item_window(kept, { id = "kept", title = "Kept", capacity = cap })
```

Agents see the window's tiles as `item-1` to `item-15` of the `quest-storage` screen, with the
instance as the value.

## A page in Config

Once a mod adds a page, the game's Config screen gets a **Mods** tab after Other 2, with the pages
in a list on the left. For settings, `rq.config.settings` (2.35.0) builds the page from a list of
rows and keeps the values; the mod draws nothing:

```lua
local settings
settings = rq.config.settings({
  title = "My Mod",
  rows = {
    { kind = "checkbox", key = "on", label = "Turn it on", default = true },
    { kind = "stepper", key = "count", label = "Count", min = 1, max = 99, default = 10,
      note = "How many each time." },
    { kind = "slider", key = "volume", label = "Volume", min = 0, max = 1, step = 0.05, default = 0.5 },
    { kind = "choice", key = "speed", label = "Speed", options = { "Slow", "Fast" }, values = { 0.5, 2 },
      disabled = function() return not settings.get("on") end },
    { kind = "input", key = "name", label = "Name", max = 20, placeholder = "A name" },
  },
})

settings.on_change(function(key, value, old)
  rq.log(key, "went from", old, "to", value)
end)
```

- **The rows.** `checkbox`, `stepper` (a whole number), `slider`, `choice` (one of `options`,
  stored as its number or as its entry in `values`) and `input` (a text) keep a value under `key`;
  `label` (a line of text) and `space` (a gap) keep none. A row may have a `default`, a `note` (dim
  lines under it), a `tip`, and `disabled`, true or a function asked on every update. The labels
  line up in one column (`label_w` sets its width).
- **Reset.** A button under the rows puts every value back to its default; `reset = false` leaves
  it out. A `draw(ui, box)` adds more after it, as on a page of the mod's own.
- **Where the values are kept.** In [`rq.store.global`](../reference/api/rq.store.md) by default, the
  same for every profile; `keep = "profile"` keeps them in `rq.store`, the profile's, and
  `keep = "save"` in [`rq.savedata`](save-data.md), the save's, with the rows greyed until a save is
  loaded (at the title too since 2.56.1, where `rq.world.current()` is nil). The key is the row's `key`, so a mod that drew its own page keeps its players' settings
  when it switches, as Morurun Items, Kaoru Quincy QoL, Custom TADA Mode and Game Speed did.
- **The object.** `settings.get(key)` gives the value; a stored value the row cannot take (a number
  past `max` after the mod lowered it) reads as the default. `set(key, value)` changes it as the page
  would, `on_change(fn)` runs on every change (the page, `set`, Reset) and returns a remover, and
  `reset()` is the button.
- **A recommended range** (since 2.44.0): `recommend = { 60, 150 }` on a stepper or a slider
  draws that range lighter on a slider's track and says "Recommended: 60 to 150" after the control.
  When the player sets a value outside it, the game's Yes / No asks first, with the value, the
  range and `warn` (what goes wrong there): Yes keeps it, No puts the range's nearest end. A slider
  shows its value beside the track (`format`, such as `"%.1f"`) and writes it when the knob is let
  go. Camera Zoom's sliders work this way.

  ```lua
  { kind = "slider", key = "out_max", label = "Farthest outdoors", min = 35, max = 250, step = 1,
    default = 150, format = "%.0f", recommend = { 60, 150 },
    warn = "Past 150 the edge of the sky shows as black corners, and past 180 the far ground is cut." },
  ```
- **Mistakes raise an error at the call**: an unknown `kind`, a value row with no key or a key used
  twice, a default the row cannot take, a `recommend` outside `min` and `max`, a `warn` without
  `recommend`.
- **Agents** see the widgets by their row's `id`, default the key: `check-on`, `stepper-count`,
  `slider-volume`, `check-speed-2`, `input-name` and `button-reset`.

A page that is more than settings is `rq.config.page`, with a `draw(ui, box)` that draws it with
[`rq.uikit`](../reference/api/rq.uikit.md) on every update.

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
  click, on a mod's Config page too. `rq.ui.choose` stays the way to open a menu at the next update
  with a callback.
- **One dialog at a time.** The game keeps one list of rows for all its dialogs, so a call made
  while another dialog is being built or shows draws nothing and gives nil.
- **Over Config** (since 2.28.0) the dialog draws over Config, on any tab, with a mod's page
  between them, as Keep Donations' Set asks. Before, it opened under Config, out of sight.
- **The text.** Only `\n` starts a line. The window wraps the rest at its width, and every 3 lines
  get a row of their own. `@` and `$`, where the game's own texts break, are drawn as `＠` and `＄`;
  pass `game = true` for a text that comes from the game, such as `h.args[2]` of its question.
  The dialog does not scroll: the rows and the lines of text together are at most 20.
- **A long menu** (since 2.56.0): the game's menu opens with its top at y 360 and grows down, so
  past about 12 rows its last rows ran off the screen, where a player cannot click them. A menu too
  tall for the room under its place now goes up just enough to fit, for `rq.ui.choose`,
  `rq.scene.choice` and these dialogs alike; a menu that fits keeps the game's place.
- **A row's `comment`** (in `ask`, `rq.ui.choose` and `rq.scene.choice`) is shown in the game's
  comment window while the mouse is on the row. Since 2.45.1 the loader cuts its lines between
  words, at most 28 half-width letters (14 Japanese) each, the width the game's menu takes; `\n`
  starts a line and an empty line stays. Before, the game cut every 28 letters mid-word and went
  on counting across a `\n`. `rq.uikit.options` shows a row's comment with the same lines.
- **"Don't ask again"**: `confirm(text, { remember = "swap", remember_label = "Swapping" })` adds
  the game's row. Once the player turns it off, `confirm` gives true without asking, in every save.
  The question is then listed on a **Confirmations** page in Config's Mods tab, where the player
  can turn it back on, and Resetting in Config's Confirmations tab turns it back on too.
  `remember = 14` (1 to 99) uses the game's own switch instead, here "Selling items".
- **`ask` has the row too** (since 2.28.0), with the same keys. It stands for one answer,
  `remember_answer` (default the first row), which `ask` gives without asking once the player
  turned the question off. Gem Lady Trade's question uses the game's switch 11, "Take Quest", so
  the player's setting counts for it as for the game's own question:

  ```lua
  local pick = rq.ui.ask(text, {
    { id = YES, text = "Yes" }, { id = TRADE, text = "Trade a Jewel" }, { id = NO, text = "No" },
  }, { game = true, remember = 11 }) -- while "Take Quest" is off: YES at once
  ```
- **Ticked from the start** (since 2.44.0): `remember_checked = true` shows the row ticked. An
  answer with it still ticked turns the question off, whichever button or row was picked, and the
  call then gives `remember_answer` (for `ask`) or true (for `confirm`) without asking. Save
  Profiles asks once this way whether to copy a vanilla save further along:

  ```lua
  local pick = rq.ui.ask(text, { { id = "yes", text = "Yes, copy it and play" },
    { id = "no", text = "No, start a new game" } },
    { remember = "vanilla-start", remember_answer = "no", remember_checked = true })
  ```
- **Agents** see the screen `select`: `confirm`'s buttons are `yes` and `no`, `notice`'s is `yes`,
  `ask`'s rows are `select-<label>`, and `select.message` holds the text.

Morurun Items and Gem Lady Trade ask this way.

See [`rq.gamebutton`](../reference/api/rq.gamebutton.md), [`rq.skilllist`](../reference/api/rq.skilllist.md),
[`rq.knownskills`](../reference/api/rq.knownskills.md),
[`rq.statuspage`](../reference/api/rq.statuspage.md), [`rq.castle`](../reference/api/rq.castle.md),
[`rq.config`](../reference/api/rq.config.md),
[`rq.ui`](../reference/api/rq.ui.md) and [`rq.uikit`](../reference/api/rq.uikit.md) for every field.
