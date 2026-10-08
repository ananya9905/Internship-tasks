from .manager import ExpenseTracker
from .exceptions import InvalidAmountError, ExpenseNotFoundError, InvalidExpenseError

expense = ExpenseTracker()

while True:
    print("========== EXPENSE TRACKER ==========")
    print("1. Add Expense\n2. View Expenses\n3. Find Expense\n4. Update Expense\n5. Delete Expense\n6. Export Expenses to CSV\n7. Exit")
    try:
        user = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Choice. Please enter a number.")
        continue
    
    if user == 1:
        try:
            amount = int(input("Enter amount of expense: "))
            category = input("Enter category of the expense: ")
            description = input("Enter the description of the expense: ")
            expense.add_expense(amount, category, description)
            print("Expenses Added Successfully...")
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        except InvalidAmountError as error:
            print(error)
        except InvalidExpenseError as error:
            print(error)
            
    elif user == 2:
        result = expense.view_expenses()
        if not result:
            print("No Expense Available.")
        else:
            for data in result:
                print(f"{data.expense_id} | {data.amount} | {data.category} | {data.description} | {data.date}")
    
    elif user == 3:
        try:
            expense_id = int(input("Enter Expense ID to find: "))
            result = expense.find_expense(expense_id)
            print(f"\nExpense ID: {result.expense_id}\nAmount: {result.amount}\nCategory: {result.category}\nDescription: {result.description}\nDate: {result.date}")
        except ExpenseNotFoundError as error:
            print(error)
        except ValueError:
            print("Invalid Expense ID. Please enter a valid Expense ID.")
            
    elif user == 4:
        try:
            expense_id = int(input("Enter Expense ID to be updated: "))
            amount = int(input("Enter updated amount: "))
            category = input("Enter updated category: ")
            description = input("Enter updated description: ")
            expense.update_expense(expense_id, amount, category, description)
            print("Expense Updated Successfully.")
        except ExpenseNotFoundError as error:
            print(error)
        except InvalidExpenseError as error:
            print(error)
        except InvalidAmountError as error:
            print(error)
        except ValueError:
            print("Please enter a valid number.")
            
    elif user == 5:
        try: 
            expense_id = int(input("Enter Expense ID to be deleted: "))
            expense.delete_expense(expense_id)
            print("Expense Deleted Successfully.")
        except ExpenseNotFoundError as error:
            print(error)
        except ValueError:
            print("Invalid Expense ID. Please enter a valid Expense ID.")
            
    elif user == 6:
        expense.export_csv()
        print("Expenses exported to CSV successfully.")
        
    elif user == 7:
        break
    
    else:
        print("Invalid choice...")