import pandas as pd
from scipy import stats
import numpy as np

class BookkeepingService:

    def __init__(self):
        self.expenses = pd.DataFrame(columns=['expense', 'category', 'amount'])

    def add_expense(self, expense, category, amount):
        self.expenses = self.expenses.append({'expense': expense, 'category': category, 'amount': amount}, ignore_index=True)
    
    def track_expenses(self):
        return self.expenses.groupby('category').sum()

    def detect_unusual_expenses(self, threshold=2):
        self.expenses['z_score'] = np.abs(stats.zscore(self.expenses['amount']))
        unusual_expenses = self.expenses[self.expenses['z_score'] > threshold]
        return unusual_expenses


# To use this service
service = BookkeepingService()

service.add_expense('Rent', 'Housing', 1000)
service.add_expense('Electricity', 'Utilities', 150)
service.add_expense('Internet', 'Utilities', 80)
service.add_expense('Groceries', 'Food', 200)
service.add_expense('Restaurant', 'Food', 500)

print(service.track_expenses())
print(service.detect_unusual_expenses())

