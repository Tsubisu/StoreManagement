from tkinter import ttk as ttk
from tkinter import *
from Animation import *
from ProductDisplay import display_product_info




def home_bar_builder(frame):
    import Pages, PageSwitcher as ps
    from LoginWindow import login 
    import app

    home_bar_style = ttk.Style()
    home_bar_style.configure("My.TFrame", background="#5D5C9A")

    HomeBar=ttk.Frame(frame, height=120, width=1200, padding=10, style="My.TFrame")


    MLabel = ttk.Label(HomeBar,text="Guitar Store", font=("Brush Script MT", 35), background="#5D5C9A")
    MLabel.place(x=600, y=45, anchor="center")

    button_style = ttk.Style()
    button_style.configure("My.TButton",font=("Segoe UI Light",11,'bold'),background="#5D5C9A",borderwidth=0,relief='raised')
    button_style.map("My.TButton", background=[("active","#5D5C9A")],foreground=[("pressed","#333333")])

    Home = ttk.Button(HomeBar, text="Home", padding='0.1,0.1',style="My.TButton", takefocus=False, width=6,command=lambda:ps.bottom_page_switcher("Default"))
    Home.place(x=10, y=75)

    Contact = ttk.Button(HomeBar, text="Contact",style="My.TButton", padding='0.1,0.1', takefocus=False, width=8,command=lambda:horizontal_animation(Pages.bottom_pages["Contact"],-1200,0,0,10))
    Contact.place(x=70, y=75)

    Search = ttk.Button(HomeBar, text="Search",style="My.TButton", padding='0.1,0.1', takefocus=False, width=6,command=lambda:vertical_animation(Pages.top_pages["Search"],0,-120,0,2))
    Search.place(x=1000, y=80)

    LogInBtn = ttk.Button(HomeBar, text="LogIn",style="My.TButton", padding='0.1,0.1', takefocus=False, width=6,command=lambda:login(app.root))
    LogInBtn.place(x=1060, y=80)

    Cart = ttk.Button(HomeBar, text="Cart",style="My.TButton", padding='0.1,0.1', takefocus=False, width=6,)
    Cart.place(x=1110, y=80)

    return HomeBar






def home_page(frame):
    import Pages
    home_style=ttk.Style()
    home_style.configure("Home.TFrame", background="#ECECFA")
    home_frame = ttk.Frame(frame,width=1200,height=(675-120),style="Home.TFrame")

    Label(home_frame,text=""" " Unleash Your Sound — Inspire the World " """,font=("Gabriola",20,'bold'),background="#ECECFA").place(x=600, y=30,anchor="center" )
    Label(home_frame,text="Every musician has a voice unheard by others. \n We are dedicated to help artists unleash their voices",font=("Arial",12),background="#ECECFA").place(x=600, y=70,anchor="center")
    Label(home_frame,text="Featured products",font=('Segoe UI Light', 21,'bold'),background="#ECECFA").place(x=30 ,y=90)

    fp_style=ttk.Style()
    fp_style.configure("FeaturedFrame.TFrame", background="green")


    f1=ttk.Frame(home_frame,width=345,height=380,style="FeaturedFrame.TFrame")
    f1.place(x=75, y=150)

    p1_button=ttk.Button(f1,text="test",command=lambda:display_product_info(1,Pages.bottom_pages["Default"]))
    p1_button.place(x=120,y=350)

    f2=ttk.Frame(home_frame,width=345,height=380,style="FeaturedFrame.TFrame")
    f2.place(x=425, y=150)

    f3 = ttk.Frame(home_frame, width=345, height=380, style="FeaturedFrame.TFrame")
    f3.place(x=775, y=150)




    return home_frame

