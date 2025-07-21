from tkinter import ttk as ttk
from tkinter import *
from tkinter import Text, messagebox
import sqlite3


def contact_page(frame):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS comments(
                name VARCHAR(40),
                email VARCHAR(30),
                contact VARCHAR(10),
                comment TEXT, 
                comment_id INTEGER PRIMARY KEY AUTOINCREMENT)
                """)
    conn.commit()
    conn.close()
    
def contact_page(frame):
    
    contact_style=ttk.Style()
    contact_style.configure("contact.TFrame", background="white")
    contact_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="contact.TFrame")
    contact_page_frame.pack_propagate(False)
    
     
    name_entry = ttk.Label(contact_page_frame, background="white", foreground="black", font=("Arial", 12))
    name_entry =ttk.Entry(contact_page_frame, width=55)
    
    name_entry.place(x=210, y=100,height=40)

    
    email_entry = ttk.Label(contact_page_frame, background="white", foreground="black", font=("Arial", 12))
    email_entry = ttk.Entry(contact_page_frame, width=60)

    email_entry.place(x=570, y=100,height=40)

    
    contact_entry = ttk.Label(contact_page_frame, background="white", foreground="black", font=("Arial", 12))
    contact_entry = ttk.Entry(contact_page_frame, width=120)
    
    contact_entry.place(x=210, y=170,height=40)
    
    comment_text = Text(contact_page_frame, font=("Arial", 10), wrap="word")
    comment_text.place(x=210, y=230, width=730, height=120)
    
    comment_text.config(foreground='black', relief="solid", bd=1)
    
    def default_text():
        if name_entry.get()!="Name":
            name_entry.delete(0, "end")
            name_entry.insert(0, "Name")
        if email_entry.get!="Email":
            email_entry.delete(0, "end")
            email_entry.insert(0, "Email")
        if contact_entry.get()!="Contact":
            contact_entry.delete(0, "end")
            contact_entry.insert(0, "Contact")
        if comment_text!="Comment":
            comment_text.delete("1.0", "end")
            comment_text.insert("1.0", "Comment")
            
    default_text()

    def save_data():
        name = name_entry.get()
        email = email_entry.get()
        contact = contact_entry.get()
        comment = comment_text.get("1.0", "end-1c")

        if name=="Name" or email=="Email" or contact=="Contact" or comment=="Comment":
            messagebox.showerror("Error", "All fields are required.")
            default_text()
            return

        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comments (name, contact, email, comment) VALUES (?, ?, ?, ?)", 
                       (name, contact, email, comment))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Your message has been sent successfully.")
        name_entry.delete(0, "end")
        email_entry.delete(0, "end")
        contact_entry.delete(0, "end")
        comment_text.delete("1.0", "end")
        default_text()
    
    send_btn = Button(contact_page_frame,background="black",foreground="white",width="20" ,text="Send", takefocus=False,command=save_data)
    send_btn.place(x=220, y=400)
    
    return contact_page_frame
