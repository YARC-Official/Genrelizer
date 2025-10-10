# Genrelizer
Genrelizer is a community-sourced attempt to organize the various genres that are encoded in the rhythm game chart formats that _[YARG](https://github.com/YARC-Official/YARG)_ supports. While all official _YARG_ content is tagged using [our official list of genres](https://wiki.yarg.in/wiki/List_of_common_genre_names), and we recommend that custom charters do the same, charts from unofficial sources can encode any number of other genres. In particular, _Clone Hero_ customs use completely freeform text for their genres, and this can make them a nightmare to sort or filter in your music library. Thus, Genrelizer was born.

Genrelizer attempts to make sense of genre metadata that falls outside the scope of YARG's official genre list. Unofficial genres are mapped to official ones for sorting purposes, and the original values get preserved in the `sub_genre` field so the charter's original description of the song isn't lost.

For example, if a chart has `genre = 12-Bar Blues`, that's not an official genre. But Genrelizer recognizes it as a type of blues music, and this is the result:

<img width="347" height="41" alt="image" src="https://github.com/user-attachments/assets/13a024bc-e048-476e-8f0a-ab682c59e181" />

Genrelizer also performs some light copy-editing, so that `12 Bar Blues`, `Twelve Bar Blues`, and `Twelve-Bar Blues` all end up under the same `12-Bar Blues` subgenre. We've taken great pains to make sure that subtle naming variations get merged into one sortable value, but even the slightest difference in _sound_ between two subgenre names gets honored as two distinct things.


## What Genrelizer is _not_
* **Genrelizer is not a tool for making new charts; it's a tool for categorizing old ones.** If you're making new charts, you don't need to consult Genrelizer. Just pick an official _YARG_ genre, then add any level of detail you want in the `sub_genre` field. Genrelizer is here to clean up external content where the original charter isn't around anymore to clarify their intent; it doesn't need to get involved with new charts.

* **Genrelizer is not a definitive list of how subgenres _must_ be categorized.** Genrelizer's mappings are only meant to be best-guesses when all we have is a single, nonstandard genre name to work with. We know it might be controversial to see `Deathcore` under `Death/Black Metal`, but that doesn't mean we think that that's the _only_ way to categorize it. If you want your deathcore chart to be categorized under `Metalcore` instead, you can set the `genre` and `sub_genre` fields accordingly, and Genrelizer won't intervene. Heck, you could use `Bubblegum Pop` as a subgenre under `Grindcore` and Genrelizer wouldn't bat an eye. It's only when `genre` is unrecognized that Genrelizer starts making decisions.

* **Genrelizer is not (usually) going to save you from updating your charts if _YARG_ adds a new official genre.** Say you have a polka chart, and you've set `genre = World ; sub_genre = Polka`, but then we at the _YARG_ team decide that polka music deserves its own entire genre tag. Since your chart still has a legitimate `genre` tag (`World`), Genrelizer isn't going to touch it. If you want to make use of that new `Polka` genre, you're going to have to update the chart yourself.

  There are, however, two exceptions to this rule:

  * If a chart has `genre = Other`, Genrelizer _is_ willing to reassign it, since the charter seemingly wasn't satisfied with their options anyway. So while that `World > Polka` example won't be changed, a chart marked as `Other > Polka` _would_ be moved over to the new `Polka` genre.

  * Genrelizer _is_ willing to push around genres when it recognizes a genre/subgenre pair from Magma, the compiler used for _Rock Band_ songs, because Magma offers only a closed list of genres and subgenres. For example, Magma lacks a `Metalcore` genre, but it does have `Core` as a subgenre of `Metal`. If Genrelizer sees that _exact_ pairing, it assumes that the chart was made by a Magma user who would have used `Metalcore` had it been an option, and reinterprets the genre as such. This only applies to a precise match of `Metal > Core`, because that's a telltale sign of Magma; Genrelizer will _not_ recategorize `Metal > Metalcore`, nor `Heavy Metal > Core`.


## File Structure
Three JSON files, in the order listed below, drive the core behavior of Genrelizer.

### `genreAliases.json`
This file contains aliases for YARG's official genres, capturing things like style differences (e.g. `nu metal` to `nu-metal`), synonyms (e.g. `kids' music` to `children's music`), and other nonsemantic variations (e.g. `black/death metal` to `death/black metal`). These must strictly add _no_ additional meaning or specificity beyond the official genre name - even something as innoccuous as `alternative rock` is technically more specific than `alternative`, and should go under one of the other files.

### `subgenreAliases.json`
This file similarly aliases various nonsemantic variants of genre names, but for genres that are _not_ within YARG's official list (but which are handled in the following file). For example, `funeral doom metal` and `funeral doom` both refer to exactly the same style of music, so we alias the former to the latter as a style consistency effort.

### `subgenreMappings.json`
This is the real meat of Genrelizer, and it maps various unofficial genre names as subgenres of official genres - for example, `funeral doom` is not an official genre, but we recognize it as a subgenre of `doom metal`, which is. This file also optionally captures localization strings for mapped subgenre names (e.g. `rock alternativo` for `alternative rock` in Spanish).

Note that these mappings apply only to cases where the charter provides a nonstandard genre and no subgenre. If the charter provides both a genre and subgenre, we still consult these files for style consistency and localization, but we do not pass judgment on whether the subgenre belongs somewhere else. For example, while Genrelizer maps `deathcore` as a subgenre of `death/black metal`, a charter could mark a chart as `metalcore > deathcore` and it would not be moved to `death/black metal`.

The only exception to this is for certain specific genre/subgenre pairs that Magma (the compiler for RB CON files) supports. Magma users are forced to contend with a smaller list of genres than YARG's official list, but Magma associates each genre with a small list of predefined subgenres, some of which map cleanly to official YARG genres. For example, a Magma user who wishes to tag a metalcore song has to settle for `metal > core`, but clearly would have preferred to use YARG's `metalcore` genre if it had been available. If we see one of these exact pairings, we _do_ alias both the genre and subgenre, under the assumption that the chart was Magma-compiled and tagged under Magma's restrictions. Most Magma genre/subgenre pairs have minor aliases for style consistency, and some are left completely unchanged. For a list of pairs that are substantially affected, see [here](Telltale%20Magma%20Value%20Pairs.md).


## Frequently-Asked Questions

### Can I submit a pull request to add a new mapping or alias?
**Yes!** Genrelizer is meant to be crowdsourced, and we're always happy to receive new mappings and aliases from the community. Please make sure you follow these rules:
* Key strings should be all-lowercase. This doesn't strictly matter because all of Genrelizer's string comparisons are case-insensitive, but we keep it that way for readability
* Value strings should be in Title Case, because they will be displayed case-sensitively in some contexts in YARG
* Don't submit aliases between genre names that have _any_ semantic difference. Aliases have to be absolutely 100% synonymous to be valid
* _Do_ try to be exhaustive with aliases for nonsemantic differences. If a genre might hyphenate two words, alias the hyphenated version to the non-hyphenated one or vice-versa (your call, depending on which is more common). If there's a shortened version of a word (like "prog" for "progressive"), alias one to the other. When a genre name has multiple of these scenarios at once, create aliases for all the possible permutations (`progressive hip-hop`, `prog hip-hop`, `progressive hip hop`, `prog hip hop`...)
* Try to avoid subgenre names that are just adjectives - we prefer "alternative rock" over "alternative". You can bend this rule if a genre name is getting overly long, or if the adjective-only form is much more common in everyday use
* Check your JSON formatting!!!!


### Can I submit a pull request to change an existing mapping?
**We'd prefer you didn't.** We understand that genres can be subjective and controversial, and that some subgenre mappings can come down to a bit of a coin flip (is `industrial rock` `rock` or `industrial`?) or be considered sacreligious to some communities (`deathcore` living under `death/black metal` vs. `metalcore`). But the point of this repo isn't to lay down the law about what subgenres _absolutely belong_ where; we're just compiling a bunch of best-effort guesses to help make sense of the wild west that is freeform genre tags. If you feel so strongly about `deathcore` belonging under `metalcore`, you can set your `genre` and `subgenre` fields that way yourself and Genrelizer won't put up a fight.

That said, if you notice something that is _truly absolutely unambiguously_ a mistake and not just a divisive decision, then please do issue a correction through a pull request.


### What is the policy on potentially-problematic/offensive genres or genre names?
This breaks down to a few subcategories.

* Some genre names contain outdated terms that are now considered discriminatory or hateful, such as `g***y jazz` (containing a slur for the Romani people) and `d****land jazz` (containing an outdated name for the southern United States). In most cases (including both of those examples), the music itself is unproblematic and only suffers from an old name that's stuck around. In these cases, we want to support the music but don't want to display the unnecessary offensive terms, so we use the `subgenreAliases.json` file to replace them with modern, more-inclusive names.
* Other genre names might contain words that some would consider profane or distasteful, such as `porn groove`. Generally speaking, we don't feel the need to censor these names; charters should take such names into account when assigning family friendliness ratings to songs, so that they don't appear in the library when a user wishes to filter out offensive content.
* When it comes to genres that are _themselves_ deeply problematic, such as `nazi punk` or `national socialist black metal`, we do not acknowledge them in any way in Genrelizer's JSON files.
