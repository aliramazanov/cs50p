# This file contains a function to simulate slower playback by adding ellipses between words.


def main():
    # Prompt the user to input a phrase
    sentence = input("Enter a sentence: ")

    # Replace spaces with ellipses
    slowed_down_phrase = sentence.replace(" ", "...")

    print("Slowed for you:", slowed_down_phrase)


main()
