#!/usr/bin/env python
# encoding: utf-8
"""
Given an integer, output the Finnish word for that number.
"""
from __future__ import print_function, unicode_literals
import argparse

# https://fi.wikipedia.org/wiki/Suurten_lukujen_nimet

MAX_INTEGER_SUPPORTED = 10**18-1


POWERS_OF_TEN = {
    100: "sata",
    1000: "tuhat",
    10**6: "miljoona",
    10**9: "miljardi",
    10**12: "biljoona",
}
POWERS_OF_TEN_PARTITIVE_SUFFIXES = {
    100: "a",
    1000: "ta",
    10**6: "a",
    10**9: "a",
    10**12: "a",
}


def less_than_ten(number):
    if number == 0:
        return "nolla"
    elif number == 1:
        return "yksi"
    elif number == 2:
        return "kaksi"
    elif number == 3:
        return "kolme"
    elif number == 4:
        return "neljä"
    elif number == 5:
        return "viisi"
    elif number == 6:
        return "kuusi"
    elif number == 7:
        return "seitsemän"
    elif number == 8:
        return "kahdeksan"
    elif number == 9:
        return "yhdeksän"


def ten_to_nineteen(number):
    if number == 10:
        return "kymmenen"
    else:
        return less_than_ten(number % 10) + "toista"


def twenty_to_ninetynine(number):
    d, m = divmod(number, 10)
    word = less_than_ten(d) + "kymmentä"
    if m > 0:
        word += less_than_ten(m)
    return word


def wordify(number, power_of_ten):
    unit_text = POWERS_OF_TEN[power_of_ten]
    partitive_suffix = POWERS_OF_TEN_PARTITIVE_SUFFIXES[power_of_ten]

    if number == power_of_ten:
        return unit_text
    d, m = divmod(number, power_of_ten)
    if d > 1:
        word = to_finnish(d) + unit_text + partitive_suffix
    else:
        word = unit_text
    if m > 0:
        word += to_finnish(m)
    return word


def to_finnish(number):
    if number >= 0 and number < 10:
        return less_than_ten(number)
    elif number >= 10 and number <= 19:
        return ten_to_nineteen(number)
    elif number >= 20 and number <= 99:
        return twenty_to_ninetynine(number)
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
        print(len(to_finnish(args.number)), to_finnish(args.number))
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
