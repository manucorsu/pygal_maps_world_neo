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

You then import the `World` or `SupranationalWorld` classes and use them as you would with the original pygal_maps_world package. You have two options for importing the classes:
- `from pygal_maps_world import World` (or `SupranationalWorld`) - this is the recommended way, as it allows type checking with [the stubs](https://github.com/manucorsu/pygal_maps_world_neo-stubs)
- Using `instance = pygal.maps.world.World()` (or `SupranationalWorld`) - this is the way pygal's docs suggest, and it will work fine at runtime, but it will break type checking if using [the stubs](https://github.com/manucorsu/pygal_maps_world_neo-stubs)

### Simple world map example

```python
from pygal_maps_world import World

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
worldmap_chart.render_in_browser()
```

You can also work with the `COUNTRIES` mapping directly:
```python
from pygal_maps_world import World, COUNTRIES

VOWELS = ("a", "e", "i", "o", "u")
data = {"a": [], "e": [], "i": [], "o": [], "u": [], "non_vowel": []}
for country_code, country_name in COUNTRIES.items():
    starting_char = country_name[0].lower()
    if starting_char in VOWELS:
        data[starting_char].append(country_code)
    else:
        data["non_vowel"].append(country_code)

world = World()
world.title = "vowels"
for k, v in data.items():
    world.add(k, v)

world.render_in_browser()
```

### Providing a custom boundaries
The default map boundaries are based on [this Wikipedia map](https://en.wikipedia.org/wiki/File:BlankMap-World-with-Circles.svg) (public domain), removing all territories that don't have an officially assigned ISO 3166-1 alpha-2 code (except for Kosovo `xk`, which is included).

If you need to provide your own boundaries to represent a specific country's perspective (as in [Kozea/pygal issue #594](https://github.com/Kozea/pygal/issues/594)), you can do so by setting a custom map SVG string after you instantiate World, but **before you render it**:

```python
from pygal_maps_world import World

with open("my_custom_boundaries.svg", "r", encoding="utf8") as f:
    custom_boundaries = f.read()

world = World()
world.svg_map = custom_boundaries

world.title = "title"
# then add data and render as usual
```

**The SVG you provide must follow the same structure the default map has**. You should probably start from the default map and modify it to your needs, rather than creating a new one. 

### Providing custom country names
By default, the territory names are their ISO names in English. You can provide your own names by using the `World.set_countries` classmethod:

```python
from pygal_maps_world import World

# changing a couple of names:
World.set_countries(
    {
        "us": "United States",
        "gb": "United Kingdom",
        "bo": "Bolivia",
    }
)
# Their default names are the long official ones so you
# might want to shorten them,
# (e.g. "Bolivia, Plurinational State of" -> "Bolivia")
# keeping the rest unchanged


# changing all names (by clearing the original mapping),
# e.g. to display all country names in Spanish:
spanish_names = {
    "ad": "Andorra",
    "ae": "Emiratos Árabes Unidos",
    "af": "Afganistán",
    # ...etc
}
World.set_countries(spanish_names, clear=True)
# Because clear=True, **countries that are not
# provided in `spanish_names` will not have a name displayed**. You should provide all countries if you want to use this option.
```

## Contributing
PRs are welcome. Please follow the rules:
- **Do not break the existing API in any way**. If you want to add new features, please do so in a backward-compatible way. This fork should be a drop-in replacement for the original.
- Type checking-related changes are welcome in [pygal_maps_world_neo-stubs](https://github.com/manucorsu/pygal_maps_world_neo-stubs), not here (see above).
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