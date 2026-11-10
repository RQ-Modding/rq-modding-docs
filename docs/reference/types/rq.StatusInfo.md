# rq.StatusInfo

`since 2.2.0`

What `rq.status.info` gives about a definition.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The id. |
| `name` | `string` | The name. |
| `kind` | `"bad"\|"good"` | The kind. |
| `mod` | `string` | The id of the mod that defined it. |
| `turns` *(optional)* | `integer` | The default turns; nil for the whole fight. |
| `stack` | `"refresh"\|"add"\|"keep"\|integer` | What adding it again does. |
| `cured_by` | `(string\|integer)[]` | What cures it. |
| `tags` | `string[]` | Its tags. |
| `keep_on_down` | `boolean` | Whether it stays when the bearer goes down. |
| `lethal` | `boolean` | Whether its damage may down the bearer. Since 2.3.0. |
| `persevere` | `boolean` | Whether Persevere saves the bearer from its lethal damage. Since 2.26.0. |
| `lasts` | `"fight"\|"quest"` | How long it can stay. Since 2.26.0. |
| `immune` *(optional)* | [`rq.StatusImmune`](rq.StatusImmune.md) | Who cannot take it, as defined; nil when the definition has none. Since 2.26.0. |
| `desc` *(optional)* | `string` | The text for players; nil when the definition has none. Since 2.26.0. |

## Used by

[`rq.status.info`](../api/rq.status.md#rqstatusinfo)
