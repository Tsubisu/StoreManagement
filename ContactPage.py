from tkinter import ttk as ttk

def contact_page(frame):
    contact_style=ttk.Style()
    contact_style.configure("contact.TFrame", background="red")
    contact_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="contact.TFrame")
    return contact_page_frame
