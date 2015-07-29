'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''
import Tkinter as tk
from Controller import Master
import gc

gc.enable()

root = tk.Tk()
root.attributes("-fullscreen", True)

Master.MasterController(root)

root.mainloop()