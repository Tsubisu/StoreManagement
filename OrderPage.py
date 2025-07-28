import sqlite3
from tkinter import ttk as ttk, messagebox
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.patches import BoxStyle

Order_frame=None
def order_page(frame):
    order_style=ttk.Style()
    order_style.configure("order.TFrame", background="#ECECFA")
    order_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="order.TFrame")

    canvas = Canvas(order_page_frame, bg="#ECECFA", width=1200, height=675 - 120, scrollregion=(0, 0, 1200, 1000))
    canvas.pack(expand=True, fill="both", padx=0, pady=0)

    scrollbar = ttk.Scrollbar(order_page_frame, orient='vertical', command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    canvas.configure(yscrollcommand=scrollbar.set)

    scroll_frame = ttk.Frame(canvas, width=1200, height=(675 - 120), padding=(0, 0, 0, 0), style="order.TFrame")
    canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_frame.bind("<Configure>", on_configure)

    global Order_frame
    Order_frame = scroll_frame

    Show_order()


    return order_page_frame

def Show_order():
    import User
    global Order_frame

    for widgets in Order_frame.winfo_children():
        widgets.destroy()
    if not User.check_log_status():
        Label(Order_frame,text="Login to see your orders",background="#ECECFA",font=("Segoe UI Light",24,'bold')).place(x=600,y=255,anchor="center")
    else:
        conn = sqlite3.connect("store.db")
        c = conn.cursor()
        c.execute("SELECT * FROM orders where user_id=?",(User.user_id,))
        orders=c.fetchall()
        if orders is not None:
            def cancel_order(order_id):
                if messagebox.askyesno("Cancel Order","Do you really want to cancel this order?"):
                    conn = sqlite3.connect("store.db")
                    cur=conn.cursor()
                    cur.execute("DELETE FROM orders WHERE order_id=?",(order_id,))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Cancel Order","Your order has been cancelled")
                    Show_order()



            for order in orders:

                pc=sqlite3.connect("store.db")
                pcur=pc.cursor()
                pcur.execute("SELECT * FROM products WHERE product_id=?",(order[2],))
                product=pcur.fetchone()
                pc.close()


                style = ttk.Style()
                style.configure("order_display.TFrame", background="white")

                order_display=ttk.Frame(Order_frame,style="order_display.TFrame",width=1100,height=100)

                product_image=Image.open("images/{}.png".format(product[0]))
                product_image=product_image.resize((120,90),Image.Resampling.LANCZOS)
                product_image=ImageTk.PhotoImage(product_image)

                image_label = ttk.Label(order_display, image=product_image)
                image_label.image = product_image
                image_label.place(x=10,y=3)



                Label(order_display,text="{}".format(product[1]),font=('Segoe UI Light',15),background='white').place(x=350,y=50,anchor="center")
                Label(order_display,text="Quantity: {}".format(order[3]),font=('Segoe UI Light',15),background='white').place(x=550,y=50,anchor="center")
                Label(order_display, text="Total price: {}".format(order[4]),font=('Segoe UI Light',15),background='white').place(x=750, y=50, anchor="center")

                bstyle = ttk.Style()
                bstyle.configure("cancel.TButton", background="black",foreground="white",borderwidth=0,relief="solid")
                bstyle.map("cancel.TButton", foreground=[("pressed","black")],background=[("pressed","white")])
                ttk.Button(order_display,text="Cancel order",takefocus=False,style="cancel.TButton",command=lambda:cancel_order(order[0])).place(x=950,y=50,anchor="center")


                order_display.grid(padx=(40,50),pady=(30,0))









