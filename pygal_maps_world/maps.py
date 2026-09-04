"""
Worldmap chart

"""

from __future__ import division
from pygal.util import cached_property
from pygal.graph.map import BaseMap
from pygal_maps_world.i18n import COUNTRIES, SUPRANATIONAL
import os

with open(os.path.join(os.path.dirname(__file__), "worldmap.svg")) as file:
    WORLD_MAP = file.read()


class World(BaseMap):
    """Worldmap graph"""

    x_labels = list(COUNTRIES.keys())
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


class SupranationalWorld(World):
    """SupranationalWorldmap graph"""

    x_labels = list(SUPRANATIONAL.keys())

    def enumerate_values(self, serie):
        """Replaces the values if it contains a supranational code."""
        for i, (code, value) in enumerate(serie.values):
            for subcode in SUPRANATIONAL.get(code, []):
                yield i, (subcode, value)
