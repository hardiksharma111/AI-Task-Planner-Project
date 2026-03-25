import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Create a Synthetic Dataset (The "Real-World" Data)
# columns: [Hours_Required, Difficulty_1_10, Days_Until_Deadline, Is_Prerequisite_Met]
data = {
    'Hours': [2, 10, 1, 5, 8, 3, 1, 12, 4, 6],
    'Difficulty': [3, 9, 2, 6, 8, 4, 1, 10, 5, 7],
    'Days_Left': [10, 2, 5, 3, 1, 7, 14, 2, 8, 4],
    'Has_Prereq': [1, 1, 1, 0, 1, 1, 1, 0, 1, 0], # 1 = Yes, 0 = No
    'Priority': ['Low', 'High', 'Low', 'High', 'High', 'Medium', 'Low', 'High', 'Medium', 'High']
}

df = pd.DataFrame(data)

# 2. Features and Target
X = df[['Hours', 'Difficulty', 'Days_Left', 'Has_Prereq']]
y = df['Priority']

# 3. Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Classifier (Decision Tree)
# We use a Decision Tree because it mimics human "logical" decision making
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Evaluate the Model
predictions = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100}%")

# 6. Predict a New Task
# Example: A task that takes 7 hours, Difficulty 8, 2 days left, Prereq met
new_task = [[7, 8, 2, 1]]
prediction = model.predict(new_task)
print(f"Predicted Priority for New Task: {prediction[0]}")