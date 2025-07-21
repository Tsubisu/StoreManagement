
from tkinter import ttk as ttk
from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def display_product_info(id,return_frame):
    from app import BtmFrame

    product_frame_style = ttk.Style()
    product_frame_style.configure("display.TFrame", background="#ECECFA")

    product_display_frame=ttk.Frame(BtmFrame,width=1200,height=555,style="display.TFrame")
    product_display_frame.place(x=0,y=0)

    image_frame_style = ttk.Style()
    image_frame_style.configure("ImageFrame.TFrame", background="#ECECFA")
    product_image_frame=ttk.Frame(product_display_frame,width=500,height=500,style="ImageFrame.TFrame")
    product_image_frame.place(x=50,y=25)

    try:
        product_image=Image.open("images/{}.png".format(id))
        product_image=product_image.resize((500,500),Image.Resampling.LANCZOS)
        image=ImageTk.PhotoImage(product_image)


        PImage=Label(product_image_frame,image=image)
        PImage.image = image
        PImage.place(x=0,y=0)
    except FileNotFoundError:
        Label(product_image_frame,text="Image Not Found",
              font=('Arial',25),
              background="White").place(x=250,y=250,anchor="center")


    conn = sqlite3.connect("store.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM products where product_id=?""",(id,))
    rows = c.fetchall()
    conn.close()




    product_name=ttk.Label(product_display_frame,text="{}".format(rows[0][1]),font=('Segoe UI Light',27),background="#ECECFA")
    product_name.place(x=700,y=10,anchor="nw")

    price=ttk.Label(product_display_frame,text="Rs {} Npr".format(rows[0][3]),font=('Segoe UI Light',18),background="#ECECFA")
    price.place(x=700,y=60,anchor="nw")

    description=ttk.Label(product_display_frame,text="{}".format(rows[0][2]),wraplength=390,font=('Segoe UI Light',14),background="#ECECFA")
    description.place(x=700,y=100,anchor="nw")







