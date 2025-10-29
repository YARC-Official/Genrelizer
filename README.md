# Genrelizer
Have you ever tried to sort your rhythm game charts by genre, and found yourself trudging through inconsistent and hyperspecific genre labels that are useless for actual sorting?

<p align="center"><img width="350" alt="A partial list of chart genres, displaying 'Prog Death', 'Prog-Death-Core', 'Progressive', 'Progressive Death Metal', 'Progressive Death-Metal', and 'Progressive Deathcore'." src="https://github.com/user-attachments/assets/1dcf64b9-4494-43b8-a81e-8f281200f684" /></p>

_YARG_'s official content sticks to [a standardized list of genres](https://wiki.yarg.in/wiki/List_of_common_genre_names) and uses the `sub_genre` tag to get into the nitty-gritty details about each song's sound. However, charts from other sources aren't bound to the same system, and a lot of charters express a lot of detail in their `genre` tags without using the `sub_genre` tag. Genrelizer attempts to keep your library organized by mapping unofficial `genre` tags to a combination of an official `genre` tag and a mostly-untouched `sub_genre` tag that retains the charter's original intent.

For example, if a chart has `genre = 12-Bar Blues`, that's not an official genre. But Genrelizer recognizes it as a type of blues music, and this is the result:

<p align="center"><img width="347" height="41" alt="A genre field in the YARG music library sidebar, displaying `Blues, 12-Bar Blues`." src="https://github.com/user-attachments/assets/13a024bc-e048-476e-8f0a-ab682c59e181" /></p>

Genrelizer also performs some light copy-editing, so that `12 Bar Blues`, `Twelve Bar Blues`, and `Twelve-Bar Blues` all end up under the same `12-Bar Blues` subgenre. We've taken great pains to make sure that subtle naming variations get merged into one sortable value, but even the slightest difference in _sound_ between two subgenre names gets honored as two distinct things.


## What Genrelizer is _not_
* **Genrelizer is not a tool for making new charts; it's a tool for categorizing old ones.** If you're making new charts, you don't need to consult Genrelizer. Just pick an official _YARG_ genre, then add any level of detail you want in the `sub_genre` field. Genrelizer is here to clean up external content where the original charter isn't around anymore to clarify their intent; it doesn't need to get involved with new charts.

* **Genrelizer is not a definitive list of how subgenres _must_ be categorized.** Genrelizer's mappings are only meant to be best-guesses when all we have is a single, nonstandard genre name to work with. We know it might be controversial to see `Deathcore` under `Death/Black Metal`, but that doesn't mean we think that that's the _only_ way to categorize it. If you want your deathcore chart to be categorized under `Metalcore` instead, you can set the `genre` and `sub_genre` fields accordingly, and Genrelizer won't intervene. Heck, you could use `Bubblegum Pop` as a subgenre under `Grindcore` and Genrelizer wouldn't bat an eye. It's only when `genre` is unrecognized that Genrelizer starts making decisions about where things belong (with some minor exceptions; see below).

* **Genrelizer is not (usually) going to save you from updating your charts if _YARG_ adds a new official genre.** Say you have a polka chart, and you've set `genre = World / sub_genre = Polka`, but then we at the _YARG_ team decide that polka music deserves its own entire genre tag. Since your chart still has a legitimate `genre` tag (`World`), Genrelizer isn't going to touch it. If you want to make use of that new `Polka` genre, you're going to have to update the chart yourself.

  There are, however, two exceptions to this rule:

  * If a chart has `genre = Other`, Genrelizer _is_ willing to reassign it, since the charter seemingly wasn't satisfied with their options anyway. So while that `World > Polka` example won't be changed, a chart marked as `Other > Polka` _would_ be moved over to the new `Polka` genre.

  * Genrelizer _is_ willing to push around genres when it recognizes a genre/subgenre pair from Magma, the compiler used for _Rock Band_ songs, because Magma offers only a closed list of genres and subgenres. For example, Magma lacks a `Metalcore` genre, but it does have `Core` as a subgenre of `Metal`. If Genrelizer sees that _exact_ pairing, it assumes that the chart was made by a Magma user who would have used `Metalcore` had it been an option, and reinterprets the genre as such. This only applies to a precise match of `Metal > Core`, because that's a telltale sign of Magma; Genrelizer will _not_ recategorize `Metal > Metalcore`, nor `Heavy Metal > Core`.

## Contributing

**Genrelizer is crowdsourced!** There are always more subgenres to account for, and you're welcome to contribute. See these resources for more information:

* [How Genrelizer Works](docs/How%20Genrelizer%20Works.md)
* [Rules for Submissions](docs/Rules%20for%20Submissions.md)
* [Frequently-Asked Questions](docs/FAQ.md)

