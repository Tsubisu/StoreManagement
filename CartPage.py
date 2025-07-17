from tkinter import ttk as ttk

def cart_page(frame):
    cart_style=ttk.Style()
    cart_style.configure("cart.TFrame", background="brown")
    cart_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="cart.TFrame")
    return cart_page_frame
