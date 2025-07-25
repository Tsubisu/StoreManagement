def top_page_switcher(name):
   import Pages
   Pages.top_pages[name].tkraise()

def bottom_page_switcher(name):
   import Pages
   Pages.bottom_pages[name].tkraise()
   
def manager_page_switcher(name):
   import Pages
   Pages.manager_pages[name].tkraise()