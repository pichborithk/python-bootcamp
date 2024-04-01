import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from characters_data import letters, symbols, numbers
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            website_info = data[website]
            messagebox.showinfo(
                title=website,
                message=f"Email: {website_info['email']} \nPassword: {website_info['password']}",
            )
        else:
            messagebox.showerror(
                title="Error", message=f"No Detail for the {website} exists"
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_entry_label = Label(text="Website:", bg="white", fg="black")
website_entry_label.grid(column=0, row=1, sticky="E")

website_entry = Entry(
    width=21,
    bg="white",
    fg="black",
    highlightthickness=1,
    insertbackground="black",
    highlightcolor="blue",
    highlightbackground="white",
)
website_entry.grid(column=1, row=1, sticky="W")
website_entry.focus()

search_button = Button(
    text="Search", width=13, highlightbackground="white", command=find_password
)
search_button.grid(column=2, row=1)

email_entry_label = Label(text="Email/Username:", bg="white", fg="black")
email_entry_label.grid(column=0, row=2, sticky="E")

email_entry = Entry(
    width=38,
    bg="white",
    fg="black",
    highlightthickness=1,
    insertbackground="black",
    highlightcolor="blue",
    highlightbackground="white",
)
email_entry.insert(END, string="python@dev.edu")
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")

password_entry_label = Label(text="Password:", bg="white", fg="black")
password_entry_label.grid(column=0, row=3, sticky="E")

password_entry = Entry(
    width=21,
    bg="white",
    fg="black",
    highlightthickness=1,
    insertbackground="black",
    highlightcolor="blue",
    highlightbackground="white",
)
password_entry.grid(column=1, row=3, sticky="W")

generate_password_button = Button(
    text="Generate Password", highlightbackground="white", command=generate_password
)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=15, highlightbackground="white", command=save)
add_button.grid(column=1, row=4)

window.mainloop()
