#!/usr/bin/env python
"""
Guess the number.
"""
import argparse
import random
import fino


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Guess the number.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-l", "--limit", type=int, default=1_000_000, help="Upper limit"
    )
    parser.add_argument(
        "-g", "--guesses", type=int, default=3, help="Number of guesses allowed"
    )
    args = parser.parse_args()

    number = random.randrange(args.limit + 1)
    print("What is " + fino.to_finnish(number) + "?")
    # print(number)

    while True:
        guess = input()
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
