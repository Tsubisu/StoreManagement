from tkinter import ttk
import sqlite3
def view_orders(frame):
    view_style=ttk.Style()
    view_style.configure("view.TFrame", background="#CCCCF3")
    view_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="view.TFrame")
    return view_page_frame