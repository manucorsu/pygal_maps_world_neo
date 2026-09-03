# 1.1.0
This will be the first release of this fork.
- Applied the fixes @a455bcd9 proposed in [the original's PR #5](https://github.com/Kozea/pygal_maps_world/pull/5) in early 2021.
    - I did modify his map to add Antarctica and make it scale properly
- ⚠️ **Migrated from setup.py to Hatchling**. This also includes dropping Python 2 support which pygal did a long time ago but was de jure still supported by this package's setup.py. The minimum supported Python version is now 3.10.
- Made every default country name match its ISO name, standardizing (most were their ISO names already, but some were not).
- Improved [i18n](./pygal_maps_world/i18n.py) significantly:
    - Added docstrings
    - Added a `USMCA` constant for the US-Mexico-Canada trade agreement (`NAFTA` is still available but discouraged).
    - Added a properly spelled `ANTARCTICA` constant (the old `ANTARTICA` is still available but discouraged).
    - Updated the Euro area (`EUR`) and OECD (`OECD`) lists which were missing some member states.
    - Standardized country names in the `i18n` module to match their ISO names (most were already, but some were not).