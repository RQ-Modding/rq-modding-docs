# rq.store

`since 0.4.0` `changed 2.34.0` `changed 2.35.0`

Small key and value storage for each mod and each save profile.

It lives in `rqmod-store.json` in the active save folder, so it follows the `rq.saves` profile, not
the game's save: the file is written on every `set` and `delete`, so after a quit without saving
or a load it is ahead of the save. Keep progress that must match the save (counts, unlocks,
"already given") in `rq.savedata`, and settings in `rq.store.global`. Values are numbers, strings
and booleans; a whole number comes back an integer. Each mod sees only its own keys. A Config page of
settings (`rq.config.settings`) keeps its values here or in `rq.store.global` for the mod.

```lua
if not rq.store.get("alice_joined", false) then
  if rq.chara.recruit("mymod:alice") then rq.store.set("alice_joined", true) end
end
```

## Namespaces

| Namespace | Summary |
| --- | --- |
| [`rq.store.global`](rq.store.global.md) | The same calls as `rq.store`, in one file for every save profile. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.store.get`](#rqstoreget) | Reads a key. |
| [`rq.store.set`](#rqstoreset) | Writes a key. |
| [`rq.store.delete`](#rqstoredelete) | Deletes a key. |
| [`rq.store.keys`](#rqstorekeys) | Lists this mod's keys. |

### rq.store.get

```lua
rq.store.get(key, default) -> number|string|boolean|nil
```

`since 0.4.0` `changed 2.35.0`

Reads a key.

A whole number comes back an integer, as it was set (`math.type` "integer"), up to 2^53.

with `math.type(v) == "integer"` failed on every value read back.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |
| `default` *(optional)* | `any` | What to return when the key is not set. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `number\|string\|boolean\|nil` | The value, or `default`. |

> Changed in 2.35.0: A whole number comes back an integer; it came back a float (3.0), so a check

### rq.store.set

```lua
rq.store.set(key, value)
```

`since 0.4.0`

Writes a key.

Raises an error for a value that is not a number, string, boolean or nil, or when the file cannot be
opened.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |
| `value` | `number\|string\|boolean\|nil` | The value; nil deletes the key. |

### rq.store.delete

```lua
rq.store.delete(key)
```

`since 0.4.0`

Deletes a key.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

### rq.store.keys

```lua
rq.store.keys() -> string[]
```

`since 0.4.0`

Lists this mod's keys.

| Returns | Type | Description |
| --- | --- | --- |
| `keys` | `string[]` | The keys. |
