from tkinter import ttk as ttk

def contact_page(frame):
    contact_style=ttk.Style()
    contact_style.configure("contact.TFrame", background="red")
    contact_page_frame= ttk.Frame(frame,width=1200,height=(675-120),style="contact.TFrame")
    contact_page_frame.pack_propagate(False)
    
     
    name_label = ttk.Label(contact_page_frame, text="Name:", background="red", foreground="white", font=("Arial", 12))
    name_label.place(x=30, y=50)
    name_entry = ttk.Entry(contact_page_frame, width=50)
    name_entry.place(x=80, y=50)

    
    email_label = ttk.Label(contact_page_frame, text="Email:", background="red", foreground="white", font=("Arial", 12))
    email_label.place(x=30, y=90)
    email_entry = ttk.Entry(contact_page_frame, width=50)
    email_entry.place(x=80, y=90)

    
    phone_label = ttk.Label(contact_page_frame, text="Phone:", background="red", foreground="white", font=("Arial", 12))
    phone_label.place(x=30, y=130)
    phone_entry = ttk.Entry(contact_page_frame, width=50)
    phone_entry.place(x=80, y=130)

    comment_label = ttk.Label(contact_page_frame, text="Comment:", background="red", foreground="white", font=("Arial", 12))
    comment_label.place(x=30, y=180)
    comment_text = ttk.Entry(contact_page_frame, font=("Arial", 12))
    comment_text.place(x=120, y=180, width=250, height=100)
    

    send_btn = ttk.Button(contact_page_frame, text="Send")
    send_btn.place(x=30, y=320)
    return contact_page_frame
 
    
    