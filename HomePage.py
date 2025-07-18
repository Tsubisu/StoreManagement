from tkinter import ttk as ttk
from Animation import *
from LoginWindow import login



def home_bar_builder(frame):
    import Pages, PageSwitcher as ps


    HomeBar=ttk.Frame(frame, height=120, width=1200, padding=10, style="My.TFrame")

    MLabel = ttk.Label(HomeBar, text="Music Store", style="My.TLabel", font=("French Script Mt", 25))
    MLabel.place(x=600, y=25, anchor="center")

    Home = ttk.Button(HomeBar, text="Home", padding='0.1,0.1', takefocus=False, width=6,command=lambda:ps.bottom_page_switcher("Default"))
    Home.place(x=10, y=80)

    Contact = ttk.Button(HomeBar, text="Contact", padding='0.1,0.1', takefocus=False, width=8,command=lambda:horizontal_animation(Pages.bottom_pages["Contact"],-1200,0,0,10))
    Contact.place(x=60, y=80)

    Search = ttk.Button(HomeBar, text="Search", padding='0.1,0.1', takefocus=False, width=6,command=lambda:vertical_animation(Pages.top_pages["Search"],0,-120,0,2))
    Search.place(x=1010, y=80)

    import app
    LogInBtn = ttk.Button(HomeBar, text="LogIn", padding='0.1,0.1', takefocus=False, width=6,command=lambda:login(app.root))
    LogInBtn.place(x=1060, y=80)

    Cart = ttk.Button(HomeBar, text="Cart", padding='0.1,0.1', takefocus=False, width=6,)
    Cart.place(x=1110, y=80)

    return HomeBar






def home_page(frame):
    home_style=ttk.Style()
    home_style.configure("Home.TFrame", background="Green")
    home_frame = ttk.Frame(frame,width=1200,height=(675-120),style="Home.TFrame")


    return home_frame

