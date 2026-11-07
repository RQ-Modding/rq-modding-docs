# rq.Sprite

`since 1.9.0`

A mod sprite among the game's own, made by `rq.sprite.new`.

The methods that return the sprite can be chained.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.Sprite:set`](#rqspriteset) | Changes only the options given. |
| [`rq.Sprite:get`](#rqspriteget) | Returns the sprite's options now. |
| [`rq.Sprite:remove`](#rqspriteremove) | Removes the sprite. |
| [`rq.Sprite:alive`](#rqspritealive) | Returns whether the sprite is still there. |
| [`rq.Sprite:play`](#rqspriteplay) | Plays the sprite's GIF. |
| [`rq.Sprite:stop`](#rqspritestop) | Holds the GIF on the frame it is on. |
| [`rq.Sprite:frame`](#rqspriteframe) | Returns the GIF frame shown, or shows one and stops. |
| [`rq.Sprite:playing`](#rqspriteplaying) | Returns whether the sprite's GIF is playing. |
| [`rq.Sprite:to`](#rqspriteto) | Moves the sprite from the values it has now to new ones, over time. |
| [`rq.Sprite:moving`](#rqspritemoving) | Returns whether a motion is waiting or moving. |
| [`rq.Sprite:halt`](#rqspritehalt) | Stops the motion where it is, without its `on_end`. |

### rq.Sprite:set

```lua
rq.Sprite:set(opts) -> rq.Sprite
```

`since 1.9.0`

Changes only the options given.

Raises an error for a bad option, or after the sprite was removed.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.SpriteOpts`](rq.SpriteOpts.md) | The options to change. |

| Returns | Type | Description |
| --- | --- | --- |
| `self` | [`rq.Sprite`](rq.Sprite.md) | The sprite. |

### rq.Sprite:get

```lua
rq.Sprite:get() -> table
```

`since 1.9.0` `changed 1.10.0` `changed 1.11.0`

Returns the sprite's options now.

Besides the options it has `id`, `mod`, `w` and `h` before the scale (the content's own size when
not set), `origin` as `{x, y}`, `screen` (with `keep = "screen"`), `in_scene` (shown and drawn),
`clock` and `moving`. A GIF sprite adds `gif`, `frame`, `frames`, `gif_ms` (one time through),
`fps` and `playing`. An attached sprite adds `attach` and `drawn = {x, y, z}`, where it is drawn now.

Raises an error after the sprite was removed.

| Returns | Type | Description |
| --- | --- | --- |
| `opts` | `table` | A copy of the options. |

> Changed in 1.10.0: Added the GIF and motion fields.

> Changed in 1.11.0: Added `attach` and `drawn`.

### rq.Sprite:remove

```lua
rq.Sprite:remove()
```

`since 1.9.0`

Removes the sprite.

`set` and `get` raise an error after that.

### rq.Sprite:alive

```lua
rq.Sprite:alive() -> boolean
```

`since 1.9.0`

Returns whether the sprite is still there.

| Returns | Type | Description |
| --- | --- | --- |
| `alive` | `boolean` | false once it was removed: by the mod, a load, the title or `keep`. |

### rq.Sprite:play

```lua
rq.Sprite:play(opts) -> rq.Sprite
```

`since 1.10.0`

Plays the sprite's GIF.

Raises an error for a sprite with no GIF, or a range outside its frames.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | `{from?: integer, to?: integer, loop?: boolean, on_end?: fun(s:` [`rq.Sprite`](rq.Sprite.md) `)}` | `from` (default 1) to `to` (default the last frame), over again unless `loop = false`. `on_end` runs when a play without loop reaches its last frame. |

| Returns | Type | Description |
| --- | --- | --- |
| `self` | [`rq.Sprite`](rq.Sprite.md) | The sprite. |

### rq.Sprite:stop

```lua
rq.Sprite:stop() -> rq.Sprite
```

`since 1.10.0`

Holds the GIF on the frame it is on.

| Returns | Type | Description |
| --- | --- | --- |
| `self` | [`rq.Sprite`](rq.Sprite.md) | The sprite. |

### rq.Sprite:frame

```lua
rq.Sprite:frame(n) -> integer|rq.Sprite, integer?
```

`since 1.10.0`

Returns the GIF frame shown, or shows one and stops.

Raises an error for a frame outside the GIF.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` *(optional)* | `integer` | The frame to show, from 1; leave it out to read. |

| Returns | Type | Description |
| --- | --- | --- |
| `frame` | `integer\|` [`rq.Sprite`](rq.Sprite.md) | Without `n`: the frame shown. With `n`: the sprite. |
| `count` | `integer?` | Without `n`: how many frames there are. |

### rq.Sprite:playing

```lua
rq.Sprite:playing() -> boolean
```

`since 1.10.0`

Returns whether the sprite's GIF is playing.

| Returns | Type | Description |
| --- | --- | --- |
| `playing` | `boolean` | true while it plays. |

### rq.Sprite:to

```lua
rq.Sprite:to(opts) -> rq.Sprite
```

`since 1.10.0`

Moves the sprite from the values it has now to new ones, over time.

A new `to` takes the place of the one moving, from where it got to, and the old `on_end` does not
run. `Sprite:set` of a value takes that value out of the motion, and the rest goes on. Removing the
sprite ends it too.

Raises an error for a negative `ms` or `delay`, an unknown `ease`, or an `on_end` that is not a
function.

```lua
rq.sprite.new({ fill = { 255, 255, 255 }, w = 1024, h = 768, z = "top" })
  :to({ alpha = 0, ms = 300, on_end = function(s) s:remove() end })  -- a white flash
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.SpriteMotion`](rq.SpriteMotion.md) | The values and the timing. |

| Returns | Type | Description |
| --- | --- | --- |
| `self` | [`rq.Sprite`](rq.Sprite.md) | The sprite. |

### rq.Sprite:moving

```lua
rq.Sprite:moving() -> boolean
```

`since 1.10.0`

Returns whether a motion is waiting or moving.

| Returns | Type | Description |
| --- | --- | --- |
| `moving` | `boolean` | true until the motion ends. |

### rq.Sprite:halt

```lua
rq.Sprite:halt() -> rq.Sprite
```

`since 1.10.0`

Stops the motion where it is, without its `on_end`.

| Returns | Type | Description |
| --- | --- | --- |
| `self` | [`rq.Sprite`](rq.Sprite.md) | The sprite. |

## Used by

[`rq.Sprite:frame`](rq.Sprite.md#rqspriteframe), [`rq.Sprite:halt`](rq.Sprite.md#rqspritehalt), [`rq.Sprite:play`](rq.Sprite.md#rqspriteplay), [`rq.Sprite:set`](rq.Sprite.md#rqspriteset), [`rq.Sprite:stop`](rq.Sprite.md#rqspritestop), [`rq.Sprite:to`](rq.Sprite.md#rqspriteto), [`rq.SpriteAttach`](rq.SpriteAttach.md), [`rq.SpriteMotion`](rq.SpriteMotion.md), [`rq.sprite.list`](../api/rq.sprite.md#rqspritelist), [`rq.sprite.new`](../api/rq.sprite.md#rqspritenew)
