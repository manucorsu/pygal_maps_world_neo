from pygal_maps_world.maps import World, SupranationalWorld
from pygal_maps_world.i18n import COUNTRIES, SUPRANATIONAL, set_countries
import operator

try:
    from functools import reduce
except ImportError:
    pass

_COUNTRIES = dict(COUNTRIES)


def test_worldmap():
    set_countries(_COUNTRIES, True)
    datas = {}
    for i, ctry in enumerate(COUNTRIES):
        datas[ctry] = i

    wmap = World()
    wmap.add("countries", datas)
    q = wmap.render_pyquery()
    assert len(q(".country.color-0")) == len(COUNTRIES)
    assert "France" in q(".country.fr").text()


def test_worldmap_i18n():
    set_countries(_COUNTRIES, True)
    datas = {}
    for i, ctry in enumerate(COUNTRIES):
        datas[ctry] = i

    set_countries({"fr": "Francia"})
    wmap = World()
    wmap.add("countries", datas)
    q = wmap.render_pyquery()
    assert len(q(".country.color-0")) == len(COUNTRIES)
    assert "Francia" in q(".country.fr").text()


def test_worldmap_i18n_clear():
    set_countries(_COUNTRIES, True)
    wmap = World()
    wmap.add("countries", dict(fr=12))
    set_countries({"fr": "Frankreich"}, clear=True)
    q = wmap.render_pyquery()
    assert len(q(".country.color-0")) == 1
    assert "Frankreich" in q(".country.fr").text()


def test_supranationalworldmap():
    set_countries(_COUNTRIES, True)
    datas = {}
    for i, supra in enumerate(SUPRANATIONAL):
        datas[supra] = i + 1

    wmap = SupranationalWorld()
    wmap.add("supra", datas)
    q = wmap.render_pyquery()
    assert len(q(".country.color-0")) == len(
        reduce(operator.or_, map(set, SUPRANATIONAL.values()))
    )
