#!/usr/bin/env python
"""
Unit tests for fino.py
"""
import unittest

import fino


class TestIt(unittest.TestCase):
    def test_unsupported_float(self):
        number = 2.5
        word = fino.to_finnish(number)
        self.assertEqual(word, "en tiedä")

    def test_negative(self):
        number = -30
        word = fino.to_finnish(number)
        self.assertEqual(word, "miinus kolmekymmentä")

    def test_0(self):
        number = 0
        word = fino.to_finnish(number)
        self.assertEqual(word, "nolla")

    def test_1(self):
        number = 1
        word = fino.to_finnish(number)
        self.assertEqual(word, "yksi")

    def test_2(self):
        number = 2
        word = fino.to_finnish(number)
        self.assertEqual(word, "kaksi")

    def test_3(self):
        number = 3
        word = fino.to_finnish(number)
        self.assertEqual(word, "kolme")

    def test_4(self):
        number = 4
        word = fino.to_finnish(number)
        self.assertEqual(word, "neljä")

    def test_5(self):
        number = 5
        word = fino.to_finnish(number)
        self.assertEqual(word, "viisi")

    def test_6(self):
        number = 6
        word = fino.to_finnish(number)
        self.assertEqual(word, "kuusi")

    def test_7(self):
        number = 7
        word = fino.to_finnish(number)
        self.assertEqual(word, "seitsemän")

    def test_8(self):
        number = 8
        word = fino.to_finnish(number)
        self.assertEqual(word, "kahdeksan")

    def test_9(self):
        number = 9
        word = fino.to_finnish(number)
        self.assertEqual(word, "yhdeksän")

    def test_10(self):
        number = 10
        word = fino.to_finnish(number)
        self.assertEqual(word, "kymmenen")

    def test_11(self):
        number = 11
        word = fino.to_finnish(number)
        self.assertEqual(word, "yksitoista")

    def test_15(self):
        number = 15
        word = fino.to_finnish(number)
        self.assertEqual(word, "viisitoista")

    def test_19(self):
        number = 19
        word = fino.to_finnish(number)
        self.assertEqual(word, "yhdeksäntoista")

    def test_20(self):
        number = 20
        word = fino.to_finnish(number)
        self.assertEqual(word, "kaksikymmentä")

    def test_42(self):
        number = 42
        word = fino.to_finnish(number)
        self.assertEqual(word, "neljäkymmentäkaksi")

    def test_85(self):
        number = 85
        word = fino.to_finnish(number)
        self.assertEqual(word, "kahdeksankymmentäviisi")

    def test_99(self):
        number = 99
        word = fino.to_finnish(number)
        self.assertEqual(word, "yhdeksänkymmentäyhdeksän")

    def test_100(self):
        number = 100
        word = fino.to_finnish(number)
        self.assertEqual(word, "sata")

    def test_101(self):
        number = 101
        word = fino.to_finnish(number)
        self.assertEqual(word, "satayksi")

    def test_111(self):
        number = 111
        word = fino.to_finnish(number)
        self.assertEqual(word, "satayksitoista")

    def test_200(self):
        number = 200
        word = fino.to_finnish(number)
        self.assertEqual(word, "kaksisataa")

    def test_827(self):
        number = 827
        word = fino.to_finnish(number)
        self.assertEqual(word, "kahdeksansataakaksikymmentäseitsemän")

    def test_999(self):
        number = 999
        word = fino.to_finnish(number)
        self.assertEqual(word, "yhdeksänsataayhdeksänkymmentäyhdeksän")

    def test_1000(self):
        number = 1000
        word = fino.to_finnish(number)
        self.assertEqual(word, "tuhat")

    def test_1001(self):
        number = 1001
        word = fino.to_finnish(number)
        self.assertEqual(word, "tuhatyksi")

    def test_1234(self):
        number = 1234
        word = fino.to_finnish(number)
        self.assertEqual(word, "tuhatkaksisataakolmekymmentäneljä")

    def test_2161(self):
        number = 2161
        word = fino.to_finnish(number)
        self.assertEqual(word, "kaksituhattasatakuusikymmentäyksi")

    def test_10000(self):
        number = 10000
        word = fino.to_finnish(number)
        self.assertEqual(word, "kymmenentuhatta")

    def test_26712(self):
        number = 26712
        word = fino.to_finnish(number)
        self.assertEqual(word, "kaksikymmentäkuusituhattaseitsemänsataakaksitoista")

    def test_99999(self):
        number = 99999
        word = fino.to_finnish(number)
        self.assertEqual(
            word, "yhdeksänkymmentäyhdeksäntuhattayhdeksänsataayhdeksänkymmentäyhdeksän"
        )

    def test_100000(self):
        number = 100_000
        word = fino.to_finnish(number)
        self.assertEqual(word, "satatuhatta")

    def test_111111(self):
        number = 111_111
        word = fino.to_finnish(number)
        self.assertEqual(word, "satayksitoistatuhattasatayksitoista")

    def test_999999(self):
        number = 999_999
        word = fino.to_finnish(number)
        self.assertEqual(
            word,
            "yhdeksänsataayhdeksänkymmentäyhdeksäntuhatta"
            "yhdeksänsataayhdeksänkymmentäyhdeksän",
        )

    def test_miljoona(self):
        number = 10 ** 6
        word = fino.to_finnish(number)
        self.assertEqual(word, "miljoona")

    def test_5002010(self):
        number = 5_002_010
        word = fino.to_finnish(number)
        self.assertEqual(word, "viisimiljoonaakaksituhattakymmenen")

    def test_999999999(self):
        number = 999_999_999
        word = fino.to_finnish(number)
        self.assertEqual(
            word,
            "yhdeksänsataayhdeksänkymmentäyhdeksänmiljoonaa"
            "yhdeksänsataayhdeksänkymmentäyhdeksäntuhatta"
            "yhdeksänsataayhdeksänkymmentäyhdeksän",
        )

    def test_miljardi(self):
        number = 10 ** 9
        word = fino.to_finnish(number)
        self.assertEqual(word, "miljardi")

    def test_1234567890(self):
        number = 1_234_567_890
        word = fino.to_finnish(number)
        self.assertEqual(
            word,
            "miljardi"
            "kaksisataakolmekymmentäneljämiljoonaa"
            "viisisataakuusikymmentäseitsemäntuhatta"
            "kahdeksansataayhdeksänkymmentä",
        )

    def test_287654321004(self):
        number = 287_654_321_004
        word = fino.to_finnish(number)
        self.assertEqual(
            word,
            "kaksisataakahdeksankymmentäseitsemänmiljardia"
            "kuusisataaviisikymmentäneljämiljoonaa"
            "kolmesataakaksikymmentäyksituhatta"
            "neljä",
        )

    def test_biljoona(self):
        number = 10 ** 12
        word = fino.to_finnish(number)
        self.assertEqual(word, "biljoona")

    def test_2biljoonaa(self):
        number = 2 * 10 ** 12
        word = fino.to_finnish(number)
        self.assertEqual(word, "kaksibiljoonaa")

    def test_4000biljoonaa(self):
        number = 4000 * 10 ** 12
        word = fino.to_finnish(number)
        self.assertEqual(word, "neljätuhattabiljoonaa")

    def test_googol(self):
        number = 10 ** 100
        word = fino.to_finnish(number)
        self.assertEqual(word, "googol")

    def test_8googolia(self):
        number = 8 * 10 ** 100 + 1
        word = fino.to_finnish(number)
        self.assertEqual(word, "kahdeksangoogoliayksi")

    def test_sentiljoona(self):
        number = 10 ** 600
        word = fino.to_finnish(number)
        self.assertEqual(word, "sentiljoona")

    def test_3sentiljoonaa(self):
        number = 3 * 10 ** 600
        word = fino.to_finnish(number)
        self.assertEqual(word, "kolmesentiljoonaa")

    def test_range(self):
        # Just check no errors
        for number in range(0, 100_000):
            word = fino.to_finnish(number)
            self.assertNotEqual(word, "en tiedä")

    def test_print_it(self):
        # Just make sure no exceptions
        fino.print_it("test")


if __name__ == "__main__":
    unittest.main()

# End of file
