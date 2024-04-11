# This file contains a function for calculating tips based on the meal cost and desired tip percentage.


def main():
    meal_cost = dollars_to_float(input("How much was the meal? "))
    tip_percentage = percent_to_float(input("What percentage would you like to tip? "))

    tip_amount = meal_cost * tip_percentage

    # Print the tip amount with two decimal places
    print(f"Leave ${tip_amount:.2f} as tip.")


def dollars_to_float(dollars_str):
    # Remove the dollar sign and convert to float
    dollars_num = float(dollars_str.replace("$", ""))
    return dollars_num


def percent_to_float(percent_str):
    # Remove the percentage sign and convert to float
    percent_num = float(percent_str.replace("%", "")) / 100
    return percent_num


main()
