from dataclasses import dataclass, field
from datetime import date

@dataclass
class Expense:
    expense_id: int
    amount: float
    category: str
    description: str
    date: date = field(default_factory=date.today)
    