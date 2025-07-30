from tkinter import ttk
from tkinter import *
import sqlite3
def manage_homepage(frame):
    manage_style=ttk.Style()
    manage_style.configure("manage.TFrame", background="#5D5C9A")
    manage_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="manage.TFrame")



    return manage_page_frame
    
    