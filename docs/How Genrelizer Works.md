# How Genrelizer Works
When YARG starts up, it consults Genrelizer's data to create a large dictionary of case-insensitive mappings from strings to `(genre, subgenre)` value pairs (with the subgenre being optional). For example, the dictionary maps `Rock` to `(Rock, null)`, because it's standard genre, and it maps `Hard Trance` to `(Trance, Hard Trance)`, because it understands that `Hard Trance` is a subgenre of `Trance`.

Under the `mappings` directory, you'll find a bunch of JSON files - one for each of YARG's official genres. Each file contains a JSON object that defines string mappings for the dictionary. As a contrived example, let's suppose that we weren't satisfied with just `Polka` as a standalone genre, and we decided to branch off a whole dedicated `Hardcore Polka` genre to separate the men from the boys.

## Standard Genres

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

You can also specify suffixes and prefixes (collectively called _affixes_) for your genre names by using the optional `suffixes` and `prefixes` properties. For example:
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


## Subgenres

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