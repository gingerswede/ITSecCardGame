'''
Created on 22 jul 2015

@author: Emil
'''
import Tkinter as tk
from Controller import Master


root = tk.Tk()
root.attributes("-fullscreen", True)

Master.MasterController(root)

root.mainloop()