# Install

RQ MOD runs Rance Quest Magnum on its own engine, which loads mods. The game's own files stay as they
are, so you can still start the game without mods.

## With RQ Manager

[RQ Manager](manager.md) does the steps of this page for you:

1. Install Rance Quest Magnum.
2. Download RQ Manager from the [Download](../download.md) page and unzip it into the game folder.
3. Start `RQ Manager\rq-manager.exe` and click **Install RQ MOD**, then **Play**.

Its Mods page installs, updates, turns off and removes mods, and puts the last version back. The
steps by hand follow, and the rest of this page holds for both.

## Install RQ MOD

1. Install Rance Quest Magnum.
2. Download the latest `RQ-MOD-*.zip` from the [Download](../download.md) page (older versions are on
   the [Releases page](https://github.com/RQ-Modding/RQ-Mod/releases)).
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
   │   ├── api.html          the API reference, offline
   │   ├── config.json
   │   └── xsystem4.exe      start the game with this
   ├── RanceQuest.exe
   └── RQ-MOD-README.txt     these steps, in short
   ```

4. Start the game with `xsystem4\xsystem4.exe`.

The window title shows "RQ MOD" and the loader version, and the main menu shows the version too,
with a Discord icon beside it: click it to open the RQ MOD server in your browser (the game asks
first).

## Add and remove mods

[RQ Manager](manager.md) does this from its Mods page. By hand:

- **Add:** extract the mod's folder into `mods`. The folder holds at least a `mod.json` and an
  `init.lua`. Do not put an extra folder level in between (`mods/camera-zoom/mod.json`, not
  `mods/camera-zoom/camera-zoom/mod.json`).
- **Remove:** delete the folder.
- **Check:** `logs\rqmod.log` has a `Loading <id>` line for each mod that loaded, and a line that says
  why for each one that did not, such as `skip some-mod: missing dependency other-mod`. Mods with
  settings add a page to the Mods tab in the game's Config screen.

Mods load when the game starts, so restart the game after you add or remove one.

The [Mods](../mods.md) page lists the mods we checked, each with its download and whether it leaves
anything in your save. Other mods are shared by their authors.

## Saves

RQ MOD keeps its saves apart from the original game's. Started from `xsystem4\xsystem4.exe`, it saves
in `xsystem4\Rance Quest\SaveData`. When the environment variable `XSYSTEM4_HOME` is set, the save
goes under that folder instead, and when only `HOME` is set, under `%HOME%\.xsystem4`. It never
writes the original game's save in `Documents\AliceSoft`.

Mods that add characters or items write them into the save like the game does, so keep a copy of the
save folder before you try a mod that adds content.

## The network box

If the game shows "Failed to send data to server (getserverversion)", click OK and play on: RQ MOD
does not connect to the game's online server, and nothing is lost. To stop the box, untick **Connect
to network** in Config, **Other 2**. It is off in a new install; a save copied from the original
game may have it on.

## A larger window

The game is drawn at 1024 by 768. In a larger window or in full screen it is scaled up with a filter,
which you pick in Config, **Other 2**, under **Magnification**: Standard (the game's own), Bicubic,
Nearest (square pixels), Lanczos or xBRZ (for pixel art). Each row's tip says how it looks. The same
five are in the menu of the window's title bar (a right click on it), with a mark on the one in use.
The Window tab has the game's two, Standard and Bicubic.

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
