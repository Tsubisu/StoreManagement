from tkinter import ttk as ttk
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
    contact_style.configure("contact.TFrame", background="red")
    contact_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="contact.TFrame")
    contact_page_frame.pack_propagate(False)
    
     
    name_label = ttk.Label(contact_page_frame, text="Name:", background="red", foreground="white", font=("Arial", 12))
    name_label.place(x=30, y=50)
    name_entry = ttk.Entry(contact_page_frame, width=50)
    name_entry.place(x=120, y=50)

    
    email_label = ttk.Label(contact_page_frame, text="Email:", background="red", foreground="white", font=("Arial", 12))
    email_label.place(x=30, y=90)
    email_entry = ttk.Entry(contact_page_frame, width=50)
    email_entry.place(x=120, y=90)

    
    contact_label = ttk.Label(contact_page_frame, text="Contact:", background="red", foreground="white", font=("Arial", 12))
    contact_label.place(x=30, y=130)
    contact_entry = ttk.Entry(contact_page_frame, width=50)
    contact_entry.place(x=120, y=130)

    comment_label = ttk.Label(contact_page_frame, text="Comment:", background="red", foreground="white", font=("Arial", 12))
    comment_label.place(x=30, y=180)
    comment_text = Text(contact_page_frame, font=("Arial", 12), wrap="word")
    comment_text.place(x=120, y=180, width=305, height=100)
    
   
    def save_data():
        name = name_entry.get()
        email = email_entry.get()
        contact = contact_entry.get()
        comment = comment_text.get("1.0", "end-1c")

        if not name or not email or not contact or not comment:
            messagebox.showerror("Error", "All fields are required.")
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
        
    
    send_btn = ttk.Button(contact_page_frame, text="Send",takefocus=False,command=save_data)
    send_btn.place(x=30, y=320)
    
    return contact_page_frame
