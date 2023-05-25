import string
import secrets
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


def generate_pin(length):
    alphabet = string.digits
    pin = ''.join(secrets.choice(alphabet) for _ in range(length))
    return pin


def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def generate_pin_button_clicked():
    global last_generated_pin
    try:
        length = int(pin_length_entry.get())
        pin = generate_pin(length)
        pin_label.config(text=pin)
        pincopy_button.config(state="normal")
        last_generated_pin = pin
    except ValueError:
        messagebox.showerror("Error", "Invalid PIN length!")


def generate_password_button_clicked():
    global last_generated_password
    try:
        length = int(password_length_entry.get())
        password = generate_password(length)
        password_label.config(text=password)
        passwordcopy_button.config(state="normal")
        last_generated_password = password
    except ValueError:
        messagebox.showerror("Error", "Invalid password length!")

def pincopy_button_clicked():
    window.clipboard_clear()
    window.clipboard_append(last_generated_pin)
    
def passwordcopy_button_clicked():
    window.clipboard_clear()
    window.clipboard_append(last_generated_password)

# Create the main window
window = tk.Tk()
window.title("Generator")
window.geometry("300x200")

# Create the style and set the initial theme to 'default'
style = ttk.Style(window)
style.theme_use('default')

# Create the notebook (tabbed interface)
notebook = ttk.Notebook(window)

# Create the PIN generator tab
pin_tab = ttk.Frame(notebook)
notebook.add(pin_tab, text="PIN Generator")

pin_length_label = tk.Label(pin_tab, text="PIN Length:")
pin_length_entry = tk.Entry(pin_tab)
generate_pin_button = tk.Button(pin_tab, text="Generate", command=generate_pin_button_clicked)
pin_label = tk.Label(pin_tab, text="")
pincopy_button = tk.Button(pin_tab, text="Copy to Clipboard", command=pincopy_button_clicked)
pincopy_button.config(state="disabled")

pin_length_label.pack()
pin_length_entry.pack()
generate_pin_button.pack()
pin_label.pack()
pincopy_button.pack()

# Create the password generator tab
password_tab = ttk.Frame(notebook)
notebook.add(password_tab, text="Password Generator")

password_length_label = tk.Label(password_tab, text="Password Length:")
password_length_entry = tk.Entry(password_tab)
generate_password_button = tk.Button(password_tab, text="Generate", command=generate_password_button_clicked)
password_label = tk.Label(password_tab, text="")
passwordcopy_button = tk.Button(password_tab, text="Copy to Clipboard", command=passwordcopy_button_clicked)
passwordcopy_button.config(state="disabled")

password_length_label.pack()
password_length_entry.pack()
generate_password_button.pack()
password_label.pack()
passwordcopy_button.pack()

# Place the notebook in the window
notebook.pack(fill="both", expand=True)

# Start the main loop
window.mainloop()
