# mod.json

Every mod folder needs a `mod.json` next to its `init.lua`. A folder with only an `init.lua` is
skipped, with `skip <folder>: no mod.json` in the log.

```json
{
  "id": "loot-preview",
  "name": "Loot Preview",
  "author": "Magnum Mods",
  "version": "1.0.0",
  "loader": "0.2.0",
  "priority": 0,
  "dependencies": [],
  "loadAfter": [],
  "loadBefore": [],
  "conflicts": []
}
```

## Fields

| Field | Type | What it does |
| --- | --- | --- |
| `id` | string | The mod's id. Other mods name it in their lists, and the engine keys the mod's `rq.store` data and log lines by it. Default: the folder's name. Keep it the same across versions. |
| `name` | string | The name for players. The engine records it, with `version`, in a save profile's mod list (`rq.saves`). Default: the id. A page in the Mods tab has its own title, set in `rq.config.page`. |
| `version` | string | The mod's own version, recorded in save profiles. Not used to order or gate anything. |
| `author` | string | Who made it. The engine does not read it. |
| `loader` | string | The lowest RQ MOD version the mod needs, such as `"1.8.0"`. A newer loader than the running one skips the mod. Leave it out and the mod always loads. |
| `priority` | number | Breaks ties in load order: lower loads first. Default 0. |
| `dependencies` | string[] | Mod ids that must be loaded. They load first; if one is missing, this mod is skipped. |
| `loadAfter` | string[] | Mod ids that load first when they are there. A missing one is fine. |
| `loadBefore` | string[] | Mod ids that load after this one when they are there. |
| `conflicts` | string[] | Mod ids that cannot run with this one. When one of them is loaded, this mod is skipped. |

Each list holds up to 16 ids; a longer one skips the mod (`too many dependencies`). Empty strings
and values that are not strings are ignored. `mod.json` must be valid JSON and at most 64 KB.

Field names are case sensitive: `loadAfter`, not `load_after`.

## Load order

The engine loads up to 64 mods. For each start it:

1. Reads every folder in `mods` that has a `mod.json` and an `init.lua`.
2. Skips a mod whose `id` another folder already took, whose `loader` is newer than the running one
   or is not a version number, or that lists a loaded mod in `conflicts`.
3. Skips a mod whose `dependencies` are not all loaded. This repeats, so a mod that needs a skipped
   mod is skipped too.
4. Orders the rest: a mod loads after its `dependencies` and `loadAfter` and before its
   `loadBefore`. Among the mods free to load next, the lowest `priority` goes first, then the id in
   alphabetical order.
5. Skips every mod caught in a cycle, such as two mods that each `loadAfter` the other.

Every mod that is skipped has a line in `logs\rqmod.log`:

| Log line | Why |
| --- | --- |
| `skip <id>: loader <v> is newer than <running>` | `loader` asks for a newer RQ MOD. |
| `skip <id>: loader '<v>' is not a semver` | `loader` is not like `1`, `1.2` or `1.2.3`. |
| `skip <id>: conflict <other>` | A mod in `conflicts` is loaded. |
| `skip <id>: missing dependency <other>` | A mod in `dependencies` is missing or was skipped. |
| `skip <id>: duplicate id <id>` | Another folder has the same `id`. |
| `skip cycle: <id>, <id>` | These mods wait on each other. |
| `skip <folder>: bad mod.json` | Not valid JSON, empty, or over 64 KB. |
| `skip <id>: no init.lua` | The folder has no `init.lua`. |

Loaded mods are listed as `Loading <id> priority <n>`, in load order.

## Load order and callbacks

Most `on_*` callbacks keep every mod's function and run them in the order the mods registered them,
which is load order for callbacks registered at the top level of `init.lua`. Where one callback's
result feeds the next, such as `rq.skill.on_describe`, a mod that wants the last word should
`loadAfter` the others.

## Versions

`loader` uses the loader version, which is also `rq.version` at runtime. Its rules:

- **Patch** (1.14.1 → 1.14.2): a fix or a small change in behavior.
- **Minor** (1.13.0 → 1.14.0): a new call or field.
- **Major** (0.31.0 → 1.0.0): a call removed, renamed, or changed in meaning.

So a mod written for 1.8.0 runs on every later 1.x. The [Changelog](../changelog.md) lists every
version.
