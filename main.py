from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.config(padx=50, pady=50)
window.title("Lock & Key")

info_list = []
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

    random_pass = '\n'.join(new_pass)

    pass_entry.delete(0, END)
    pass_entry.insert(0, random_pass)
    pyperclip.copy(random_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    if len(website_entry.get()) != 0 or len(user_entry.get()) != 0 or len(pass_entry.get()) != 0:
        new_pass = {
            "website": website_entry.get(),
            "user": user_entry.get(),
            "password": pass_entry.get(),
        }
        info_list.append(new_pass)

        is_okay = messagebox.askokcancel(title=new_pass["website"],
                                         message=f"You have selected the following information"
                                                 f" for {new_pass['website']}. \n Username:"
                                                 f" {new_pass['user']}\n Password:"
                                                 f" {new_pass['password']}\n Is this correct?")
        if is_okay:
            with open("saved_passwords.txt", mode="w") as logins:
                for login in info_list:
                    logins.write(login["website"] + " | " + login["user"] + " | " + login["password"] + "\n")

            website_entry.delete(0, END)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)

            website_entry.focus()
            user_entry.insert(0, "paul.jaro@me.com")
        else:
            info_list.pop()
            pass_entry.focus()
            pass_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Password Error", message="Please fill in all the fields to add a password.")


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
website_entry.config(width=35)
website_entry.focus()
website_entry.grid(row=2, column=1, columnspan=2)

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

window.mainloop()
