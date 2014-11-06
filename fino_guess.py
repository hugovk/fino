#!/usr/bin/env python
# encoding: utf-8
"""
Guess the number.
"""
from __future__ import print_function, unicode_literals
import argparse
import random
import fino
import sys

try:
   input = raw_input  # raw_input in Py2 == input in Py3
except NameError:
   pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Guess the number.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--limit',
                        type=int, default=1000000,
                        help="Upper limit")
    parser.add_argument('-g', '--guesses',
                        type=int, default=3,
                        help="Number of guesses allowed")
    args = parser.parse_args()

    number = random.randrange(args.limit+1)
    print("What is " + fino.to_finnish(number) + "?")
    # print(number)

    while(True):
        guess = raw_input()
        if str(guess) == str(number):
            print("Yes!")
            break
        else:
            print("No!")
            args.guesses -= 1
            if args.guesses > 0:
                print("Guess again!")
            else:
                print(number)
                break


# End of file
