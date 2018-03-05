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
    def hide(self):
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x + self.r,self.y + self.r,fill = BG_COLOR, outline = BG_COLOR)
    def move(self):
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy   
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()
    def changeMove(self):
         if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
         if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy  
         self.hide()
         self.x += self.dx*5
         self.draw()



#mouse event
def mouse_click(event):
    global ball
    if event.num == 1:
        ball = Balls(event.x,event.y,R,BL_COLOR,2,2)
        ball.draw()
    elif event.num == 3:
        ball.changeMove()

def main():
    if "ball" in globals():
        ball.move()
    root.after(10,main)


root = Tkinter.Tk()
root.title("Balls")
canvas = Tkinter.Canvas(root, width=300, height=300, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
if "ball" in globals():
    del ball
main()
root.mainloop()