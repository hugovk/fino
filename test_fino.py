#!/usr/bin/env python
"""
Unit tests for fino.py
"""

from __future__ import annotations

import pytest

import fino


def test_unsupported_float() -> None:
    number = 2.5
    word = fino.to_finnish(number)  # type: ignore[arg-type]
    assert word == "en tiedä"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (-30, "miinus kolmekymmentä"),
        (0, "nolla"),
        (1, "yksi"),
        (2, "kaksi"),
        (3, "kolme"),
        (4, "neljä"),
        (5, "viisi"),
        (6, "kuusi"),
        (7, "seitsemän"),
        (8, "kahdeksan"),
        (9, "yhdeksän"),
        (10, "kymmenen"),
        (11, "yksitoista"),
        (15, "viisitoista"),
        (19, "yhdeksäntoista"),
        (20, "kaksikymmentä"),
        (42, "neljäkymmentäkaksi"),
        (85, "kahdeksankymmentäviisi"),
        (99, "yhdeksänkymmentäyhdeksän"),
        (42, "neljäkymmentäkaksi"),
        (100, "sata"),
        (101, "satayksi"),
        (111, "satayksitoista"),
        (200, "kaksisataa"),
        (827, "kahdeksansataakaksikymmentäseitsemän"),
        (999, "yhdeksänsataayhdeksänkymmentäyhdeksän"),
        (1000, "tuhat"),
        (1001, "tuhatyksi"),
        (1234, "tuhatkaksisataakolmekymmentäneljä"),
        (2161, "kaksituhattasatakuusikymmentäyksi"),
        (10000, "kymmenentuhatta"),
        (26712, "kaksikymmentäkuusituhattaseitsemänsataakaksitoista"),
        (99999, "yhdeksänkymmentäyhdeksäntuhattayhdeksänsataayhdeksänkymmentäyhdeksän"),
        (100_000, "satatuhatta"),
        (111_111, "satayksitoistatuhattasatayksitoista"),
        (
            999_999,
            "yhdeksänsataayhdeksänkymmentäyhdeksäntuhatta"
            "yhdeksänsataayhdeksänkymmentäyhdeksän",
        ),
        (10**6, "miljoona"),
        (5_002_010, "viisimiljoonaakaksituhattakymmenen"),
        (
            999_999_999,
            "yhdeksänsataayhdeksänkymmentäyhdeksänmiljoonaa"
            "yhdeksänsataayhdeksänkymmentäyhdeksäntuhatta"
            "yhdeksänsataayhdeksänkymmentäyhdeksän",
        ),
        (10**9, "miljardi"),
        (
            1234567890,
            "miljardi"
            "kaksisataakolmekymmentäneljämiljoonaa"
            "viisisataakuusikymmentäseitsemäntuhatta"
            "kahdeksansataayhdeksänkymmentä",
        ),
        (
            287_654_321_004,
            "kaksisataakahdeksankymmentäseitsemänmiljardia"
            "kuusisataaviisikymmentäneljämiljoonaa"
            "kolmesataakaksikymmentäyksituhatta"
            "neljä",
        ),
        (10**12, "biljoona"),
        (2 * 10**12, "kaksibiljoonaa"),
        (4000 * 10**12, "neljätuhattabiljoonaa"),
        (10**100, "googol"),
        (8 * 10**100 + 1, "kahdeksangoogoliayksi"),
        (10**600, "sentiljoona"),
        (3 * 10**600, "kolmesentiljoonaa"),
    ],
)
def test_fino(test_input: int, expected: str) -> None:
    number = test_input
    word = fino.to_finnish(number)
    assert word == expected


def test_range() -> None:
    # Just check no errors
    for number in range(0, 100_000):
        word = fino.to_finnish(number)
        assert word != "en tiedä"


def test_print_it() -> None:
    # Just make sure no exceptions
    fino.print_it("test")
