from .storage import save_expenses, load_expenses, export_to_csv
from .exceptions import InvalidExpenseError, InvalidAmountError, ExpenseNotFoundError
from .models import Expense
from .logger import logger

class ExpenseTracker():
    def __init__(self):
        self.expenses = load_expenses()
        if not self.expenses:
            last_id = 0
        else:
            last_id = max(self.expenses, key=lambda expense: expense.expense_id).expense_id
            
        self.next_id = last_id

    def add_expense(self, amount, category, description):
        if amount <= 0:
            logger.warning(f"Invalid amount: {amount}")
            raise InvalidAmountError("Amount must be greater than 0.")
        if category.strip() == "" or description.strip() == "":
            logger.warning(f"Invalid information \nCategory: {category} \nDescription: {description}")
            raise InvalidExpenseError("Data cannot be empty.")
        self.next_id += 1
        new_expense = Expense(self.next_id, amount, category, description)
        self.expenses.append(new_expense)
        logger.info(f"Expense added successfully: ID {self.next_id}")
        save_expenses(self.expenses)
    
    def view_expenses(self):
        return self.expenses
    
    def find_expense(self, expense_id):
        for expense in self.expenses:
            if expense_id == expense.expense_id:
                return expense
        logger.warning(f"Expense not found: ID {expense_id}")
        raise ExpenseNotFoundError("Cannot find expense.")
    
    def update_expense(self, expense_id, amount, category, description):
        for expense in self.expenses:
            if expense_id == expense.expense_id:
                if amount <= 0:
                    logger.warning(f"Invalid amount: {amount}")
                    raise InvalidAmountError("Amount must be greater than 0.")
                if category.strip() == "" or description.strip() == "":
                    logger.warning(f"Invalid information \nCategory: {category} \nDescription: {description}")
                    raise InvalidExpenseError("Data cannot be empty.")
                expense.amount = amount
                expense.category = category
                expense.description = description
                save_expenses(self.expenses)
                logger.info(f"Expense updated successfully: ID {expense_id}")
                return self.expenses
        logger.warning(f"Expense not found: ID {expense_id}")
        raise ExpenseNotFoundError("Cannot find expense.")
    
    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense_id == expense.expense_id:
                self.expenses.remove(expense)
                save_expenses(self.expenses)
                logger.info(f"Expense deleted successfully: ID {expense_id}")
                return self.expenses
        logger.warning(f"Expense not found: ID {expense_id}")
        raise ExpenseNotFoundError("Cannot find expense.")
    
    def export_csv(self):
        return export_to_csv(self.expenses)