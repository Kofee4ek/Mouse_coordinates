import pyautogui as p
from tkinter import *


def button_clicked():
    quit()


def xy():
    label.after(200, xy)
    label['text'] = p.position()


root = Tk()
root.title("Координаты мышки")
root.minsize(300, 50)
root.resizable(width=False, height=False)
label = Label(root)
label.configure(text=p.position())
label.pack()
label.after_idle(xy)
button = Button(root)
button.configure(text='Выход', command=button_clicked)
button.pack()

root.mainloop()
