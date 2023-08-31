from tkinter import *
from add import AddPage
from analytics import AnalyticsPage
from home import HomePage

class Controller(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry("1200x800")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.home_page = HomePage(container, self)
        self.home_page.grid(row=0, column=0, sticky="nsew")

        self.analytics_pages = {}
        self.add_pages = {}
        for workout in ["Push", "Pull", "Legs"]:
            self.analytics_pages[workout] = AnalyticsPage(container, self, workout)
            self.analytics_pages[workout].grid(row=0, column=0, sticky="nsew")
            self.add_pages[workout] = AddPage(container, self, workout)
            self.add_pages[workout].grid(row=0, column=0, sticky="nsew")

        self.load_home_page()

    def load_home_page(self):
        self.home_page.tkraise()

    def load_add_page(self, workout):
        self.add_pages[workout].tkraise()
    
    def load_analytics_page(self, workout):
        self.analytics_pages[workout].tkraise()

if __name__ == "__main__":
    c = Controller()
    c.mainloop()
