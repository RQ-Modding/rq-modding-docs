---
description: RQ Manager installs RQ MOD and its mods, keeps them up to date, turns mods off and on, and puts the last version back.
---

# RQ Manager

RQ Manager installs RQ MOD and the mods you pick in your copy of Rance Quest Magnum, keeps them up to
date, turns mods off and on, and puts the last version back when an update goes wrong. It reads the
same list as the [Mods](../mods.md) page, so it offers the mods we checked, each at its checked
release.

It is a public beta, like RQ MOD, and runs on Windows.

## Get it

1. Download `rq-manager-*.zip` from the [Download](../download.md) page.
2. Unzip it into the game folder (the one with `RanceQuest.exe`). It makes a folder `RQ Manager`
   there, and the Manager finds the game at once. Unzipped anywhere else, it asks for the game folder
   the first time and remembers it.
3. Start `rq-manager.exe` in the folder `RQ Manager`. There is nothing to install.

When a newer RQ Manager is out, a bar at the top of its window offers it. One click, and it starts
again as the new version.

## The RQ MOD page

- **Install RQ MOD**, or **Update** when a newer release is out.
- **Play** starts the game with RQ MOD (`xsystem4\xsystem4.exe`).
- **Desktop shortcut** puts a shortcut to it on your desktop.
- **Back to the last version** puts back the RQ MOD that the last update replaced.
- **Remove RQ MOD** takes out the files RQ MOD's zip put in. Your mods, logs and saves stay, and the
  game runs without RQ MOD as before.

Below them: how many mods are installed and on, **Update all**, and where your saves are.

## The Mods page

Every mod of the list and every mod you have, in one table, with a search box and the
[tags](../mods.md) as filters. Pick a mod to see what it does, what it needs, whether it leaves
anything in your save, and its buttons:

| Button | What it does |
| --- | --- |
| Install, Update | Downloads the release, checks it, and puts it in `mods` |
| Turn off, Turn on | Moves the mod's folder to `rq-manager\off` and back. The game does not load a mod that is off; its settings stay |
| Remove | Takes the mod's folder out. Its settings and saved data stay |
| Back to the last version | Puts back what the last update or removal replaced |
| Read me, Changes | The mod's README and changelog, in your browser |

Each change asks first when it does more than you clicked:

- a mod that needs a newer RQ MOD updates RQ MOD first;
- a mod that needs another mod brings it in, or turns it on;
- two mods that do not work together are never on together: the other one is turned off;
- turning off or removing a mod that another one needs turns that one off too.

Restart the game after a change: mods load when the game starts.

## What it keeps safe

- **Your saves.** The Manager never writes or removes them. Before a mod that leaves things in the
  save is installed or removed, it offers a copy of the whole save folder first, in
  `rq-manager\save-copies` (it never deletes these copies).
- **Your RQ MOD settings.** An update keeps every value of your `xsystem4\config.json` and adds the
  new settings.
- **What a mod wrote in its own folder** stays when the mod is updated.
- **The game's own files** are never touched.
- **A change stopped halfway** (the PC turned off, the network gone) is finished the next time the
  Manager starts: each change unpacks into a side folder first and keeps a list of its moves until
  the end.

It downloads only over HTTPS, only from GitHub, and only the files the list names. Each one is
checked against the list's size and SHA-256 before anything is unpacked, and a zip that would put a
file outside its own folder is refused.

Close the game before you change anything: while the game, Rance Browser or `rqmod-ctl` runs from
that folder, the Manager waits.

## Mods you installed by hand

They are listed too:

- **A mod of the list**, put in by hand, shows as *installed by hand*. The Manager can update it; the
  first update keeps every file the new release does not have.
- **A mod that is not in the list** shows as *not in the catalog*. The Manager can turn it off and on
  and remove it, never update it.
- **A zip unpacked one folder too deep** (`mods\camera-zoom\camera-zoom\mod.json`) is named, with a
  button that moves it up.
- **Two folders with one mod's id** are named: the game loads neither, so remove one.

## Where it keeps things

In the game folder, beside `mods`:

| `rq-manager\` | What it holds |
| --- | --- |
| `state.json` | What the Manager installed: RQ MOD's version and files, each mod's version, folder and files |
| `off\` | The mods turned off |
| `backup\` | The last version of RQ MOD and of each mod, for Back to the last version |
| `save-copies\` | The copies of the save folder |
| `rq-manager.log` | What it did. Attach it to a bug report |

Its own settings (the game folders it was used on) are in `%LOCALAPPDATA%\RQ Manager`. To stop using
the Manager, delete its folder `RQ Manager` and that folder; the game folder's `rq-manager` can go too
(keep `off` if a mod you want is in it, and `save-copies` if you want the copies).

## When something goes wrong

| It says | What to do |
| --- | --- |
| The Manager cannot write in the folder | The game is in a folder Windows protects, such as `Program Files`. RQ MOD writes its logs and saves there too: move the game to a folder of yours, such as `C:\Games`, and pick it again. |
| `xsystem4.exe` runs from this folder | Close the game (or Rance Browser), then try again. |
| The site did not answer | No network, or GitHub is down. The list read last time is shown, with its date; turning off and on, removing and going back still work. |
| A file does not match the list's SHA-256 | The download was damaged or changed. Nothing was written. Try again later; if it stays, tell us. |
| The catalog is of a format this RQ Manager cannot read | Update RQ Manager (the bar at the top offers it). |
| A change stopped halfway could not be finished | Start the Manager again. If it says so again, `rq-manager\rq-manager.log` says why: send it to us. |

The [Discord server](https://discord.gg/maCKqfTGne) is the place to ask.

## The command line

The same work with no window, for scripts:

```text
rq-manager [--game DIR] [--yes] [--no-save-copy] COMMAND [ID...]
    status                       JSON: RQ MOD, each mod and its state
    install-rqmod | update-rqmod | remove-rqmod
    install ID... | update ID... | update-all
    off ID... | on ID... | remove ID... | restore ID|rqmod | fix FOLDER
    update-manager
```

A change that would ask a question in the window ends with exit code 3 and prints the question;
`--yes` answers yes. Exit codes: 0 done, 1 failed, 2 a wrong command line, 3 asks first.
`rq-manager --help` lists the rest.
