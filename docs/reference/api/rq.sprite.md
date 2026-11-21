# rq.sprite

`since 1.9.0` `changed 1.10.0` `changed 1.11.0` `changed 2.63.0`

Sprites a mod makes once and changes later, drawn among the game's own in z order.

The game's windows, menus and fades cover them where they are above; `rq.hud` is drawn after
everything and nothing covers it. A sprite shows a CG or a part of one, a GIF, a Flash file, a fill
color or text, and can be moved, stretched, scaled, turned, faded and tinted, at once or over time,
and can follow a card or another sprite.

They are the loader's own: the game does not save them or give their numbers out. Every mod sprite
goes on a load and at the title, and `rq.sprite.on_reset` says so, so a mod can make them again.
Call `new` from `rq.on_frame` or a callback, not at the top level of `init.lua`. GIF frames are
textures made once per file and shared: up to 64 GIF files and 64 million pixels in all. A delay
under 20 ms in a GIF plays as 100 ms, as browsers do. A Flash file is drawn as the game draws its
own, with the file's blend modes and colours under the sprite's; each sprite that shows one has its
own copy, as each of the game's parts has: up to 64 at once and 64 million pixels in all.

The game's own z, from `rq.sprite.scene`: 1 to 22 the hub's page and the quest list; 101 to 262 a
fight's field and cards, the dungeon view; 801 to 823 the bottom bar; 8001 to 8301 messages; 9001
and 9002 fades; 9101 the System menu; 15000 to 15010 Config.

```lua
local glow
rq.on_frame(function()
  if not glow or not glow:alive() then
    glow = rq.sprite.new({ cg = rq.image.add("glow", "glow.png"), x = 400, y = 200,
      origin = "center", blend = "add", alpha = 180 })
  end
  glow:set({ rotate = (rq.time_ms() / 20) % 360 })
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.sprite.new`](#rqspritenew) | Makes a sprite and shows it. |
| [`rq.sprite.list`](#rqspritelist) | Lists this mod's sprites. |
| [`rq.sprite.clear`](#rqspriteclear) | Removes all of this mod's sprites. |
| [`rq.sprite.scene`](#rqspritescene) | Lists everything in the game's scene list now, back to front. |

### rq.sprite.new

```lua
rq.sprite.new(opts) -> rq.Sprite
```

`since 1.9.0`

Makes a sprite and shows it.

Up to 256 per mod and 1024 in all.

Raises an error for a bad option (and leaves nothing behind), or past the limits.

```lua
rq.battle.on_start(function()
  -- a star over the card of whoever starts on rank 1, which follows them in a switch
  rq.sprite.new({ gif = "star.gif", x = 260, y = 4, z = 20, attach = { chara = rq.party.get()[1] } })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.SpriteOpts`](../types/rq.SpriteOpts.md) | What it shows and where. |

| Returns | Type | Description |
| --- | --- | --- |
| `sprite` | [`rq.Sprite`](../types/rq.Sprite.md) | The new sprite. |

### rq.sprite.list

```lua
rq.sprite.list() -> rq.Sprite[]
```

`since 1.9.0`

Lists this mod's sprites.

| Returns | Type | Description |
| --- | --- | --- |
| `sprites` | [`rq.Sprite`](../types/rq.Sprite.md) `[]` | The same objects `new` gave, oldest first. |

### rq.sprite.clear

```lua
rq.sprite.clear() -> integer
```

`since 1.9.0`

Removes all of this mod's sprites.

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | How many were removed. |

### rq.sprite.scene

```lua
rq.sprite.scene() -> rq.SceneRow[]
```

`since 1.9.0`

Lists everything in the game's scene list now, back to front.

The pipe's `scene` command gives the same as JSON, with the screen.

| Returns | Type | Description |
| --- | --- | --- |
| `rows` | [`rq.SceneRow`](../types/rq.SceneRow.md) `[]` | The rows, back to front. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.sprite.on_reset`](#rqspriteon_reset) | Calls `fn` after a load or the title removed every mod sprite. |

### rq.sprite.on_reset

```lua
rq.sprite.on_reset(fn) -> fun()
```

`since 1.9.0`

Calls `fn` after a load or the title removed every mod sprite.

These are the same callbacks as `rq.on_reset`.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(why: "load"\|"title")` | `why` says which one happened. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
