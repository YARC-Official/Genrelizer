# Genrelizer
Genrelizer is a community-sourced collection of JSON data that attempts to neatly sort music genres and subgenres into the set of official genre tags that YARG officially recognizes.

# Motivations and Background
Most rhythm games tag their soundtracks with various genres. In most freeware games like _Clone Hero_ and _Phase Shift_, charters can enter any freeform text for their chart's genre. This is great for expressing the nuances of scenes and subgenres, but it creates a music library that can't be easily searched, sorted, or filtered by genre.

Meanwhile, most commercial games like _Rock Band_, _Guitar Hero_, and _Power Gig_ pull genre tags from a static list of a dozen or two recognized genres. This is obviously necessary for searchability and so on, but it can miss a lot of nuance and character that would come through with a hand-crafted genre description. The YARG Charting Team maintains a [list of official genres for YARG](https://wiki.yarg.in/wiki/List_of_common_genre_names), which builds off the set supported by _Rock Band 3_. 

_Rock Band Network_ charts contain hidden subgenre tags in addition to the regular genre tags. _Rock Band_ games never made use of these, and they were still chosen from a static list of subgenres for each genre rather than being freeform, but the YARG team decided to take that standard and expand it into a genre/subgenre system that achieves both searchability _and_ freeform expression. YARG charters are encouraged to include both an official `genre` tag and a freeform `sub_genre` tag in their chart metadata, and YARG will honor their choices (aside from a few style tweaks and edge cases). But for the wealth of existing charts that don't fit neatly into YARG's system, Genrelizer steps in to make sense of it all.


# File Structure
Three JSON files, in the order listed below, drive the core behavior of Genrelizer.

## `genreAliases.json`
This file contains aliases for YARG's official genres, capturing things like style differences (e.g. `nu metal` to `nu-metal`), synonyms (e.g. `kids' music` to `children's music`), and other nonsemantic variations (e.g. `black/death metal` to `death/black metal`). These must strictly add _no_ additional meaning or specificity beyond the official genre name - even something as innoccuous as `alternative rock` is technically more specific than `alternative`, and should go under one of the other files.

## `subgenreAliases.json`
This file similarly aliases various nonsemantic variants of genre names, but for genres that are _not_ within YARG's official list (but which are handled in the following file). For example, `funeral doom metal` and `funeral doom` both refer to exactly the same style of music, so we alias the former to the latter as a style consistency effort.

## `subgenreMappings.json`
This is the real meat of Genrelizer, and it maps various unofficial genre names as subgenres of official genres - for example, `funeral doom` is not an official genre, but we recognize it as a subgenre of `doom metal`, which is. This file also optionally captures localization strings for mapped subgenre names (e.g. `rock alternativo` for `alternative rock` in Spanish).

Note that these mappings apply only to cases where the charter provides a nonstandard genre and no subgenre. If the charter provides both a genre and subgenre, we still consult these files for style consistency and localization, but we do not pass judgment on whether the subgenre belongs somewhere else. For example, while Genrelizer maps `deathcore` as a subgenre of `death/black metal`, a charter could mark a chart as `metalcore > deathcore` and it would not be moved to `death/black metal`.

The only exception to this is for certain specific genre/subgenre pairs that Magma (the compiler for RB CON files) supports. Magma users are forced to contend with a smaller list of genres than YARG's official list, but Magma associates each genre with a small list of predefined subgenres, some of which map cleanly to official YARG genres. For example, a Magma user who wishes to tag a metalcore song has to settle for `metal > core`, but clearly would have preferred to use YARG's `metalcore` genre if it had been available. If we see one of these exact pairings, we _do_ alias both the genre and subgenre, under the assumption that the chart was Magma-compiled and tagged under Magma's restrictions. Most Magma genre/subgenre pairs have minor aliases for style consistency, and some are left completely unchanged. For a list of pairs that are substantially affected, see [here](Telltale%20Magma%20Value%20Pairs.md).


# Frequently-Asked Questions

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
