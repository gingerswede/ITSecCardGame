'''
Created on 23 jul 2015

@author: Emil
'''

from types import NoneType

def CloseWindow(event, root):
    if (type(root.master) == NoneType):
        root.destroy()    
    else:
        CloseWindow(event, root.master)

def RemoveAllChildren(frame):
    for child in frame.winfo_children():
        child.destroy()