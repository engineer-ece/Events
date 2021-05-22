from tkinter import *

#column
#row
#columnspan
#rowspan
#padx,pady
#ipadx,ipady
#sticky = N,E,S,W,NE,NW,SE,SW 

# grid_forget()
# grid_remove()
# l3.after(3000, lambda: l3.grid_remove() )

root = Tk() 
root.title("grid")
count = 1
def out(event):
   #print(a)
   x = event.x_root - root.winfo_rootx()
   y = event.y_root - root.winfo_rooty()
   z = root.grid_location(x,y) 
   print(root.grid_slaves(z[1],z[0])[0]['text'])
   
   

for i in range(3):
   for j in range(5):
       b = Button(root,text="Button {}".format(count), width = 40,)
       b.bind("<Button>",out)

       b.grid(sticky=NW,row=i,column=j,pady=5,padx=5,ipady=10,ipadx=10)
       count += 1

print(root.grid_size())

root.mainloop() 