import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("utility_data.csv")

# Input and Output
X = data[["FamilyMembers", "UsageHours", "PreviousUnits"]]
y = data["NextMonthUnits"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Test prediction
family = int(input("Enter Family Members: "))
hours = int(input("Enter Usage Hours: "))
units = int(input("Enter Previous Month Units: "))

prediction = model.predict([[family, hours, units]])

print("Predicted Next Month Units:", round(prediction[0], 2))