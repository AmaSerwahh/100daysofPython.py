from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    passwords = []
    passwords += [random.choice(letters) for letter in range(nr_letters)]
    passwords += [random.choice(numbers) for number in range(nr_numbers)]
    passwords += [random.choice(symbols) for symbol in range(nr_symbols)]

    random.shuffle(passwords)
    passwords = ''.join(passwords)

    password_entry.insert(0, passwords)
    pyperclip.copy(passwords)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title='Oopsie', message='Please fill in all fields')
    else:
        save_details = messagebox.askokcancel(title=website, message=f"Details entered:\nWebsite:{website}\nEmail:{email}\nPassword:{password}"
                                                      f"\nDo you want to save this website?")
        if save_details:
            with open('data.txt', 'a') as data:
                data.write(f'{website}, {email}, {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, )
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)

password_label = Label(text='Password')
password_label.grid(row=3, column=0)

website_entry = Entry(width=53, highlightcolor='blue', highlightthickness=1,)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=53,)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'eugeniafrimpong27@gmail.com')

password_entry = Entry(width=35, highlightcolor='blue', highlightthickness=1)
password_entry.grid(row=3, column=1, )

generate_button = Button(text='Generate Password', relief='solid',fg='blue', border= 1, command=generate_password)
generate_button.grid(row=3, column=2, )

add_button = Button(text='Add', width=45, height=1, overrelief="groove", fg='white', bg='light blue', command=save)
add_button.grid(row=4, column=1, columnspan=2)

screen.mainloop()
