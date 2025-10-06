# Genrelizer
Genrelizer is a community-sourced collection of JSON data that attempts to neatly sort music genres and subgenres into the set of official genre tags that YARG officially recognizes.

# Motivations and Background
Most rhythm games tag their soundtracks with various genres. In most freeware games like _Clone Hero_ and _Phase Shift_, charters can enter any freeform text for their chart's genre. This is great for expressing the nuances of scenes and subgenres, but it creates a music library that can't be easily searched, sorted, or filtered by genre.

Meanwhile, most commercial games like _Rock Band_, _Guitar Hero_, and _Power Gig_ pull genre tags from a static list of a dozen or two recognized genres. This is obviously necessary for searchability and so on, but it can miss a lot of nuance and character that would come through with a hand-crafted genre description. The YARG Charting Team maintains a [list of official genres for YARG](https://wiki.yarg.in/wiki/List_of_common_genre_names), which builds off the set supported by _Rock Band 3_. 

_Rock Band Network_ charts contain hidden subgenre tags in addition to the regular genre tags. _Rock Band_ games never made use of these, and they were still chosen from a static list of subgenres for each genre rather than being freeform, but the YARG team decided to take that standard and expand it into a genre/subgenre system that achieves both searchability _and_ freeform expression.



# How It Works
Chart metadata files can contain both `genre` and `sub_genre` fields. Rather than use these fields as-is, our goal is to produce a sanitized `genre` value that corresponds directly to one of [YARG's official genres](https://wiki.yarg.in/wiki/List_of_common_genre_names), and optionally to also produce a `sub_genre` value that preserves any more-nuanced description of the song from the charter (possibly with some nonsemantic edits for style consistency). This section will notate a genre/subgenre pair with the format `[genre] > [subgenre]` (e.g. `rock > hard rock`), and an empty field as `{}` (e.g. `rock > {}` for the `rock` genre with no subgenre).

We generally expect that a chart will provide both fields, neither field, or only the `genre` field. If a chart provides only the `sub_genre` field, YARG will treat it as if it were the `genre` field instead (and as if the `sub_genre` field were blank).

Note that all values are converted to and returned as lowercase. Ingame, YARG renders all genres in all caps.

## Phase 0 - Early Exit Conditions
Before consulting Genrelizer, YARG checks for a few conditions that allow it to determine genre tags immediately.

### 

### Neither Field Populated
If both `genre` and `sub_genre` are blank, YARG immediately returns `unknown genre > {}`.

### Genre Is Standardized, Subgenre Is Blank or Redundant
If `genre` precisely matches one of YARG's official genres and `sub_genre` is either blank or an exact copy of `genre`, then YARG returns `[genre] > {}`.

### Telltale Magma Value Pairs
Magma, the compiler used to create RBN charts and RB customs, offers a static list of subgenres for each of RB's official genres. These subgenres exist in the resulting RBCON files, and often in `song.ini` files that were converted from RBCONs. For the most part, these values can be passed onto further phases as-is. However, there are some cases where YARG has introduced a new official genre tag that represents something that Magma offered as a subgenre. For example, RB did not support a `folk` genre but did support the `country > traditional folk` pair. If YARG finds a genre/subgenre pair that _precisely_ matches one of these Magma-generated value pairs that corresponds to a new YARG genre, it automatically converts that pair to a predefined YHARG genre/subgenre pair without consulting Genrelizer. This is analogous to how RB3 converted old RBN1.0 value pairs to its new genres, such as converting RBN1.0's `other > techno` pair to `pop/dance/electronic > techno`.

Because Magma values are a closed set, these conversions are hardcoded into YARG rather than being part of Genrelizer. They are listed in the following table.
| Magma Value Pair                       | Genrelizer Output                      |
|----------------------------------------|----------------------------------------|
| `country > traditional folk`           | `folk > traditional folk`              |
| `indie rock > noise`                   | `noise > noise rock`                   |
| `metal > alternative`                  | `heavy metal > alternative metal`      |
| `metal > black`                        | `death/black metal > black metal`      |
| `metal > metalcore`                    | `metalcore > {}`                       |
| `metal > death`                        | `death/black metal > death metal`      |
| `metal > hair`                         | `heavy metal > hair metal`             |
| `metal > industrial`                   | `industrial > industrial metal`        |
| `metal > metal`                        | `heavy metal > {}`                     |
| `metal > power`                        | `melodic/power metal > power metal`    |
| `metal > progressive`                  | `heavy metal > progressive metal`      |
| `metal > speed`                        | `speed/thrash metal > speed metal`     |
| `metal > thrash`                       | `speed/thrash metal > thrash metal`    |
| `metal > other`                        | `heavy metal > {}`                     |
| `new wave > synthpop`                  | `synthpop/electropop > synthpop`       |
| `pop/dance/electronic > ambient`       | `ambient/drone > ambient`              |
| `pop/dance/electronic > breakbeat`     | `d&b/breakbeat/jungle > breakbeat`     |
| `pop/dance/electronic > chiptune`      | `chiptune > {}`                        |
| `pop/dance/electronic > dance`         | `dance > {}`                           |
| `pop/dance/electronic > downtempo`     | `electronic > downtempo`               |
| `pop/dance/electronic > dub`           | `dubstep > {}`                         |
| `pop/dance/electronic > drum and bass` | `d&b/breakbeat/jungle > drum and bass` |
| `pop/dance/electronic > electronica`   | `electronic > electronica`             |
| `pop/dance/electronic > garage`        | `electronic > garage`                  |
| `pop/dance/electronic > hardcore edm`  | `hardcore edm > hardcore dance`        |
| `pop/dance/electronic > house`         | `house > {}`                           |
| `pop/dance/electronic > industrial`    | `industrial > {}`                      |
| `pop/dance/electronic > techno`        | `techno > {}`                          |
| `pop/dance/electronic > trance`        | `trance > {}`                          |
| `pop/dance/electronic > other`         | `electronic > {}`                      |
| `pop-rock > pop`                       | `pop > pop-rock`                       |
| `punk > pop-punk`                      | `pop-punk > {}`                        |
| `r&b/soul/funk > disco`                | `disco > {}`                           |
| `rock > folk`                          | `folk > folk rock`                     |
| `rock > rockabilly`                    | `rock & roll > rockabilly`             |
| `rock > rock and roll`                 | `rock & roll > {}`                     |
| `rock > surf`                          | `surf rock > {}`                       |
| `other > contemporary folk`            | `folk > contemporary folk`             |

All other Magma value pairs are passed onto the following phases for style consistency edits.



## Phase 1 - Genre Aliases
Assuming we did not hit one of the predefined Magma conversions, the first proper step of the process is to consult `genreAliases.json`. This file is meant to catch values that are semantically indistinguishable from official genres despite having some cosmetic difference. This tends to fall into three categories:

* Differences in punctuation and style, such as converting `nu metal` to `nu-metal`
* Alternative orderings of "slashed" genre names, such as converting `black/death metal` to `death/black metal`
* Cases where the YARG charting team decided to split up one of RB3's genres and created an "umbrella" genre with a new name to act as a bucket for legacy content. There are currently two such cases: `heavy metal` as the umbrella for the old `metal` genre, and `electronic` for `pop/dance/electronic`

**TODO - Still under construction**
