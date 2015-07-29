'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
'''

from types import NoneType

def CloseWindow(event, root):
    if (type(root.master) == NoneType):
        root.destroy()    
    else:
        CloseWindow(event, root.master)

def RemoveAllChildren(frame):
    for child in frame.winfo_children():
        try:
            child.destroy()
        except:
            pass