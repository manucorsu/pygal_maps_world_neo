_The most up-to-date version of this README is on [GitHub](https://github.com/manucorsu/pygal_maps_world_neo/blob/master/README.md)._

# pygal_maps_world_neo

This is a fork of the seemingly unmaintained [pygal_maps_world](https://github.com/Kozea/pygal_maps_world) (last commit in July 2015), initially updated with the fixes Antoine Dusséaux ([@a455bcd9](https://github.com/a455bcd9)) proposed in [the original's PR #5](https://github.com/Kozea/pygal_maps_world/pull/5) (early 2021) + some additional fixes and improvements (see [CHANGELOG](https://github.com/manucorsu/pygal_maps_world_neo/blob/master/CHANGELOG.md)).

In the spirit of respecting the [preferences](https://github.com/Kozea/CairoSVG/issues/373#issuecomment-1365838194) of pygal's authors, **this repository has no type hints or type stubs**. You can get those by installing [pygal_maps_world_neo-stubs](https://github.com/manucorsu/pygal_maps_world_neo-stubs) alongside [pygal-stubs](https://github.com/manucorsu/pygal-stubs) for the rest of pygal.
## Installation and usage

> [!IMPORTANT]
> The oldest Python version that this fork supports is the newest of:
>    - the oldest Python version that is still receiving security updates (currently 3.11)
>    - the oldest version that pygal supports (currently 3.9)
>
> Currently, this means that the oldest Python version we support is **Python 3.11** until its [EOL](https://devguide.python.org/versions/) in **October 2027**

To install, simply run `pip install pygal_maps_world_neo`, `uv add pygal_maps_world_neo`, or however you install packages from PyPI. This will also install pygal.

After that, we recommend using it like this instead of how [pygal's docs](https://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html) suggest:

```python
from pygal_maps_world import World

# Optional: set custom country names (ISO names in
# English are used by default.)
# If clear is True, the existing countries will be cleared
# before updating. (you should only really use clear=True
# if you're providing a mapping of all the countries
# you're going to use)

World.set_countries(
    {
        "us": "Estados Unidos",
        "de": "Alemania",
        "fr": "Francia",
        # ...
    },
    clear=True,
)

worldmap_chart = World()
worldmap_chart.title = "Some countries"
worldmap_chart.add("F countries", ["fr", "fi"])
worldmap_chart.add(
    "M countries",
    [
        "ma",
        "mc",
        "md",
        "me",
        "mg",
        "mk",
        "ml",
        "mm",
        "mn",
        "mo",
        "mr",
        "mt",
        "mu",
        "mv",
        "mw",
        "mx",
        "my",
        "mz",
    ],
)
worldmap_chart.add("U countries", ["ua", "ug", "us", "uy", "uz"])
worldmap_chart.render()
```

While you can still use it how the docs suggest (using `pygal.maps.world.World`) and it will work fine at runtime, this **will break type checking** when using [the stubs](https://github.com/manucorsu/pygal_maps_world_neo-stubs). Static type checkers cannot tell that pygal imports all installed maps dynamically at runtime, so everything will be `Unknown`. If you do not type-check your code, do whatever approach you prefer, but if you want type-checking you **must** use this as shown above.

## Contributing
PRs are welcome. Please follow the rules:
- **Do not break the existing API in any way**. If you want to add new features, please do so in a backward-compatible way. This fork should be a drop-in replacement for the original.
- Type checking-related changes will soon be/are welcome in [pygal_maps_world_neo-stubs](https://github.com/manucorsu/pygal_maps_world_neo-stubs), but not here (see above).
- Manually review all AI-generated code.

To work on this project:
1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.
2. Fork this repository and clone it.
3. Make a new branch for your changes.
4. Run `uv sync` to install dependencies and create a virtual environment. You don't need to activate it; uv will use it automatically
5. Make your changes.
6. Run `uv run check`. This will:
    1. Run the tests (pytest)
    2. Run the linter, auto fixing where possible (ruff)
    3. Format your code (black)

    Make sure your code passes the checks before submitting it. If you need to ignore a rule, use an ignore comment and explain why you ignore the rule directly in another comment directly above or below it. If you believe a rule should be ignored globally, open a separate PR for that.
7. Commit your changes, then submit a PR requesting to merge your branch to this repository's `master` branch.

Thanks!