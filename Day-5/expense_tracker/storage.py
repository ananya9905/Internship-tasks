import json, csv
from pathlib import Path
from dataclasses import asdict
from .models import Expense
from datetime import date

path = Path("data/expenses.json")

def expense_encode(expense):
    return asdict(expense)

def save_expenses(expenses):
    expense_list = []
    with open(path, "w") as file:
        for expense in expenses:
            encoded = expense_encode(expense)
            encoded["date"] = encoded["date"].isoformat()
            expense_list.append(encoded)
        json.dump(expense_list, file, indent=4)
        
def load_expenses():
    json_list = []
    with open(path, "r") as file:
        datas = json.load(file)
        for data in datas:
            data["date"] = date.fromisoformat(data["date"])
            json_list.append(Expense(**data))
        return json_list
    
def export_to_csv(expenses):
    path = Path("data/expenses.csv")
    with open(path, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["expense_id", "amount", "category", "description", "date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            encoded = expense_encode(expense)
            encoded["date"] = encoded["date"].isoformat()
            writer.writerow(encoded)