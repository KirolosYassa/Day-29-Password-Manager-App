from tkinter import *

window = Tk(title="Password Manager App")

FONT_SIZE = 14

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window.config(padx=50, pady=50)

canvas = Canvas(width=500, height=400, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=logo_img)


website_label = Label(text="Website", font=(FONT_SIZE))
email_and_password_label = Label(text="Email/Password", font=(FONT_SIZE))
password_label = Label(text="Password", font=(FONT_SIZE))

website_label.grid(row=1, column=0)
email_and_password_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_label_input = Entry(width=40)
email_and_password_label_input = Entry(width=40)
password_label_input = Entry(width=40)


website_label_input.grid(row=1, column=1)
email_and_password_label_input.grid(row=2, column=1)
password_label_input.grid(row=3, column=1)


window.mainloop()