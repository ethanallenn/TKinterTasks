import tkinter
import _tkinter
from tkinter import *
from tkinter import messagebox

def submit():
    password = entry_password.get()
    username = entry_username.get()
    messageAlert = Label(root, width=30)
    messageAlert.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    if password != "test":
        messageAlert.config(text="Incorrect passowrd!")
        entry_username.delete(0, END)
        entry_password.delete(0, END)
        entry_username.focus_set()
    else:
        messageAlert.config(text="Password accepted!")
        print("Password accepted!")
        print("Username: ", username)
        print("Password: ", password)
        messagebox.showinfo(title="Password incorrect", font=("Calibri", 18))

    if username != "test":
        messageAlert.config(text="Username incorrect!")
        entry_username.delete(0, "END")
        entry_password.delete(0, "END")
        entry_username.focus_set()
    
    else:
        messageAlert.config(text="Username accepted!")
        print("Username: ", username)
        print("Password: ", password)
        messagebox.showinfo(title="Username = OK", message="Press OK to continue.")
        root.destroy()

root = Tk()
root.geometry("305x300")
root.resizable(False, False)
root.configure(background="Blue")

def font_style():
    Label.config(font=('Helvetica bold', 16))

frame_heading = Frame(root)
frame_heading.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

frame_entry = Frame(root)                                               #Creating the Frame
frame_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

frame_buttons = Frame(root)                                             #Creating the Buttons
frame_buttons.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

TLabel = Label(frame_heading, text="Enter details: ", font=('Calibri',18))
TLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

UNlabel = Label(frame_entry, text="Enter username: ", font=('Helvetica bold', 16))
UNlabel.grid(row=0, column=0, padx=5, pady=5)

entry_username = Entry(frame_entry, width=15, bg="white")               
entry_username.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

PLabel = Label(frame_entry, text="Enter password: ", font=('Helvetica bold', 16))
PLabel.grid(row=1, column=0, padx=10, pady=10)

entry_password = Entry(frame_entry, width=15, bg="white", show="*")
entry_password.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

submit_button = Button(frame_buttons, text="Submit", font=('Comic Sans MS', 16), bg="White", width=8, command=submit)
submit_button.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()
print("")