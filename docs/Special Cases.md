# Special Cases
Genrelizer contains some special cases for maximum compatibility with legacy charts that were originally designed for RB games. Because the set of RB genres is closed and finite, these cases are hardcoded into YARG rather than being part of Genrelizer. They are documented in the following sections for reference, but **this file does not drive actual Genrelizer behavior. Do not submit a pull request for this file.**


## Telltale Magma Value Pairs
Users of Magma (the compiler for RB CON files) are forced to contend with a smaller list of genres than YARG's official list. However, Magma associates each genre with a small list of predefined subgenres, some of which map cleanly to official YARG genres, and others of which are out of sync with Genrelizer's style guide.

### Mappings to New Genres
Some Magma subgenres map cleanly to official YARG genres. For example, a Magma user who wishes to tag a metalcore song has to settle for `metal > core`, but clearly would have preferred to use YARG's `metalcore` genre if it had been available. If we see one of these exact pairings, we alias both the genre and subgenre, under the assumption that the chart was Magma-compiled and tagged under Magma's restrictions.

| Magma Value Pair                       | Genrelizer Output                      | Notes                                                                                                                        |
|----------------------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `country > traditional folk`           | `folk > traditional folk`              |                                                                                                                              |
| `indie rock > math rock`               | `math rock > {}`                       |                                                                                                                              |
| `indie rock > noise`                   | `noise > noise rock`                   | It's unlikely that a Magma user seeking to tag a pure noise track would use `indie rock`, so assume this is rock-leaning     |
| `metal > alternative`                  | `heavy metal > alternative metal`      |                                                                                                                              |
| `metal > black`                        | `death/black metal > black metal`      |                                                                                                                              |
| `metal > core`                         | `metalcore > {}`                       |                                                                                                                              |
| `metal > death`                        | `death/black metal > death metal`      |                                                                                                                              |
| `metal > hair`                         | `heavy metal > hair metal`             | Magma users had the option of using `glam` and passed it up, so assume hair is a secondary descriptor and prioritize `metal` |
| `metal > industrial`                   | `industrial > industrial metal`        |                                                                                                                              |
| `metal > metal`                        | `heavy metal > {}`                     |                                                                                                                              |
| `metal > power`                        | `melodic/power metal > power metal`    |                                                                                                                              |
| `metal > progressive`                  | `heavy metal > progressive metal`      | Magma users had the option of using `prog` and passed it up, so assume prog is a secondary descriptor and prioritize `metal` |
| `metal > speed`                        | `speed/thrash metal > speed metal`     |                                                                                                                              |
| `metal > thrash`                       | `speed/thrash metal > thrash metal`    |                                                                                                                              |
| `metal > other`                        | `heavy metal > {}`                     |                                                                                                                              |
| `new wave > synthpop`                  | `synthpop/electropop > synthpop`       |                                                                                                                              |
| `pop/dance/electronic > ambient`       | `ambient/drone > ambient`              | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > breakbeat`     | `d&b/breakbeat/jungle > breakbeat`     | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > chiptune`      | `chiptune > {}`                        | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > dance`         | `dance > {}`                           | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > downtempo`     | `electronic > downtempo`               | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > dub`           | `dubstep > {}`                         | Exclusive to Magma v2. In the context of electronic music, this is more likely to refer to dubstep than to dub reggae        |
| `pop/dance/electronic > drum and bass` | `d&b/breakbeat/jungle > drum and bass` | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > electronica`   | `electronic > electronica`             | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > garage`        | `electronic > garage`                  | Exclusive to Magma v2. In the context of electronic music, "garage" is a noun (UK Garage), not an adjective (Garage Rock)    |
| `pop/dance/electronic > hardcore edm`  | `hardcore edm > hardcore dance`        | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > house`         | `house > {}`                           | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > industrial`    | `industrial > {}`                      | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > techno`        | `techno > {}`                          | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > trance`        | `trance > {}`                          | Exclusive to Magma v2                                                                                                        |
| `pop/dance/electronic > other`         | `electronic > {}`                      | Exclusive to Magma v2                                                                                                        |
| `pop-rock > disco`                     | `disco > {}`                           | Exclusive to Magma v1                                                                                                        |
| `pop-rock > motown`                    | `r&b/soul/funk > motown`               | Exclusive to Magma v1                                                                                                        |
| `pop-rock > pop`                       | `pop > pop-rock`                       |                                                                                                                              |
| `pop-rock > rhythm and blues`          | `r&b/soul/funk > rhythm and blues`     | Exclusive to Magma v1                                                                                                        |
| `pop-rock > soul`                      | `r&b/soul/funk > soul`                 | Exclusive to Magma v1                                                                                                        |
| `punk > pop-punk`                      | `pop-punk > {}`                        |                                                                                                                              |
| `r&b/soul/funk > disco`                | `disco > {}`                           | Exclusive to Magma v2                                                                                                        |
| `reggae/ska > reggae`                  | `reggae > {}`                          | Exclusive to Magma v2                                                                                                        |
| `reggae/ska > ska`                     | `ska > {}`                             | Exclusive to Magma v2                                                                                                        |
| `reggae/ska > other`                   | [special case; see below]              | Exclusive to Magma v2                                                                                                        |
| `rock > folk rock`                     | `folk > folk rock`                     |                                                                                                                              |
| `rock > funk`                          | `r&b/soul/funk > funk`                 | Exclusive to Magma v1                                                                                                        |
| `rock > psychedelic`                   | `psychedelic > psychedelic rock`       |                                                                                                                              |
| `rock > reggae`                        | `reggae > {}`                          | Exclusive to Magma v1                                                                                                        |
| `rock > rockabilly`                    | `rock & roll > rockabilly`             |                                                                                                                              |
| `rock > rock and roll`                 | `rock & roll > {}`                     |                                                                                                                              |
| `rock > ska`                           | `ska > {}`                             | Exclusive to Magma v1                                                                                                        |
| `rock > surf`                          | `surf rock > {}`                       |                                                                                                                              |
| `urban > alternative rap`              | `hip-hop/rap > alternative rap`        | Exclusive to Magma v1                                                                                                        |
| `urban > downtempo`                    | `electronic > downtempo`               | Exclusive to Magma v1                                                                                                        |
| `urban > drum and bass`                | `dnb/breakbeat/jungle > drum and bass` | Exclusive to Magma v1                                                                                                        |
| `urban > dub`                          | `reggae > dub`                         | Exclusive to Magma v1. Outside the context of electronic music, this is more likely to refer to dub reggae than to dubstep   |
| `urban > electronica`                  | `electronic > electronica`             | Exclusive to Magma v1                                                                                                        |
| `urban > gangsta`                      | `hip-hop/rap > gangsta rap`            | Exclusive to Magma v1                                                                                                        |
| `urban > hardcore dance`               | `hardcore edm > hardcore dance`        | Exclusive to Magma v1                                                                                                        |
| `urban > hardcore rap`                 | `hip-hop/rap > hardcore rap`           | Exclusive to Magma v1                                                                                                        |
| `urban > hip hop`                      | `hip-hop/rap > hip-hop`                | Exclusive to Magma v1                                                                                                        |
| `urban > industrial`                   | `industrial > {}`                      | Exclusive to Magma v1                                                                                                        |
| `urban > old school hip hop`           | `hip-hop/rap > oldschool hip-hop`      | Exclusive to Magma v1                                                                                                        |
| `urban > rap`                          | `hip-hop/rap > rap`                    | Exclusive to Magma v1                                                                                                        |
| `urban > trip hop`                     | `hip-hop/rap > trip hop`               | Exclusive to Magma v1                                                                                                        |
| `urban > underground rap`              | `hip-hop/rap > underground rap`        | Exclusive to Magma v1                                                                                                        |
| `other > ambient`                      | `ambient/drone > {}`                   | Exclusive to Magma v1                                                                                                        |
| `other > breakbeat`                    | `dnb/breakbeat/jungle > breakbeat`     | Exclusive to Magma v1                                                                                                        |
| `other > chiptune`                     | `chiptune > {}`                        | Exclusive to Magma v1                                                                                                        |
| `other > classical`                    | `classical > {}`                       | Exclusive to Magma v1                                                                                                        |
| `other > contemporary folk`            | `folk > contemporary folk`             |                                                                                                                              |
| `other > dance`                        | `dance > {}`                           | Exclusive to Magma v1                                                                                                        |
| `other > electronica`                  | `electronic > electronica`             | Exclusive to Magma v1                                                                                                        |
| `other > house`                        | `house > {}`                           | Exclusive to Magma v1                                                                                                        |
| `other > techno`                       | `techno > {}`                          | Exclusive to Magma v1                                                                                                        |
| `other > trance`                       | `trance > {}`                          | Exclusive to Magma v1                                                                                                        |


### Stylistic Adjustments

Many of Magma's subgenres aren't aligned with Genrelizer's style guide, such as preferring adjective-noun forms over adjective-only. This table lists cases where we stylize the subgenre compared to its literal Magma value, without redirecting to a new genre. This also includes cases where we scrub the subgenre entirely, either because it's `other` or because it's fully redundant with the genre name.

| Magma Value Pair                      | Stylized Subgenre         | Notes                                                                                                                     |
|---------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `alternative > alternative`           | (none)                    |                                                                                                                           | 
| `alternative > college`               | `college rock`            |                                                                                                                           |
| `alternative > other`                 | (none)                    |                                                                                                                           |
| `blues > acoustic`                    | `acoustic blues`          |                                                                                                                           |
| `blues > chicago`                     | `chicago blues`           |                                                                                                                           |
| `blues > classic`                     | `classic blues`           |                                                                                                                           |
| `blues > contemporary`                | `contemporary blues`      |                                                                                                                           |   
| `blues > country`                     | `country blues`           |                                                                                                                           |
| `blues > delta`                       | `delta blues`             |                                                                                                                           |
| `blues > electric`                    | `electric blues`          |                                                                                                                           |
| `blues > other`                       | (none)                    |                                                                                                                           |
| `classical > classical`               | (none)                    | Exclusive to Magma v2                                                                                                     |
| `classic rock > classic rock`         | (none)                    |                                                                                                                           |
| `country > alternative`               | `alternative country`     |                                                                                                                           |
| `country > contemporary`              | `contemporary country`    |                                                                                                                           |
| `country > outlaw`                    | `outlaw country`          |                                                                                                                           |
| `country > other`                     | (none)                    |                                                                                                                           |
| `emo > emo`                           | (none)                    |                                                                                                                           |
| `fusion > fusion`                     | (none)                    | Exclusive to Magma v2                                                                                                     |
| `glam > glam`                         | (none)                    |                                                                                                                           |
| `glam > other`                        | (none)                    |                                                                                                                           |
| `grunge > grunge`                     | (none)                    |                                                                                                                           |
| `hip-hop/rap > gangsta`               | `gangsta rap`             | Exclusive to Magma v2                                                                                                     |
| `hip-hop/rap > hip hop`               | `hip-hop`                 | Exclusive to Magma v2                                                                                                     |
| `hip-hop/rap > old school hip hop`    | `oldschool hip-hop`       | Exclusive to Magma v2                                                                                                     |
| `hip-hop/rap > other`                 | (none)                    | Exclusive to Magma v2                                                                                                     |
| `indie rock > indie rock`             | (none)                    |                                                                                                                           |
| `indie rock > shoegazing`             | `shoegaze`                |                                                                                                                           |
| `indie rock > other`                  | (none)                    |                                                                                                                           |
| `inspirational > inspirational`       | (none)                    | Exclusive to Magma v2                                                                                                     |
| `jazz > contemporary`                 | `contemporary jazz`       |                                                                                                                           |
| `jazz > experimental`                 | `experimental jazz`       |                                                                                                                           |
| `jazz > smooth`                       | `smooth jazz`             |                                                                                                                           |
| `jazz > other`                        | (none)                    |                                                                                                                           |
| `j-rock > j-rock`                     | (none)                    | Exclusive to Magma v2                                                                                                     |
| `latin > latin`                       | (none)                    | Exclusive to Magma v2                                                                                                     |
| `new wave > dark wave`                | `darkwave`                |                                                                                                                           |
| `new wave > new wave`                 | (none)                    |                                                                                                                           |
| `new wave > other`                    | (none)                    |                                                                                                                           |
| `nu-metal > nu-metal`                 | (none)                    |                                                                                                                           |
| `pop-rock > contemporary`             | `contemporary pop-rock`   |                                                                                                                           |
| `pop-rock > other`                    | (none)                    |                                                                                                                           |
| `prog > prog rock`                    | (none)                    | Magma offers no other `prog` subgenres, so this is effectively meaningless                                                |
| `punk > alternative`                  | `alternative punk rock`   |                                                                                                                           |
| `punk > classic`                      | `classic punk rock`       |                                                                                                                           |
| `punk > dance punk`                   | `dance-punk`              |                                                                                                                           |
| `punk > garage`                       | `garage punk`             |                                                                                                                           |
| `punk > hardcore`                     | `hardcore punk`           |                                                                                                                           |
| `punk > other`                        | (none)                    |                                                                                                                           |
| `r&b/soul/funk > other`               | (none)                    | Exclusive to Magma v2                                                                                                     |
| `rock > blues`                        | `blues rock`              | Magma users had the option of `blues` and passed it up, so assume blues is a secondary descriptor and prioritize `rock`   |
| `rock > garage`                       | `garage rock`             |                                                                                                                           |
| `rock > rock`                         | (none)                    |                                                                                                                           |
| `rock > other`                        | (none)                    |                                                                                                                           |
| `southern rock > southern rock`       | (none)                    |                                                                                                                           |
| `urban > other`                       | (none)                    | Exclusive to Magma v1                                                                                                     |
| `world > world`                       | (none)                    | Exclusive to Magma v2                                                                                                     |
| `other > other`                       | (none)                    |                                                                                                                           |


### Unchanged Value Pairs
This table lists the remaining Magma value pairs, which Genrelizer does not edit in any way.

| Magma Value Pair                      | Notes                 |
|---------------------------------------|-----------------------|
| `country > bluegrass`                 |                       |
| `country > honky tonk`                |                       |
| `glam > goth`                         |                       |
| `hip-hop/rap > alternative rap`       | Exclusive to Magma v2 |
| `hip-hop/rap > hardcore rap`          | Exclusive to Magma v2 |
| `hip-hop/rap > rap`                   | Exclusive to Magma v2 |
| `hip-hop/rap > trip hop`              | Exclusive to Magma v2 |
| `hip-hop/rap > underground rap`       | Exclusive to Magma v2 |
| `indie rock > lo-fi`                  |                       |
| `indie rock > post rock`              |                       |
| `jazz > acid jazz`                    |                       |
| `jazz > ragtime`                      |                       |
| `new wave > electroclash`             |                       |
| `pop-rock > soft rock`                |                       |
| `r&b/soul/funk > funk`                | Exclusive to Magma v2 |
| `r&b/soul/funk > motown`              | Exclusive to Magma v2 |
| `r&b/soul/funk > rhythm and blues`    | Exclusive to Magma v2 |
| `r&b/soul/funk > soul`                | Exclusive to Magma v2 |
| `other > a capella`                   |                       |
| `other > acoustic`                    |                       |
| `other > experimental`                |                       |
| `other > oldies`                      |                       |



## Reggae/Ska

RB3 introduced the `reggae/ska` genre tag, which fuses two genres that are historically related but in practice are usually quite different from each other. The _YARG_ team decided to split this tag into separate `reggae` and `ska` genres, but this presents the problem of deciding how to alias a chart that has RB's combined tag.

Most Magma-compiled `reggae/ska` charts do not have this problem, because they have either the `reggae` or `ska` subgenre tag, which is handled as described above. However, this leaves behind 3 sets of problematic charts:

1) The 33 Harmonix-authored (and thus subgenreless) RB charts that use `reggae/ska`
2) Any Magma-generated charts that use the `reggae/ska > other` subgenre
3) Any charts from any other source that use `reggae/ska` with no subgenre (or `other` as the subgenre)

Sets 2 and 3 are likely negligible, so our solution focuses on the Harmonix-authored charts. Of these, 23 are clear-cut reggae songs (22 of which are by Bob Marley and the Wailers, plus one by UB40), while the rest are unambiguously ska. Thus, _YARG_ includes a hardcoded artist name check that it runs against any `reggae/ska > {}` or `reggae/ska > other` charts. If the artist contains `Bob Marley` or is exactly `UB40` or `Zing Experience` (catching one additional RBN edge case), the chart is categorized as `reggae`; otherwise, it defaults to `ska`.

This correctly handles all of set 1. `ska` is also a decent assumption for the other two, since ska is generally much more popular to chart than reggae, and the substring check against `Bob Marley` rather than a hard comparison against `Bob Marley and the Wailers` makes it a little extra flexible for catching reggae music.
