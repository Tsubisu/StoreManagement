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
    login_frame = ttk.Frame(frame, width=600, height=600)
    
    Label(login_frame, text='Login', font=('Arial', 16)).place(x=200,y=30,anchor="center")
    
    Label(login_frame, text='Username:').place(x=20, y=75)
    username_entry = Entry(login_frame)
    username_entry.place(x=90, y=75)
    
    Label(login_frame, text='Password:').place(x=20, y=115)
    password_entry = Entry(login_frame, show="*")
    password_entry.place(x=90, y=115)

    Button(login_frame, text='Login').place(x=90, y=155)
    Button(login_frame, text='Signup', command=lambda: page_switcher("Sign up")).place(x=150,y=155)
    return login_frame


def show_signup(frame, page_switcher):
    signup_frame = ttk.Frame(frame, width=600, height=600)
    
    login_label=Label(signup_frame,text="Sign Up",font=('Arial',20))
    login_label.place(x=200,y=20,anchor="center")
    
    Button(signup_frame, text='Back' , width=7,command=lambda: page_switcher("Login")).place(x=30, y=10)
    
    fullname=Label(signup_frame,text='Full Name :',font=('Arial, 11'))
    fullname.place(x=20,y=55)
    
    fullname_entry=ttk.Entry(signup_frame,width=30)
    fullname_entry.place(x=110,y=55)
    
    username_label=Label(signup_frame,text="Username :",font=('Arial, 11'))
    username_label.place(x=20,y=90)
    
    username_entry=ttk.Entry(signup_frame,width=30)
    username_entry.place(x=110,y=90)
    
    contact_label=Label(signup_frame,text="Contact     :",font=('Arial, 11'))
    contact_label.place(x=20,y=125)
    
    contact_entry=ttk.Entry(signup_frame,width=30)
    contact_entry.place(x=110,y=125)
    
    address_label=Label(signup_frame,text="Address    :",font=('Arial, 11'))
    address_label.place(x=20,y=155)
    
    address_entry=ttk.Entry(signup_frame,width=30)
    address_entry.place(x=110,y=155)
    
    email_label=Label(signup_frame,text="E-mail       :",font=('Arial, 11'))
    email_label.place(x=20,y=185)
    
    email_entry=ttk.Entry(signup_frame,width=30)
    email_entry.place(x=110,y=185)
    
    password_label=Label(signup_frame,text="Password :",font=('Arial', 11))
    password_label.place(x=20,y=215)
    
    password_entry=ttk.Entry(signup_frame,width=30)
    password_entry.place(x=110,y=215)
    
    Button(signup_frame, text='Submit').place(x=160, y=255)
    
    
    


    return signup_frame

