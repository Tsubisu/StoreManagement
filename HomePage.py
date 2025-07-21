from tkinter import ttk as ttk
from tkinter import *

from PIL.Image import Resampling

from Animation import *
from ProductDisplay import display_product_info
import sqlite3
from PIL import ImageTk, Image


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

    Label(home_frame,text=""" " Unleash Your Sound — Inspire the World " """,font=("Gabriola",28,'bold'),background="#ECECFA").place(x=600, y=30,anchor="center" )
    Label(home_frame,text="Every musician has a voice unheard by others. \n We are dedicated to help artists unleash their voices",font=("Verdana",13),background="#ECECFA").place(x=600, y=75,anchor="center")
    Label(home_frame,text="Featured products",font=('Segoe UI Light', 21,'bold'),background="#ECECFA").place(x=30 ,y=90)

    fp_style=ttk.Style()
    fp_style.configure("FeaturedFrame.TFrame", background="#ECECFA")


    conn=sqlite3.connect("store.db")
    c=conn.cursor()
    c.execute('''SELECT * FROM Products WHERE product_id IN (1,2,3,4)''')
    rows=c.fetchall()
    conn.close()


    button_style=ttk.Style()
    button_style.configure("Name.TButton", background="#ECECFA",font=("Segoe UI Light",16),borderwidth=0,relief='solid')
    button_style.map("Name.TButton", background=[("active","#ECECFA"),("pressed","#ECECFA")])


    f1=ttk.Frame(home_frame,width=290,height=380,style="FeaturedFrame.TFrame")
    f1.place(x=15, y=150)

    f1_image=Image.open("images/1.png")
    f1_image=f1_image.resize((290,300),Image.Resampling.LANCZOS)
    f1_image=ImageTk.PhotoImage(f1_image)
    f1_label=Label(f1,image=f1_image)
    f1_label.place(x=0,y=0)
    f1_label.image=f1_image

    p1_button=ttk.Button(f1,text=rows[0][1],width=52,style="Name.TButton",takefocus=False,command=lambda:display_product_info(1,Pages.bottom_pages["Default"]))
    p1_button.place(x=145,y=325,anchor="center")

    p1_label=Label(f1,text="Rs{} NPR".format(rows[0][3]),background="#ECECFA",font=("Segoe UI Light",14))
    p1_label.place(x=145,y=351,anchor="center")





    f2=ttk.Frame(home_frame,width=290,height=380,style="FeaturedFrame.TFrame")
    f2.place(x=308, y=150)

    f2_image = Image.open("images/2.png")
    f2_image = f2_image.resize((290, 300), Image.Resampling.LANCZOS)
    f2_image = ImageTk.PhotoImage(f2_image)
    f2_label = Label(f2, image=f2_image)
    f2_label.place(x=0, y=0)
    f2_label.image = f2_image

    p2_button = ttk.Button(f2, text=rows[1][1], width=52, style="Name.TButton", takefocus=False,
                           command=lambda: display_product_info(2, Pages.bottom_pages["Default"]))
    p2_button.place(x=145, y=325, anchor="center")

    p2_label = Label(f2, text="Rs{} NPR".format(rows[1][3]), background="#ECECFA", font=("Segoe UI Light", 14))
    p2_label.place(x=145, y=351, anchor="center")






    f3 = ttk.Frame(home_frame, width=290, height=380, style="FeaturedFrame.TFrame")
    f3.place(x=601, y=150)



    f3_image = Image.open("images/3.png")
    f3_image = f3_image.resize((290, 300), Image.Resampling.LANCZOS)
    f3_image = ImageTk.PhotoImage(f3_image)
    f3_label = Label(f3, image=f3_image)
    f3_label.place(x=0, y=0)
    f3_label.image = f3_image

    p3_button = ttk.Button(f3, text=rows[2][1], width=52, style="Name.TButton", takefocus=False,
                           command=lambda: display_product_info(3, Pages.bottom_pages["Default"]))
    p3_button.place(x=145, y=325, anchor="center")

    p3_label = Label(f3, text="Rs{} NPR".format(rows[2][3]), background="#ECECFA", font=("Segoe UI Light", 14))
    p3_label.place(x=145, y=351, anchor="center")


    f4 = ttk.Frame(home_frame, width=290, height=380, style="FeaturedFrame.TFrame")
    f4.place(x=894, y=150)

    f4_image = Image.open("images/4.png")
    f4_image = f4_image.resize((290, 300), Image.Resampling.LANCZOS)
    f4_image = ImageTk.PhotoImage(f4_image)
    f4_label = Label(f4, image=f4_image)
    f4_label.place(x=0, y=0)
    f4_label.image = f4_image

    p4_button = ttk.Button(f4, text=rows[3][1], width=52, style="Name.TButton", takefocus=False,
                           command=lambda: display_product_info(4, Pages.bottom_pages["Default"]))
    p4_button.place(x=145, y=325, anchor="center")

    p4_label = Label(f4, text="Rs{} NPR".format(rows[2][3]), background="#ECECFA", font=("Segoe UI Light", 14))
    p4_label.place(x=145, y=351, anchor="center")
    return home_frame

