# rq.TrapCtx

What an `rq.dungeon.on_trap` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `x` | `integer` | The trap's cell, east. |
| `z` | `integer` | The trap's cell, north. |
| `kind` | `"shroom"\|"shock"\|"alarm"\|"pit"` | Writable. The kind the game drew. |
| `chance` | `integer` | Writable. The chance to avoid it, 0 to 100: the game's 20, 50 with a ranger (class 6) in the party, 100 while a member's Trap Evasion (skill 266) rank is above the traps they disarmed, 0 on quest 190. |
| `who` *(optional)* | `integer` | The roster slot (iic) of the member who tries; nil for none. |
| `cancel` | `boolean` | Writable. true removes the trap with no scene. |

## Used by

[`rq.dungeon.on_trap`](../api/rq.dungeon.md#rqdungeonon_trap)
