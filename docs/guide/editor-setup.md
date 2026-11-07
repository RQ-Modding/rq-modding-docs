# Editor setup

The release ships `lua/rq.lua`, a file of [LuaLS](https://luals.github.io/) annotations for every
`rq.*` call. With it, an editor that runs the Lua language server completes `rq.` as you type, shows
each call's documentation on hover, and warns about wrong argument types. It is the same text as
this site's [API reference](../reference/index.md).

## VS Code

1. Install the **Lua** extension by sumneko (`sumneko.lua`).
2. Open the game folder (the one with `mods` and `lua`) with **File > Open Folder**.
3. Open a mod's `init.lua` and type `rq.`.

The release puts a `.luarc.json` in the game folder that points the extension at `lua`:

```json
{
  "runtime.version": "Lua 5.4",
  "workspace.library": ["lua"]
}
```

## Working on a mod in its own folder

When you keep a mod somewhere else (its own git repository, say), copy `rq.lua` from the game's `lua`
folder into it, or point `workspace.library` at the game's `lua` folder with a full path:

```json
{
  "runtime.version": "Lua 5.4",
  "workspace.library": ["C:/Games/Rance Quest Magnum/lua"]
}
```

Update the copy when you install a newer RQ MOD, so new calls complete too.

## Other editors

Any editor that runs the Lua language server (LuaLS) works the same way, such as Neovim with
`lua_ls`, Zed, or Sublime Text with LSP. Point the server's `workspace.library` setting at the folder
that holds `rq.lua`.

## mod.json

For completion and checks in `mod.json`, add a `$schema` line:

```json
{
  "$schema": "https://rq-modding.github.io/rq-modding-docs/schemas/mod.schema.json",
  "id": "hello-mod"
}
```

The engine ignores `$schema`. The schema is in this site's repository (`docs/public/schemas`).
