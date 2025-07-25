
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
    manager_frame_style=ttk.Style()
    manager_frame_style.configure("manager.TFrame",background="#ECECFA")
    manager_frame = ttk.Frame(top, width=1200, height=675,style="manager.TFrame")
    manager_frame.place(x=0,y=0)
   
    Topframe = ttk.Frame(manager_frame, height=120, width=1200)
    Topframe.place(x=0,y=0)

   
    BtmFrame = ttk.Frame(manager_frame, height=(675 - 120), width=1200)
    BtmFrame.place(x=0, y=120)

    
    
    
    pages=Pages.manager_page_init(BtmFrame)
  
    for page in pages.values():
        page.place(x=0,y=0) 
    PageSwitcher.manager_page_switcher("Default") 
    
    manage_homepage_btn = Button(Topframe, text="Manage Homepage", font=('Arial', 14),command=lambda: PageSwitcher.manager_page_switcher("Default"))
    manage_homepage_btn.place(x=20, y=40)
    
    check_comments_btn= Button(Topframe,text="Check Comments", font=('Arial',14),command=lambda: PageSwitcher.manager_page_switcher("Check_Comments"))
    check_comments_btn.place(x=370,y=40)
    
    view_orders_btn=Button(Topframe,text="View Orders",font=('Arial',14),command=lambda:PageSwitcher.manager_page_switcher("View_Orders"))
    view_orders_btn.place(x=690,y=40)
    
    add_manager_btn=Button(Topframe,text="Add Manager",font=('Arial',14), command=lambda: PageSwitcher.manager_page_switcher("Add_Manager"))
    add_manager_btn.place(x=1030,y=40)
    
    
    return manager_frame

