import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


def add_product(frame):
    style = ttk.Style()
    style.configure("TFrame", background="#ECECFA")
    add_product_page=ttk.Frame(frame,style="TFrame",width=1200,height=(675-120))
    add_product_page.place(x=0,y=0)

    ttk.Label(add_product_page, text="Name        :", background="#ECECFA", font=("Segoe UI Light", 16)).place(
        x=10, y=40, anchor="nw")
    ttk.Label(add_product_page, text="Price          :", background="#ECECFA", font=("Segoe UI Light", 16)).place(
        x=10, y=70, anchor="nw")
    ttk.Label(add_product_page, text="Quantity     :", background="#ECECFA", font=("Segoe UI Light", 16)).place(
        x=10, y=100, anchor="nw")
    ttk.Label(add_product_page, text="Description :", background="#ECECFA", font=("Segoe UI Light", 16)).place(
        x=10, y=130, anchor="nw")

    name = ttk.Entry(add_product_page, font=("Segoe UI Light", 12), width=40)
    name.place(x=140, y=40, anchor="nw")

    price = ttk.Entry(add_product_page, font=("Segoe UI Light", 12), width=40)
    price.place(x=140, y=70, anchor="nw")

    quantity = ttk.Entry(add_product_page, font=("Segoe UI Light", 12), width=40)
    quantity.place(x=140, y=100, anchor="nw")

    ds = Text(add_product_page, font=("Segoe UI Light", 12), width=40, height=10, wrap='word', relief='flat')
    ds.place(x=140, y=140, anchor="nw")


    def add_new_product():
        if messagebox.askyesno("Product Update", "Do you want to add the product? Check for mistakes"):
            p_name = name.get()
            p_price = price.get()
            p_quantity = quantity.get()
            p_ds = ds.get("1.0", "end-1c")

            con = sqlite3.connect("store.db")
            cursor = con.cursor()
            cursor.execute(
                """INSERT INTO products (product_name, product_price, quantity, product_description) VALUES (?,?,?,?) """,
                (p_name, p_price, p_quantity, p_ds))
            product_id=cursor.lastrowid
            import User
            cursor.execute("INSERT INTO manager_product (product_id,manager_id) VALUES (?,?)", (product_id,User.manager_id))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Product Updated")

    Button(add_product_page, text="Add", relief='raised', font=("Seoge UI Light", 13), command=add_new_product,
           takefocus=False).place(x=140, y=370, anchor="nw")
    return add_product_page

def product(frame):
    from ProductDisplay import display_product_info
    import PageSwitcher as ps
    product_page_frame=ttk.Frame(frame,width=1200,height=675-120)
    product_page_frame.place(x=0,y=0)
    canvas = Canvas(product_page_frame, bg="#ECECFA", width=1200, height=675 - 120, scrollregion=(0, 0, 1200, 1000))
    canvas.pack(expand=True, fill="both", padx=0, pady=0)

    scrollbar = ttk.Scrollbar(product_page_frame, orient='vertical', command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    canvas.configure(yscrollcommand=scrollbar.set)

    scroll_frame = ttk.Frame(canvas, width=1200, height=(675 - 120), padding=(0, 0, 0, 0), style="order.TFrame")
    canvas_window = canvas.create_window((0, 45), window=scroll_frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_frame.bind("<Configure>", on_configure)
    scroll_frame.bind("<Configure>", on_configure)
    lblstyle = ttk.Style()
    lblstyle.configure("TLabel", background="#ECECFA", font=("Seoge UI Light", 12))

    product_id = ttk.Label(product_page_frame, style="TLabel", text="Product id", font=("Arial", 12))
    product_id.place(x=0, y=0)

    name = ttk.Label(product_page_frame, style="TLabel", text="Name", font=("Arial", 12))
    name.place(x=240, y=0)

    price = ttk.Label(product_page_frame, style="TLabel", text="Price", font=("Arial", 12))
    price.place(x=480, y=0)

    amount = ttk.Label(product_page_frame, style="TLabel", text="Quantity", font=("Arial", 10))
    amount.place(x=700, y=0)

    Button(product_page_frame,text="Add product",font=("Seoge UI Light", 10),takefocus=False,relief='raised',background="#ECECFA",command=lambda:ps.manager_page_switcher("AddProduct")).place(x=920,y=0)





    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    datas= cursor.fetchall()
    conn.close()
    for data in datas:

        style = ttk.Style()
        style.configure("TFrame", background="#ECECFA")
        product_frame = ttk.Frame(scroll_frame, width=1200, height=50,style="TFrame")

        bstyle=ttk.Style()
        bstyle.configure("TButton", background="#ECECFA",font=("Segoe UI Light",12),borderwidth=0)
        bstyle.map("TButton", background=[("active", "#ECECFA"),["pressed", "#ECECFA"]])

        ttk.Label(product_frame, text=data[0], font=("Segoe UI Light",12), background="#ECECFA").place(x=0, y=0, anchor="nw")
        ttk.Button(product_frame,style="TButton", text=data[1],takefocus=False,command=lambda p_id=data[0]:display_product_info(p_id,'Product',"manager")).place(x=240, y=0, anchor="nw")
        ttk.Label(product_frame, text=data[3], font=("Segoe UI Light",12), background="#ECECFA").place(x=480, y=0, anchor="nw")
        ttk.Label(product_frame, text=data[4],font=("Segoe UI Light",12), background="#ECECFA").place(x=700, y=0, anchor="nw")

        product_frame.grid(padx=5,pady=5)



    return product_page_frame






