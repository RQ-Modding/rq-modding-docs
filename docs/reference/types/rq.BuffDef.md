# rq.BuffDef

A mod's buff on a card, for `rq.battle.set_buff` and `set_rank_buff`.

The marks of a card (Protect, Berserk, Stealth, Barrier, Guard, the flame and mods' buffs) take
turns in one spot, fading in and out, 1.5 seconds each; a single mark stays still.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `icon` *(optional)* | `integer` | A CG number, such as one from `rq.image.add` with `fit`, `w` and `h`; the spot holds about 56×56. A number that is no CG raises an error. Since 0.27.1 the icon is a game mark, so the game's windows cover it. |
| `anim` *(optional)* | `string` | An `rq.image.add_gif` key, played in the game's mark spot (about 35×26, from the top-left corner); wins over `icon`. Since 0.19.0. |
| `text` *(optional)* | `string` | A short text over the icon. |
| `order` *(optional)* | `integer` | The place in the turns, lowest first. Default 0, as the game's marks; equal ones keep the order they were added. Since 0.30.0. |
| `x` *(optional)* | `integer` | Pixels from the card's left edge to the icon's. Default 111 on an ally, 37 on an enemy. Since 0.30.0. |
| `y` *(optional)* | `integer` | Pixels from the card's top edge to the icon's. Default 80 on an ally, 22 on an enemy. Since 0.30.0. |
| `layer` *(optional)* | `integer` | The z from the card's base, -100 to 100, with the text one above. Default 10. The game's: on an ally 0 base, 1 text, face, skills and arrows, 40 dead, 50 no skill, 55 mask; on an enemy 0 base and name, 1 arrows and states, 2 bar, 15 second line. Since 0.30.0. |
| `pinned` *(optional)* | `boolean` | Stays shown, out of the turns; it hides with the card's marks. Since 0.30.0. |

## Used by

[`rq.battle.set_buff`](../api/rq.battle.md#rqbattleset_buff), [`rq.battle.set_rank_buff`](../api/rq.battle.md#rqbattleset_rank_buff)
