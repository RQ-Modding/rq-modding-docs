# RQ MOD docs

The documentation site for [RQ MOD](https://github.com/RQ-Modding/RQ-Mod), the Lua mod loader for
Rance Quest Magnum: guides for players and mod makers, and the `rq.*` API reference. Built with
[VitePress](https://vitepress.dev/).

The pages are plain Markdown, so they read on GitHub too: start at [docs/index.md](docs/index.md),
the [guides](docs/guide/) or the [API reference](docs/reference/index.md).

## Where the text comes from

| Path | Source | Edit it |
| --- | --- | --- |
| `docs/guide/`, `docs/index.md`, `docs/roadmap.md` | Written here | Here |
| `docs/reference/` | Generated from the engine's `dist/lua/rq.lua` (LuaLS annotations) by its `tools/apidoc/rqdoc.py` | In the engine, then run `npm run sync` |
| `docs/changelog.md` | A copy of the engine's `CHANGELOG.md` | In the engine, then run `npm run sync` |
| `docs/public/schemas/mod.schema.json` | Written here, from the engine's manifest reader | Here, when `mod.json` gains a field |

Never edit `docs/reference/` or `docs/changelog.md` by hand: the next sync overwrites them, and CI
fails when they differ from the engine.

## Working on it

Needs Node.js 20 or newer and Python 3.

```sh
npm install
npm run sync      # regenerate the reference from ../RQ_modding_xsystem4 (or: python scripts/sync.py --engine PATH)
npm run dev       # live preview at http://localhost:5173
npm run build     # the static site, in docs/.vitepress/dist
```

`python scripts/sync.py --check` exits 1 when the committed reference is older than the engine.

## Deploy

`.github/workflows/deploy.yml` checks the reference against the engine's `main`, builds the site and
publishes it to GitHub Pages on every push to `main`.

## License

The documentation text is [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/): share
and adapt it with credit, under the same license. The code examples are public domain
([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)): copy them into a mod under any
license. The build scripts and the `mod.json` schema are MIT. See [LICENSE](LICENSE).
