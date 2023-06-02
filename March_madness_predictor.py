import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loads the CSV data into a pandas DataFrame so it can be manipulated
df = pd.read_csv('March Madness Data/2023 Game Data.csv')

# The 5 categories that we are evaluating 
selected_features = ['Kenpom adjusted efficiency', 'BARTTORVIK ADJUSTED EFFICIENCY', 
                     'EFG %', 'DEFENSE, EFG', 'POINTS PER POSSESSION OFFENSE', 
                     'POINTS PER POSSESSION DEFENSE']

# Now create a new dataframe with the most valuable feautures
df_X = df[selected_features]

# Assuming 'target' is the name of your target column
if 'target' in df.columns:
    df_y = df['target']
else:
    df_y = None  # Set the target variable to None or any appropriate default value

# Split the data into a training set and a test set. This will likely be a statistic and the output of that statistic
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=42)

# Creates an instance of the model
lr = LogisticRegression()

# Trains the model to observe accuracy
lr.fit(X_train, y_train)

# Makes predictions on the test set to see how effective it is 
predictions = lr.predict(X_test)

# Print the accuracy
print("Accuracy: ", accuracy_score(y_test, predictions))
