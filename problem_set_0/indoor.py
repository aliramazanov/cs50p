# This file contains a function, which you can use to lower voices of people who yell


def main():
    # Prompt the user to input a uppercase word
    shouted_phrase = input("Yell: ")

    # Convert the input to lowercase
    lowered_phrase = shouted_phrase.lower()

    print("Echo:", lowered_phrase)


main()
