# rq.FlashBitmap

One bitmap of a game Flash file, as `rq.image.flash_bitmaps` lists it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The bitmap's id in the file. |
| `w` | `integer` | Width. |
| `h` | `integer` | Height. |
| `mod` | `boolean` | A mod's picture is on it. |
| `used` *(optional)* | `integer` | With `mod`: how many loads of the file got the mod's picture. |

## Used by

[`rq.image.flash_bitmaps`](../api/rq.image.md#rqimageflash_bitmaps)
