---
layout: home

hero:
  name: RQ MOD
  text: Lua mods for Rance Quest Magnum
  tagline: Change the HUD, skills, items, characters, fights and quests at runtime, with no decompiling or recompiling of the game.
  image:
    src: /rq-mod.png
    alt: RQ MOD icon
  actions:
    - theme: brand
      text: Make your first mod
      link: /guide/first-mod
    - theme: alt
      text: Install
      link: /guide/install
    - theme: alt
      text: API reference
      link: /reference/

features:
  - title: Plain Lua 5.4
    details: A mod is a folder with an init.lua and a mod.json. Drop it into the mods folder and start the game.
  - title: The game's own pieces
    details: Hook the game's code, draw with its sprites and CGs, play its sounds and scenes, and build Config pages that look like the game's.
  - title: Mods that get along
    details: Dependencies, load order and conflicts in mod.json, and callbacks that every mod keeps instead of replacing each other's.
  - title: Editor support
    details: The release ships rq.lua, so VS Code's Lua extension completes every rq.* call and shows its documentation on hover.
---
