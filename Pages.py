import HomePage
import SearchPage
import ContactPage
import CartPage

top_pages={}
bottom_pages={}
def top_page_init(frame):
    global top_pages
    top_pages={"Home_bar":HomePage.home_bar_builder(frame),"Search":SearchPage.search_bar(frame)}
    return top_pages


def bottom_page_init(frame):
    global bottom_pages
    bottom_pages={"Default":HomePage.home_page(frame),"Contact":ContactPage.contact_page(frame),"Search":SearchPage.search_page(frame),"Cart":CartPage.cart_page(frame)}
    return bottom_pages


