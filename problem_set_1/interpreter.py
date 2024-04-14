# This file contains a function which prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place


def main():
    expression = input("Expression: ")
    x, y, z = expression.split()

    x = float(x)
    z = float(z)

    if y == "+":
        calculation = x + z
    elif y == "-":
        calculation = x - z
    elif y == "*":
        calculation = x * z
    elif y == "/":
        calculation = x / z
    else:
        print("Invalid operator")
        return

    print(f"Result: {calculation:.1f}")


main()
