#!/usr/bin/env python3
# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if u got the right random number


def main():
    # this program checks if a letter is uppercase or lowercase

    # input
    letter = input("Enter a Letter :")
    # process

    if(letter >= 'A' and letter <= 'Z'):
        print(letter, "is an UpperCase character")
    elif (letter >= 'a' and letter <= 'z'):
        print(letter, "is an LowerCase character")
    else:
        print("This is not a letter ")


if __name__ == "__main__":
    main()
