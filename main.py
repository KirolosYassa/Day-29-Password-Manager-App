from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


window = Tk()
FONT_SIZE = 14

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    
    password_list = []
    
    symbols = ["{", "}", "[", "]", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", ":", "'", ";", "/", "?", ">", "<", "|", "~", "`", ",", "."]
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    password_list += [choice(letters) for i in range(randint(8, 12)) ]
    password_list += [choice(symbols) for i in range(randint(2, 4)) ]
    password_list += [choice(numbers) for i in range(randint(2, 4)) ]
    print(password_list)
    shuffle(password_list)
    print(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty inputs!", message="Please don't leave blank fields!")
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f"Are these info correct for this website '{website}'?\nEmail: {email}\nPassword: {password}\n")
    
    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
    
        website_entry.delete(0, END)
        website_entry.focus()
        email_entry.delete(0, END)
        email_entry.insert(0, "kirolosyassa@gmail.com")
        password_entry.delete(0, END)
        
        
# ---------------------------- UI SETUP ------------------------------- #

window.config(padx=70, pady=70)
window.title("Password Manager App")


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=(FONT_SIZE))
email_label = Label(text="Email/Password", font=(FONT_SIZE))
password_label = Label(text="Password", font=(FONT_SIZE))

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=50)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.insert(0, "kirolosyassa@gmail.com")
password_entry = Entry(width=21)


website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)


generate_button = Button(text="Generate Password",width=15, font=(FONT_SIZE), command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add",width=35, font=(FONT_SIZE), command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()