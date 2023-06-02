import pandas as pd
from sklearn.cluster import KMeans
#Import neccesary packages that allow program to automate the processes
#Class contains all the main operations of the algorithm
class BookkeepingService:

    def __init__(self):
        # We can initialize an empty DataFrame to keep track of expenses
        self.expenses = pd.DataFrame(columns=['expense', 'category', 'amount'])

    def add_expense(self, expense, category, amount):
        # We can add a new expense to the DataFrame
        self.expenses = self.expenses.append({'expense': expense, 'category': category, 'amount': amount}, ignore_index=True)
    
    def track_expenses(self):
        # Let's summarize expenses by category
        return self.expenses.groupby('category').sum()

    def detect_unusual_expenses(self, clusters=3):
        # Let's use KMeans clustering to group expenses and detect any unusual expenses (outliers)
        model = KMeans(n_clusters=clusters, random_state=42)
        self.expenses['cluster'] = model.fit_predict(self.expenses[['amount']])
        
        # Any cluster with significantly fewer expenses might be considered 'unusual'
        cluster_counts = self.expenses['cluster'].value_counts()
        unusual_clusters = cluster_counts[cluster_counts < cluster_counts.mean()].index
        
        return self.expenses[self.expenses['cluster'].isin(unusual_clusters)]


# To use this service
service = BookkeepingService()

service.add_expense('Rent', 'Housing', 1000)
service.add_expense('Electricity', 'Utilities', 150)
service.add_expense('Internet', 'Utilities', 80)
service.add_expense('Groceries', 'Food', 200)
service.add_expense('Restaurant', 'Food', 500)

print(service.track_expenses())
print(service.detect_unusual_expenses())
