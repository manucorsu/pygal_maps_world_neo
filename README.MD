# pygal_maps_world_neo

This is a fork of the seemingly unmaintained [pygal-maps-world](https://github.com/pygal/pygal-maps-world) (last commit in July 2015), updated with the fixes @a455bcd9 proposed in [the original's PR #5](https://github.com/Kozea/pygal_maps_world/pull/5) in early 2021.

**The original repository lacks a license**. Since it's intended for use with pygal and that is [under GNU LGPL 3.0](https://github.com/Kozea/pygal/blob/master/LICENSE), I assumed that this package should also be under GNU LGPL 3.0 and added a [LICENSE](./LICENSE) file to that effect. If you are a pygal maintainer and disagree, please submit an issue and I'll remove this repository.

In the spirit of respecting the [preferences](https://github.com/Kozea/CairoSVG/issues/373#issuecomment-1365838194) of pygal's authors, **this file has no type hints or type stubs**. Type checking users will soon be able to get them via [pygal-stubs](https://github.com/manucorsu/pygal-stubs) (will go public as soon as it's done, please be patient)

## Roadmap
- Having already applied the fixes proposed in [the original's PR #5](https://github.com/Kozea/pygal_maps_world/pull/5) in early 2021, we should check that there isn't anything else that needs to be updated. I've already identified:
    - `ANTARTICA` is a misspelling of `ANTARCTICA`, should be marked deprecated in favour of the latter.
    - `NAFTA` no longer exists and should be deprecated in favour of `USMCA`.
- Potentially:
    - Add a way to customize country names, so that you aren't forced to use the ISO names in `i18n.py` if you don't want to (great for multilingual support or if you want to [upset the PRC](https://github.com/manucorsu/pygal_maps_world_neo/commit/e1c3fa5bbaa2be10ff9f7b8322af58f06cd2495b)), in such a way that is compatible with the original.