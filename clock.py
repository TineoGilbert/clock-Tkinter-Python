from tkinter import *
from time import *


def updateTime():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)


    window.after(1000, updateTime)

window = Tk()

time_label = Label(window, font=("Arial", 35), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Gotham", 25))
day_label.pack()

updateTime()
window.mainloop()