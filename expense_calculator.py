# ==========================================
# Python Utility Tool - Expense Calculator
# ==========================================

def get_positive_number(message):
    """Get a valid positive number from the user."""
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("❌ Please enter a number greater than 0.")
            else:
                return value

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def get_expense_name():
    """Get a valid expense name."""
    while True:
        name = input("Enter expense name: ").strip()

        if name:
            return name

        print("❌ Expense name cannot be empty.")


def add_expense(expenses):
    """Add a new expense."""
    name = get_expense_name()
    amount = get_positive_number("Enter amount: ₹")

    expenses.append({
        "name": name,
        "amount": amount
    })

    print(f"✅ Expense '{name}' added successfully!")


def show_expenses(expenses):
    """Display all expenses."""
    if not expenses:
        print("\n📭 No expenses added yet.")
        return

    print("\n========== EXPENSES ==========")

    total = 0

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']:.2f}")
        total += expense["amount"]

    print("------------------------------")
    print(f"Total Expense: ₹{total:.2f}")


def calculate_total(expenses):
    """Calculate total expense."""
    return sum(expense["amount"] for expense in expenses)


def show_summary(expenses):
    """Display expense summary."""
    if not expenses:
        print("\n📭 No expenses available.")
        return

    total = calculate_total(expenses)
    average = total / len(expenses)

    print("\n========== SUMMARY ==========")
    print(f"Number of Expenses : {len(expenses)}")
    print(f"Total Expense      : ₹{total:.2f}")
    print(f"Average Expense    : ₹{average:.2f}")


def main():
    expenses = []

    while True:
        print("\n================================")
        print("      EXPENSE CALCULATOR")
        print("================================")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Summary")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_summary(expenses)

        elif choice == "4":
            print("\n👋 Thank you for using Expense Calculator!")
            break

        else:
            print("❌ Invalid choice! Please select 1, 2, 3 or 4.")


# Program starts here
if __name__ == "__main__":
    main()