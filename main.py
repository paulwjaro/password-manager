from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip

window = Tk()
window.config(padx=50, pady=50)
window.title("Lock & Key")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]


def random_password():
    let_num = random.randint(8, 10)
    num_num = random.randint(1, 3)
    char_num = random.randint(1, 2)

    pass_lett = [letters[random.randint(0, len(letters) - 1)] for _ in range(let_num)]
    pass_num = [numbers[random.randint(0, len(numbers) - 1)] for _ in range(num_num)]
    pass_char = [char[random.randint(0, len(char) - 1)] for _ in range(char_num)]

    new_pass = pass_lett + pass_char + pass_num

    random.shuffle(new_pass)

    random_pass = ''.join(new_pass)

    pass_entry.delete(0, END)
    pass_entry.insert(0, random_pass)
    pyperclip.copy(random_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    if len(website_entry.get()) != 0 or len(user_entry.get()) != 0 or len(pass_entry.get()) != 0:
        new_login = {
            website_entry.get(): {
                "user": user_entry.get(),
                "password": pass_entry.get(),
            },
        }
        try:
            with open("saved_passwords.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("saved_passwords.json", "w") as data_file:
                json.dump(new_login, data_file, indent=4)
        else:
            data.update(new_login)
            with open("saved_passwords.json", mode="w") as logins:
                json.dump(data, logins, indent=4)
        finally:
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)

        website_entry.focus()
        user_entry.insert(0, "paul.jaro@me.com")
    else:
        messagebox.showinfo(title="Password Error", message="Please fill in all the fields to add a password.")


def search_logins():
    try:
        with open("saved_passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Account Info", message="Sorry, there is no account information available.")
    else:
        try:
            website = website_entry.get()
            pyperclip.copy(data[website]['password'])
            messagebox.showinfo(title="Account Info", message=f"Here is you account information for {website}:\n"
                                                              f"User/Email: {data[website]['user']}\n"
                                                              f"Password: {data[website]['password']}\n\n"
                                                              f"Password copied to clipboad!")
        except KeyError:
            website = website_entry.get()
            messagebox.showinfo(title="Account Info", message=f"Sorry, there is no account info for {website}")


# ---------------------------- UI SETUP ------------------------------- #

# -- Set Up Image Canvas
canvas = Canvas(width=200, height=200)
app_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=app_image)
canvas.grid(row=1, column=0, columnspan=3)

# -- Set Up Labels
website_label = Label(text="Website:")
website_label.config(font=("arial", 10, "normal"), pady=5)
website_label.grid(row=2, column=0)

user_label = Label(text="Email/Username:")
user_label.config(font=("arial", 10, "normal"), pady=5)
user_label.grid(row=3, column=0)

pass_label = Label(text="Password:")
pass_label.config(font=("arial", 10, "normal"), pady=5)
pass_label.grid(row=4, column=0)

# -- Set Up Input
website_entry = Entry()
website_entry.config(width=21)
website_entry.focus()
website_entry.grid(row=2, column=1)

user_entry = Entry()
user_entry.config(width=35)
user_entry.insert(0, "paul.jaro@me.com")
user_entry.grid(row=3, column=1, columnspan=2)

pass_entry = Entry()
pass_entry.config(width=21)
pass_entry.grid(row=4, column=1)

# -- Setup Buttons
gen_button = Button(text="Generate", command=random_password)
gen_button.grid(row=4, column=2)

add_button = Button(text="Add", command=save_password)
add_button.config(width=32)
add_button.grid(row=5, column=1, columnspan=2)

search_button = Button(text="Search", command=search_logins)
search_button.grid(row=2, column=2)


window.mainloop()
