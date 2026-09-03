# pygal_maps_world_neo

This is a fork of the seemingly unmaintained [pygal-maps-world](https://github.com/pygal/pygal-maps-world) (last commit in July 2015), initially updated with the fixes  Antoine Dusséaux ([@a455bcd9](https://github.com/a455bcd9)) proposed in [the original's PR #5](https://github.com/Kozea/pygal_maps_world/pull/5) in early 2021 + some additional fixes and improvements (see [CHANGELOG](./CHANGELOG.md)).

In the spirit of respecting the [preferences](https://github.com/Kozea/CairoSVG/issues/373#issuecomment-1365838194) of pygal's authors, **this file has no type hints or type stubs**. Type checking users will soon be able to get them via [pygal-stubs](https://github.com/manucorsu/pygal-stubs) (will go public as soon as it's done, please be patient)

## Contributing
PRs are welcome. Please follow the rules:
- Do not break the existing API. If you want to add new features, please do so in a backward-compatible way.
- Type checking-related changes will soon be welcome in [pygal-stubs](https://github.com/manucorsu/pygal-stubs), but not here (see above).
- Review all AI generated code.

To work on this project:
1. [Install Hatch](https://hatch.pypa.io/latest/install/) if you don't have it already. **This fork has migrated from `setup.py` to Hatchling**.
2. Fork this repository and clone it.
3. Make a new branch for your changes.
4. Run `hatch shell`. This will create a virtual environment, activate it, and install all of the dependencies (pygal itself + dev dependencies pytest, pyquery and black)
5. Make your changes. Once you're done, run `hatch run check:all` to test your code with pytest and autoformat with black.
6. Commit, push and open a PR asking to merge your fork's branch into this repository's `master` branch.