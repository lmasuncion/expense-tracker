# Project: Expense Tracker | Installment 5
# Author : Luis Miguel A. Asuncion
# Expense Tracker for your expenses

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your everyday expenses")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print("\t[1] Add an expense\t(coming soon)")
    print("\t[2] View all expenses\t(coming soon)")
    print("\t[3] Show total spent\t(coming soon)")
    print("\t[4] Exit\t\t(coming soon)")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    elif choice == "2":
        print (" Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total
        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal}")
        print(f"  Tax ({tax_percent}%):\t${tax}")
        print(f"  Grand total:\t${total}")
        if over_budget:
            print(f"  Over budget by ${total - budget}!")
        elif total > budget * 0.9: 
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
    else:
        print("  Please choose 1, 2, 3, or 4.")

print("-" * 40)
print("Made by: Luis Miguel A. Asuncion | Installment 5")
print("=" * 40)