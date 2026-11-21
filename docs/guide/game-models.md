# Game models in Blender

Rance Browser draws the game's 3D models as the game draws them, plays their motions, and exports
each one as a `.glb` file that Blender opens with its skeleton and animations. This page goes from
finding a model to looking at its mesh, UVs, skeleton, weights and animations in Blender. The words
are explained in [Learning 3D](./learning-3d).

The 3D models tab came with Rance Browser 1.2.0, in RQ MOD's package from loader 2.63.0.

Exported game models are for your own use, to learn from and to work beside. They belong to
AliceSoft: a mod ships its own work, never the game's files.

## 1. Find the model

Open Rance Browser (`rance-browser.exe` in the game's `xsystem4` folder) and its **3D models** tab.
The list holds the game's 647 models in four kinds: **Monsters and figures** (the monsters and the
party's small figures on the map), **Rooms** (the dungeon rooms), **Fight backgrounds** and
**Props** (chests, springs, doors and the like on the map). The search takes a folder, the game's
name, the English name, a prop's look, or a number: a MonsterInfo entry, a model number such as
100122, a fight background's or a map object's number.

![The 3D models tab: Rance's figure standing, its motions, its details and the Lua lines that use it](/3d/tab.png)

The Names tab also leads there: a monster's row shows its model, and **Open in the 3D tab** goes to
it with that monster's own motions.

![The Names tab's monsters, each with its model's picture](/3d/names.png)

## 2. Watch it move

- **Play** (Space) plays the chosen motion at the game's 30 frames a second; the buttons beside it
  (and Comma and Period) go to the first frame, a frame back, a frame on and the last frame. The
  speed list slows it down to a tenth.
- **The motion list** names each motion the game plays with the frames it shows and how
  (`待機 · shujinkou_taiki · 61 to 541, in a loop`), then each MOT file of the folder whole, and
  **None** for the rest pose. A monster with more than one MonsterInfo entry has an entry list too.
- **The view:** left drag turns the camera, right drag moves it, the wheel comes closer, a
  double-click goes back; **Reset the camera** starts again.
- **Under it** puts squares, black or white behind the model. **Outline**, **Light map**,
  **Bones** and, in a room, **Walk mesh** turn those off and on.
- **A monster in a fight:** the background list puts it on one of the game's fight backgrounds, at
  the size and place a fight gives it, with its **Shadow** and the game's **Fight camera**.
- **Save this frame as PNG...** saves the view at its size, see-through where nothing is drawn.

On the right, the details give the model's kind, folder, names, its MonsterInfo entries and fight
scale, what the model holds (meshes, bones, the walk mesh, its size, its pictures and MOT files),
and **From a mod**, the Lua lines that use it: `rq.monster.model` for a mod's monster on this
model, `rq.battle.start` for a fight on this background, `rq.dungeon.place` for an object with this
prop's look. **Its textures** shows the model's pictures; a click opens one in the 3D textures tab.

## 3. Export it

**Export the model as glTF (.glb)...** asks where to save, and writes one file: its meshes,
materials and pictures, its bones and weights, and one animation per MOT file. The status bar says
where it went.

From a command line, without the window:

```
rance-browser.exe --export shujinkou.glb --select shujinkou
rance-browser.exe --export models --kind chara
rance-browser.exe --export models --all
```

The first writes one model (`--select` takes a folder, `Kind/folder` such as `Etc/takarabako`, or
a model number). The others write every model of a kind (`chara`, `map`, `bg` or `etc`) or all 647
into the folder, each as `models\Kind\folder.glb`, with a report `export.json` beside them.

## 4. Install Blender

Blender is free, from [blender.org](https://www.blender.org/download/). This page was written with
Blender 5.2 LTS, the version the exported files are checked with; in another version a menu may sit
elsewhere. The installer and the portable zip both work.

## 5. Open the model

1. Start Blender and click outside the splash screen.
2. **Clear the scene.** Move the mouse over the 3D view, press **A** to select everything (the
   cube, the camera and the light), then **X** and **Delete**.
3. **Set 30 frames a second, before the import.** In the Properties editor on the right, open the
   **Output** tab (the printer): under **Format**, set **Frame Rate** to **30**; under **Frame
   Range**, set **Frame Start** to **0**. The game's animations run at 30 frames a second from frame
   0, and Blender places the keys by the frame rate when it imports: imported at its own 24, every
   key lands between frames.
4. **Import.** **File**, **Import**, **glTF 2.0 (.glb/.gltf)**, and pick the file. Blender's own
   settings are right. To also get the pictures the materials do not show (light maps, the texture
   animations' frames), tick **Import Unused Materials & Images** first.
5. **Look at it in colour.** Press **Z** over the 3D view and choose **Material Preview**.

![Rance's figure after the import, in Material Preview, with the Output tab's 30 fps and Frame Start 0 on the right](/3d/blender-import.png)

The grey balls are the bones' joints, the importer's own look for bones. The model faces Blender's
front: **Numpad 1** looks at it from the front, **Numpad 3** from the side and **Numpad 7** from
above. The middle mouse button turns the view, **Shift** with it moves the view, and the wheel
comes closer; **Numpad .** brings the selected object into view. Without a numpad, the axes at the
top right of the 3D view turn it with a click.

## 6. The mesh

In the Outliner (top right), open the model's armature to see its meshes. Click one, such as
`karada` (the body), move the mouse over the 3D view and press **Tab** for **Edit Mode**: its
points and edges show, and they can be selected and moved. **Tab** again goes back.

![Rance's body in Edit Mode, its points and edges drawn over the other meshes](/3d/blender-mesh.png)

The bones' balls can hide the mesh: click the armature's eye in the Outliner to hide it, or turn
**Bones** off in the **Overlays** menu (the two circles above the view).

## 7. The UVs and the pictures

Select a mesh and choose the **UV Editing** workspace (the tabs at the top): the mesh opens in Edit
Mode on the right. Press **A** over the 3D view on the right, then **A** over the left side: the
left side shows the mesh's UVs over its picture. If the picture is empty, pick it from the picture
list at the top of the left side.

![The UV Editing workspace: the body's UVs over its picture on the left, the body in Edit Mode on the right](/3d/blender-uv.png)

The game keeps many UVs a whole square away from their picture (the pictures repeat, so the game
shows the same); the export moves each mesh's UVs by whole squares onto its picture, so they line
up here.

## 8. The skeleton

Back in the **Layout** workspace, click the armature (in the Outliner, or a ball) and choose **Pose
Mode** in the menu at the top left of the 3D view. Click a ball and press **R** to turn that bone;
the mesh follows it. **Alt+R** puts it back.

![Pose Mode: the armature selected, its bones' balls over the figure on frame 20 of its walk](/3d/blender-pose.png)

## 9. The weights

Select a mesh in **Object Mode** and choose **Weight Paint**. In the Properties editor's **Object
Data** tab (the green triangle), **Vertex Groups** lists one group per bone; click one to see where
that bone pulls: red where it pulls fully, blue where it does not. To see one mesh alone, hide the
others and the armature (their eyes in the Outliner).

![Weight Paint on Rance's body for the bone Bip01 Spine1, the other meshes hidden](/3d/blender-weights.png)

## 10. The animations

Choose the **Animation** workspace. In the Dope Sheet at the bottom, switch **Dope Sheet** to
**Action Editor**, select the armature, and pick an action from the list beside it: one per MOT
file, named by its stem (`aruki`, `taiki`). **Space** plays it. In the timeline, set **End** to the
action's last frame (its frames minus one: 42 for `aruki`) to see it whole.

![The Animation workspace: the action aruki in the Action Editor, a key for every bone on every frame, the figure on frame 20](/3d/blender-actions.png)

The game often plays only some of an action's frames: the `rq_motions` property (below) says which,
as Rance Browser's motion list does.

## What Blender does not show

glTF has no word for some of what the game draws, so the export keeps it in custom properties,
which Blender shows under **Custom Properties** at the bottom of a tab:

| Where | Property | What it holds |
| --- | --- | --- |
| The armature (Object tab), or the model's top object if it has no bones | `rq_folder`, `rq_kind`, `rq_label`, `rq_label_en` | The model's folder, kind and names |
| | `rq_motions` | Each MOT: its action, its frames, the frames the game plays for each MonsterInfo entry and how, and its texture animation (which picture on each frame) |
| | `rq_entries` | Each MonsterInfo entry: name, model number, size and place in a fight, shadow |
| | `rq_look`, `rq_background`, `rq_object` | A prop's look for `rq.dungeon.place`, a fight background's number, a map object's number and frames |
| A mesh (Object Data tab) | `rq_name`, `rq_flags` | The game's name for the mesh and its settings as words (`nolighting`, `both`, `additive`, `no_edge`...) |
| | `rq_edge`, `rq_uv_scroll` | The outline's colour and size, the picture's scrolling |
| A material (Material tab) | `rq_material`, `rq_alpha` | The game's name, and how the game draws its see-through parts |
| | `rq_light_map`, `rq_frames` | The light map's picture, the texture animation's pictures |
| A bone (Bone tab) | `rq_bone_id` | The bone's number in the game's file |

- **The outline and the light map** are not drawn; their pictures come in with **Import Unused
  Materials & Images**.
- **See-through parts:** glTF draws a part either cut out or blended, while the game can do both
  on one material; `rq_alpha` says what the game does.
- **The points' colours** are kept as a colour attribute (Object Data tab, **Color Attributes**):
  the game multiplies the picture by them.
- **Texture animations and fades** are not played (see [Learning 3D](./learning-3d#texture-animation)).

## Rooms

A room has no bones and no animations. Its walk mesh is the object `collision`: hide it (its eye in
the Outliner) to see the room. Rooms are large: **Home** over the 3D view (**View**, **Frame All**)
brings the whole room into view.
