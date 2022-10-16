from tkinter import *


def bindrb(root, element):
    def callback1(event=None):
        element.event_generate('<<Cut>>')

    def callback2(event=None):
        element.event_generate('<<Copy>>')

    def callback3(event=None):
        element.event_generate('<<Paste>>')

    menu = Menu(root, tearoff=False)
    menu.add_command(label="剪切", command=callback1)
    menu.add_command(label="复制", command=callback2)
    menu.add_command(label="粘贴", command=callback3)

    def popup(event):
        menu.post(event.x_root, event.y_root)

    element.bind("<Button-3>", popup)
