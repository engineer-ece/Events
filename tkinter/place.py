from tkinter import * 

# anchor 
# bordermode 
# height, width 
# relheight, relwidth 
# relx,rely 
# x ,y

root = Tk()
root.title("place")
root.geometry("200x60")
a = StringVar()

l = Entry(root,textvariable=a,font=(20))
l.place(x=0,y=0)

def cal():
    ev = eval(a.get())
    a.set(ev)
    print(ev)

b = Button(root,text="calculate",width=20,command=cal)
b.place(x=0,y=30)

print((root.place_slaves()))
root.mainloop()