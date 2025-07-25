import sqlite3
from tkinter import ttk as ttk
from tkinter import*
from PIL import Image, ImageTk

import Pages
from Animation import *
from re import sub
from ProductDisplay import display_product_info

Product_frame=None

def search_bar(frame):
    global search_string

    import PageSwitcher as ps

    search_bar_style = ttk.Style()
    search_bar_style.configure("Search_bar.TFrame", background="#D1D1E9")
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

    def search():
        search_item = search_box.get()
        if search_item!="":
            ps.bottom_page_switcher("Search")
            update_scroll_frame(search_item)
        search_box.delete(0, "end")


    search_button=ttk.Button(search_box_frame,image=icon,style="Search_button.TButton",width=4,takefocus=0,padding=(0,0),command=search)
    search_button.image = icon
    search_button.place(x=430,y=4)






    exit_style=ttk.Style()
    exit_style.configure("Search.TButton", background="#D1D1E9",borderwidth=0,font=("Arial Unicode MS", 18))
    exit_style.map("Search.TButton",background=[("active", "#D1D1E9")],foreground=[("pressed", "grey")])
    exit_btn=ttk.Button(search_bar_frame,text="X",takefocus=False,style="Search.TButton",width=2,command=lambda:exit(search_box,search_bar_frame))
    exit_btn.place(x=850,y=60)

    return search_bar_frame


def search_page(frame):
    search_style=ttk.Style()
    search_style.configure("Search.TFrame", background="#ECECFA")
    search_frame = ttk.Frame(frame,width=1200,height=(675-120),style="Search.TFrame")

    canvas = Canvas(search_frame, bg="#ECECFA", width=1200, height=675 - 120, scrollregion=(0, 0, 1200, 1000))
    canvas.pack(expand=True, fill="both",padx=0, pady=0)

    scrollbar = ttk.Scrollbar(search_frame, orient='vertical', command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 120), "units"))

    scroll_frame = ttk.Frame(canvas,width=1200,height=(675-120),padding=(0,0,0,0),style="Search.TFrame")

    canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_frame.bind("<Configure>", on_configure)

    global Product_frame
    Product_frame = scroll_frame
    return search_frame

def exit(entry,search_bar_frame):
    vertical_animation(search_bar_frame, 0, 0, -120, -2, Pages.top_pages["Home_bar"])
    entry.delete(0,END)

def update_scroll_frame(string):
    global Product_frame
    for widgets in Product_frame.winfo_children():
        widgets.destroy()
    conn=sqlite3.connect("store.db")
    c=conn.cursor()
    c.execute("SELECT * FROM products;" )
    row=c.fetchall()
    conn.close()
    name=string.lower()
    max_col=4
    Row=0
    Col=0
    for data in row:

        if sub(r"\s+","",name) in sub(r"\s+","",data[1].lower()) :
            id=data[0]
            style = ttk.Style()
            style.configure("Product.TFrame",background="#ECECFA")
            p_frame=ttk.Frame(Product_frame,width=275,height=250,style="Product.TFrame")

            product_image=Image.open("images/{}.png".format(data[0]))
            product_image=product_image.resize((275,180),Image.Resampling.LANCZOS)
            product_image=ImageTk.PhotoImage(product_image)

            image_label=Label(p_frame,image=product_image)
            image_label.image = product_image
            image_label.place(x=10,y=6)


            style = ttk.Style()
            style.configure("Product.TButton",background="#ECECFA",font=("Segoe UI",12),borderwidth=0)
            style.map("Product.TButton",background=[("selected", "#ececfa")])

            p_name=ttk.Button(p_frame,text=data[1],style="Product.TButton",takefocus=False,command=lambda:display_product_info(id,"Search"))
            p_name.place(x=125,y=210,anchor="center")

            price = Label(p_frame, text="Rs{:,}.00 NPR".format(data[3]), background="#ECECFA", font=("Segoe UI Light", 14))
            price.place(x=125,y=240,anchor="center")

            p_frame.grid(row=Row,column=Col,padx=((50,0) if Col==0 else (0,50) if Col==max_col-1 else (0,0)),pady=((30,0) if Row==0 else 10))
            p_frame.pack_propagate(False)

            Col=Col+1
            if Col>=max_col:
                Row=Row+1
                Col=0



