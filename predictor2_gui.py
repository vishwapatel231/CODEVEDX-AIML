import pandas as pd
from sklearn.linear_model import LogisticRegression
import tkinter as tk
from tkinter import messagebox

# Load data
data = pd.read_csv("student.csv")

X = data[['Study', 'Attendance', 'Marks']]
y = data['Result']

model = LogisticRegression()
model.fit(X, y)

# Prediction function
def predict():
    try:
        study = int(entry_study.get())
        attendance = int(entry_attendance.get())
        marks = int(entry_marks.get())

        result = model.predict([[study, attendance, marks]])

        if result[0] == "Pass":
            label_result.config(text="🎉 Student will PASS", fg="green")
        else:
            label_result.config(text="❌ Student may FAIL", fg="red")

    except:
        messagebox.showerror("Error", "Enter valid numbers!")

# GUI
root = tk.Tk()
root.title("Student Predictor")
root.geometry("400x350")
root.configure(bg="lightblue")

# Title
title = tk.Label(root, text="Student Performance Predictor",
                 font=("Arial", 16, "bold"), bg="lightblue")
title.pack(pady=10)

# Inputs
tk.Label(root, text="Study Hours", bg="lightblue").pack()
entry_study = tk.Entry(root, width=30)
entry_study.pack(pady=5)

tk.Label(root, text="Attendance (%)", bg="lightblue").pack()
entry_attendance = tk.Entry(root, width=30)
entry_attendance.pack(pady=5)

tk.Label(root, text="Marks", bg="lightblue").pack()
entry_marks = tk.Entry(root, width=30)
entry_marks.pack(pady=5)

# Button
tk.Button(root, text="Predict", command=predict,
          bg="green", fg="white",
          font=("Arial", 12, "bold"),
          width=15).pack(pady=15)

# Result
label_result = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg="lightblue")
label_result.pack()

root.mainloop()