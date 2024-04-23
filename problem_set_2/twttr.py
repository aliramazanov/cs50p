# This file contains a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

from typing import List

vowels: List[str] = ["a", "e", "i", "o", "u"]


def remove_vowels(tweet: str) -> str:
    tweet_without_vowels: str = ""
    for char in tweet:
        if char.lower() not in vowels:
            tweet_without_vowels += char
    return tweet_without_vowels


def main() -> None:
    tweet: str = input("Input: ")
    tweet_without_vowels: str = remove_vowels(tweet)
    print("Tweet without vowels:", tweet_without_vowels)


if __name__ == "__main__":
    main()
