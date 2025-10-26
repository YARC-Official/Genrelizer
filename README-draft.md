# Genrelizer
Have you ever tried to sort your rhythm game charts by genre, and found yourself trudging through inconsistent and hyperspecific genre labels that are useless for actual sorting?

<img width="350" alt="A partial list of chart genres, displaying 'Prog Death', 'Prog-Death-Core', 'Progressive', 'Progressive Death Metal', 'Progressive Death-Metal', and 'Progressive Deathcore'." src="https://github.com/user-attachments/assets/1dcf64b9-4494-43b8-a81e-8f281200f684" />

_YARG_'s official content sticks to [a standardized list of genres](https://wiki.yarg.in/wiki/List_of_common_genre_names) and uses the `sub_genre` tag to get into the nitty-gritty details about each song's sound. However, charts from other sources aren't bound to the same system, and a lot of charters express a lot of detail in their `genre` tags without using the `sub_genre` tag. Genrelizer attempts to keep your library organized by mapping unofficial `genre` tags to a combination of an official `genre` tag and a mostly-untouched `sub_genre` tag that retains the charter's original intent.

For example, if a chart has `genre = 12-Bar Blues`, that's not an official genre. But Genrelizer recognizes it as a type of blues music, and this is the result:

<img width="347" height="41" alt="image" src="https://github.com/user-attachments/assets/13a024bc-e048-476e-8f0a-ab682c59e181" />

Genrelizer also performs some light copy-editing, so that `12 Bar Blues`, `Twelve Bar Blues`, and `Twelve-Bar Blues` all end up under the same `12-Bar Blues` subgenre. We've taken great pains to make sure that subtle naming variations get merged into one sortable value, but even the slightest difference in _sound_ between two subgenre names gets honored as two distinct things.


## What Genrelizer is _not_
* **Genrelizer is not a tool for making new charts; it's a tool for categorizing old ones.** If you're making new charts, you don't need to consult Genrelizer. Just pick an official _YARG_ genre, then add any level of detail you want in the `sub_genre` field. Genrelizer is here to clean up external content where the original charter isn't around anymore to clarify their intent; it doesn't need to get involved with new charts.

* **Genrelizer is not a definitive list of how subgenres _must_ be categorized.** Genrelizer's mappings are only meant to be best-guesses when all we have is a single, nonstandard genre name to work with. We know it might be controversial to see `Deathcore` under `Death/Black Metal`, but that doesn't mean we think that that's the _only_ way to categorize it. If you want your deathcore chart to be categorized under `Metalcore` instead, you can set the `genre` and `sub_genre` fields accordingly, and Genrelizer won't intervene. Heck, you could use `Bubblegum Pop` as a subgenre under `Grindcore` and Genrelizer wouldn't bat an eye. It's only when `genre` is unrecognized that Genrelizer starts making decisions about where things belong (with some minor exceptions; see below).

* **Genrelizer is not (usually) going to save you from updating your charts if _YARG_ adds a new official genre.** Say you have a polka chart, and you've set `genre = World / sub_genre = Polka`, but then we at the _YARG_ team decide that polka music deserves its own entire genre tag. Since your chart still has a legitimate `genre` tag (`World`), Genrelizer isn't going to touch it. If you want to make use of that new `Polka` genre, you're going to have to update the chart yourself.

  There are, however, two exceptions to this rule:

  * If a chart has `genre = Other`, Genrelizer _is_ willing to reassign it, since the charter seemingly wasn't satisfied with their options anyway. So while that `World > Polka` example won't be changed, a chart marked as `Other > Polka` _would_ be moved over to the new `Polka` genre.

  * Genrelizer _is_ willing to push around genres when it recognizes a genre/subgenre pair from Magma, the compiler used for _Rock Band_ songs, because Magma offers only a closed list of genres and subgenres. For example, Magma lacks a `Metalcore` genre, but it does have `Core` as a subgenre of `Metal`. If Genrelizer sees that _exact_ pairing, it assumes that the chart was made by a Magma user who would have used `Metalcore` had it been an option, and reinterprets the genre as such. This only applies to a precise match of `Metal > Core`, because that's a telltale sign of Magma; Genrelizer will _not_ recategorize `Metal > Metalcore`, nor `Heavy Metal > Core`.


## How It Works
When YARG starts up, it consults Genrelizer's data to create a large dictionary of case-insensitive mappings from strings to `(genre, subgenre)` value pairs (with the subgenre being optional). For example, the dictionary maps `Rock` to `(Rock, null)`, because it's standard genre, and it maps `Hard Trance` to `(Trance, Hard Trance)`, because it understands that `Hard Trance` is a subgenre of `Trance`.

Under the `mappings` directory, you'll find a bunch of JSON files - one for each of YARG's official genres. Each file contains a JSON object that defines string mappings for the dictionary. As a contrived example, let's suppose that we weren't satisfied with just `Polka` as a standalone genre, and we decided to branch off a whole dedicated `Hardcore Polka` genre to separate the men from the boys.

### Standard Genres

At the absolute minimum, the object in the `Hardcore Polka.json` file must establish the name of the genre.
```
{
  "name": "Hardcore Polka"
}
```
The name should match the name of the genre in [YARG's `en-US.json` localization file](https://github.com/YARC-Official/YARG/blob/master/Assets/StreamingAssets/lang/en-US.json). Doing this establishes one entry in the dictionary: `Hardcore Polka` maps to `(Hardcore Polka, null)`. Since the dictionary is case-insensitive, this already means that we'll collate `hardcore polka`, `HARDCORE POLKA`, and the like all into one grouping, which is a good start.

However, some genres might be known by various names, or with certain style variations - maybe some people are using the original Czech terms `Pulka` or `Půlka`, and maybe some people spell `Hardcore` with a space or a hyphen. To account for this, we can use the optional `substitutions` property. This property is an object that contains any number of mappings from substring (of the original genre name) to replacements of that substring. For example:
```
{
  "name": Hardcore Polka",
  "substitutions": {
    "hardcore": [ "hard core", "hard-core" ],
    "polka": [ "pulka", "půlka" ]
  }
}
```
YARG will create variations on the `Hardcore Polka` string based on the cartesian product of all of the substitutions - that means that `Hard Core Polka`, `Hard-Core Polka`, `Hardcore Pulka`, `Hard Core Pulka`, `Hard-Core Pulka`, `Hardcore Půlka`, `Hard Core Půlka`, and `Hard-Core Půlka` will all also map to `(Hardcore Polka, null)`. This lets you account for a wide variety of style variations without getting stuck in the combinatorical hell of listing every possible combination of variants (note - sometimes you will still have to brute-force a bunch of combinations, usually when you need to reorder terms in a string rather than just substitute them, but most of the time it's not necessary).

Note that these substitutions are written in all-lowercase as a matter of convention, because the dictionary is case-insensitive. The only value so far where the capitalization actually matters is `name`.

You can also specify affixes for your genre names using the optional `suffixes` and `affixes` properties. For example:
```
{
  "name": Hardcore Polka",
  "substitutions": {
    "hardcore": [ "hard core", "hard-core" ],
    "polka": [ "pulka", "půlka" ]
  },
  "prefixes": [ "the " ],
  "suffixes": [ " music", " musik" ]
}
```
This means that we'll also produce duplicate keys of the forms `The Hardcore Polka`, `Hardcore Polka Music`, `Hardcore Polka Musik`, `The Hardcore Polka Music`, and `The Hardcore Polka Musik` -- _for every one of the variations we created with the `substitutions` property_. In just these 7 lines of JSON, we've defined 45 ways to write `Hardcore Polka` that will all map to the same official YARG genre. Now let's move on to describing the subgenres of `Hardcore Polka`.

P.S.: Note the trailing and leading spaces in the prefix and suffix values - we don't want to create `TheHardcore Polka` or `Hardcore Polkamusik`.


### Subgenres

The last property for the genre object is `subgenres` - this property is technically optional, but in practice we use it everywhere. This object can contain any arbitrary number of properties (each holding an object) to define known subgenres of the genre in question. The key of the property should define the "standardized" rendering of the subgenre name, including capitalization. This is how the subgenre will be rendered in the game.

In the simplest cases, the property can hold an empty object. For example:
```
{
  "name": Hardcore Polka",
  "substitutions": {
    "hardcore": [ "hard core", "hard-core" ],
    "polka": [ "pulka", "půlka" ]
  },
  "prefixes": [ "the " ],
  "suffixes": [ " music", " musik" ],
  "subgenres": {
    "First-Wave Hardcore Polka": {}
  }
}
```

This means that `First-Wave Hardcore Polka`, `First-wave hardcore polka`, `FIRST-WAVE HARDCORE POLKA`, and all other capitalization variations will all map to `(Hardcore Polka, First-Wave Hardcore Polka)`. But of course, we have the same concerns about `hardcore` and `polka` variations as before, plus now we have to worry about `first-wave` vs `first wave` vs `1st wave` and so on. The subgenre doesn't inherit the substitutions and affixes from the parent genre, but we can define them on a per-subgenre basis in the same way:
```
{
  "name": Hardcore Polka",
  "substitutions": {
    "hardcore": [ "hard core", "hard-core" ],
    "polka": [ "pulka", "půlka" ]
  },
  "prefixes": [ "the " ],
  "suffixes": [ " music", " musik" ],
  "subgenres": {
    "First-Wave Hardcore Polka": {
      "substitutions": {
        "first": [ "1st" ],
        "-wave": [ "wave", " wave" ],
        "hardcore": [ "hard core", "hard-core" ],
        "polka": [ "pulka", "půlka" ]
      },
      "prefixes": [ "the " ],
      "suffixes": [ " music", " musik" ]
    }
  }
}
```

We can continue doing this for any number of subgenres of `Hardcore Polka`. Each must define its own substitutions and affixes; these will often repeat among subgenres, so feel free to use some careful copy-pasting.

Lastly, there is one more optional property that is unique to the `subgenre` objects: `localizations`. Standard genres are localized via YARG's localization files, but those files don't keep up with everything inside Genrelizer. Instead, we can define localizations for each subgenre, like so:
```
{
  "name": Hardcore Polka",
  "substitutions": {
    "hardcore": [ "hard core", "hard-core" ],
    "polka": [ "pulka", "půlka" ]
  },
  "prefixes": [ "the " ],
  "suffixes": [ " music", " musik" ],
  "subgenres": {
    "First-Wave Hardcore Polka": {
      "substitutions": {
        "first": [ "1st" ],
        "-wave": [ "wave", " wave" ],
        "hardcore": [ "hard core", "hard-core" ],
        "polka": [ "pulka", "půlka" ]
      },
      "prefixes": [ "the " ],
      "suffixes": [ " music", " musik" ],
      "localizations": {
        "es-ES": "Primera Ola del Polca Hardcore",
        "fr-FR": "Première Vague Polka Hardcore"
      }
    }
  }
}
```

You do not need to provide an `en-US` value, because the property name implicitly acts as that value. When a localization is not provided for the player's selected language, we fall back to the `en-US` value.



## Frequently-Asked Questions

### Can I submit a pull request to add a new subgenre or new variations on an existing one?
**Yes!** Genrelizer is meant to be crowdsourced, and we're always happy to receive new mappings and aliases from the community. Please make sure you follow these rules:
* Follow the capitalization and spacing standards used throughout the JSON files
* Don't submit aliases between genre names that have _any_ semantic difference. Aliases have to be absolutely 100% synonymous to be valid. `Blackened Progressive Metal` and `Progressive Black Metal` are not strictly the same thing!
* _Do_ try to be exhaustive with your substitutions and affixes. It's okay if you end up producing some implausible combinations (e.g. in the example above, we're producing `the 1stwave hard-core půlkamusik`, which is overkill, but it would be more work to specifically exclude it)
* Try to avoid subgenre names that are just adjectives - we prefer "alternative rock" over "alternative". You can bend this rule if a genre name is getting overly long, or if the adjective-only form is much more common in everyday use
* Don't define duplicate instances of the same dictionary key. This can happen in a few ways:
  * Adding a subgenre that's already considered a subgenre of something else. Before you add `Industrial Death Metal` to `Death/Black Metal`, you better check if it's already under `Industrial`
  * Defining substitutions for substrings that don't exist in the original name. If you add `"polka": [ "pulka" ]` as a substitution for `Industrial`, then it's going to change nothing and produce a second `Industrial` key
  * Defining overlapping substitutions. To alias `foo bar` to `foobar`, you can use `"foo ": [ "foo" ]` or `" bar": [ " bar" ]`, but not both


### Can I submit a pull request to change an existing mapping?
**We'd prefer you didn't.** We understand that genres can be subjective and controversial, and that some subgenre mappings can come down to a bit of a coin flip (is `industrial rock` `rock` or `industrial`?) or be considered sacreligious to some communities (`deathcore` living under `death/black metal` vs. `metalcore`). But the point of this repo isn't to lay down the law about what subgenres _absolutely belong_ where; we're just compiling a bunch of best-effort guesses to help make sense of the wild west that is freeform genre tags. If you feel so strongly about `deathcore` belonging under `metalcore`, you can set your `genre` and `subgenre` fields that way yourself and Genrelizer won't put up a fight.

That said, if you notice something that is _truly absolutely unambiguously_ a mistake and not just a divisive decision, then please do issue a correction through a pull request.

### Can I submit a pull request to add a new standard genre?
**Not without prior discussion.** Adding a new standard genre is a pretty big decision that requires changes on the YARG side in addition to in Genrelizer. You're welcome to float ideas in our Discord or Reddit communities, but don't make a pull request as your first step.

### What is the policy on potentially-problematic/offensive genres or genre names?
This breaks down to a few subcategories.

* Some genre names contain outdated terms that are now considered discriminatory or hateful, such as `g***y jazz` (containing a slur for the Romani people) and `d****land jazz` (containing an outdated name for the southern United States). In most cases (including both of those examples), the music itself is unproblematic and only suffers from an old name that's stuck around. In these cases, we want to support the music but don't want to display the unnecessary offensive terms, so we use the `subgenreAliases.json` file to replace them with modern, more-inclusive names.
* Other genre names might contain words that some would consider profane or distasteful, such as `porn groove`. Generally speaking, we don't feel the need to censor these names; charters should take such names into account when assigning family friendliness ratings to songs, so that they don't appear in the library when a user wishes to filter out offensive content.
* When it comes to genres that are _themselves_ deeply problematic, such as `nazi punk` or `national socialist black metal`, we do not acknowledge them in any way in Genrelizer's JSON files.
