import pandas as pd 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import csv
# Load the CSV data into a pandas DataFrame
df = pd.read_csv('2023 Game Data.csv')

# Added Code that finds correct matchups for round of 32, 16, and 8
teams_dict = {}
count = 2

with open('2023 Game Data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        team = row['TEAM']
        teams_dict[count] = team
        count += 1


dictionary = {}

for i in range(1, 9):
    dictionary[i] = 17 - i


# Define the target values
target_values = ["Alabama", "Maryland"]

round_32 = {"South" : [(1, 8), (5, 13), (6, 3), (7, 15)],
            "East" : [(9, 16), (4, 5), (3, 6), (2, 7)],
            "Midwest" : [(1, 9), (4, 5), (3, 11), (2, 10)],
            "West" : [(1, 8), (4, 5), (3, 6), (2, 7)]
           }

round_16 = {"South" : [(1, 5), (6, 15)],
            "East" : [(4, 9), (3, 7)],
            "Midwest" : [(1, 5), (2, 3)],
            "West" : [(4, 8), (2, 3)]
            }

round_8 = { "South" : [(5, 6)],
            "East" : [(3, 9)],
            "Midwest" : [(2, 5)],
            "West" : [(3, 4)]
            }

final_four = {
        "South vs. East" : (5, 9),
        "Midwest vs. West": (4, 5)
}

South_schools = {
    'Alabama': 1,
    'Arizona': 2,
    'Baylor': 3,
    'Virginia': 4,
    'San Diego St.': 5,
    'Creighton': 6,
    'Missouri': 7,
    'Maryland': 8,
    'West Virginia': 9,
    'Utah St.': 10,
    'North Carolina St.': 11,
    'College of Charleston': 12,
    'Furman': 13,
    'UC Santa Barbara': 14,
    'Princeton': 15,
    'Texas A&M Corpus Chris': 16
}

East_schools = {
    'Purdue': 1,
    'Marquette': 2,
    'Kansas St.': 3,
    'Tennessee': 4,
    'Duke': 5,
    'Kentucky': 6,
    'Michigan St.': 7,
    'Memphis': 8,
    'Florida Atlantic': 9,
    'USC': 10,
    'Providence': 11,
    'Oral Roberts': 12,
    'Louisiana Lafayette': 13,
    'Montana St.': 14,
    'Vermont': 15,
    'Fairleigh Dickinson': 16
}
Midwest_schools = {
    'Houston': 1,
    'Texas': 2,
    'Xavier': 3,
    'Indiana': 4,
    'Miami FL': 5,
    'Iowa St.': 6,
    'Texas A&M': 7,
    'Iowa': 8,
    'Auburn': 9,
    'Penn St.': 10,
    'Pittsburgh': 11,
    'Drake': 12,
    'Kent St.': 13,
    'Kennesaw St.': 14,
    'Colgate': 15,
    'Northern Kentucky': 16
}
smaries = "Saint Mary's"
West_schools = {
    'Kansas': 1,
    'UCLA': 2,
    'Gonzaga': 3,
    'Connecticut': 4,
    f'{smaries}': 5,
    'TCU': 6,
    'Northwestern': 7,
    'Arkansas': 8,
    'Illinois': 9,
    'Boise St.': 10,
    'Arizona St.': 11,
    'VCU': 12,
    'Iona': 13,
    'Grand Canyon': 14,
    'UNC Asheville': 15,
    'Howard': 16
}
champions = {
    (4, 5) : 4
}

count = 0
# Open the CSV file
with open('2023 Game Data.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)

    # List of matches to not delete
    unique_matches = {}


    # Iterate over each row in the CSV file
    for i, row in enumerate(reader):
        # Iterate over each cell in the row
        for j, cell in enumerate(row):

            # Check if the cell contains a target value
            if cell in South_schools:
                # Print the row and column index (converted to letter format)
                # print(f" {cell} Cell found at {chr(65 + j)}{i + 1}")

                if cell in South_schools:
                    unique_matches[cell] = []

                    for start, end in round_32["South"]:
                        if 1 in range(start, end + 1):
                            for key, value in South_schools.items():

                                if (value, South_schools[cell]) in round_32["South"] or (South_schools[cell], value) in round_32["South"]:
                                    unique_matches[cell].append([cell, key])
                                    break  # Break the loop if the key is found
                    # Round of 16
                    for start, end in round_16["South"]:
                        if 1 in range(start, end + 1):
                            for key, value in South_schools.items():
                                if (value, South_schools[cell]) in round_16["South"] or (South_schools[cell], value) in round_16["South"]:
                                    unique_matches[cell].append([cell, key])
                                    break  # Break the loop if the key is found

                            # print(South_schools[])

                    # Round of 8
                    for start, end in round_8["South"]:
                        if 1 in range(start, end + 1):
                            #print("Tuple containing 1:", (start, end))
                            for key, value in South_schools.items():

                                if (value, South_schools[cell]) in round_8["South"] or (South_schools[cell], value) in round_8["South"]:
                                    unique_matches[cell].append([cell, key])
                                    break  # Break the loop if the key is found
                # print(f" {teams_dict[j + 1]} Cell found at {chr(65 + j)}{i + 2}")

                count += 1
                print()
                print()
                print()
            if cell in East_schools:
                unique_matches[cell] = []

                for start, end in round_32["East"]:
                    if any(i in range(start, end + 1) for i in range(1, 17)):
                        for key, value in East_schools.items():
                            if (value, East_schools[cell]) in round_32["East"] or (East_schools[cell], value) in \
                                    round_32["East"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found
                # Round of 16
                for start, end in round_16["East"]:
                    if any(i in range(start, end + 1) for i in range(1, 17)):
                        for key, value in East_schools.items():
                            if (value, East_schools[cell]) in round_16["East"] or (East_schools[cell], value) in \
                                    round_16["East"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found

                        # print(East_schools[])

                # Round of 8
                for start, end in round_8["East"]:
                    if any(i in range(start, end + 1) for i in range(1, 17)):
                        # print("Tuple containing 1:", (start, end))
                        for key, value in East_schools.items():

                            if (value, East_schools[cell]) in round_8["East"] or (East_schools[cell], value) in round_8["East"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found

            if cell in West_schools:
                unique_matches[cell] = []

                for start, end in round_32["West"]:
                    if any(i in range(start, end + 1) for i in range(1, 17)):
                        for key, value in West_schools.items():
                            if (value, West_schools[cell]) in round_32["West"] or (West_schools[cell], value) in \
                                    round_32["West"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found
                # Round of 16
                for start, end in round_16["West"]:
                    if any(i in range(start, end + 1) for i in range(1, 17)):
                        for key, value in West_schools.items():
                            if (value, West_schools[cell]) in round_16["West"] or (West_schools[cell], value) in \
                                    round_16["West"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found

                        # print(West_schools[])

                # Round of 8
                for start, end in round_8["West"]:
                    if any(i in range(start, end + 1) for i in range(1, 17)):
                        # print("Tuple containing 1:", (start, end))
                        for key, value in West_schools.items():

                            if (value, West_schools[cell]) in round_8["West"] or (West_schools[cell], value) in round_8["West"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found



            if cell in Midwest_schools:
                unique_matches[cell] = []

                for start, end in round_32["Midwest"]:
                    if 1 in range(start, end + 1):
                        for key, value in Midwest_schools.items():

                            if (value, Midwest_schools[cell]) in round_32["Midwest"] or (
                            Midwest_schools[cell], value) in round_32["Midwest"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found
                # Round of 16
                for start, end in round_16["Midwest"]:
                    if 1 in range(start, end + 1):
                        for key, value in Midwest_schools.items():
                            if (value, Midwest_schools[cell]) in round_16["Midwest"] or (
                            Midwest_schools[cell], value) in round_16["Midwest"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found

                        # print(Midwest_schools[])

                # Round of 8
                for start, end in round_8["Midwest"]:
                    if 1 in range(start, end + 1):
                        # print("Tuple containing 1:", (start, end))
                        for key, value in Midwest_schools.items():

                            if (value, Midwest_schools[cell]) in round_8["Midwest"] or (Midwest_schools[cell], value) in \
                                    round_8["Midwest"]:
                                unique_matches[cell].append([cell, key])
                                break  # Break the loop if the key is found
            #print(f" {teams_dict[j + 1]} Cell found at {chr(65 + j)}{i + 2}")

            count += 1
            print()


# Remove duplicates of unique matches
for key in unique_matches:
    value = unique_matches[key]
    tuple_of_tups = tuple(map(tuple, value))
    unique_tuples = set(tuple_of_tups)
    unique_list = [list(t) for t in unique_tuples]
    unique_matches[key] = unique_list


print(f"This is the amount of times {target_values[0]} occurs {count//2}")

# prints unique values clean
count_teams = 0
for key, value in unique_matches.items():
    print(f"Key : {key}")
    print("Value:")
    count_teams += 1
    for sublist in value:
        print(sublist)
    print()
print(count_teams)

print()
print(unique_matches)
#print(unique_arr)

# The 5 categories that you want to use
selected_features = ['KENPOM ADJUSTED EFFICIENCY', 'BARTTORVIK ADJUSTED EFFICIENCY',
                     'EFG %', 'EFG % DEFENSE', 'POINTS PER POSSESSION OFFENSE',
                     'POINTS PER POSSESSION DEFENSE']

df_X = df[selected_features]

# Replace 'Game Result' with the name of the column that indicates the result
if 'Game Result' in df.columns:
    df_y = df['Game Result']
else:
    raise ValueError("Target column 'Game Result' not found in DataFrame")

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
