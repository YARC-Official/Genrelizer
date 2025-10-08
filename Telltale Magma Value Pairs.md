# Telltale Magma Value Pairs
Users of Magma (the compiler for RB CON files) are forced to contend with a smaller list of genres than YARG's official list. However, Magma associates each genre is with a small list of predefined subgenres, some of which map cleanly to official YARG genres.

For example, a Magma user who wishes to tag a metalcore song has to settle for `metal > metalcore`, but clearly would have preferred to use YARG's `metalcore` genre if it had been available. If we see one of these exact pairings, we do alias both the genre and subgenre, under the assumption that the chart was Magma-compiled and tagged under Magma's restrictions.

Because Magma values are a closed set, these conversions are hardcoded into YARG rather than being part of Genrelizer. They are listed in the following table for reference, but **this file does not drive actual Genrelizer behavior. Do not submit a pull request for this file.**

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
