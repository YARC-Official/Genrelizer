# Frequently-Asked Questions

## Can I submit a pull request to add a new subgenre or new variations on an existing one?
**Yes!** Genrelizer is meant to be crowdsourced, and we're always happy to receive new mappings and aliases from the community. Please make sure you follow the [rules for submissions](Rules%20for%20Submissions.md).


## Can I submit a pull request to relocate an existing subgenre?
**We'd prefer you didn't.** We understand that genres can be subjective and controversial, and that some subgenre mappings can come down to a bit of a coin flip (is `industrial rock` `rock` or `industrial`?) or be considered sacreligious to some communities (`deathcore` living under `death/black metal` vs. `metalcore`). But the point of this repo isn't to lay down the law about what subgenres _absolutely belong_ where; we're just compiling a bunch of best-effort guesses to help make sense of the wild west that is freeform genre tags. If you feel so strongly about `deathcore` belonging under `metalcore`, you can set your `genre` and `subgenre` fields that way yourself and Genrelizer won't put up a fight.

That said, if you notice something that is _truly absolutely unambiguously_ a mistake and not just a divisive decision, then please do issue a correction through a pull request.

## Can I submit a pull request to add a new standard genre?
**Not without prior discussion.** Adding a new standard genre is a pretty big decision that requires changes on the YARG side in addition to in Genrelizer. You're welcome to float ideas in our Discord or Reddit communities, but don't make a pull request as your first step.

## What is the policy on potentially-problematic/offensive genres or genre names?
This breaks down to a few subcategories.

* Some genre names contain outdated terms that are now considered discriminatory or hateful, such as `g***y jazz` (containing a slur for the Romani people) and `d****land jazz` (containing an outdated name for the southern United States). In most cases (including both of those examples), the music itself is unproblematic and only suffers from an old name that's stuck around. In these cases, we want to support the music but don't want to display the unnecessary offensive terms, so we use substitutions to replace them with modern, more-inclusive names. This does mean that some mapping files contain offensive terms, but it's better to have them there than in _YARG_'s UI.
* Other genre names might contain words that some would consider profane or distasteful, such as `porn groove`. Generally speaking, we don't feel the need to censor these names; charters should take such names into account when assigning family friendliness ratings to songs, so that they don't appear in the library when a user wishes to filter out offensive content.
* When it comes to genres that are _themselves_ deeply problematic, such as `nazi punk` or `national socialist black metal`, we do not acknowledge them in any way in Genrelizer's JSON files.
