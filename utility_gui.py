import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load Dataset
data = pd.read_csv("utility_data.csv")

# Training Data
X = data[["FamilyMembers", "UsageHours", "PreviousUnits"]]
y = data["NextMonthUnits"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Prediction Function
def predict_usage():
    try:
        family = int(family_entry.get())
        hours = int(hours_entry.get())
        units = int(units_entry.get())

        prediction = model.predict(
            pd.DataFrame(
                [[family, hours, units]],
                columns=["FamilyMembers", "UsageHours", "PreviousUnits"]
            )
        )

        result_label.config(
            text=f"⚡ Predicted Next Month Units: {round(prediction[0], 2)}"
        )

    except:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )

# Main Window
root = tk.Tk()
root.title("Smart Utility Usage Prediction Tool")
root.geometry("500x450")
root.configure(bg="#E8F5E9")

# Heading
title = tk.Label(
    root,
    text="⚡ Smart Utility Usage Prediction Tool",
    font=("Arial", 16, "bold"),
    bg="#E8F5E9"
)
title.pack(pady=15)

# Family Members
tk.Label(
    root,
    text="Family Members",
    font=("Arial", 12),
    bg="#E8F5E9"
).pack()

family_entry = tk.Entry(root, width=25)
family_entry.pack(pady=5)

# Usage Hours
tk.Label(
    root,
    text="Usage Hours",
    font=("Arial", 12),
    bg="#E8F5E9"
).pack()

hours_entry = tk.Entry(root, width=25)
hours_entry.pack(pady=5)

# Previous Units
tk.Label(
    root,
    text="Previous Month Units",
    font=("Arial", 12),
    bg="#E8F5E9"
).pack()

units_entry = tk.Entry(root, width=25)
units_entry.pack(pady=5)

# Predict Button
predict_btn = tk.Button(
    root,
    text="Predict",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=predict_usage
)
predict_btn.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    bg="#E8F5E9"
)
result_label.pack(pady=10)

root.mainloop()