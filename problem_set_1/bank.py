# This file contains a function for user input (greeting).
# If the greeting starts with “hello”, it will output $0.
# If the greeting starts with an “h” (but not “hello”), it will output $20.
# Otherwise, it will output $100.


def main():
    greeting = input("Greeting: ").strip().lower()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
