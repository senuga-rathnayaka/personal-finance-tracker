import json
from datetime import datetime

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    try:
        with open("Transactions.json", "r") as file:
            transactions.extend(json.load(file))
    except FileNotFoundError:
        print("Transactions file not found. Starting with an empty transaction list.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty transaction list.")

def save_transactions():
    with open("Transactions.json", "w") as file:
        file.write("[")
        file.write("\n")
        for transaction in transactions:
            file.write("\t")
            json.dump(transaction, file)
            file.write("\n")
        file.write("]")

# Validation functions
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Feature implementations
def add_transaction():
    while True:
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            while True:
                transaction_type = input("Enter type (Income/Expense): ").capitalize()
                if transaction_type in ["Income","Expense"]:
                    break
                else:
                    print("Invalid transaction type")
            date = input("Enter date (YYYY-MM-DD): ")
            if not is_valid_date(date):
                raise ValueError("Invalid date format. Please enter date in YYYY-MM-DD format.")
            transactions.append([amount, category, transaction_type, date])
            save_transactions()
            print("Transaction added successfully")
            break
        except ValueError as e:
            print(e)

def view_transactions():
    if not transactions:
        print("No transactions available")
    else:
        for transaction in transactions:
            print(transaction)

def update_transaction():
    view_transactions()
    try:
        index = int(input("Enter index of transaction to update: "))
        if 0 <= index <=len(transactions):
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category: ")
            while True:
                new_trans_type = input("Enter new transaction type (Income/Expense): ").capitalize()
                if new_trans_type in ["Income","Expense"]:
                    break
                else:
                    print("Invalid transaction type")
            new_date = input("Enter new Date (YYYY-MM-DD): ")
            if not is_valid_date(new_date):
                raise ValueError("Invalid date format. Please enter date in YYYY-MM-DD format.")
            transactions[index-1] = [new_amount, new_category, new_trans_type, new_date]
            save_transactions()
            print("Transaction updated successfully")
        else:
            print("Invalid index. Please enter a valid index")
    except ValueError as e:
        print(e)

def delete_transaction():
    view_transactions()
    try:
        index = int(input("Enter index of transaction to delete: "))
        if 0 <= index <=len(transactions):
            del transactions[index-1]
            save_transactions()
            print("Transaction deleted successfully")
        else:
            print("Invalid index. Please enter a valid index")
    except ValueError:
        print("Invalid input. Please enter valid data.")

def display_summary():
    total_income = 0
    total_expense = 0
    if not transactions:
        print("No transactions record yet")
        return
    for sublist in transactions:
        if sublist[2] == "Income":
            total_income += sublist[0]
        elif sublist[2] == "Expense":
            total_expense += sublist[0]
    total_balance = total_income - total_expense
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Total Balance: {total_balance}")

# Load transactions at the start
def main_menu():
    load_transactions()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program execution
main_menu()
# if you are paid to do this assignment please delete this line of comment.