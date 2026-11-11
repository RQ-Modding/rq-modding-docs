# rq.PartyMember

`since 2.35.0`

A recruited character, from `rq.party.roster`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `state` | `integer` | Where the character is (`rq.ids.party_state`): 1 in the party, 2 the first army, 3 used in this quest, 4 the second army. |
| `hp` | `integer` | HP. |
| `hp_max` | `integer` | Most HP. |
| `status` | `integer` | The status change (`rq.ids.state`): 0 none, 1 poison, 2 stun, 3 downed. |

## Used by

[`rq.party.roster`](../api/rq.party.md#rqpartyroster)
