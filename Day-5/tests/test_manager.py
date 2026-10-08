import pytest
from expense_tracker.manager import ExpenseTracker
from expense_tracker.exceptions import InvalidAmountError, InvalidExpenseError, ExpenseNotFoundError
@pytest.fixture
def tracker(monkeypatch):
    monkeypatch.setattr("expense_tracker.manager.load_expenses", lambda: [])
    monkeypatch.setattr("expense_tracker.manager.save_expenses", lambda expenses: None)
    return ExpenseTracker()

def test_add_expense(tracker):
    tracker.add_expense(500, "Food", "Lunch")
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].amount == 500
    assert tracker.expenses[0].category == "Food"
    assert tracker.expenses[0].description == "Lunch"
    assert tracker.expenses[0].expense_id == 1

def test_add_expense_invalid_amount(tracker):
    with pytest.raises(InvalidAmountError):
        tracker.add_expense(0, "Food", "Lunch")

def test_add_expense_negative_amount(tracker):
    with pytest.raises(InvalidAmountError):
        tracker.add_expense(-100, "Food", "Lunch")

def test_add_expense_empty_category(tracker):
    with pytest.raises(InvalidExpenseError):
        tracker.add_expense(500, "", "Lunch")

def test_add_expense_empty_description(tracker):
    with pytest.raises(InvalidExpenseError):
        tracker.add_expense(500, "Food", "")

def test_find_expense(tracker):
    tracker.add_expense(500, "Food", "Lunch")
    result = tracker.find_expense(1)
    assert result.expense_id == 1
    assert result.amount == 500
    assert result.category == "Food"
    assert result.description == "Lunch"

def test_find_expense_not_found(tracker):
    with pytest.raises(ExpenseNotFoundError):
        tracker.find_expense(999)

def test_update_expense(tracker):
    tracker.add_expense(500, "Food", "Lunch")
    tracker.update_expense(1, 800, "Shopping", "New shoes")
    result = tracker.find_expense(1)
    assert result.amount == 800
    assert result.category == "Shopping"
    assert result.description == "New shoes"

def test_update_expense_not_found(tracker):
    with pytest.raises(ExpenseNotFoundError):
        tracker.update_expense(999, 800, "Shopping", "New shoes")

def test_update_expense_invalid_amount(tracker):
    tracker.add_expense(500, "Food", "Lunch")
    with pytest.raises(InvalidAmountError):
        tracker.update_expense(1, 0, "Shopping", "New shoes")

def test_update_expense_empty_category(tracker):
    tracker.add_expense(500, "Food", "Lunch")
    with pytest.raises(InvalidExpenseError):
        tracker.update_expense(1, 800, "", "New shoes")
        
def test_delete_expense(tracker):
    tracker.add_expense(500, "Food", "Lunch")
    tracker.delete_expense(1)
    assert len(tracker.expenses) == 0

def test_delete_expense_not_found(tracker):
    with pytest.raises(ExpenseNotFoundError):
        tracker.delete_expense(999)

def test_export_csv(tracker, monkeypatch, tmp_path):
    csv_file = tmp_path / "expenses.csv"
    def fake_export_to_csv(expenses):
        with open(csv_file, "w", newline="", encoding="utf-8") as file:
            file.write("expense_id,amount,category,description,date\n")
            for expense in expenses:
                file.write(
                    f"{expense.expense_id},"
                    f"{expense.amount},"
                    f"{expense.category},"
                    f"{expense.description},"
                    f"{expense.date}\n"
                )
    monkeypatch.setattr("expense_tracker.manager.export_to_csv", fake_export_to_csv)
    tracker.add_expense(500, "Food", "Lunch")
    tracker.export_csv()
    assert csv_file.exists()
    content = csv_file.read_text(encoding="utf-8")
    assert "expense_id,amount,category,description,date" in content
    assert "1,500,Food,Lunch" in content