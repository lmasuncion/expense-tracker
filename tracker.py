# Project: Expense Tracker | Installment 2
# Author : Luis Miguel A. Asuncion
# Expense Tracker for your expenses

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your everyday expenses")
print("=" * 40)

print("MAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("\nFirst expense: ")
amount1 = float(input("Amount: "))

item2 = input("Second expense: ")
amount2 = float(input("Amount: "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"\t{item1}:\t\t${amount1}")
print(f"\t{item2}:\t\t${amount2}")
print(f"\tTotal spent:\t${total}")
print(f"\tAverage:\t${average}")
print("-" * 40)

print("-" * 40)
print("Made by: Luis Miguel A. Asuncion | Installment 2")
print("=" * 40)