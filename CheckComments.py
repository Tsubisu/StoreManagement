from tkinter import ttk
from tkinter import *
import sqlite3


def check_comments(frame):
    check_style=ttk.Style()
    check_style.configure("check.TFrame", background="white")
    check_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="check.TFrame")

    canvas = Canvas(check_page_frame, bg="#ECECFA", width=1200, height=675 - 120, scrollregion=(0, 0, 1200, 10000))
    canvas.pack(expand=True, fill="both", padx=0, pady=0)

    scrollbar = ttk.Scrollbar(check_page_frame, orient='vertical', command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    canvas.configure(yscrollcommand=scrollbar.set)
    # canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 120), "units"))

    scroll_frame = ttk.Frame(canvas, width=1200, height=(675 - 120), padding=(0, 0, 0, 0), style="order.TFrame")
    canvas_window = canvas.create_window((0, 30), window=scroll_frame, anchor="nw")
   

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
     
    scroll_frame.bind("<Configure>", on_configure)
    lblstyle = ttk.Style()
    lblstyle.configure("TLabel",  background="#ECECFA", font=("Seoge UI Light", 12))
    
    comment_id = ttk.Label(check_page_frame,style="TLabel",text="Comment id",font=("Arial", 12))
    comment_id.place(x=0, y=0)
    
    name = ttk.Label(check_page_frame,style="TLabel",text="Name",font=("Arial", 12))
    name.place(x=240, y=0)

    
    email = ttk.Label(check_page_frame,style="TLabel",text="Email",font=("Arial", 12))
    email.place(x=480, y=0)

    
    contact= ttk.Label(check_page_frame,style="TLabel",text="Contact",font=("Arial", 12)) 
    contact.place(x=700, y=0)
    
    comment = ttk.Label(check_page_frame,style="TLabel",text="Comment",font=("Arial", 10))
    comment.place(x=960, y=0)
    
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comments")
    datas=cursor.fetchall()
    conn.close()

    for data in datas:
        style=ttk.Style()
        style.configure("TFrame", background="#ECECFA")
        comment_frame = ttk.Frame(scroll_frame, width=1200, height=40,style="TFrame")
        ttk.Label(comment_frame, text=data[4], font=("Arial", 12), background="#ECECFA").place(x=0,y=10,anchor="nw")
        ttk.Label(comment_frame, text=data[0], font=("Arial", 12), background="#ECECFA").place(x=240,y=10,anchor="nw")
        ttk.Label(comment_frame, text=data[1], font=("Arial", 12), background="#ECECFA").place(x=480,y=10,anchor="nw")
        ttk.Label(comment_frame, text=data[2], font=("Arial", 12), background="#ECECFA").place(x=700,y=10,anchor="nw")
    
        estyle = ttk.Style()
        estyle.configure("E.TEntry", font=("Arial", 12),fieldbackground="#ECECFA", foreground="black", borderwidth=0,relief='flat')
        entry=ttk.Entry(scroll_frame,width=30,font=("Arial", 12),style="E.TEntry")
        entry.insert(0,data[3])
        entry.config(state='readonly')
        entry.place(x=900,y=10,anchor="nw")
        comment_frame.grid(padx=5, pady=2)
       
        
    return check_page_frame