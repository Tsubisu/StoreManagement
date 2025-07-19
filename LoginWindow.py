from tkinter import *
from tkinter import ttk as ttk
import sqlite3
from tkinter import messagebox

pages={}
def login(tk):
    global pages
    top = Toplevel(tk)
    top.geometry('400x400')
    top.title('Login  page')
    parent = ttk.Frame(top, width=600, height=600)
    parent.place(x=0, y=0)

    def page_switcher(name):
        pages[name].tkraise()

    pages["Login"] = show_login(parent, page_switcher)
    pages["Sign up"] = show_signup(parent, page_switcher)
    for page in pages.values():
        page.place(x=0,y=0)
    page_switcher("Login")

    mainloop()


def show_login(frame, page_switcher):
    login_frame_style=ttk.Style()
    login_frame_style.configure("login.TFrame",background="#ECECFA")
    login_frame = ttk.Frame(frame, width=600, height=600,style="login.TFrame")
    
    Label(login_frame, text='Login', font=('Arial', 16),background="#ECECFA").place(x=200,y=30,anchor="center")
    
    Label(login_frame, text='E-mail:').place(x=20, y=75)
    email_entry = Entry(login_frame)
    email_entry.place(x=90, y=75)
    
    Label(login_frame, text='Password:').place(x=20, y=115)
    password_entry = Entry(login_frame, show="*")
    password_entry.place(x=90, y=115)


    def user_login():
        email = email_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
        if cur.fetchone():
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login", "Invalid fullname or password.")
        conn.commit()
        conn.close()

    def manager_login():
         email = email_entry.get()
         password = password_entry.get()
         conn = sqlite3.connect("store.db")
         cur = conn.cursor()
         cur.execute("SELECT * FROM managers WHERE email=? AND password=?", (email, password))
         if cur.fetchone():
            messagebox.showinfo("Login", "Login successful as a manager")
         else:
            messagebox.showerror("Login", "Invalid  manager's email or password.")
         conn.commit()
         conn.close()



    Button(login_frame,text='Manager',command=manager_login).place(x=20,y=155)
    Button(login_frame, text='Login',command=user_login , width=7).place(x=90, y=155)
    Button(login_frame, text='Signup', command=lambda: page_switcher("Sign up"), width=7).place(x=165,y=155)
    return login_frame


def show_signup(frame, page_switcher):
    signup_frame = ttk.Frame(frame, width=600, height=600)
    
    login_label=Label(signup_frame,text="Sign Up",font=('Arial',20))
    login_label.place(x=200,y=20,anchor="center")
    
    Button(signup_frame, text='Back' , width=7,command=lambda: page_switcher("Login")).place(x=30, y=10)
    
    full_name=Label(signup_frame,text='Full Name :',font=('Arial, 11'))
    full_name.place(x=20,y=55)
    
    full_name_entry=ttk.Entry(signup_frame,width=30)
    full_name_entry.place(x=110,y=55)
    
    contact_label=Label(signup_frame,text="Contact     :",font=('Arial, 11'))
    contact_label.place(x=20,y=90)
    
    contact_entry=ttk.Entry(signup_frame,width=30)
    contact_entry.place(x=110,y=90)
    
    address_label=Label(signup_frame,text="Address    :",font=('Arial, 11'))
    address_label.place(x=20,y=125)
    
    address_entry=ttk.Entry(signup_frame,width=30)
    address_entry.place(x=110,y=125)
    
    email_label=Label(signup_frame,text="E-mail       :",font=('Arial, 11'))
    email_label.place(x=20,y=155)
    
    email_entry=ttk.Entry(signup_frame,width=30)
    email_entry.place(x=110,y=155)
    
    password_label=Label(signup_frame,text="Password :",font=('Arial', 11))
    password_label.place(x=20,y=215)
    
    password_entry=ttk.Entry(signup_frame,width=30)
    password_entry.place(x=110,y=185)
    
    def submit_signup():
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
            c.execute("INSERT INTO user (full_name, contact, address, email, password) VALUES (?, ?, ?, ?, ?)",
            (full_name, contact, address, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful!")
            page_switcher("Login")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email or username already exists")
    
    Button(signup_frame, text='Submit',command=submit_signup).place(x=160, y=255)


    return signup_frame

