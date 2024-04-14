# This file contains a fucntion which prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time


def main():
    meal_time = input("What time is it? ")
    converted_time = convert(meal_time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        return


def convert(meal_time):
    hours, minutes = meal_time.split(":")
    return float(hours) + float(minutes) / 60.0


if __name__ == "__main__":
    main()
