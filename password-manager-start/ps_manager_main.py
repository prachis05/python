from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def ps_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_sym = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_sym + password_num

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, f"{password}")
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    ps = pass_entry.get()

    if len(web) == 0 or len(ps) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty")

    else:

        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email}"
                                                          f"\nPassword: {ps}\nIs it okay to save")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{web} | {email} | {ps}\n")
            f.close()


def on_clicked_add():
    save()
    website_entry.delete(0, END)
    pass_entry.delete(0, END)





# ------------------------------ UI SETUP ----------------------------------- #


window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

# Label
email_user_label = Label(text="Email/Username :")
email_user_label.grid(column=0, row=2)

# Label
password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "salunkheprachi05@gmail.com")

# Entry
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Button
gen_button = Button(text="Generate Password", command=ps_gen)
gen_button.grid(row=3, column=2)

# Button
add_butt = Button(text="Add", width=36, command=on_clicked_add)
add_butt.grid(column=1, row=4, columnspan=2)
















window.mainloop()