from tkinter import ttk
from tkinter import *
import sqlite3
def view_orders(frame):
    view_style=ttk.Style()
    view_style.configure("view.TFrame", background="#CCCCF3")
    view_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="view.TFrame")
    
    canvas = Canvas(view_page_frame, bg="#ECECFA", width=1200, height=675 - 120, scrollregion=(0, 0, 1200, 10000))
    canvas.pack(expand=True, fill="both", padx=0, pady=0)

    scrollbar = ttk.Scrollbar(view_page_frame, orient='vertical', command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    canvas.configure(yscrollcommand=scrollbar.set)
    #canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 120), "units"))

    scroll_frame = ttk.Frame(canvas, width=1200, height=(675 - 120), padding=(0, 0, 0, 0), style="order.TFrame")
    canvas_window = canvas.create_window((0, 30), window=scroll_frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_frame.bind("<Configure>", on_configure)
     
    scroll_frame.bind("<Configure>", on_configure)
    lblstyle = ttk.Style()
    lblstyle.configure("TLabel",  background="#ECECFA", font=("Seoge UI Light", 12))
    
    order_id = ttk.Label(view_page_frame,style="TLabel",text="order id",font=("Arial", 12))
    order_id.place(x=0, y=0)
    
    user_id = ttk.Label(view_page_frame,style="TLabel",text="user id",font=("Arial", 12))
    user_id.place(x=240, y=0)

    
    product_id= ttk.Label(view_page_frame,style="TLabel",text="product_id",font=("Arial", 12))
    product_id.place(x=480, y=0)

    
    quantity= ttk.Label(view_page_frame,style="TLabel",text="quantity",font=("Arial", 12)) 
    quantity.place(x=700, y=0)
    
    total_price = ttk.Label(view_page_frame,style="TLabel",text="total_price",font=("Arial", 10))
    total_price.place(x=900, y=0)
    
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    datas=cursor.fetchall()
    conn.close()
    
    for data in datas:
        style=ttk.Style()
        style.configure("TFrame", background="#ECECFA")
        orders_frame = ttk.Frame(scroll_frame, width=1200, height=40,style="TFrame")
        ttk.Label(orders_frame, text=data[0], font=("Arial", 12), background="#ECECFA").place(x=0,y=10,anchor="nw")
        ttk.Label(orders_frame, text=data[1], font=("Arial", 12), background="#ECECFA").place(x=240,y=10,anchor="nw")
        ttk.Label(orders_frame, text=data[2], font=("Arial", 12), background="#ECECFA").place(x=480,y=10,anchor="nw")
        ttk.Label(orders_frame, text=data[3], font=("Arial", 12), background="#ECECFA").place(x=700,y=10,anchor="nw")
        ttk.Label(orders_frame, text=data[4], font=("Arial", 12), background="#ECECFA").place(x=900,y=10,anchor="nw")
        orders_frame.grid(padx=5, pady=2)
    return view_page_frame
