from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox
import app
def add_manager(frame):
    add_style=ttk.Style()
    add_style.configure("add.TFrame", background="#ECECFA")
    
    add_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="add.TFrame")
    
    full_name=Label(add_page_frame,text='Full Name       :',font=('Arial, 11'),background="#ECECFA")
    full_name.place(x=20,y=55)
    
    full_name_entry=ttk.Entry(add_page_frame,width=30)
    full_name_entry.place(x=150,y=55)
    
    contact_label=Label(add_page_frame,text="Contact           :",font=('Arial',11),background="#ECECFA")
    contact_label.place(x=20,y=90)
    
    contact_entry=ttk.Entry(add_page_frame,width=30)
    contact_entry.place(x=150,y=90)
    
    address_label=Label(add_page_frame,text="Address          :",font=('Arial',11),background="#ECECFA")
    address_label.place(x=20,y=125)
    
    address_entry=ttk.Entry(add_page_frame,width=30)
    address_entry.place(x=150,y=125)
    
    email_label=Label(add_page_frame,text="E-mail             :",font=('Arial',11),background="#ECECFA")
    email_label.place(x=20,y=155)
    
    email_entry=ttk.Entry(add_page_frame,width=30)
    email_entry.place(x=150,y=155)
    
    password_label=Label(add_page_frame,text="Create Password:",font=('Arial',11),background="#ECECFA")
    password_label.place(x=20,y=185)
    
    password_entry=ttk.Entry(add_page_frame,width=30)
    password_entry.place(x=150,y=185)
    
    def submit_manager():
        full_name=full_name_entry.get()
        email = email_entry.get()
        contact=contact_entry.get()
        address=address_entry.get()
        password = password_entry.get()

        if not all([full_name, contact, address, email, password]):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = sqlite3.connect("store.db")
            c = conn.cursor()
            c.execute("INSERT INTO managers (full_name, contact, address, email, password) VALUES (?, ?, ?, ?, ?)",
            (full_name, contact, address, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful!")
            full_name_entry.delete(0, END)
            contact_entry.delete(0, END)
            address_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email or username already exists")
    
    Button(add_page_frame, text='Submit',command=submit_manager).place(x=160, y=255)
    
    
    return add_page_frame