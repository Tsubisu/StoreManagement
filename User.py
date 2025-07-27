import sqlite3
import Pages
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
user=None
user_id=None
manager=None
manager_id=None
manager_contact=None
manager_address=None
manager_password=None
manager_email=None
def update_logged_status(email):
    global user,user_id
    from LoginWindow import login
    from OrderPage import Show_order
    import app
    if email!=None:
        conn=sqlite3.connect('store.db')
        c=conn.cursor()
        c.execute('''SELECT * FROM user WHERE email=?''', (email,))
        data=c.fetchone()
        conn.close()
        user=data[0]
        user_id=data[5]

        Show_order()
        Label(Pages.top_pages["Home_bar"],text="Logged in: {}".format(data[0]),background="#5D5C9A",font=("Segoe UI Light",8,"bold")).place(x=10,y=0)
        for child in Pages.top_pages["Home_bar"].winfo_children():
            if (isinstance(child,ttk.Button)) and child['text']=="LogIn":
                child.configure(text="profile")
                child.configure(command=lambda:profile(data[5]))

    else:

        user=None
        user_id=None
        Show_order()
        print("updated the order page")
        for child in Pages.top_pages["Home_bar"].winfo_children():
            if (isinstance(child, ttk.Button)) and child['text'] == "profile":
                child.configure(text="LogIn")
                child.configure(command=lambda:login(app.root))

            if (isinstance(child, Label)) and child.cget("text").startswith("Logged in:"):
                child.destroy()







def profile(id):
    import app
    conn=sqlite3.connect('store.db')
    c=conn.cursor()
    c.execute('''SELECT * FROM user WHERE user_id=?''', (id,))
    data=[c.fetchone()]
    conn.close()

    def log_out():
       if messagebox.askquestion("Log out", "Are you sure you want to log out?", icon="warning"):
           update_logged_status(None)
           top.destroy()

    def update_profile():

        Label(update, text="Update Profile", font=("Segoe UI Light", 18), background="#ECECFA").place(x=200, y=40,
                                                                                                       anchor="center")
        Label(update, text="Name                :", font=("Segoe UI Light", 15), background="#ECECFA").place(x=30, y=80)
        Label(update, text="Email                 :", font=("Segoe UI Light", 15), background="#ECECFA").place(x=30, y=110)
        Label(update, text="Contact             :", font=("Segoe UI Light", 15), background="#ECECFA").place(x=30, y=140)
        Label(update, text="Address            :", font=("Segoe UI Light", 15), background="#ECECFA").place(x=30, y=170)
        Label(update, text="Old Password   :", font=("Segoe UI Light", 15), background="#ECECFA").place(x=30, y=200)
        Label(update, text="New Password :", font=("Segoe UI Light", 15), background="#ECECFA").place(x=30, y=230)

        Name=ttk.Entry(update)
        Name.place(x=170, y=90)

        Email=ttk.Entry(update)
        Email.place(x=170, y=120)

        Contact=ttk.Entry(update)
        Contact.place(x=170, y=150)

        Address=ttk.Entry(update)
        Address.place(x=170, y=180)

        Old_password=ttk.Entry(update,show="*")
        Old_password.place(x=170, y=210)

        New_password=ttk.Entry(update,show="*")
        New_password.place(x=170, y=240)

        def default_text():
            Name.delete(0, END)
            Name.insert(0, data[0][0])

            Email.delete(0, END)
            Email.insert(0, data[0][3])

            Contact.delete(0, END)
            Contact.insert(0, data[0][1])

            Address.delete(0, END)
            Address.insert(0, data[0][2])

            Old_password.delete(0, END)
            New_password.delete(0, END)

        default_text()

        def save_data():

            name = Name.get().strip()
            email = Email.get().strip()
            contact = Contact.get().strip()
            address = Address.get().strip()
            old_password = Old_password.get().strip()
            new_password = New_password.get().strip()

            connect = sqlite3.connect('store.db')
            cursor = connect.cursor()

            if ((name!="" and name==data[0][0]) and (email!="" and email==data[0][3]) and (contact!="" and contact==data[0][1]) and (address!="" and address==data[0][2])) and(old_password!="" and new_password!=""):
                if old_password!=data[0][4]:
                    messagebox.showerror("Error", "Old password is incorrect")

                elif old_password==data[0][4] and old_password!=new_password:
                    cursor.execute('''UPDATE user SET password=? WHERE user_id=?''', (new_password,id))
                    messagebox.showinfo("Success", "password changed")
                    connect.commit()
                    connect.close()
                    update_logged_status(None)
                    top.destroy()
                else:
                    messagebox.showerror("Error", "Enter a new password")

            elif (name!="" and email!="" and contact!="" and address!="" and old_password!="" and new_password!="") and(old_password==data[0][4] and old_password!=new_password ) :
                    messagebox.showinfo("success","details changed")

                    cursor.execute("""UPDATE user SET full_name=?,contact=?,address=?,email=?,password=?  WHERE user_id=?""",(name,contact,address,email,new_password,id))
                    cursor.execute('''SELECT * FROM user WHERE user_id=?''', (id,))
                    data[0] = cursor.fetchone()
                    connect.commit()
                    connect.close()
                    update_logged_status(None)
                    top.destroy()
            elif (name!="" and email!="" and contact!="" and address!="" and old_password!="" and new_password!="") and(old_password==data[0][4] and old_password==new_password ) :
                    messagebox.showerror("Error", "Enter a new password")
            elif (name != "" and email != "" and contact != "" and address != "" and old_password != "" and new_password != "") and old_password != data[0][4] :

                messagebox.showerror("Error", "Old password is incorrect")
            else:
                messagebox.showerror("Error", "All fields are required.")



        Button(update, text="Update", command=save_data).place(x=300, y=350)
        update.tkraise()

    def delete_data():
        if messagebox.askyesno("delete", "Do you want to delete this record?"):
            connect=sqlite3.connect('store.db')
            cursor=connect.cursor()
            cursor.execute('''DELETE FROM user WHERE user_id=?''', (id,))
            connect.commit()
            connect.close()
            update_logged_status(None)
            top.destroy()



    top=Toplevel(app.root)
    top.geometry("400x400")

    style = ttk.Style()
    style.configure("Update.TFrame",background="#ECECFA")

    Parent=ttk.Frame(top,width=400,height=400,style="Update.TFrame")
    Parent.place(x=0,y=0)

    default=ttk.Frame(Parent,width=400,height=400,style="Update.TFrame")
    update=ttk.Frame(Parent,width=400,height=400,style="Update.TFrame")

    default.place(x=0,y=0)
    update.place(x=0,y=0)


    Label(default, text="Profile Page",font=("Segoe UI Light",18),background="#ECECFA").place(x=200,y=40,anchor="center")
    Label(default, text="Name     : {}".format(data[0][0]),font=("Segoe UI Light",15),background="#ECECFA").place(x=30,y=80)
    Label(default, text="Email      : {}".format(data[0][3]),font=("Segoe UI Light",15),background="#ECECFA").place(x=30,y=110)
    Label(default, text="Contact  : {}".format(data[0][1]), font=("Segoe UI Light", 15), background="#ECECFA").place(x=30,y=140)
    Label(default, text="Address : {}".format(data[0][2]), font=("Segoe UI Light", 15), background="#ECECFA").place(x=30,y=170)

    style.configure("Update.TButton",background="#ECECFA",font=("Segoe UI Light",10),width=6)
    style.map("Update.TButton",background=[("pressed","#ECECFA")])
    ttk.Button(default,text="Update",style="Update.TButton",takefocus=False,command=update_profile).place(x=30,y=220)
    ttk.Button(default,text="Delete",style="Update.TButton",takefocus=False,command=delete_data).place(x=100,y=220)
    ttk.Button(default,text="LogOut",style="Update.TButton",takefocus=False,command=log_out).place(x=170,y=220)

    default.tkraise()
    top.mainloop()


def check_log_status():
    if user is not None:
        return True

    return False

def update_manager_login(email):
    global manager,manager_id,manager_address,manager_contact,manager_email,manager_password
    if email!=None:
        conn=sqlite3.connect('store.db')
        c=conn.cursor()
        c.execute('''SELECT * FROM managers WHERE email=?''',(email,))
        data=c.fetchone()
        manager=data[0]
        manager_contact=data[1]
        manager_address=data[2]
        manager_email=data[3]
        manager_password=data[4]
        manager_id=data[5]
        conn.close()
        