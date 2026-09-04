_This README has some GitHub exclusive features, please read it [there](https://github.com/manucorsu/pygal_maps_world_neo/blob/master/README.md) instead of on PyPI_

# pygal_maps_world_neo

This is a fork of the seemingly unmaintained [pygal_maps_world](https://github.com/Kozea/pygal_maps_world) (last commit in July 2015), initially updated with the fixes Antoine Dusséaux ([@a455bcd9](https://github.com/a455bcd9)) proposed in [the original's PR #5](https://github.com/Kozea/pygal_maps_world/pull/5) (early 2021) + some additional fixes and improvements (see [CHANGELOG](https://github.com/manucorsu/pygal_maps_world_neo/blob/master/CHANGELOG.md)).

In the spirit of respecting the [preferences](https://github.com/Kozea/CairoSVG/issues/373#issuecomment-1365838194) of pygal's authors, **this file has no type hints or type stubs**. Type checking users will soon be able to get them via [pygal-stubs](https://github.com/manucorsu/pygal-stubs) (will go public as soon as it's done, please be patient).

## Installation and usage

> [!IMPORTANT]
> Similar to pygal-stubs, the oldest Python version that this fork supports is the newest of:
>    - the oldest Python version that is still receiving security updates (currently 3.10)
>    - the oldest version that pygal supports (currently 3.9)
>
> At the time of writing, that means that the oldest Python version we support is **Python 3.10** until its [EOL](https://devguide.python.org/versions/) in **October 2026**

To install, simply do `pip install pygal-maps-world-neo` (or however you install packages from PyPI. This will also install pygal.)

Then, in your code (for now, since we haven't added any major new features, you can use it exactly like the original package), e.g.:

```python
import pygal

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Some countries'
worldmap_chart.add('F countries', ['fr', 'fi'])
worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                                   'mk', 'ml', 'mm', 'mn', 'mo',
                                   'mr', 'mt', 'mu', 'mv', 'mw',
                                   'mx', 'my', 'mz'])
worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
worldmap_chart.render()
```

See [pygal's docs](https://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html) for a comprehensive guide (ignoring the Installation step.)

## Contributing
PRs are welcome. Please follow the rules:
- **Do not break the existing API in any way**. If you want to add new features, please do so in a backward-compatible way. This fork should be a drop-in replacement for the original.
- Type checking-related changes will soon be welcome in [pygal-stubs](https://github.com/manucorsu/pygal-stubs), but not here (see above).
- Review all AI generated code.

To work on this project:
1. [Install Hatch](https://hatch.pypa.io/latest/install/) if you don't have it already. **This fork has migrated from `setup.py` to Hatchling**.
2. Fork this repository and clone it.
3. Make a new branch for your changes.
4. Run `hatch shell`. This will create a virtual environment, activate it, and install all of the dependencies (pygal itself + dev dependencies pytest, pyquery and black). Use that shell exclusively while working
5. Make your changes. Once you're done, run `hatch run check:all` to test your code with pytest and autoformat with black.
6. Commit, push and open a PR asking to merge your fork's branch into this repository's `master` branch.
7. Leave your hatch shell by using `exit` (not `deactivate`!)

### To-do list
I'll add these fixes myself once I find the time. Right now I need to focus in getting pygal-stubs out the door  and school. If you want to help, please open a PR with your changes. Thanks!
#### High-ish priority
- Make it so that the `1` value does not appear in maps where it is not needed, e.g. in maps like this one
[![incorrect1.png](https://i.postimg.cc/Y0JFKjvd/incorrect1.png)](https://postimg.cc/kRvGWJFS)
- Fix the label that appears on hover, which after updating the SVG seems to be completely broken and I've haven't been able to fix it yet. The label instead of appearing on top of the country, it sometimes appears very far away from it, like in this example
[![malawi.png](https://i.postimg.cc/G24PZWMR/malawi.png)](https://postimg.cc/zb1RhcZ2)
##### Low priority
- Add more constants to the `i18n` module, e.g. ASEAN, MERCOSUR, EU, etc.
- (veery low priority as I know it'll be a mess to implement) add the ability for maps to have both countries and supranational groups, e.g. a map that shows the entire EU in one color while showing every other country as separate.
- Any other improvements you can think of. If you want to help, please open a PR with your changes. Thanks!
