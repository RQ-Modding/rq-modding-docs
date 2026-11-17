# rq.knownskills

`since 2.54.0` `changed 2.57.0`

More known skills than the game's 17, shown 17 at a time on the status page and in the skill window.

The game keeps a character's skills in 21 rows (`Ｃ[iic].スキル`): 17 known skills and the item
effect skill fill rows 1 to 18, and rows 19 and 20 stay empty. With `install{ most = n }`, every
character's rows grow to n + 4, a new skill can take rows 1 to n + 1, and the game's own code walks
all of them: battles, passives and stats (`Ｃ再計算`), refills, the hotbar, the free-row check
before a buy, Skill Again. `rq.chara.slots`, `rq.chara.skill_room`, `rq.chara.learn` and the
other skill calls count the new rows too.

Both screens show the known skills as one list of 17 plus the item effect skill. While the game
builds that list, the page's 17 take the place of the whole: they are sorted as the game sorts
(panel color, then skill number), the item effect skill stays last, and the empty item slot (569) is
left out as the game leaves it out. REMOVE, upgrades and dragging a skill to the hotbar work on the
skill shown, on any page. The status page opens on page 1, and so does another character.

The save stays the game's own: before it is written the rows past 18 move into the loader's data
beside the save (`rq.savedata`) and the arrays go back to 21; after the write, and after a load,
they come back. A row a smaller `most` has no room for stays in that data and comes back at a save
or a load once a row is free (or `most` is larger); one whose skill the character holds again by
then is dropped. A save made with no mod calling `install` drops what an earlier save kept apart, so old
rows never come back over a later game: a character then has only the skills in the game's 18
rows, and Skill Again gives the skill points back.

The page controls are drawn for the mod that calls `install`: a scroll bar 14 pixels wide between
the known skills and the equipment on the status page (the wheel over the skills turns it too) and
the game's two arrows beside KNOWN SKILLS in the skill window. Page Up and Page Down turn the page
on both screens (held, they turn again after 400 ms and then every 150 ms); the game reads neither
there. `install{ controls = false }` leaves all of them out, for a mod with its own; it then turns
pages with `set_page`.

```lua
rq.knownskills.install({ most = 34 })
rq.log(("%d known skills at most, page %d of %d"):format(rq.knownskills.most(),
  rq.knownskills.page(), rq.knownskills.page_count()))
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.knownskills.install`](#rqknownskillsinstall) | Makes the skill rows longer and turns the pages on. |
| [`rq.knownskills.most`](#rqknownskillsmost) | Returns the most known skills a character can have. |
| [`rq.knownskills.page`](#rqknownskillspage) | Returns the page of known skills shown, or shown next. |
| [`rq.knownskills.page_count`](#rqknownskillspage_count) | Returns how many pages of known skills the character shown has. |
| [`rq.knownskills.set_page`](#rqknownskillsset_page) | Shows another page of known skills. |

### rq.knownskills.install

```lua
rq.knownskills.install(opts) -> boolean
```

`since 2.54.0`

Makes the skill rows longer and turns the pages on.

Call it from a mod's `init.lua`, before the game starts: the rows of every character made from then
on are longer, the boot's too. It changes the game's code (the numbers 21, 20, 19 and 18 in the
functions that read the rows), and checks each place first: when the code is not as expected,
nothing changes and it raises an error. A second call does nothing and returns true; a different
`most` is logged and not used, so the first mod's number stays until the game starts again.

Raises an error for `opts` that is not a table, a `most` that is not a whole number from 17 to 102,
or game code that is not as expected.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | `{most?: integer, controls?: boolean}` | `most`: the most known skills, 17 to 102 (17 is the game's own, 17 more for each page). Default 34. `controls = false` leaves out the scroll bar, the arrows and the keys. Default true. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the rows are longer (or were already). |

See also: [`rq.knownskills.set_page`](rq.knownskills.md#rqknownskillsset_page)

### rq.knownskills.most

```lua
rq.knownskills.most() -> integer
```

`since 2.54.0`

Returns the most known skills a character can have.

| Returns | Type | Description |
| --- | --- | --- |
| `most` | `integer` | From `install`; 17, the game's own, before it. |

### rq.knownskills.page

```lua
rq.knownskills.page() -> integer
```

`since 2.54.0`

Returns the page of known skills shown, or shown next.

Raises an error before `rq.knownskills.install`.

| Returns | Type | Description |
| --- | --- | --- |
| `page` | `integer` | The page, from 1. |

### rq.knownskills.page_count

```lua
rq.knownskills.page_count() -> integer
```

`since 2.54.0`

Returns how many pages of known skills the character shown has.

Counted when the game last built the list (the status page or the skill window).

Raises an error before `rq.knownskills.install`.

| Returns | Type | Description |
| --- | --- | --- |
| `pages` | `integer` | The page count, at least 1. |

### rq.knownskills.set_page

```lua
rq.knownskills.set_page(page) -> boolean
```

`since 2.54.0`

Shows another page of known skills.

The status page or the skill window, whichever is on top, is drawn again at once. With neither
shown, the page is kept for the next time the list is built.

Raises an error before `rq.knownskills.install`, or for a page that is not a whole number.

```lua
rq.knownskills.install({ most = 51, controls = false })
rq.gamebutton.add({ group = "skill-window", id = "known-next", label = "Next Known",
  enabled = function() return rq.knownskills.page() < rq.knownskills.page_count() end,
  on_click = function() rq.knownskills.set_page(rq.knownskills.page() + 1) end })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `page` | `integer` | The page; below 1 is page 1, past the last page is the last page. |

| Returns | Type | Description |
| --- | --- | --- |
| `drawn` | `boolean` | true when a screen was drawn again with it. |
