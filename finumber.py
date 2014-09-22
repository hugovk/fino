#!/usr/bin/env python
# encoding: utf-8
"""
Given an integer, output the Finnish word for that number.
"""
from __future__ import print_function, unicode_literals
import argparse

# https://fi.wikipedia.org/wiki/Suurten_lukujen_nimet

MAX_INTEGER_SUPPORTED = 999999999


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


def hundred_to_999(number):
    if number == 100:
        return "sata"
    d, m = divmod(number, 100)
    if d > 1:
        word = less_than_ten(d) + hundred_to_999(100) + "a"
    else:
        word = hundred_to_999(100)
    if m > 0:
        word += to_finnish(m)
    return word


def thousand_to_999999(number):
    if number == 1000:
        return "tuhat"
    d, m = divmod(number, 1000)
    if d > 1:
        word = to_finnish(d) + thousand_to_999999(1000) + "ta"
    else:
        word = thousand_to_999999(1000)
    if m > 0:
        word += to_finnish(m)
    return word


def million_to_999999999(number):
    if number == 1000000:
        return "miljoona"
    d, m = divmod(number, 1000000)
    if d > 1:
        word = to_finnish(d) + million_to_999999999(1000000) + "a"
    else:
        word = million_to_999999999(1000000)
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
        return hundred_to_999(number)
    elif number >= 1000 and number <= 999999:
        return thousand_to_999999(number)
    elif number >= 1000000 and number <= 999999999:
        return million_to_999999999(number)
    else:
        return "en tiedä"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Given an integer, "
                    "output the Finnish word for that number.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('number', type=int, help="An input integer")
    parser.add_argument(
        'end', type=int, nargs='?',
        help="An optional end integer. Prints all numbers from the first one "
             "up to this one.")
    args = parser.parse_args()

    if not args.end:
        print(to_finnish(args.number))
    else:
        for i in range(args.number, args.end+1):
            print(i, to_finnish(i))

# End of file
