import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('March Madness Data/2023 Game Data.csv')

# The 5 categories that you want to use
selected_features = ['Kenpom adjusted efficiency', 'BARTTORVIK ADJUSTED EFFICIENCY', 
                     'EFG %', 'DEFENSE, EFG', 'POINTS PER POSSESSION OFFENSE', 
                     'POINTS PER POSSESSION DEFENSE']

# Now create a new dataframe with only the selected features
df_X = df[selected_features]

# Assuming 'target' is the name of your target column
if 'target' in df.columns:
    df_y = df['target']
else:
    df_y = None  # Set the target variable to None or any appropriate default value

# Split the data into a training set and a test set.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=42)

# Create an instance of the model
lr = LogisticRegression()

# Train the model
lr.fit(X_train, y_train)

# Make predictions on the test set
predictions = lr.predict(X_test)

# Print the accuracy
print("Accuracy: ", accuracy_score(y_test, predictions))
