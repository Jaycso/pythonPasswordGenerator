

import random
from tkinter import messagebox
from tkinter import *
import pyperclip

def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror(message="Please enter the required inputs")
        return
    #Check if the user allows repititon of characters
    if repeat == 1:
        password = random.sample(character_string, length)
    else:  
        password = random.choices(character_string, k=length)
    #Convert from a list to a string
    password = ''.join(password)
    #Allow the password to be used in other functions
    global password_export 
    password_export = password
    #Declare a string var
    password_v = StringVar()
    password = "Created password: "+str(password)
    #Assign the password to the declared string variables
    password_v.set(password)
    #Create a read only entry box to view the output, position using place
    password_label = Entry(password_gen, bd=0, bg="gray85", textvariable=password_v, state="readonly")
    password_label.place(x=10, y=140, height=50, width=320)

def copy_to_clipboard():
    # try:
    pyperclip.copy(password_export)
    # except:
    #     messagebox.showerror(message="Password has not yet been generated, please generate a password before copying to the clipboard.")
    #     return



#Define a string containing letters, symbols and numbers
character_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]{},.<>/?-=_+\\|"

#Define the UI
password_gen = Tk()
password_gen.geometry("350x200")
password_gen.title("Password Generator")

#Mention the title of the app
title_label = Label(password_gen, text="Password Generator", font=('Jetbrains Nerd Font Mono', 12))
title_label.pack()
#Read length
length_label = Label(password_gen, text="Enter length of password: ")
length_label.place(x=20, y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190, y=30)
#Read repitition
repeat_label = Label(password_gen, text="Repitition? 1: No repition, 2: Otherwise: ")
repeat_label.place(x=20, y=60)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=300, y=60)

#Generate password
password_button = Button(password_gen, text="Generate Password", command=generate_password)
password_button.place(x=20, y=100)

#Copy to clipboard
clipboard_button = Button(password_gen, text="Copy to clipboard", command=copy_to_clipboard)
clipboard_button.place(x=200, y =100)

#Exit and close app
password_gen.mainloop()