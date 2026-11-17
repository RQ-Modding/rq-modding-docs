# Install

RQ MOD runs Rance Quest Magnum on its own engine, which loads mods. The game's own files stay as they
are, so you can still start the game without mods.

## Install RQ MOD

1. Install Rance Quest Magnum.
2. Download the latest `RQ-MOD-*.zip` from the [Releases page](https://github.com/RQ-Modding/RQ-Mod/releases).
3. Extract it into the game folder, so it looks like this:

   ```text
   Rance Quest Magnum/
   ├── Data/
   ├── DLL/
   ├── Face CG/
   ├── lua/
   │   └── rq.lua            definitions for mod authors' editors
   ├── mods/                 put mods here, one folder each
   ├── xsystem4/
   │   ├── config.json
   │   └── xsystem4.exe      start the game with this
   └── RanceQuest.exe
   ```

4. Start the game with `xsystem4\xsystem4.exe`.

The window title shows "RQ MOD" and the loader version, and the main menu shows the version too.

## Add and remove mods

- **Add:** extract the mod's folder into `mods`. The folder holds at least a `mod.json` and an
  `init.lua`. Do not put an extra folder level in between (`mods/camera-zoom/mod.json`, not
  `mods/camera-zoom/camera-zoom/mod.json`).
- **Remove:** delete the folder.
- **Check:** `logs\rqmod.log` has a `Loading <id>` line for each mod that loaded, and a line that says
  why for each one that did not, such as `skip some-mod: missing dependency other-mod`. Mods with
  settings add a page to the Mods tab in the game's Config screen.

Mods load when the game starts, so restart the game after you add or remove one.

## Saves

RQ MOD keeps its saves apart from the original game's. Started from `xsystem4\xsystem4.exe`, it saves
in `xsystem4\Rance Quest\SaveData`. When the environment variable `XSYSTEM4_HOME` is set, the save
goes under that folder instead, and when only `HOME` is set, under `%HOME%\.xsystem4`. It never
writes the original game's save in `Documents\AliceSoft`.

Mods that add characters or items write them into the save like the game does, so keep a copy of the
save folder before you try a mod that adds content.

## A gamepad

A gamepad does nothing in RQ MOD yet: Rance Quest reads the pad through a part of the engine that is
not written yet, so the game sees no pad. A tool that maps the pad to keys and the mouse (Steam Input,
for one) can stand in until then.

## When something goes wrong

Everything is written to the `logs` folder next to `mods`:

| File | What it is |
| --- | --- |
| `rqmod.log` | This run's log. |
| `rqmod.prev.log` | The run before. |
| `rqmod-crash-<date>-<time>.log` | Written when the game crashes: what happened, where, the game-script call stack and the last log lines. |
| `rqmod-crash-<date>-<time>.dmp` | A small Windows minidump of the same moment. |
| `rqmod-unclean-<date>-<time>.log` | The log of a run that never closed cleanly (crash, kill, hang). |

When you report a problem, attach the crash `.log` (and the `.dmp` if it is small) and say which mods
you had installed.
