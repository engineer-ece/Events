from tkinter import * 


class Drag:

    def add(self,widget):
      
      widget.bind("<ButtonPress-1>",self.on_start)
      widget.bind("<B1-Motion>",self.on_drag)
      widget.configure(cursor="hand2")
      self.w_ = widget 
      pass

    def on_start(self,event):
      self.x = event.x 
      self.y = event.y 
      pass 

    def on_drag(self,event):
      dx = event.x - self.x 
      dy = event.y - self.y
      x = self.w_.winfo_x() + dx
      y = self.w_.winfo_y() + dy
      self.w_.place(x=x,y=y)
      pass    

root = Tk()
root.title("drag")
root.geometry("500x500")

b1 = Button(root,text="Drag")
b1.place(x=0,y=0)
d = Drag()
d.add(b1)


root.mainloop() 