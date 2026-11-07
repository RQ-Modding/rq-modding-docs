# rq.store.global

`since 1.8.0`

The same calls as `rq.store`, in one file for every save profile.

The file is `rqmod-global.json` in the base profile's save folder. Use it for settings, such as what
a mod's Config page changes. Its keys are apart from `rq.store`'s.

```lua
local on = rq.store.global.get("on", true)
rq.store.global.set("on", not on)
```

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `get` | `fun(key: string, default?: any): number\|string\|boolean\|nil` | Reads a key, or returns `default`. |
| `set` | `fun(key: string, value: number\|string\|boolean\|nil)` | Writes a key; nil deletes it. |
| `delete` | `fun(key: string)` | Deletes a key. |
| `keys` | `fun(): string[]` | Lists this mod's keys. |
