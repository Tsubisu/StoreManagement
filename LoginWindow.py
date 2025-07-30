from tkinter import *
from tkinter import ttk as ttk
import sqlite3
from tkinter import messagebox
import User
pages={}
import ManagerWindow
def login(tk):
    global pages
    top = Toplevel(tk)
    top.geometry('400x400')
    top.title('Login  page')
    parent = ttk.Frame(top, width=600, height=600)
    parent.place(x=0, y=0)

    def page_switcher(name):
        pages[name].tkraise()

    pages["Login"] = show_login(parent, page_switcher,top)
    pages["Sign up"] = show_signup(parent, page_switcher,top)
    for page in pages.values():
        page.place(x=0,y=0)
    page_switcher("Login")

    mainloop()


def show_login(frame, page_switcher,Top):
    login_frame_style=ttk.Style()
    login_frame_style.configure("login.TFrame",background="#ECECFA")

    login_frame = ttk.Frame(frame, width=600, height=600,style="login.TFrame")
    Label(login_frame, text='Login', font=('Segoe UI Light', 18,'bold'),background="#ECECFA").place(x=200,y=30,anchor="center")

    Label(login_frame, text='E-mail       :',font=('Segoe UI Light', 15),background="#ECECFA").place(x=20, y=75)
    email_entry = ttk.Entry(login_frame)
    email_entry.place(x=120, y=85)
    
    Label(login_frame, text='Password :',font=('Segoe UI Light', 15),background="#ECECFA").place(x=20, y=115)
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.place(x=120, y=125)


    def user_login():
        email = email_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
        if cur.fetchone():
            messagebox.showinfo("Login", "Login successful!")
            User.update_logged_status(email)
            Top.destroy()

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
            ManagerWindow.show_manager()
            User.update_manager_login(email)
            Top.destroy()
         else:
            messagebox.showerror("Login", "Invalid  manager's email or password.")
         conn.commit()
         conn.close()


    style=ttk.Style()
    style.configure("login.TButton",background="#ECECFA",font=("Segoe UI Light",10),width=7)
    style.map("login.TButton",background=[("pressed","#ECECFA")])
    ttk.Button(login_frame,text='Manager',style="login.TButton",command=manager_login,takefocus=False).place(x=20,y=165)
    ttk.Button(login_frame, text='Login',style="login.TButton",command=user_login , width=7,takefocus=False).place(x=90, y=165)
    ttk.Button(login_frame, text='Signup',style="login.TButton", command=lambda: page_switcher("Sign up"), width=7,takefocus=False).place(x=165,y=165)
    return login_frame


def show_signup(frame, page_switcher,Top):

    style = ttk.Style()
    style.configure("Signup.TLabel",background="#ECECFA")

    style = ttk.Style()
    style.configure("signin.TButton", background="#ECECFA", font=("Segoe UI Light", 10), width=7)
    style.map("signin.TButton", background=[("pressed", "#ECECFA")])

    signup_frame = Frame(frame, width=600, height=600,background="#ECECFA")
    
    login_label=ttk.Label(signup_frame,style="Signup.TLabel",text="Sign Up",font=('Arial',20))
    login_label.place(x=200,y=20,anchor="center")
    
    ttk.Button(signup_frame, text='Back' , width=7,command=lambda: page_switcher("Login"),style="signin.TButton",takefocus=False).place(x=30, y=10)
    
    full_name=ttk.Label(signup_frame,style="Signup.TLabel",text='Full Name :',font=('Arial, 11'))
    full_name.place(x=20,y=55)
    
    full_name_entry=ttk.Entry(signup_frame,width=30)
    full_name_entry.place(x=110,y=55)
    
    contact_label=ttk.Label(signup_frame,style="Signup.TLabel",text="Contact     :",font=('Arial, 11'))
    contact_label.place(x=20,y=90)
    
    contact_entry=ttk.Entry(signup_frame,width=30)
    contact_entry.place(x=110,y=90)
    
    address_label=ttk.Label(signup_frame,style="Signup.TLabel",text="Address    :",font=('Arial, 11'))
    address_label.place(x=20,y=125)
    
    address_entry=ttk.Entry(signup_frame,width=30)
    address_entry.place(x=110,y=125)
    
    email_label=ttk.Label(signup_frame,style="Signup.TLabel",text="E-mail       :",font=('Arial, 11'))
    email_label.place(x=20,y=155)
    
    email_entry=ttk.Entry(signup_frame,width=30)
    email_entry.place(x=110,y=155)
    
    password_label=ttk.Label(signup_frame,style="Signup.TLabel",text="Password :",font=('Arial', 11))
    password_label.place(x=20,y=185)
    
    password_entry=ttk.Entry(signup_frame,width=30,show="*")
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
            Top.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email or username already exists")
    
    ttk.Button(signup_frame, text='Submit',command=submit_signup,takefocus=False,style="signin.TButton").place(x=160, y=255)


    return signup_frame

