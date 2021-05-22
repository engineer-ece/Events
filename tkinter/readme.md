
# Tkinter

1. [FullScreen](https://github.com/engineer-ece/Python/blob/main/tkinter/fullscreen.md)
2. [Title Icon Image & Simple Event Bind](https://github.com/engineer-ece/Python/blob/main/tkinter/1.py)

## Layout 
  
   ### 1. Pack(side,fill,expand)      
   [code](https://github.com/engineer-ece/Python/blob/main/tkinter/pack.py)
        
    
       side = TOP,LEFT,BOTTOM,RIGHT
       fill = X,Y,BOTH,NONE 
       expand = True,False
   
   ### 2. Grid(row,column,rowspan,columnspan,padx,pady,ipadx,ipady,sticky)
   [code](https://github.com/engineer-ece/Python/blob/main/tkinter/grid.py)
   
       row        = no.of rows 
       column     = no.of column
       rowspan    = no.of row join
       columnspan = no.of column join 
       padx       = border X size between the cell 
       pady       = border Y size between the cell 
       ipadx      = X side of cell changes 
       ipady      = Y side of cell changes
       sticky     = Position like, N,E,S,W,NE,NW,SE,SW 
       
       x = event.x_root - root.winfo_rootx()
       y = event.y_root - root.winfo_rooty()
       z = root.grid_location(x,y) 
       print(root.grid_slaves(z[1],z[0])[0]['text']) # to get the widget from grid
   
   ### 3. Place(x,y,width,height,bordermode,relx,rely,relwidth,relheight,anchor)
   [code](https://github.com/engineer-ece/Python/blob/main/tkinter/place.py)
      
       x          = widget x position to screen
       y          = widget y position to screen
       width      = widget width
       height     = widget height
       relx       = relx [0.0 - 1.0] offset for widget x position
       rely       = rely [0.0 - 1.0] offset for widget y position
       relwidth   = relwidth [0.0 - 1.0] offset for widget width position
       relheight  = relheight [0.0 - 1.0] offset for widget height position
       anchor     = N,E,S,W,NE,NW,SE,SW
       bordermode = INSIDE,OUTSIDE
       


