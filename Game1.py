import Tkinter
#constants 
WIDTH = 300
HEIGHT = 300
BG_COLOR = "white"
BL_COLOR = "blue"
R = 30
#class Ball
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
        self.dx=dx
        self.dy=dy
    def draw(self):
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x + self.r,self.y + self.r,fill = self.color)



#mouse event
def mouse_click(event):
    ball = Balls(event.x,event.y,R,BL_COLOR)
    ball.draw()


root = Tkinter.Tk()
root.title("Balls")
canvas = Tkinter.Canvas(root, width=300, height=300, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
root.mainloop()