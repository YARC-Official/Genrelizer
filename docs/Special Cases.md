# Special Cases
Genrelizer contains some special cases for maximum compatibility with legacy charts that were originally designed for RB games. Because the set of RB genres is closed and finite, these cases are hardcoded into YARG rather than being part of Genrelizer. They are documented in the following sections for reference, but **this file does not drive actual Genrelizer behavior. Do not submit a pull request for this file.**


## Telltale Magma Value Pairs
Users of Magma (the compiler for RB CON files) are forced to contend with a smaller list of genres than YARG's official list. However, Magma associates each genre with a small list of predefined subgenres, some of which map cleanly to official YARG genres.

For example, a Magma user who wishes to tag a metalcore song has to settle for `metal > core`, but clearly would have preferred to use YARG's `metalcore` genre if it had been available. If we see one of these exact pairings, we alias both the genre and subgenre, under the assumption that the chart was Magma-compiled and tagged under Magma's restrictions.

| Magma Value Pair                       | Genrelizer Output                      |
|----------------------------------------|----------------------------------------|
| `country > traditional folk`           | `folk > traditional folk`              |
| `indie rock > noise`                   | `noise > noise rock`                   |
| `metal > alternative`                  | `heavy metal > alternative metal`      |
| `metal > black`                        | `death/black metal > black metal`      |
| `metal > core`                         | `metalcore > {}`                       |
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
| `reggae/ska > reggae`                  | `reggae > {}`                          |
| `reggae/ska > ska`                     | `ska > {}`                             |
| `reggae/ska > other`                   | [special case; see below]              |
| `rock > folk`                          | `folk > folk rock`                     |
| `rock > rockabilly`                    | `rock & roll > rockabilly`             |
| `rock > rock and roll`                 | `rock & roll > {}`                     |
| `rock > surf`                          | `surf rock > {}`                       |
| `other > contemporary folk`            | `folk > contemporary folk`             |


## Reggae/Ska

RB3 introduced the `Reggae/Ska` genre tag, which fuses two genres that are historically related but in practice are usually quite different from each other. The _YARG_ team decided to split this tag into separate `Reggae` and `Ska` genres, but this presents the problem of deciding how to alias a chart that has RB's combined tag.

Most Magma-compiled `Reggae/Ska` charts do not have this problem, because they have either the `Reggae` or `Ska` subgenre tag, which is handled as described above. However, this leaves behind 3 sets of problematic charts:

1) The 33 Harmonix-authored (and thus subgenreless) RB charts that use `Reggae/Ska`
2) Any Magma-generated charts that use the `Reggae/Ska > Other` subgenre
3) Any charts from any other source that use `Reggae/Ska` with no subgenre (or `Other` as the subgenre)

Sets 2 and 3 are likely negligible, so our solution focuses on the Harmonix-authored charts. Of these, 23 are clear-cut reggae songs (22 of which are by Bob Marley and the Wailers, plus one by UB40), while the rest are unambiguously ska. Thus, _YARG_ includes a hardcoded artist name check that it runs against any `Reggae/Ska > {}` or `Reggae/Ska > Other` charts. If the artist contained `Bob Marley` or is exactly `UB40`, the chart is categorized as `Reggae`; otherwise, it defaults to `Ska`.

This correctly handles all of set 1. `Ska` is also a decent assumption for the other two, since ska is generally much more popular to chart than reggae, and the substring check against `Bob Marley` rather than a hard comparison against `Bob Marley and the Wailers` makes it a little extra flexible for catching reggae music.
