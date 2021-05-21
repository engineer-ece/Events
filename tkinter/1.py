from tkinter import * 
from PIL import *

def image(filename):
    return PhotoImage(filename)


#<Motion> binding 
def xy(event):
    print("{},{}".format(event.x,event.y))

def motion(root,e):
    root.bind('<Motion>',e)

def b1_drag(root,e):
    root.bind('<B1-Motion>',e)

def char(event):
    print("event.char=='a'")

def key(root,e):
    root.bind('<Control-Alt-a>',e)

top = Tk() 
top.title("Gobal Krishnan V")
width, height = top.winfo_screenwidth(), top.winfo_screenheight() 
top.geometry("{}x{}".format(int(width/2),int(height/2)))
top.iconphoto(False,image("heart.png"))

#top.iconbitmap(r'heart.ico')
b1_drag(top,xy)
key(top,char)
top.mainloop()


