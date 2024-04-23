# This file contains a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case


def main():
    camel_case_expression = input("camelCase: ")

    snake_case_expression = ""

    for letter in camel_case_expression:
        if letter == letter.upper():
            if snake_case_expression:
                snake_case_expression += "_"
            snake_case_expression += letter.lower()
        else:
            snake_case_expression += letter

    print("snake_case:", snake_case_expression)


main()
