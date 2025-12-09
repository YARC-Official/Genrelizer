# Rules for Submissions

## Follow formatting conventions
Follow the capitalization and spacing standards used throughout the JSON files. In some cases, these are just conventions for readability, but some fields' capitalizations directly control how text appears in the game.

## Keep subgenres separate unless they are _completely_ synonymous

Substitutions and affixes are meant to handle cosmetic variations on a subgenre name that have _absolutely no bearing on the semantic meaning of the subgenre_. Do not use substitutions or affixes to combine terms that have any difference in meaning, even slightly.

### Examples of terms that should be combined
* `Hard Rock` might be rendered as `Hard-Rock` or `Hardrock`, purely as a matter of style. We use the `" ": [ "-", "" ]` substitution set to account for all variations.
* `Funeral Doom` and `Funeral Doom Metal` are completely synonymous; the former is just shorthand for the latter. We use `Funeral Doom Metal` as the canonical name, with the `"doom metal": [ "doom" ]` substitution to account for the short version. If we preferred `Funeral Doom` as the default, we could have used `suffixes: [ " metal" ]` instead.
* `Étude` contains an accented character, which many charters will often replace with a plain `E` due to keyboard limitations. We use the `"é": [ "e" ]` substitution to ensure the simpler form is also recognized.
* `Braindance` is an alternative name for `IDM`. While it's a completely different term, it refers to the exact same thing, so we use the `idm: [ "braindance" ]` substitution to accept it.

### Examples of terms that should _not_ be combined
* `Blackened Progressive Metal` and `Progressive Black Metal` sure sound similar, but they each carry slightly different implications (is it black metal with prog influence, or vice-versa?). We treat these as separate subgenres instead of aliasing one to the other.
* Some people might tell you that all `Classic Rock` is `Dad Rock`, but others might consider only _some_ of the classics to be meant for dads. Since `Dad Rock` can carry some more-specific implications than `Classic Rock`, we treat the former as a subgenre of the latter, rather than substituting `classic` for `dad` at the genre level.
* Can't hear (or at least appreciate) the difference between `Harsh Noise` and `Harsh Noise Wall`? Doesn't matter - if they mean different things to _some_ people, that's all that matters to keep them separate.


## Be exhaustive with substitutions and affixes (and overkill is okay!)

When you do use substitutions and affixes, try to be exhaustive and cover any variation that you can even conceive of someone using. You might not know anyone who writes `Dubstep` as `Dub-Step`, but surely someone does.

When you have multiple substitutions for different parts of a genre name, you might start to feel like you're going overboard and including some implausible combinations. Take this for example:
```
 "Hardcore Punk": {
      "substitutions": {
        "core": [ " core", "-core" ]
      },
      "suffixes": [ " rock", "rock", "-rock" ]
    }
```
 It makes sense to cover `Hardcore Punkrock`, `Hard-Core Punk`, and maybe even `Hard-Core Punk-Rock`, but you might wonder if we really need to generate a `Hard-Core Punkrock` key. Truthfully, we probably don't, but it's easier to just not worry about it. Listing out each plausible combination one-by-one and excluding the weird ones is torture, and the extraneous keys don't have any measurable performance impact.

## Prefer adjective-noun form over just adjectives

Generally speaking, we prefer `Epic Doom Metal` over `Epic Doom`, `Crust Punk` over `Crust`, and `Big Band Jazz` over `Big Band`. This isn't a hard-and-fast rule though, and you can bend it if the adjective-only form is much more common (`Drone Doom` over `Drone Doom Metal`) or if the name is getting overly long (`Progressive Big Band` over `Progressive Big Band Jazz`). Make sure to use substitutions and affixes to account for the form you don't pick.


## Don't generate duplicate keys

Every entry in Genrelizer creates one or more strings, and all of those strings become keys in one big C# dictionary. That means every single generated key needs to be globally unique across the whole repo. If the same key is generated more than one time, _YARG_ will ignore all but the first instance.

The `verify.py` script checks for this - you can check before submitting by running the script yourself, or let the GitHub action do it for you after pushing.

Here are some common ways to accidentally introduce duplicate keys:

* Adding a subgenre to one file without checking if it already exists in another. Before you add `Industrial Death Metal` to `Death/Black Metal`, you better check if it's already under `Industrial`.
* Defining substitutions for substrings that don't exist in the original name. If you add `"polka": [ "pulka" ]` as a substitution for `Industrial`, then it's going to change nothing and produce a second `Industrial` key.
* Defining overlapping substitutions. To alias `foo bar` to `foobar`, you can use `"foo ": [ "foo" ]` or `" bar": [ "bar" ]`, but not both.

