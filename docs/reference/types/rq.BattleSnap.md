# rq.BattleSnap

What `rq.battle.snapshot` returns: a copy of the fight screen.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `up` | `boolean` | Ally skill select is open. |
| `allies` | `{id: integer, no: integer, name: string}[]` | Each ally: `id` the roster slot, `no` the battle number, `name`. |
| `enemies` | `{id: integer, no: integer, name: string}[]` | Each enemy, as for `allies`. |
| `skills` | `{id: integer, name: string, uses: integer, enabled: boolean}[]` | The acting ally's skills: number, name, uses left, and whether the button can be clicked. |
| `log` | `string[]` | The battle log lines, oldest first. |

## Used by

[`rq.battle.snapshot`](../api/rq.battle.md#rqbattlesnapshot)
