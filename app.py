from tkinter import ttk as ttk
from tkinter import *
import sqlite3


def database_init():
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS user (
                  full_name VARCHAR(40),
                  contact CHAR(10),
                  email VARCHAR(30),
                  address VARCHAR(30),
                  user_id INTEGER PRIMARY KEY AUTOINCREMENT)
                   """)
    c.execute("""CREATE TABLE IF NOT EXISTS managers(
                full_name VARCHAR(40),
                contact CHAR(10),
                email VARCHAR(30),
                address VARCHAR(30),
                manager_id INTEGER PRIMARY KEY AUTOINCREMENT)
                 """)

    c.execute("""CREATE TABLE IF NOT EXISTS products(
                    product_id varchar(100),
                    product_description TEXT,
                    product_price INTEGER check(product_price>=0),
                    quantity INTEGER check(quantity>=0))""")

    c.execute("""CREATE TABLE IF NOT EXISTS comments(
                name VARCHAR(40),
                email VARCHAR(30),
                contact VARCHAR(10),
                comment TEXT, 
                comment_id INTEGER PRIMARY KEY AUTOINCREMENT)
                """)


    conn.commit()
    conn.close()

root=None

def app_initializer():
    global root
    root = Tk()
    root.geometry('1200x675')
    root.title('Music Store')
    root.resizable(False, False)

    '''
        Our window is created with a main frame called ParentFrame that occupies whole window space.This parent frame contains (3) child frames
        that is accessed via .tkraise() function accessed via the page switch buttons.

        The default home_bar contains all our home widgets including the page switch buttons.This default frame is then
        divided into two frames Top and Bottom  
        Top frame is approx 1/4 th height of the total window and width spans the total width of the window
            Here our decorative widgets/ login, search,shopping cart buttons are placed along with logo

        The bottom frame covers rest of the windows and houses the widgets to display the product
        The bottom frame contains sub frame widget that is raised to the top depending upon the button pressed
         Example. When product button is pressed the frame containing the selected product type along with
         the sort buttons are shown 
    '''

    # Creating the parent frame

    ParentFrame = ttk.Frame(root, height=675, width=1200)
    ParentFrame.grid(row=0, column=0)
    ParentFrame.grid_propagate(False)


    # for the top frame widgets

    WindowStyle = ttk.Style()
    WindowStyle.theme_use("clam")
    WindowStyle.configure("My.TFrame", background="#25beb3")
    WindowStyle.configure("My.TButton", background="white",padding=(0,10,15,5))

    Topfrm = ttk.Frame(ParentFrame, height=120, width=1200)
    Topfrm.place(x=0,y=0)

    # =====Bottom Frame with its sub Frames=====
    BtmFrame = ttk.Frame(ParentFrame, height=(675 - 120), width=1200)
    BtmFrame.place(x=0, y=120)

    #======Loads all the pages/frames for the top fram and place them


    import Pages

    top_page=Pages.top_page_init(Topfrm)
    bottom_page = Pages.bottom_page_init(BtmFrame)


    for page in top_page.values():
            page.place(x=0,y=0)


    for page in bottom_page.values():
        page.place(x=0, y=0)

    import PageSwitcher

    PageSwitcher.top_page_switcher("Home_bar")
    PageSwitcher.bottom_page_switcher("Default")


    root.mainloop()











