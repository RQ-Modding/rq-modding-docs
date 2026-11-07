# rq.SpriteAttach

`since 1.11.0`

What an attached sprite follows. Give one of these.

An attached sprite follows its target's place, not its scale or turn, is hidden while the target
is, and goes when the target goes. On a card it follows the card's own sprite; the card's parts
sit over it (marks +1, the HP bar +2, the flame +10, an enemy's weak point +15), so `z = 20` is over
all of them. A dead enemy's card stays up until the fight ends, and a sprite on it stays too.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `card` *(optional)* | `integer` | The card at this place, whoever stands there: 1 to 5 allies, 11 to 15 enemies. Only in a fight; goes at its end. |
| `chara` *(optional)* | `integer` | This character's card, wherever a switch puts it; hidden while they are not on a card. Only in a fight; goes at its end. |
| `sprite` *(optional)* | [`rq.Sprite`](rq.Sprite.md) | Another mod sprite, with its motion. Up to 8 can follow one another, not in a ring. Goes when that one is removed. |
| `game` *(optional)* | `integer` | A game sprite number from `rq.sprite.scene` (kind "sprite"). Goes when the game deletes it. |

## Used by

[`rq.SpriteOpts`](rq.SpriteOpts.md)
