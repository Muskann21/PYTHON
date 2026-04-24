name="Muskan"
age=17
a=97
b=88
c=94
d=94
e=99

import tkinter as tk
from tkinter import ttk

def submit_form():
    # Retrieve input values
    first_name = first_name_var.get()
    last_name = last_name_var.get()
    email = email_var.get()
    contact = contact_var.get()
    password = password_var.get()
    gender = gender_var.get()

    # Display the entered information
    result_text = (
        f"First Name: {first_name}\n"
        f"Last Name: {last_name}\n"
        f"Email: {email}\n"
        f"Contact: {contact}\n"
        f"Password: {password}\n"
        f"Gender: {gender}"
    )
    result_label.config(text=result_text)

# Create the main application window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg='lightgreen')

# Define StringVar variables to store user inputs
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_var = tk.StringVar()
contact_var = tk.StringVar()
password_var = tk.StringVar()
gender_var = tk.StringVar()

# Create and place the form labels and entry widgets
tk.Label(root, text="First Name:", bg='lightgreen').grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Entry(root, textvariable=first_name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Last Name:", bg='lightgreen').grid(row=1, column=0, padx=10, pady=5, sticky='e')
tk.Entry(root, textvariable=last_name_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", bg='lightgreen').grid(row=2, column=0, padx=10, pady=5, sticky='e')
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Contact:", bg='lightgreen').grid(row=3, column=0, padx=10, pady=5, sticky='e')
tk.Entry(root, textvariable=contact_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Password:", bg='lightgreen').grid(row=4, column=0, padx=10, pady=5, sticky='e')
tk.Entry(root, textvariable=password_var, show='*').grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:", bg='lightgreen').grid(row=5, column=0, padx=10, pady=5, sticky='e')
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combobox.grid(row=5, column=1, padx=10, pady=5)
gender_combobox.current(0)  # Set default value

# Create and place the Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="", bg='lightgreen', justify='left')
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
