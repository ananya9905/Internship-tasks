# Expense Tracker

A simple Python-based Expense Tracker application for managing personal expenses.

The application allows users to add, view, find, update, and delete expenses. Expense data is stored in JSON format, and users can export their expenses to CSV format.

## Features

- Add new expenses
- View all expenses
- Find an expense using its ID
- Update existing expenses
- Delete expenses
- Store expense data in JSON
- Export expenses to CSV
- Custom exception handling
- Application logging
- Automated testing using pytest
- Modular Python package structure
- Virtual environment support

## Technologies Used

- Python
- JSON
- CSV
- pathlib
- dataclasses
- logging
- pytest

## Project Structure

```text
Expense_tracker/
│
├── data/
│   ├── expenses.json
│   └── expenses.csv
│
├── expense_tracker/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── main.py
│   ├── manager.py
│   ├── models.py
│   └── storage.py
│
├── logs/
│   └── app.log
│
├── tests/
│   ├── __init__.py
│   └── test_manager.py
│
├── venv/
├── .gitignore
├── README.md
└── requirements.txt