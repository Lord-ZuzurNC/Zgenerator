import string
import secrets
import tkinter as tk
from tkinter import messagebox


def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def generate_button_clicked():
    global last_generated_password  # Declare last_generated_password as a global variable
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_label.config(text=password)
        copy_button.config(state="normal")  # Enable the copy button
        last_generated_password = password
    except ValueError:
        messagebox.showerror("Error", "Invalid password length!")


def copy_button_clicked():
    window.clipboard_clear()  # Clear the clipboard
    window.clipboard_append(last_generated_password)  # Append the last generated password to the clipboard


# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")

# Create the widgets
length_label = tk.Label(window, text="Password Length:")
length_entry = tk.Entry(window)
generate_button = tk.Button(window, text="Generate", command=generate_button_clicked)
password_label = tk.Label(window, text="")
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_button_clicked)
copy_button.config(state="disabled")  # Disable the copy button initially


# Place the widgets in the window
length_label.pack()
length_entry.pack()
generate_button.pack()
password_label.pack()
copy_button.pack()

# Initialize last generated password
last_generated_password = ""

# Start the main loop
window.mainloop()
