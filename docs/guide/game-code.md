# The game's own code

When no `rq.*` call does what a mod needs, [`rq.ain`](../reference/api/rq.ain.md) reaches into the
game's own code, the AIN (`RanceQuest.ain`): it calls the game's functions, runs Lua around them,
reads and writes the game's globals, and changes constants in its code. Use a dedicated `rq.*` call
when one exists: it is checked, documented and kept working across loader versions, while the
game's code has none of that.

## Names

Functions and globals go by the game's own names, most of them Japanese: `クエスト_名前`,
`Ｃ敵登録`, `◆ランダムエンカウント歩数`. A method is written `Class@method`, as in
`T_Player@checkEncount`. Write them in UTF-8, as `init.lua` is, and copy them from the log rather
than typing them: many use full-width letters and digits (`Ｃ`, `８`), which look like the plain
ones and are not.

## Finding a function

`rq.ain.find` writes every function whose name contains a text to the log, one per line, with its
number and its full name:

```lua
rq.ain.find("Encount")
```

```text
[rqmod] find 'Encount' fno=10717 T_Player@getEncountFlag
[rqmod] find 'Encount' fno=10733 T_Player@checkEncount
[rqmod] find 'Encount' fno=10734 T_Player@addEncount
[rqmod] find 'Encount' fno=14290 T_EncountBar@isSuspend
...
```

The Japanese names need the Japanese text: `rq.ain.find("エンカウント")` finds
`ランダムエンカウント_あり`, which "Encount" does not.

The match is on the game's spelling, so case and full-width letters count. It lists at most 40
names: a longer text narrows the list. The call works at the top level of `init.lua`; to try names
while you play, put it on an [F3 menu row](debugging.md#the-f3-menu). The name is what
`rq.ain.call` and `rq.ain.hook` take. `find` gives names only, not what a function takes or does.

To learn that, read the game's code. Tools for the System 4 engine, such as alice-tools, turn your
copy's `RanceQuest.ain` into readable source. That source is the game's own work: read it to
understand the game, and do not share it or copy it into a mod.

## Calling a function

```lua
local name = rq.ain.call("クエスト_名前", 126)   -- the quest's name
```

The arguments are int, bool, float or string, and every one is needed. A function that takes a
reference or a struct cannot be called this way. A method (`Class@method`) needs its object:
`rq.ain.method` (2.16.0) calls it on the struct a global reaches.

```lua
local rows = rq.ain.method({ "g_sSystemMenu", "m_sButton" }, "T_ButtonGroup@getButtonCount")
```
 A scene command waits until it ends,
so call it from a callback the game runs, not at the top level. See
[`rq.ain.call`](../reference/api/rq.ain.md#rqaincall) for what happens when the call reaches a save
or a load.

## Running Lua around a function

A hook runs before and after every call of a function. `before` can change the arguments or skip
the function and give its result; `after` can change the result:

```lua
-- Every roll of 乱数(10) comes up 1, as long as the hook stays.
local remove = rq.ain.hook("乱数", { after = function(h)
  if h.args[1] == 10 then h.result = 1 end
end })
remove()   -- takes the hook away again
```

Hooks can sit at the top level of `init.lua`. Several mods may hook the same function. A hook on a
function the game calls often, such as `乱数`, runs every time, so keep its work small, and remove
it once it is no longer needed.

## Globals

```lua
local fa = rq.ain.global("FA", 87)              -- FA[87]
local name = rq.ain.global("Ｑ", 126, "名前")   -- Ｑ[126].名前
rq.ain.set_global("◆ランダムエンカウント歩数", 1)
```

Indexes and field names follow the global's name, mixed as the game nests them.
`rq.ain.global_len` gives an array's size. Many of the game's arrays start at 1 and leave 0 unused.
What `set_global` writes is the game's own state and goes into the next save, so put back what you
change for a test.

## Changing constants in the code

`rq.ain.patch_int` and `rq.ain.patch_float` replace a number written in a function, such as a skill
number or a multiplier. `rq.ain.patch_int_after` finds one by the global it follows. Each returns how
many it replaced: check that count, since a game update can move or remove the number.

```lua
-- 衝撃計算 checks for Fortune by its number; make that check match no skill.
if rq.ain.patch_int("衝撃計算", rq.ids.skill.FORTUNE, -1) ~= 1 then
  rq.log("衝撃計算 changed; the patch is off")
end
```

`rq.ain.skip_msgbox` takes the game's message boxes that hold a text out of its code.

## Take care

- The names and the code are the game's, not ours. They hold for this version of Rance Quest
  Magnum, and a mod that leans on them should check what it gets (a count, a nil) and say so in the
  log when it does not fit.
- A bad index passed to a game function is a fatal error in the game, and `rq.ain.call` cannot
  check it.
- Something many mods would do through `rq.ain` is a call `rq.*` is missing. The
  [roadmap](../roadmap.md) lists the ones planned, such as `rq.ain.call` with reference and struct
  arguments.
