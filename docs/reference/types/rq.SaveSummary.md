# rq.SaveSummary

What a profile's save holds, read from its file.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `has_save` | `boolean` | The profile holds a game save. |
| `saved_at` *(optional)* | `string` | When the game save was written, "YYYY-MM-DD HH:MM" (the file's time). |
| `world` *(optional)* | `integer` | The world. |
| `fame_rank` *(optional)* | `integer` | The fame rank. |
| `fame` *(optional)* | `integer` | Fame. |
| `gold` *(optional)* | `integer` | Gold. |
| `quests` *(optional)* | `integer` | Quests cleared. |
| `suspend` | `boolean` | A suspend save exists. |
| `read_error` *(optional)* | `string` | Why the save could not be read. |

## Used by

[`rq.SaveProfile`](rq.SaveProfile.md), [`rq.VanillaSave`](rq.VanillaSave.md)
