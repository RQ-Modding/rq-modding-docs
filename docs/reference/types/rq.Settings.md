# rq.Settings

`since 2.35.0`

A settings page's values, from `rq.config.settings`.

Its calls read and write the store the page keeps its values in, under the mod that made the page,
so a value the mod reads is the one the page shows.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The page's id. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.Settings.get`](#rqsettingsget) | Returns a row's value: the stored one when the row can take it, else the row's default. |
| [`rq.Settings.set`](#rqsettingsset) | Changes a row's value, as the page would. The page shows it, and `on_change` callbacks run when it changed. |
| [`rq.Settings.reset`](#rqsettingsreset) | Puts every row back to its default: the keys are taken out of the store. `on_change` callbacks run for the values that change. |

### rq.Settings.get

```lua
rq.Settings.get(key) -> boolean|integer|number|string
```

`since 2.35.0`

Returns a row's value: the stored one when the row can take it, else the row's default.

Raises an error for a key no row has.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The row's key. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `boolean\|integer\|number\|string` | The value. |

### rq.Settings.set

```lua
rq.Settings.set(key, value)
```

`since 2.35.0`

Changes a row's value, as the page would. The page shows it, and `on_change` callbacks run when it
changed.

Raises an error for a key no row has, or a value the row cannot take (a stepper's number outside
`min` and `max`, a choice's value it does not list).

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The row's key. |
| `value` | `boolean\|integer\|number\|string` | The new value. |

### rq.Settings.reset

```lua
rq.Settings.reset()
```

`since 2.35.0`

Puts every row back to its default: the keys are taken out of the store. `on_change` callbacks run
for the values that change.

## Events

| Name | Summary |
| --- | --- |
| [`rq.Settings.on_change`](#rqsettingson_change) | Calls `fn` when a value changes: on the page, by `set` or by Reset. |

### rq.Settings.on_change

```lua
rq.Settings.on_change(fn) -> fun()
```

`since 2.35.0`

Calls `fn` when a value changes: on the page, by `set` or by Reset.

An error in `fn` is written to the log and the other callbacks still run.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(key: string, value: any, old: any)` | Gets the row's key, the new value and the one before. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

## Used by

[`rq.config.settings`](../api/rq.config.md#rqconfigsettings)
