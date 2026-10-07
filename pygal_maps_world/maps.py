"""
Worldmap chart

"""

import os

from pygal.graph.map import BaseMap
from pygal.util import cached_property

from pygal_maps_world import i18n
from pygal_maps_world.i18n import COUNTRIES, SUPRANATIONAL

with open(os.path.join(os.path.dirname(__file__), "worldmap.svg")) as file:
    WORLD_MAP = file.read()


class World(BaseMap):
    """Worldmap graph"""

    x_labels = list(COUNTRIES.keys())  # noqa: RUF012
    # can't break compatibility with the base class
    # (also the x_labels would be the ISO codes) so it's
    # not like the user would need to change them anyways

    # The following three attributes should probably be
    # moved to __init__. Not all maps necessarily share 
    # the same area names, prefixes and SVGs (can think of
    # a use case where the user would need different names
    # and boundaries to represent multiple countries'
    # perspectives in conflicts, having one instance for
    # each). Moving them would be a breaking change though.
    area_names = COUNTRIES
    area_prefix = ""
    svg_map = WORLD_MAP
    
    kind = "country"

    @cached_property
    def countries(self):
        return [
            val[0]
            for serie in self.all_series
            for val in serie.values
            if val[0] is not None
        ]

    @cached_property
    def _values(self):
        """Getter for series values (flattened)"""
        return [
            val[1]
            for serie in self.series
            for val in serie.values
            if val[1] is not None
        ]

    @classmethod
    def set_countries(cls, countries, clear=False):
        """
        Update the countries dictionary with the given countries.

        If clear is True, the existing countries will be cleared before updating.

        The countries parameter should be a dictionary-like object where the keys
        are lowercase ISO 3166-1 alpha-2 codes and the values are country names.

        This classmethod is just a shortcut for `i18n.set_countries`.

        Examples:
        ```python
            my_country_names = {"fr": "Francia"}

            World.set_countries(my_country_names)
            # clear is False (by default), so "fr"
            # will map to "Francia" and everything else
            # will remain the same

            World.set_countries(my_country_names, clear=True)
            # clear is True, so "fr" will map to
            # "Francia" and everything else will
            # be cleared: **all other countries
            # will have no name displayed**. You
            # should only really use clear=True
            # if you're passing a mapping of all
            # countries.
        ```
        """
        return i18n.set_countries(countries, clear)


class SupranationalWorld(World):
    """SupranationalWorldmap graph"""

    x_labels = list(SUPRANATIONAL.keys())  # noqa: RUF012

    def enumerate_values(self, serie):
        """Replaces the values if it contains a supranational code."""
        for i, (code, value) in enumerate(serie.values):
            for subcode in SUPRANATIONAL.get(code, []):
                yield i, (subcode, value)
