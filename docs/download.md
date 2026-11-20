---
title: Download
description: Download RQ MOD, the mod loader for Rance Quest Magnum.
aside: false
outline: false
---

# Download RQ MOD

RQ MOD runs Rance Quest Magnum on its own engine, which loads mods. The game's own files stay as
they are, so you can still start the game without mods.

<RqManager />

<RqDownload />

## What you need

- **Windows.**
- **Rance Quest Magnum**, installed. RQ MOD ships nothing of the game: it runs your copy.

## Install

1. Download the zip above.
2. Extract it into the game folder, the one with `RanceQuest.exe`. It adds `xsystem4`, `lua`, `mods`
   and `RQ-MOD-README.txt`.
3. Start the game with `xsystem4\xsystem4.exe`.

The window title shows "RQ MOD" and the version. The [Install](guide/install.md) guide has the
details: where RQ MOD saves, the game's network box, and what to send when something goes wrong.

## What is in the zip

| File | What it is |
| --- | --- |
| `xsystem4\xsystem4.exe` | The game's engine with the mod loader. Start the game with it. |
| `mods\` | Empty: put mods here, one folder each. |
| `xsystem4\rance-browser.exe` | [Rance Browser](guide/file-browser.md), a window over the game's pictures, music and sounds. |
| `xsystem4\rq-scene-editor.exe` | [RQ Scene Editor](guide/scene-editor.md), a window that writes a mod's scene files and plays them in the game. |
| `xsystem4\api.html` | The API reference, offline. |
| `lua\rq.lua` | Definitions for mod makers' editors. |
| `RQ-MOD-README.txt` | These steps, in short. |

## Next: some mods

RQ MOD alone changes nothing in the game. Pick some on the [Mods](mods.md) page.

Older versions are on the [Releases page](https://github.com/RQ-Modding/RQ-Mod/releases) on
GitHub.
