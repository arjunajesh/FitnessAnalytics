from tkinter import *
from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Misc
from typing import Any
from typing_extensions import Literal

window = Tk()
window.geometry("1200x800")
window.title("Fitness Analytics - Home Page")


def createHomeButtons(window):
    buttonFrame = Frame(window)
    button = Button(buttonFrame, text="Push")
    button.pack(side='left')
    button = Button(buttonFrame, text="Pull")
    button.pack(side='left')
    button = Button(buttonFrame, text="Legs")
    button.pack(side='left')
    buttonFrame.pack()

label = Label(window, text="Add Workout")
label.pack()

createHomeButtons(window)


label = Label(window, text="Analytics")
label.pack()

createHomeButtons(window)

window.mainloop()
