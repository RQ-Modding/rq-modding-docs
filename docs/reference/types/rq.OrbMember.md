# rq.OrbMember

A roster member, from `rq.orb.roster`. `rq.party.roster` gives the same with `hp_max` and `status`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `state` | `integer` | Where the character is (`登録状態`, `rq.ids.party_state`): 1 in the party, 2 the first army, 3 used in this quest, 4 the second army. |
| `hp` | `integer` | HP. |
| `max_hp` | `integer` | Most HP. |

## Used by

[`rq.orb.roster`](../api/rq.orb.md#rqorbroster)
