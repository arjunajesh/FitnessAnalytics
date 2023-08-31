from tkinter import *

class HomePage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.build_frame()

        
    def build_frame(self):
        label = Label(self, text="Add Workout")
        label.pack()

        self.createHomeButtons(self.controller.load_add_page)

        label = Label(self, text="Analytics")
        label.pack()

        self.createHomeButtons(self.controller.load_analytics_page)

    def createHomeButtons(self, load_page):
        buttonFrame = Frame(self) #? button creation with for loop
        button = Button(buttonFrame, text="Push", command=lambda:load_page("Push"))
        button.pack(side='left')
        button = Button(buttonFrame, text="Pull", command=lambda:load_page("Pull"))
        button.pack(side='left')
        button = Button(buttonFrame, text="Legs", command=lambda:load_page("Legs"))
        button.pack(side='left')
        buttonFrame.pack()