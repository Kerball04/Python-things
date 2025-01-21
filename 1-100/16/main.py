# Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.

import tkinter as tk
from tkinter import messagebox

def process_input():
    user_input = entry.get()
    if user_input.lower() == 'q':
        root.destroy()
    elif not user_input.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number or 'q' to quit.")
    else:
        usr = int(user_input)
        if usr == 17:
            result_label.config(text="I said not 17! Try again!")
        elif usr > 17:
            diff = abs(17 - usr) * 2
            result_label.config(text=f"Double the absolute difference is {diff}")
        elif usr < 17:
            diff = abs(17 - usr)
            result_label.config(text=f"The absolute difference is {diff}")


# Create the main application window
root = tk.Tk()
root.title("Number Difference Calculator")

# Create UI Elements
prompt_label = tk.Label(root, text="Input any number EXCEPT 17 ('q' to quit):")
prompt_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=process_input)
submit_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()

# very much correct