import Pages
def  vertical_animation(Switching_frame,start_x,start_y,end_y,step=2,Switched_frame=None):
    def animate(y):
        if y <=end_y:
            Switching_frame.place(x=start_x, y=y)
            Switching_frame.after(6, lambda: animate(y +step))


    def deanimate(y):
        if y >=end_y:
            Switching_frame.place(x=start_x, y=y)
            Switching_frame.after(6, lambda: deanimate(y+step))
        else:
            Switched_frame.tkraise()
    if Switched_frame is None:
        Switching_frame.tkraise()
        animate(start_y)
    else:
        deanimate(start_y)

def horizontal_animation(frame,start_x,end_x,start_y,step=2):

   def animate(x):
       if x <=end_x:
           frame.place(x=x, y=start_y)
           frame.after(6, lambda: animate(x + step))
   frame.tkraise()
   animate(start_x)

