# Buttons in the game's menus

Since loader 2.16.0 a mod can put a way in to itself inside the game's own menus, drawn and moved
by the game itself, instead of a HUD button over the screen. Two places so far:

- the **SYSTEM menu**: one MODS row for every mod, with each mod's entries in a list;
- **Rance Castle**: a room of the mod's own.

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

See [`rq.gamebutton`](../reference/api/rq.gamebutton.md) and
[`rq.castle`](../reference/api/rq.castle.md) for every field.
