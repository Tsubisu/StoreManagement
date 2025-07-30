
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox


Mg_BtmFrame = None
def show_manager():
    import Pages, PageSwitcher,app
    global top,Mg_BtmFrame
    top=Toplevel(app.root)
    top.geometry("1200x675")
    top.title("Manager")
    top.resizable(False,False)
    manager_frame = ttk.Frame(top, width=1200, height=675)
    manager_frame.place(x=0,y=0)
   
    Topframe_style=ttk.Style()
    Topframe_style.configure("tf.TFrame",background="#5D5C9A")
    Topframe = ttk.Frame(manager_frame, height=120, width=1200,style="tf.TFrame")
    Topframe.place(x=0,y=0)

    BtmFrame = ttk.Frame(manager_frame, height=(675 - 120), width=1200)
    BtmFrame.place(x=0, y=120)
    Mg_BtmFrame = BtmFrame

    
    
    
    pages=Pages.manager_page_init(BtmFrame)
  
    for page in pages.values():
        page.place(x=0,y=0) 
    PageSwitcher.manager_page_switcher("Check_Comments")
    
    buttons=ttk.Style()
    buttons.configure("button.TButton",background="#5D5C9A",font=("Segoe UI Light",11,'bold'),borderwidth=0)
    buttons.map("button.TButton", background=[("active","#5D5C9A")],foreground=[("pressed","#333333")])


    def manage_page():
        update_featured_products=Toplevel(app.root)
        update_featured_products.geometry("280x100")
        Label(update_featured_products, text="Enter 4 integers (comma or space separated):").pack(pady=10)

        entry = Entry(update_featured_products, width=40)
        entry.pack()

        def get_numbers():
            text = entry.get()
            try:
                # Allow comma or space separators
                parts = text.replace(',', ' ').split()
                if len(parts) != 4:
                    raise ValueError("You must enter exactly 4 integers.")

                numbers = [int(x) for x in parts]
                messagebox.showinfo("Success", f"You entered: {numbers}")
                filename = "numbers.txt"  # You can replace these with any 4 integers

                with open(filename, "w") as f:
                    for num in numbers:
                        f.write(f"{num}\n")
                print(f"{filename} has been overwritten with: {numbers}")

            except ValueError as e:
                messagebox.showerror("Error", str(e))

        Button(update_featured_products, text="Submit", command=get_numbers).pack(pady=10)

        mainloop()
    MLabel = ttk.Label(Topframe, text="Guitar Store", font=("Brush Script MT", 35), background="#5D5C9A")
    MLabel.place(x=600, y=45, anchor="center")

    manage_homepage_btn = ttk.Button(Topframe, text="Manage Homepage",style="button.TButton",takefocus=False,command=manage_page)
    manage_homepage_btn.place(x=20, y=120,anchor="sw")

    product_btn=ttk.Button(Topframe,text="Product",style="button.TButton",takefocus=False,command=lambda: PageSwitcher.manager_page_switcher("Product"))
    product_btn.place(x=170,y=120,anchor="sw")
    
    check_comments_btn= ttk.Button(Topframe,text="Check Comments",style="button.TButton",takefocus=False,command=lambda: PageSwitcher.manager_page_switcher("Check_Comments"))
    check_comments_btn.place(x=280,y=120,anchor="sw")
    
    view_orders_btn=ttk.Button(Topframe,text="View Orders",style="button.TButton",takefocus=False,command=lambda:PageSwitcher.manager_page_switcher("View_Orders"))
    view_orders_btn.place(x=430,y=120,anchor="sw")
    
    add_manager_btn=ttk.Button(Topframe,text="Add Manager",style="button.TButton",takefocus=False, command=lambda: PageSwitcher.manager_page_switcher("Add_Manager"))
    add_manager_btn.place(x=550,y=120,anchor="sw")
    
    update_manager_btn=ttk.Button(Topframe,text="Update Manager Profile",style="button.TButton",takefocus=False, command=lambda: PageSwitcher.manager_page_switcher("Update_Profile"))
    update_manager_btn.place(x=670,y=120,anchor="sw")
    
    return manager_frame

