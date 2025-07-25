
from tkinter import *
from tkinter import ttk as ttk
import sqlite3
from tkinter import messagebox



def show_manager():
    import Pages, PageSwitcher,app
    global top, Btmframe
    top=Toplevel(app.root)
    top.geometry("1200x675")
    top.title("Manager")
    top.resizable(False,False)
    manager_frame = ttk.Frame(top, width=1200, height=675)
    manager_frame.place(x=0,y=0)
   
    Topframe_style=ttk.Style()
    Topframe_style.configure("tf.TFrame",background="#5D5C9A")
    Topframe = ttk.Frame(manager_frame, height=120, width=1200,style="tf.TFrame")
    Topframe.place(x=0,y=0)

   
    BtmFrame = ttk.Frame(manager_frame, height=(675 - 120), width=1200)
    BtmFrame.place(x=0, y=120)

    
    
    
    pages=Pages.manager_page_init(BtmFrame)
  
    for page in pages.values():
        page.place(x=0,y=0) 
    PageSwitcher.manager_page_switcher("Default") 
    
    buttons=ttk.Style()
    buttons.configure("button.TButton",background="#5D5C9A",font=("Segoe UI Light",11,'bold'),borderwidth=0)
    buttons.map("button.TButton", background=[("active","#5D5C9A")],foreground=[("pressed","#333333")])
    manage_homepage_btn = ttk.Button(Topframe, text="Manage Homepage",style="button.TButton",takefocus=False,command=lambda: PageSwitcher.manager_page_switcher("Default"))
    manage_homepage_btn.place(x=20, y=120,anchor="sw")
    
    check_comments_btn= ttk.Button(Topframe,text="Check Comments",style="button.TButton",takefocus=False,command=lambda: PageSwitcher.manager_page_switcher("Check_Comments"))
    check_comments_btn.place(x=185,y=120,anchor="sw")
    
    view_orders_btn=ttk.Button(Topframe,text="View Orders",style="button.TButton",takefocus=False,command=lambda:PageSwitcher.manager_page_switcher("View_Orders"))
    view_orders_btn.place(x=345,y=120,anchor="sw")
    
    add_manager_btn=ttk.Button(Topframe,text="Add Manager",style="button.TButton",takefocus=False, command=lambda: PageSwitcher.manager_page_switcher("Add_Manager"))
    add_manager_btn.place(x=470,y=120,anchor="sw")
    
    
    return manager_frame

