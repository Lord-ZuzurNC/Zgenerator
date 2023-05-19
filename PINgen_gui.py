import string
import secrets
import tkinter as tk
from tkinter import messagebox


def generate_pin(length):
    alphabet = string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def generate_button_clicked():
    global last_generated_pin
    try:
        length = int(length_entry.get())
        pin = generate_pin(length)
        pin_label.config(text=pin)
        copy_button.config(state="normal")
        last_generated_pin = pin
    except ValueError:
        messagebox.showerror("Error", "Invalid pin length!")


def copy_button_clicked():
    window.clipboard_clear()
    window.clipboard_append(last_generated_pin)


# Create the main window
window = tk.Tk()
window.title("PIN Generator")
window.geometry("300x200")

# Create the widgets
length_label = tk.Label(window, text="PIN Length:")
length_entry = tk.Entry(window)
generate_button = tk.Button(window, text="Generate", command=generate_button_clicked)
pin_label = tk.Label(window, text="")
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_button_clicked)
copy_button.config(state="disabled")

# Place the widgets in the window
length_label.pack()
length_entry.pack()
generate_button.pack()
pin_label.pack()
copy_button.pack()

# Initialize last generated password
last_generated_pin = ""

# Start the main loop
window.mainloop()
