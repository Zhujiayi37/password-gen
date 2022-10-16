from tkinter import *
import ctypes
from tkinter.ttk import *
root = Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
root.title("密码生成器")
