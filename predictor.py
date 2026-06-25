import pandas as pd
from sklearn.linear_model import LogisticRegression

print("Loading data...")

data = pd.read_csv("student.csv")

X = data[['Study', 'Attendance', 'Marks']]
y = data['Result']

model = LogisticRegression()
model.fit(X, y)

print("Model ready 👍")

study = int(input("Enter study hours: "))
attendance = int(input("Enter attendance: "))
marks = int(input("Enter marks: "))

result = model.predict([[study, attendance, marks]])

print("Prediction:", result[0])