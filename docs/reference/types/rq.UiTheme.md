# rq.UiTheme

`since 1.7.0` `changed 2.6.0`

A look for the kit: pieces, text styles, colors and sounds.

`rq.uikit.themes.config` is the look of the game's Config screen; it holds Config's pieces only.
`rq.uikit.themes.hub` (2.6.0) is Config's theme with the hub's pieces added: with it in use,
`rq.uikit.button` is the castle's grey button and `rq.uikit.list` has the game's scroll bar.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `label` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | Label text. |
| `dim` | `{r: integer, g: integer, b: integer}` | The grey-green of Config's Low and High. |
| `page` | [`rq.UiPiece`](rq.UiPiece.md) | A Config page. |
| `block` | [`rq.UiPiece`](rq.UiPiece.md) | The 3D tab's dark block. |
| `button` | [`rq.UiPiece`](rq.UiPiece.md) | A button. |
| `button_text` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | Button text. |
| `button_cover` | `{r: integer, g: integer, b: integer, a: integer}` | The cover that pulses over a hovered button. |
| `tab` | `{normal:` [`rq.UiPiece`](rq.UiPiece.md) `, hover:` [`rq.UiPiece`](rq.UiPiece.md) `, current:` [`rq.UiPiece`](rq.UiPiece.md) `}` | The tabs. |
| `tab_text` | `{normal:` [`rq.HudTextStyle`](rq.HudTextStyle.md) `, hover:` [`rq.HudTextStyle`](rq.HudTextStyle.md) `, current:` [`rq.HudTextStyle`](rq.HudTextStyle.md) `}` | Tab text. |
| `check_frame` | [`rq.UiPiece`](rq.UiPiece.md) | The checkbox frame. |
| `check_mark` | [`rq.UiPiece`](rq.UiPiece.md) | The checkmark. |
| `hover_bar` | [`rq.UiPiece`](rq.UiPiece.md) | The bar over a hovered row. |
| `track` | [`rq.UiPiece`](rq.UiPiece.md) | The slider track. |
| `knob` | [`rq.UiPiece`](rq.UiPiece.md) | The slider knob. |
| `knob_hot` | [`rq.UiPiece`](rq.UiPiece.md) | The knob while hovered or dragged. |
| `list_text` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | List row text. |
| `list_current` | `{r: integer, g: integer, b: integer}` | The color of the chosen list row. |
| `scrollbar` | `{r: integer, g: integer, b: integer, a: integer}` | A list's scroll bar. |
| `sound` | `{hover?: integer, click?: integer, error?: integer}` | Sound numbers; nil plays none. |
| `button_style` *(optional)* | `string` | The button style `rq.uikit.button` draws without `opts.style`. The hub theme's is "large". Since 2.6.0. |
| `tabs_style` *(optional)* | `string` | The tabs style `rq.uikit.tabs` draws without `opts.style`. Since 2.6.0. |
| `styles` *(optional)* | `{button?: table<string,` [`rq.UiButtonStyle`](rq.UiButtonStyle.md) `>, tabs?: table<string,` [`rq.UiTabsStyle`](rq.UiTabsStyle.md) `>}` | Button and tabs styles by name. A name the theme in use lacks is taken from `themes.hub`. Since 2.6.0. |
| `castle` *(optional)* | `table` | Rance Castle's room row: `base`, `frame`, `new` (pieces) and `marks` (`heart`, `run`: pieces with their `x`, `y`). Since 2.6.0. |
| `quest` *(optional)* | `table` | A quest row: `normal`, `hover`, `box` (pieces), `no`, `name`, `mark` (text styles), `name_fit`, `current` (a color), `gap`. Since 2.6.0. |
| `rack` *(optional)* | `table` | Frostbuy's rack tile: `w`, `h`, `outer`, `line`, `fill` (colors), `text`, `fit`. Since 2.6.0. |
| `sort` *(optional)* | `table` | The sort column: `back`, `base`, `normal`, `hover`, `current` (pieces), `text`, `fit`, `fit_w`. Since 2.6.0. |
| `scroll` *(optional)* | [`rq.UiScrollPieces`](rq.UiScrollPieces.md) | The game's scroll bar. A theme with it gives `rq.uikit.list` that bar. Since 2.6.0. |
| `close` *(optional)* | `{normal:` [`rq.UiPiece`](rq.UiPiece.md) `, hover:` [`rq.UiPiece`](rq.UiPiece.md) `}` | The close button. Since 2.6.0. |
| `hub_page` *(optional)* | `table` | A page over the hub: `x`, `y`, `w`, `h`, `dim`, `outer`, `line` (colors), `title` (a text style), `pad`. Since 2.6.0. |
| `options` *(optional)* | `table` | The choice menu's look for `rq.uikit.options`: `base` (the menu's background), `sep`, `panels` (the text row's pieces for 1 to 3 lines, with `ph`, their height), `text`, `text_fit` (text styles). Since 2.7.0; `comment` gone in 2.13.0 (the comment is the game's window). |
| `vault` *(optional)* | `table` | The vault's item rows: `rows` (the backgrounds by style: vault, storage, and since 2.9.0 shop and equip), `name`, `info`, `number`, `level_text`, `count` (text styles), `name_fit`, `info_fit`, `level_fit`, `level`, `locked`, `count_box`, `stock_box` (2.9.0) (pieces), `rank` (the first rank badge CG), `kinds` (the kind marks' CGs), `current` (a color), `buttons` (the row buttons' pieces and places), `gold` (the gold digits), `price` (2.9.0: the shop's price place, cells and gap). Since 2.8.0. |
| `item_window` *(optional)* | `table` | The Quest Storage window for `rq.uikit.item_window`: `top`, `middle`, `last`, `foot` (pieces of CG 11335; `foot` closes a window of one row), `w`, `cols`, `cell`, `tile_x`, `tile_y`, `band`, `close_x`, `close_y`, `x`, `y`, `bottom` (where a taller window ends), `title`, `page`, `empty` (text styles), `title_x`. Since 2.32.0. |
| `section` *(optional)* | `table` | The quest panel's heading for `rq.uikit.section`: `left`, `middle`, `right`, `box` (pieces of CG 11014), `w`, `h`, `text_x`, `box_x`, `box_y`, `box_right`, `text` (the heading's gold), `fit` (as a button style's), `body` (the panel's own text style, for text in the box). Since 2.32.0. |
| `balloon` *(optional)* | `table` | Frostbuy's balloon for `rq.uikit.balloon`: `top`, `base`, `left`, `tail`, `right` (pieces of CG 11110), `w`, `h`, `edge`, `tail_x`, `tail_w`, `tail_h`, `pad_x`, `pad_y`, `pad_r`, `line_h`, `text`. Since 2.32.0. |
| `parchment` *(optional)* | `table` | Trivia's paper for `rq.uikit.page`'s `style = "parchment"`: `paper` (a piece of CG 20001), `x`, `y`, `w`, `h`, `pad_x`, `pad_y`, `pad_b`, `close_x`, `close_y`, `text` (the brown text, also the labels inside), `dim`, `title_h`. Since 2.32.0. |
| `filters` *(optional)* | `table` | The vault's filter column: `back`, `backs` (2.9.0: the column's grey by style), `cats`, `classes`, `lock`, `equip` (2.9.0) (each with `lit` and `dim` pieces), and `sub` (the sub-filters' panel: `base`, `title`, and by category `title`, `cgs`, `names`). Since 2.8.0. |

## Used by

[`rq.uikit`](../api/rq.uikit.md), [`rq.uikit.copy_theme`](../api/rq.uikit.md#rquikitcopy_theme), [`rq.uikit.use`](../api/rq.uikit.md#rquikituse)
