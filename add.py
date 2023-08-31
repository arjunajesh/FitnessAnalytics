from tkinter import *

class AddPage(Frame):
    def __init__(self, parent, controller, workout):
        super().__init__(parent)
        self.controller = controller
        self.workout = workout
        self.build_frame()
        
    def build_frame(self):
        label = Label(self, text=f"This is the add {self.workout} workout page")
        label.pack()

        backbutton = Button(self, text="Back to Home Page", command=lambda: self.controller.load_home_page())
        backbutton.pack()
        