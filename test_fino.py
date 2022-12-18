#!/usr/bin/env python
"""
Unit tests for fino.py
"""
from __future__ import annotations

import fino


def test_unsupported_float() -> None:
    number = 2.5
    word = fino.to_finnish(number)  # type: ignore
    assert word == "en tiedä"


def test_negative() -> None:
    number = -30
    word = fino.to_finnish(number)
    assert word == "miinus kolmekymmentä"


def test_0() -> None:
    number = 0
    word = fino.to_finnish(number)
    assert word == "nolla"


def test_1() -> None:
    number = 1
    word = fino.to_finnish(number)
    assert word == "yksi"


def test_2() -> None:
    number = 2
    word = fino.to_finnish(number)
    assert word == "kaksi"


def test_3() -> None:
    number = 3
    word = fino.to_finnish(number)
    assert word == "kolme"


def test_4() -> None:
    number = 4
    word = fino.to_finnish(number)
    assert word == "neljä"


def test_5() -> None:
    number = 5
    word = fino.to_finnish(number)
    assert word == "viisi"


def test_6() -> None:
    number = 6
    word = fino.to_finnish(number)
    assert word == "kuusi"


def test_7() -> None:
    number = 7
    word = fino.to_finnish(number)
    assert word == "seitsemän"


def test_8() -> None:
    number = 8
    word = fino.to_finnish(number)
    assert word == "kahdeksan"


def test_9() -> None:
    number = 9
    word = fino.to_finnish(number)
    assert word == "yhdeksän"


def test_10() -> None:
    number = 10
    word = fino.to_finnish(number)
    assert word == "kymmenen"


def test_11() -> None:
    number = 11
    word = fino.to_finnish(number)
    assert word == "yksitoista"


def test_15() -> None:
    number = 15
    word = fino.to_finnish(number)
    assert word == "viisitoista"


def test_19() -> None:
    number = 19
    word = fino.to_finnish(number)
    assert word == "yhdeksäntoista"


def test_20() -> None:
    number = 20
    word = fino.to_finnish(number)
    assert word == "kaksikymmentä"


def test_42() -> None:
    number = 42
    word = fino.to_finnish(number)
    assert word == "neljäkymmentäkaksi"


def test_85() -> None:
    number = 85
    word = fino.to_finnish(number)
    assert word == "kahdeksankymmentäviisi"


def test_99() -> None:
    number = 99
    word = fino.to_finnish(number)
    assert word == "yhdeksänkymmentäyhdeksän"


def test_100() -> None:
    number = 100
    word = fino.to_finnish(number)
    assert word == "sata"


def test_101() -> None:
    number = 101
    word = fino.to_finnish(number)
    assert word == "satayksi"


def test_111() -> None:
    number = 111
    word = fino.to_finnish(number)
    assert word == "satayksitoista"


def test_200() -> None:
    number = 200
    word = fino.to_finnish(number)
    assert word == "kaksisataa"


def test_827() -> None:
    number = 827
    word = fino.to_finnish(number)
    assert word == "kahdeksansataakaksikymmentäseitsemän"


def test_999() -> None:
    number = 999
    word = fino.to_finnish(number)
    assert word == "yhdeksänsataayhdeksänkymmentäyhdeksän"


def test_1000() -> None:
    number = 1000
    word = fino.to_finnish(number)
    assert word == "tuhat"


def test_1001() -> None:
    number = 1001
    word = fino.to_finnish(number)
    assert word == "tuhatyksi"


def test_1234() -> None:
    number = 1234
    word = fino.to_finnish(number)
    assert word == "tuhatkaksisataakolmekymmentäneljä"


def test_2161() -> None:
    number = 2161
    word = fino.to_finnish(number)
    assert word == "kaksituhattasatakuusikymmentäyksi"


def test_10000() -> None:
    number = 10000
    word = fino.to_finnish(number)
    assert word == "kymmenentuhatta"


def test_26712() -> None:
    number = 26712
    word = fino.to_finnish(number)
    assert word == "kaksikymmentäkuusituhattaseitsemänsataakaksitoista"


def test_99999() -> None:
    number = 99999
    word = fino.to_finnish(number)
    assert (
        word == "yhdeksänkymmentäyhdeksäntuhattayhdeksänsataayhdeksänkymmentäyhdeksän"
    )


def test_100000() -> None:
    number = 100_000
    word = fino.to_finnish(number)
    assert word == "satatuhatta"


def test_111111() -> None:
    number = 111_111
    word = fino.to_finnish(number)
    assert word == "satayksitoistatuhattasatayksitoista"


def test_999999() -> None:
    number = 999_999
    word = fino.to_finnish(number)
    assert word == (
        "yhdeksänsataayhdeksänkymmentäyhdeksäntuhatta"
        "yhdeksänsataayhdeksänkymmentäyhdeksän"
    )


def test_miljoona() -> None:
    number = 10**6
    word = fino.to_finnish(number)
    assert word == "miljoona"


def test_5002010() -> None:
    number = 5_002_010
    word = fino.to_finnish(number)
    assert word == "viisimiljoonaakaksituhattakymmenen"


def test_999999999() -> None:
    number = 999_999_999
    word = fino.to_finnish(number)
    assert word == (
        "yhdeksänsataayhdeksänkymmentäyhdeksänmiljoonaa"
        "yhdeksänsataayhdeksänkymmentäyhdeksäntuhatta"
        "yhdeksänsataayhdeksänkymmentäyhdeksän"
    )


def test_miljardi() -> None:
    number = 10**9
    word = fino.to_finnish(number)
    assert word == "miljardi"


def test_1234567890() -> None:
    number = 1_234_567_890
    word = fino.to_finnish(number)
    assert word == (
        "miljardi"
        "kaksisataakolmekymmentäneljämiljoonaa"
        "viisisataakuusikymmentäseitsemäntuhatta"
        "kahdeksansataayhdeksänkymmentä"
    )


def test_287654321004() -> None:
    number = 287_654_321_004
    word = fino.to_finnish(number)
    assert word == (
        "kaksisataakahdeksankymmentäseitsemänmiljardia"
        "kuusisataaviisikymmentäneljämiljoonaa"
        "kolmesataakaksikymmentäyksituhatta"
        "neljä"
    )


def test_biljoona() -> None:
    number = 10**12
    word = fino.to_finnish(number)
    assert word == "biljoona"


def test_2biljoonaa() -> None:
    number = 2 * 10**12
    word = fino.to_finnish(number)
    assert word == "kaksibiljoonaa"


def test_4000biljoonaa() -> None:
    number = 4000 * 10**12
    word = fino.to_finnish(number)
    assert word == "neljätuhattabiljoonaa"


def test_googol() -> None:
    number = 10**100
    word = fino.to_finnish(number)
    assert word == "googol"


def test_8googolia() -> None:
    number = 8 * 10**100 + 1
    word = fino.to_finnish(number)
    assert word == "kahdeksangoogoliayksi"


def test_sentiljoona() -> None:
    number = 10**600
    word = fino.to_finnish(number)
    assert word == "sentiljoona"


def test_3sentiljoonaa() -> None:
    number = 3 * 10**600
    word = fino.to_finnish(number)
    assert word == "kolmesentiljoonaa"


def test_range() -> None:
    # Just check no errors
    for number in range(0, 100_000):
        word = fino.to_finnish(number)
        assert word != "en tiedä"


def test_print_it() -> None:
    # Just make sure no exceptions
    fino.print_it("test")
