import tkinter
from tkinter import messagebox
from tkinter import *

root = Tk()
root.title("Customer Details Form")
root.geometry("350x350")
root.resizable(False, False)

def validate_name(name):
    return name.isalpha() and len(name) <= 30

def validate_dob(dob):
    if len(dob) != 10:
        return False
    parts = dob.split('/')
    if len(parts) != 3:
        return False
    for part in parts:
        if not part.isdigit():
            return False
    return True

def validate_address(address):
    return len(address) <= 100

def validate_postcode(postcode):
    if len(postcode) != 8:
        return False
    if not (postcode[:2].isalpha() and postcode[2:4].isdigit() and
            postcode[5:6].isdigit() and postcode[6:].isalpha()):
        return False
    return True

def validate_entry(entry, validate_function, field_name):
    value = entry.get()
    if not value:
        messagebox.showerror("Error", f"{field_name} field cannot be empty!")
        return False
    elif not validate_function(value):
        messagebox.showerror("Error", f"Invalid {field_name}!")
        return False
    return True

def details():
    if (validate_entry(fName_entry, validate_name, "First Name") and
        validate_entry(sName_entry, validate_name, "Surname") and
        validate_entry(Address_entry, validate_address, "Address") and
        validate_entry(dob_entry, validate_dob, "Date of Birth") and
        validate_entry(postcode_entry, validate_postcode, "Postcode")):

        with open("detailsFile.txt", "a") as detailsFile:
            fName = fName_entry.get()
            sName = sName_entry.get()
            address = Address_entry.get()
            dob = dob_entry.get()
            pcode = postcode_entry.get()

            detailsFile.write(fName + "," + sName + "," + address + "," + pcode + "," + dob + "\n")
            messagebox.showinfo("Success", "Details have been successfully uploaded!")

def remove_record(index, record_window):
    with open("detailsFile.txt", "r") as file:
        records = file.readlines()
    del records[index]
    with open("detailsFile.txt", "w") as file:
        file.writelines(records)
    record_window.destroy()
    messagebox.showinfo("Success", "Record removed successfully!")

def display_record_details(record, index):
    record_window = Toplevel(root)
    record_window.title("Record Details")
    record_window.geometry("500x300")

    fName_label = Label(record_window, text="First Name: ")
    fName_label.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
    fName_entry = Entry(record_window)
    fName_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
    fName_entry.insert(0, record[0])

    sName_label = Label(record_window, text="Surname: ")
    sName_label.grid(row=2, column=0, columnspan=1, padx=5, pady=5)
    sName_entry = Entry(record_window)
    sName_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
    sName_entry.insert(0, record[1])

    dob_label = Label(record_window, text="Date of Birth: ")
    dob_label.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
    dob_entry = Entry(record_window)
    dob_entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
    dob_entry.insert(0, record[4])

    Address_label = Label(record_window, text="Address: ")
    Address_label.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
    Address_entry = Entry(record_window)
    Address_entry.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
    Address_entry.insert(0, record[2])

    postcode_label = Label(record_window, text="Postcode: ")
    postcode_label.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
    postcode_entry = Entry(record_window)
    postcode_entry.grid(row=5, column=1, columnspan=3, padx=5, pady=5)
    postcode_entry.insert(0, record[3])

    remove_button = Button(record_window, text="Remove", command=lambda: remove_record(index, record_window))
    remove_button.grid(row=6, column=1, columnspan=2, padx=20, pady=20)

def display_details():
    with open("detailsFile.txt", "r") as detailsFile:
        records = detailsFile.readlines()
        if not records:
            messagebox.showinfo("Info", "No records found!")
            return

        details_window = Toplevel(root)
        details_window.title("Details")
        details_window.geometry("500x300")

        scrollbar = Scrollbar(details_window)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(details_window, yscrollcommand=scrollbar.set)
        for record in records:
            listbox.insert(END, record.strip())
        listbox.pack(side=LEFT, fill=BOTH)

        scrollbar.config(command=listbox.yview)

        def on_select(event):
            index = listbox.curselection()[0]
            selected_record = records[index].strip().split(',')
            display_record_details(selected_record, index)

        listbox.bind('<<ListboxSelect>>', on_select)

fName_label = Label(root, text="First Name: ")
fName_label.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
fName_entry = Entry(root)
fName_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

sName_label = Label(root, text="Surname: ")
sName_label.grid(row=2, column=0, columnspan=1, padx=5, pady=5)
sName_entry = Entry(root)
sName_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

dob_label = Label(root, text="Date of Birth: ")
dob_label.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
dob_entry = Entry(root)
dob_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

Address_label = Label(root, text="Address: ")
Address_label.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
Address_entry = Entry(root)
Address_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

postcode_label = Label(root, text="Postcode: ")
postcode_label.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
postcode_entry = Entry(root)
postcode_entry.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

submit_button = Button(root, text="Submit", command=details)
submit_button.grid(row=6, column=1, columnspan=2, padx=20, pady=20)

display_button = Button(root, text="Display Details", command=display_details)
display_button.grid(row=7, column=1, columnspan=2, padx=20, pady=20)

root.mainloop()
