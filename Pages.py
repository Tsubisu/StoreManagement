import HomePage
import SearchPage
import ContactPage
import OrderPage
import ManageHomepage
import CheckComments
import ViewOrders
import AddManager

top_pages={}
bottom_pages={}

manager_pages={}
def top_page_init(frame):
    global top_pages
    top_pages={"Home_bar":HomePage.home_bar_builder(frame),"Search":SearchPage.search_bar(frame)}
    return top_pages


def bottom_page_init(frame):
    global bottom_pages
    bottom_pages={"Default":HomePage.home_page(frame),"Contact":ContactPage.contact_page(frame),"Search":SearchPage.search_page(frame),"Order":OrderPage.order_page(frame)}
    return bottom_pages

def manager_page_init(frame):
    global manager_pages
    manager_pages={"Default":ManageHomepage.manage_homepage(frame),"Check_Comments":CheckComments.check_comments(frame),"View_Orders":ViewOrders.view_orders(frame),"Add_Manager":AddManager.add_manager(frame)}
    return manager_pages
