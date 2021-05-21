from tkinter import * 
from PIL import Image, ImageTk

def image_(filename):
    return 


def a1():
    print("Head")

def a2():
    print("Left")
def a3():
    print("Right")
def a4():
    print("Bottom")


root = Tk()

head = Frame(root)
head.pack(side=TOP,fill=BOTH,expand=True)  
left = Frame(root)
left.pack(side=LEFT,fill=BOTH,expand=True)  
right = Frame(root)
right.pack(side=RIGHT,fill=BOTH,expand=True)  

foot = Frame(root)
foot.pack(side=BOTTOM,fill=BOTH,expand=True)  

#==========================================================
img = ImageTk.PhotoImage(Image.open(r"heart.png"))

b1= Button(head,bg="orange",text="Head",relief=GROOVE,compound="top",image=img,font=("Unicode", 50, "bold"),command=a1)
b1.pack(side=TOP,fill=BOTH,expand=True)
b2= Button(left,text="Left",bg="green",command=a2)
b2.pack(side=TOP,fill=BOTH,expand=True)
b3= Button(right,text="Right",bg="red",command=a3)
b3.pack(side=TOP,fill=BOTH,expand=True)
b4= Button(foot,text="Bottom",bg="blue",command=a4)
b4.pack(side=TOP,fill=BOTH,expand=True)





root.mainloop()

# from tkinter import * 
# from PIL import Image, ImageTk

# def image_(filename):
#     return 


# def a1():
#     print("Head")

# def a2():
#     print("Left")
# def a3():
#     print("Right")
# def a4():
#     print("Bottom")


# root = Tk()

# head = Frame(root)
# head.pack(side=TOP,fill=BOTH,expand=True)  
# left = Frame(root)
# left.pack(side=LEFT,fill=BOTH,expand=True)  
# right = Frame(root)
# right.pack(side=RIGHT,fill=BOTH,expand=True)  

# foot = Frame(root)
# foot.pack(side=BOTTOM,fill=BOTH,expand=True)  

# #==========================================================
# img = ImageTk.PhotoImage(Image.open(r"heart.png"))

# b1= Button(head,bg="orange",text="Head",activebackground="green",width=300,wraplength=True,pady=20,bd=20,activeforeground="white",relief=GROOVE,compound="top",image=img,font=("Unicode", 50, "bold"),command=a1)
# b1.pack(side=TOP,fill=BOTH,expand=True)
# b2= Button(left,text="Left",bg="green",command=a2)
# b2.pack(side=TOP,fill=BOTH,expand=True)
# b3= Button(right,text="Right",bg="red",command=a3)
# b3.pack(side=TOP,fill=BOTH,expand=True)
# b4= Button(foot,text="Bottom",bg="blue",command=a4)
# b4.pack(side=TOP,fill=BOTH,expand=True)



# root.mainloop()







