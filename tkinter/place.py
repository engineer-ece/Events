from tkinter import * 

# anchor 
# bordermode 
# height, width 
# relheight, relwidth 
# relx,rely 
# x ,y

root = Tk()
root.title("place")
root.geometry("210x80")
a = StringVar()

sb = Scrollbar(root,orient=HORIZONTAL,)
sb.pack(fill=X,expand=True)


l = Entry(root,textvariable=a,font=(20),xscrollcommand=sb.set)
l.place(x=0,y=0,bordermode=INSIDE)
sb.config(command=l.xview)
def cal():
    ev = eval(a.get())
    a.set(ev)
    print(ev)

b = Button(root,text="calculate",width=20,command=cal)
b.place(x=0,y=50)

print((root.place_slaves()))
root.mainloop()