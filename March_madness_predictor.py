import pandas as pd 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('March Madness Data/2023 Game Data.csv')

# Data cleaning, preprocessing, and feature engineering code here...

# The 5 categories that you want to use
selected_features = ['KENPOM ADJUSTED EFFICIENCY', 'BARTTORVIK ADJUSTED EFFICIENCY', 
                     'EFG %', 'EFG % DEFENSE', 'POINTS PER POSSESSION OFFENSE', 
                     'POINTS PER POSSESSION DEFENSE']

df_X = df[selected_features]

if 'target' in df.columns:
    df_y = df['target']
else:
    df_y = None

# Standardize the features
scaler = StandardScaler()
df_X = scaler.fit_transform(df_X)

# Split the data into a training set and a test set.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=42)

# Define the model
rf = RandomForestClassifier()

# Define hyperparameters for grid search
param_grid = {
    'n_estimators': [100, 200, 500],
    'max_features': ['auto', 'sqrt'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}

# Initialize grid search
grid_search = GridSearchCV(rf, param_grid, cv=5)

# Fit the model
grid_search.fit(X_train, y_train)

# Make predictions on the test set
predictions = grid_search.predict(X_test)

# Print the accuracy
print("Accuracy: ", accuracy_score(y_test, predictions))

# Print the confusion matrix and classification report for additional insights
print(classification_report(y_test, predictions))

