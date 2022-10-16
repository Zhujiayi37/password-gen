from tkinter import *
import ctypes
from tkinter.ttk import *
import hashlib
import pyperclip as pclip
import random
root = Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
root.title("密码生成器")
e = StringVar()
f = StringVar()
g = StringVar()
resss = ""


def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0, len(obj), sec)]


def func():
    global e
    global f
    global g
    global resss
    base = e.get()
    salt = f.get()
    obj = hashlib.sha1(salt.encode("utf-8"))
    obj.update(base.encode("utf-8"))
    res = obj.hexdigest()
    ress = cut(res, 8)

    for i in range(1, 8, 2):
        ress.insert(i, "-")
    sep = ""
    resss = sep.join(ress)
    g.set(resss)


def func2():
    pclip.copy(resss)


a = Frame(root)
b = Frame(root)
c = Frame(root)
d = Frame(root)
i1 = Entry(a, textvariable=e, width=25, font=("consolas", 15))
i2 = Entry(b, textvariable=f, width=25, font=("consolas", 15))
o1 = Entry(c, textvariable=g, width=25, font=("consolas", 15))
l1 = Label(a, text="base:", font=("consolas", 15)).grid(row=0, column=0)
l2 = Label(b, text="salt:", font=("consolas", 15)).grid(row=0, column=0)
l3 = Label(c, text="outp:", font=("consolas", 15)).grid(row=0, column=0)
b1 = Button(d, text="Generate", command=func).grid(
    row=3, column=1)
b2 = Button(d, text="Copy", command=func2).grid(
    row=3, column=2)
o1['state'] = 'readonly'
i1.grid(row=0, column=1, columnspan=2, padx=(10, 20))
i2.grid(row=0, column=1, columnspan=2, padx=(10, 20))
o1.grid(row=0, column=1, columnspan=2, padx=(10, 20))
a.grid(row=0, column=0, pady=(20, 10))
b.grid(row=1, column=0, pady=(10, 10))
c.grid(row=2, column=0, pady=(10, 10))
d.grid(row=3, column=0, pady=(10, 20))


bindrb(a, i1)
bindrb(b, i2)
root.mainloop()
