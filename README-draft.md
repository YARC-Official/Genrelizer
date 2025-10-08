# Genrelizer
Genrelizer is a community-sourced collection of JSON data that attempts to neatly sort music genres and subgenres into the set of official genre tags that YARG officially recognizes.

# Motivations and Background
Most rhythm games tag their soundtracks with various genres. In most freeware games like _Clone Hero_ and _Phase Shift_, charters can enter any freeform text for their chart's genre. This is great for expressing the nuances of scenes and subgenres, but it creates a music library that can't be easily searched, sorted, or filtered by genre.

Meanwhile, most commercial games like _Rock Band_, _Guitar Hero_, and _Power Gig_ pull genre tags from a static list of a dozen or two recognized genres. This is obviously necessary for searchability and so on, but it can miss a lot of nuance and character that would come through with a hand-crafted genre description. The YARG Charting Team maintains a [list of official genres for YARG](https://wiki.yarg.in/wiki/List_of_common_genre_names), which builds off the set supported by _Rock Band 3_. 

_Rock Band Network_ charts contain hidden subgenre tags in addition to the regular genre tags. _Rock Band_ games never made use of these, and they were still chosen from a static list of subgenres for each genre rather than being freeform, but the YARG team decided to take that standard and expand it into a genre/subgenre system that achieves both searchability _and_ freeform expression.


# File Structure
Three JSON files, in the order listed below, drive the core behavior of Genrelizer.

## `genreAliases.json`
This file contains aliases for YARG's official genres, capturing things like style differences (e.g. `nu metal` to `nu-metal`), synonyms (e.g. `kids' music` to `children's music`), and other nonsemantic variations (e.g. `black/death metal` to `death/black metal`). These must strictly add _no_ additional meaning or specificity beyond the official genre name - even something as innoccuous as `alternative rock` is technically more specific than `alternative`, and should go under one of the other files.

## `subgenreAliases.json`
This file similarly aliases various nonsemantic variants of genre names, but for genres that are _not_ within YARG's official list (but which are handled in the following file). For example, `funeral doom metal` and `funeral doom` both refer to exactly the same style of music, so we alias the former to the latter as a style consistency effort.

## `subgenreMappings.json`
This is the real meat of Genrelizer, and it maps various unofficial genre names as subgenres of official genres - for example, `funeral doom` is not an official genre, but we recognize it as a subgenre of `doom metal`, which is. This file also optionally captures localization strings for mapped subgenre names (e.g. `rock alternativo` for `alternative rock` in Spanish).

Note that these mappings apply only to cases where the charter provides a nonstandard genre and no subgenre. If the charter provides both a genre and subgenre, we still consult the first two files for style consistency, but we do not pass judgment on whether the subgenre belongs somewhere else. For example, while Genrelizer maps `deathcore` as a subgenre of `death/black metal`, a charter could mark a chart as `metalcore > deathcore` and it would not be aliased to `death/black metal`.

The only exception to this is for certain specific genre/subgenre pairs that Magma (the compiler for RB CON files) supports. Magma users are forced to contend with a smaller list of genres than YARG's official list, but each genre is associated with a small list of predefined subgenres, some of which map cleanly to official YARG genres. For example, a Magma user who wishes to tag a metalcore song has to settle for `metal > metalcore`, but clearly would have preferred to use YARG's `metalcore` genre if it had been available. If we see one of these exact pairings, we _do_ alias both the genre and subgenre, under the assumption that the chart was Magma-compiled and tagged under Magma's restrictions. Most Magma genre/subgenre pairs are not aliased; for a list of those that are, see [here](Telltale%20Magma%20Value%20Pairs.md).


