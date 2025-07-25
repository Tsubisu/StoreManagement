
from tkinter import ttk as ttk
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox


def display_product_info(id,return_frame):
    from app import BtmFrame
    import PageSwitcher as ps
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
    rows = c.fetchone()
    conn.close()




    product_name=ttk.Label(product_display_frame,text="{}".format(rows[1]),font=('Segoe UI Light',27),background="#ECECFA")
    product_name.place(x=700,y=10,anchor="nw")

    price=ttk.Label(product_display_frame,text="Rs {} Npr".format(rows[3]),font=('Segoe UI Light',18),background="#ECECFA")
    price.place(x=700,y=60,anchor="nw")

    availability=""
    if rows[4]>0:
        availability="Available"
    else:
        availability="Not Available"
    ttk.Label(product_display_frame,text="{}".format(availability),font=('Segoe UI Light',18,'bold'),background="#ECECFA",foreground="Red").place(x=700,y=90,anchor="nw")
    ttk.Label(product_display_frame, text="Quantity", font=('Segoe UI Light',10,), background="#ECECFA").place(x=710, y=130, anchor="nw")
    quantity=Entry(product_display_frame,width=10)
    quantity.place(x=710, y=160, anchor="nw")




    def take_order():
        import User
        n = quantity.get()
        if not User.check_log_status():
            messagebox.showerror("Log Error","You need to be logged in to take an order")
        elif  User.check_log_status() and availability!="Available":
            messagebox.showerror("Error","The product is not currently available")
        elif User.check_log_status() and availability=="Available" :
            try:
                if int(n)<=0:
                    messagebox.showerror("Error","Enter quantity greater than 0 ")

                elif int(n)>rows[4]:
                    messagebox.showerror("Error","We only have {} remaining in stock".format(rows[4]))

                else:
                    messagebox.showinfo("Order Success", "Order has been taken")

                    conn=sqlite3.connect("store.db")


                    c = conn.cursor()
                    c.execute( '''INSERT INTO orders (user_id,product_id,quantity,total_price) VALUES (?,?,?,?) ''',
                        (User.user_id, id, int(n), (int(n) * rows[3])))
                    conn.commit()
                    conn.close()


                    oc=sqlite3.connect("store.db")
                    cu = oc.cursor()
                    cu.execute("""UPDATE products SET quantity=quantity-? WHERE product_id=?""",(int(n), id))
                    oc.commit()
                    oc.close()

                    from OrderPage import Show_order
                    Show_order()

            except ValueError:
                messagebox.showerror("Error","Enter correct quantity ")








    Button(product_display_frame,text="Buy it now",font=("Arial",13,'bold'),width=12,background="black",foreground="white",command=take_order).place(x=710,y=200)
    description=ttk.Label(product_display_frame,text="{}".format(rows[2]),wraplength=390,font=('Segoe UI Light',14),background="#ECECFA")


    description.place(x=700,y=250,anchor="nw")



    style = ttk.Style()
    style.configure("Display.TButton",background="#ECECFA")
    style.map("Display.TButton",background=[("selected", "#ececfa")])
    return_btn=ttk.Button(product_display_frame,style="Display.TButton",text="Return",command=lambda:ps.bottom_page_switcher(return_frame),takefocus=False)
    return_btn.place(x=1050,y=20,anchor="nw")











