```python
import tkinter as tk
root = tk.Tk()
root.attributes('-type', 'dock')
root.attributes("-fullscreen", True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

size = str(width)+"x"+str(height)
root.geometry(size)
root.focus_force()
root.mainloop()


```
