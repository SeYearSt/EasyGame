import Tkinter
#constants 
WIDTH = 300
HEIGHT = 300
BG_COLOR = "white"


#mouse event
def mouse_click(event):
    print(event.num,event.x,event.y)


root = Tkinter.Tk()
root.title("Balls")
canvas = Tkinter.Canvas(root, width=300, height=300, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
root.mainloop()