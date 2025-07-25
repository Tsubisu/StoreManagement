from tkinter import ttk
import sqlite3


def check_comments(frame):
    check_style=ttk.Style()
    check_style.configure("check.TFrame", background="white")
    check_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="check.TFrame")
    return check_page_frame


    
    