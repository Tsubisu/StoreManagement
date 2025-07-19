from tkinter import ttk as ttk
from tkinter import*
from PIL import Image, ImageTk
from Animation import *

def search_bar(frame):

    import PageSwitcher as ps

    search_bar_style = ttk.Style()
    search_bar_style.configure("Search_bar.TFrame", background="white")
    search_bar_frame=ttk.Frame(frame, style="Search_bar.TFrame",width=1200,height=120)

    search_box_frame_style = ttk.Style()
    search_box_frame_style.configure("Search_box_frame.TFrame", background="white",bd=0,relief="solid")
    search_box_frame=ttk.Frame(search_bar_frame, style="Search_box_frame.TFrame",width=475,height=39)
    search_box_frame.place(x=600,y=80,anchor="center")

    search_box=Entry(search_box_frame,width=41,bd=0,font=("Verdana",12))
    search_box.place(x=5,y=10)

    search_button_style = ttk.Style()
    search_button_style.configure("Search_button.TButton",borderwidth=0,background="white")

    search_img=Image.open("images/search.png")
    search_img=search_img.resize((36,27),Image.Resampling.LANCZOS)
    icon = ImageTk.PhotoImage(search_img)
    search_button=ttk.Button(search_box_frame,style="Search_button.TButton",image=icon,width=4,takefocus=0,padding=(0,0))
    search_button.image = icon
    search_button.place(x=430,y=3)

    exit_style=ttk.Style()
    exit_style.configure("Search.TButton", background="white",borderwidth=0,font=("Arial Unicode MS", 18))
    exit_style.map("Search.TButton",background=[("active", "white")],foreground=[("pressed", "grey"),("active", "grey")])
    exit_btn=ttk.Button(search_bar_frame,text="X",takefocus=False,style="Search.TButton",width=2,command=lambda:exit(search_box,search_bar_frame))
    exit_btn.place(x=850,y=60)

    return search_bar_frame

def search_page(frame):
    search_style=ttk.Style()
    search_style.configure("Search.TFrame", background="pink")
    search_frame = ttk.Frame(frame,width=1200,height=(675-120),style="Search.TFrame")

    return search_frame

def exit(entry,search_bar_frame):
    vertical_animation(search_bar_frame, 0, 0, -120, -2, Pages.top_pages["Home_bar"])
    entry.delete(0,END)



