import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contacts
contacts = {}


# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Please enter a name for the contact.")


# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, name)


# Function to clear the input entries
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# Function to view contact details
def view_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        details = contacts[selected_contact]
        messagebox.showinfo("Contact Details",
                            f"Name: {selected_contact}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")


# Function to search for a contact
def search_contact():
    search_term = search_entry.get().strip().lower()
    contact_list.delete(0, tk.END)

    for name, info in contacts.items():
        if search_term in name.lower() or search_term in info['Phone']:
            contact_list.insert(tk.END, name)


# Function to update a contact
def update_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        new_phone = phone_entry.get()
        new_email = email_entry.get()
        new_address = address_entry.get()

        if new_phone:
            contacts[selected_contact]['Phone'] = new_phone
        if new_email:
            contacts[selected_contact]['Email'] = new_email
        if new_address:
            contacts[selected_contact]['Address'] = new_address

        update_contact_list()
        clear_entries()


# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        del contacts[selected_contact]
        update_contact_list()
        clear_entries()


# Create the main application window
app = tk.Tk()
app.title("Contact Management App")

# Create and place widgets
name_label = tk.Label(app, text="Name:")
name_label.pack()

name_entry = tk.Entry(app)
name_entry.pack()

phone_label = tk.Label(app, text="Phone:")
phone_label.pack()

phone_entry = tk.Entry(app)
phone_entry.pack()

email_label = tk.Label(app, text="Email:")
email_label.pack()

email_entry = tk.Entry(app)
email_entry.pack()

address_label = tk.Label(app, text="Address:")
address_label.pack()

address_entry = tk.Entry(app)
address_entry.pack()

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.pack()

view_button = tk.Button(app, text="View Contact", command=view_contact)
view_button.pack()

search_label = tk.Label(app, text="Search:")
search_label.pack()

search_entry = tk.Entry(app)
search_entry.pack()

search_button = tk.Button(app, text="Search", command=search_contact)
search_button.pack()

update_button = tk.Button(app, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.pack()

contact_list = tk.Listbox(app)
contact_list.pack()

# Start the Tkinter main loop
app.mainloop()
