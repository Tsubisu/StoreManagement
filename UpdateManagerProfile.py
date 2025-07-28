from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox
import AddManager
def update_profile(frame):
        import User
        update_style=ttk.Style()
        update_style.configure("update.TFrame", background="#ECECFA")
    
        update_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="update.TFrame")
        full_name=Label(update_page_frame,text='Full Name       :',font=('Arial, 11'),background="#ECECFA")
        full_name.place(x=20,y=55)
        
        full_name_entry=ttk.Entry(update_page_frame,width=30)
        full_name_entry.place(x=150,y=55)
        
        contact_label=Label(update_page_frame,text="Contact           :",font=('Arial',11),background="#ECECFA")
        contact_label.place(x=20,y=90)
        
        contact_entry=ttk.Entry(update_page_frame,width=30)
        contact_entry.place(x=150,y=90)
        
        address_label=Label(update_page_frame,text="Address          :",font=('Arial',11),background="#ECECFA")
        address_label.place(x=20,y=125)
        
        address_entry=ttk.Entry(update_page_frame,width=30)
        address_entry.place(x=150,y=125)
        
        email_label=Label(update_page_frame,text="E-mail             :",font=('Arial',11),background="#ECECFA")
        email_label.place(x=20,y=155)
        
        email_entry=ttk.Entry(update_page_frame,width=30)
        email_entry.place(x=150,y=155)
        
        password_label=Label(update_page_frame,text="New Password:",font=('Arial',11),background="#ECECFA")
        password_label.place(x=20,y=185)
        
        password_entry=ttk.Entry(update_page_frame,width=30)
        password_entry.place(x=150,y=185)
   
        def save_changes():
                full_name = full_name_entry.get()
                contact = contact_entry.get()
                address = address_entry.get()
                email = email_entry.get()
                password=password_entry.get()
                if not all([full_name, contact, address, email,password]):
                    messagebox.showerror("Error", "All fields are required")
                    return

                try:
                    conn = sqlite3.connect("store.db")
                    c = conn.cursor()
                    c.execute("""UPDATE managers SET full_name=?, contact=?, address=?, email=? ,password=? WHERE manager_id=?""",
                            (full_name, contact, address, email, password,User.manager_id))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Profile updated successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Update failed: {e}")
       

        Button(update_page_frame, text="Save Changes", command=save_changes).place(x=150, y=410)
        
        return update_page_frame

    