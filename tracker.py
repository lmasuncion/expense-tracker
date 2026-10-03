# Project: Expense Tracker | Installment 3
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

subtotal = 0

item1 = input("\nFirst expense: ")
amount1 = float(input("Amount: "))
subtotal += amount1

item2 = input("Second expense: ")
amount2 = float(input("Amount: "))
subtotal += amount2

average = subtotal / 2

tax_percent = int(input("Tax rate%? "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f"\t{item1}:\t\t${amount1}")
print(f"\t{item2}:\t\t${amount2}")
print(f"\tSubtotal:\t${subtotal}")
print(f"\tAverage:\t${average}")
print(f"\tTax ({tax_percent}%):\t${tax}")
print(f"\tGrand total:\t${total}")
print(f"\tOver budget?\t{over_budget}")
print(f"\tLeft in budget:\t${left}")
print("-" * 40)

print("-" * 40)
print("Made by: Luis Miguel A. Asuncion | Installment 3")
print("=" * 40)