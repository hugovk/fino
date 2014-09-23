#!/usr/bin/env python
# encoding: utf-8
"""
Given an integer, output the Finnish word for that number.
"""
from __future__ import print_function, unicode_literals
import argparse

# https://fi.wikipedia.org/wiki/Suurten_lukujen_nimet

MAX_INTEGER_SUPPORTED = 10**18-1

LESS_THAN_TEN = {
    0: "nolla",
    1: "yksi",
    2: "kaksi",
    3: "kolme",
    4: "neljä",
    5: "viisi",
    6: "kuusi",
    7: "seitsemän",
    8: "kahdeksan",
    9: "yhdeksän"
}
SINGULAR_TENS = {
    10: "kymmenen",
    100: "sata",
    1000: "tuhat",
    10**6: "miljoona",
    10**9: "miljardi",
    10**12: "biljoona",
}
# Just the few which don't have a simple -a partitive suffix
PLURAL_TENS = {
    10: "kymmentä",
    1000: "tuhatta",
}


def wordify(number, tens):
    if number == tens:
        return SINGULAR_TENS[tens]
    d, m = divmod(number, tens)
    if d > 1:
        if tens in PLURAL_TENS:
            plural = PLURAL_TENS[tens]
        else:
            plural = SINGULAR_TENS[tens] + "a"
        word = to_finnish(d) + plural
    else:
        word = SINGULAR_TENS[tens]
    if m > 0:
        word += to_finnish(m)
    return word


def to_finnish(number):
    if number >= 0 and number < 10:
        return LESS_THAN_TEN[number]
    elif number >= 11 and number <= 19:
        return LESS_THAN_TEN[number % 10] + "toista"
    elif number == 10 or number >= 20 and number <= 99:
        return wordify(number, 10)
    elif number >= 100 and number <= 999:
        return wordify(number, 100)
    elif number >= 10**3 and number <= 10**6-1:
        return wordify(number, 10**3)
    elif number >= 10**6 and number <= 10**9-1:
        return wordify(number, 10**6)
    elif number >= 10**9 and number <= 10**12-1:
        return wordify(number, 10**9)
    elif number >= 10**12 and number <= 10**18-1:
        return wordify(number, 10**12)
    else:
        return "en tiedä"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Given an integer, "
                    "output the Finnish word for that number.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('number', type=int, help="An input integer")
    parser.add_argument(
        'end', nargs='?',  # type=int,
        help="An optional end integer. Prints all numbers from the first one "
             "up to this one. Use 'max' for the maximum supported integer.")
    args = parser.parse_args()

    if not args.end:
        print(to_finnish(args.number))
    else:
        if args.end == "max":
            end = MAX_INTEGER_SUPPORTED
        else:
            end = int(args.end)
        i = args.number
        while(i < end+1):
            print(i, to_finnish(i))
            i += 1

# End of file
