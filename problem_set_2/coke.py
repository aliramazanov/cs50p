# This file contains a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.


def amount(total_amount):
    while True:
        print(f"Amount Due: {total_amount}")
        amount_due = int(input("Insert Coin: "))
        if amount_due in [5, 10, 25]:
            return amount_due
        else:
            print("Invalid amount! Enter (5, 10, or 25).")


def main():
    total_amount = 0
    while total_amount < 50:
        amount_due = amount(50 - total_amount)
        total_amount += amount_due
        if total_amount > 50:
            print("Change Owed:", total_amount - 50)
            break
    else:
        print("Change Owed: 0")


if __name__ == "__main__":
    main()
