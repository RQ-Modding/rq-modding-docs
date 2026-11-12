# rq.MonsterDrop

An item a monster may leave after a won fight (`rq.MonsterEdit.drops`).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `item` | `integer\|string` | An item number or a text id (`rq.item.define`). |
| `chance` | `integer` | The chance, 1 to 100, rolled with the game's own roll (`rq.random.fix` fixes it). |

## Used by

[`rq.MonsterEdit`](rq.MonsterEdit.md)
