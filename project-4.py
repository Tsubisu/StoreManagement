from tkinter import *
from tkinter import messagebox
import sqlite3

def init_db():
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
               email TEXT PRIMARY KEY,
               username TEXT UNIQUE,
               password TEXT)""")
    conn.commit()
    conn.close()

init_db()

top = Tk()
top.title('User Authentication')
top.geometry('600x600')

login_frame = Frame(top)
signup_frame = Frame(top)

def show_login():
    signup_frame.pack_forget()  
    login_frame.pack(fill=BOTH, expand=True)  

def show_signup():
    login_frame.pack_forget()  
    signup_frame.pack(fill=BOTH, expand=True)  

Label(login_frame, text='Login', font=('Arial', 16)).pack(side=TOP)
Label(login_frame, text='Username:').place(x=20,y=40)
username_entry = Entry(login_frame)
username_entry.place(x=90, y=40)
Label(login_frame, text='Password:').place(x=20, y=80)
password_entry = Entry(login_frame, show="*")
password_entry.place(x=90, y=80)

def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid username or password")

Label(signup_frame, text='Sign Up', font=('Arial', 16)).pack(side=TOP)
Label(signup_frame, text='E-mail:').place(x=20, y=20)
email_entry = Entry(signup_frame)
email_entry.place(x=130, y=20)
Label(signup_frame, text='Username:').place(x=20, y=60)
new_username_entry = Entry(signup_frame)
new_username_entry.place(x=130, y=60)
Label(signup_frame, text='Password:').place(x=20, y=100)
new_password_entry = Entry(signup_frame, show="*")
new_password_entry.place(x=130, y=100)

def submit_signup():
    email = email_entry.get()
    username = new_username_entry.get()
    password = new_password_entry.get()

    if not all([email, username, password]):
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = sqlite3.connect("user_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (email, username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration successful!")
        show_login()  
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email or username already exists")

Button(signup_frame, text='Submit', command=submit_signup).place(x=130, y=140)
Button(signup_frame, text='Back to Login', command=show_login).place(x=130, y=180)

Button(login_frame, text='Login', command=login).place(x=90, y=120) 
Button(login_frame, text='Signup', command=show_signup).place(x=150, y=120)

show_login()

top.mainloop()