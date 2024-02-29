import tkinter
import _tkinter
#Importing TKinter
from tkinter import *
from tkinter import messagebox
#Importing Mesagebox
def submit():
    password = entry_password.get()
    username = entry_username.get()
    messageAlert = Label(root, width=30)
    messageAlert.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    #Getting the password and username

    if password != "test":
        messageAlert.config(text="Password incorrect, please try again!")         #Password incorrect Popup
        entry_username.delete(0, "END")
        entry_password.delete(0, "END")
        entry_username.focus_set()
    else:
        messageAlert.config(text="Password accepted!")                            #Password correct Popup
        print("Password accepted")
        print("Username: ", username)
        print("Password: ", password)
        messagebox.showinfo(title="Password = OK", message="Press OK to continue.")
        root.destroy()

    if username != "admin":
        messageAlert.config(text="Username incorrect, please try again!", font=("Times", 16))  #Username incorrect Popup
        entry_username.delete(0, "END")
        entry_password.delete(0, "END")
        entry_username.focus_set()
    
    else:
        messageAlert.config(text="Username accepted!")                                         #Username correct Popup
        print("Username: ", username)
        print("Password: ", password)
        messagebox.showinfo(title="Username = OK", message="Press OK to continue.")
        root.destroy()

root = Tk()
root.geometry("325x285")
root.title("Login")
root.resizable(False, False)
root.configure(background="Light blue")

def font_style():
    Label.config(font=('Helvetica bold', 12))
frame_heading = Frame(root)
frame_heading.grid(row=0, column=0, columnspan=2, padx=30, pady=5)
frame_entry = Frame(root)                                               #Creating the Frame
frame_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frame_buttons = Frame(root)                                             #Creating the Buttons
frame_buttons.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
TLabel = Label(frame_entry, text="Enter details:", font=('Arial',14))
TLabel =
UNlabel = Label(frame_entry, text="Enter username: ", font=('Helvetica bold', 12)).grid(row=0, column=0, padx=5, pady=5)

entry_username = Entry(frame_entry, width=15, bg="white")               
entry_username.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

Label(frame_entry, text="Enter password: ", font=('Helvetica bold', 12)).grid(row=1, column=0, padx=10, pady=10)

entry_password = Entry(frame_entry, width=15, bg="white", show="*")
entry_password.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

def callback():
    submit_button = Button(frame_buttons, text="Submit", command=callback, ont=('Comic Sans MS', 16), bg="White", width=8)
    submit_button.grid(row=0, column=0, padx=5, pady=5)
          

root.mainloop()
print("")
