import Tkinter
import random

#constants 
WIDTH = 1200    
HEIGHT = 600
BG_COLOR = "white"
BL_COLOR = "blue"
BAD_COLOR = "red"
COLORS = ["pink", "yellow", "gold", BAD_COLOR]
R = 20
INIT_DX = 4 
INIT_DY = 4
DELAY = 5
BALLS_INIT_NUMBER = 20
 


#class Ball
class Balls():
    def __init__(self, x, y, r, color, dx=INIT_DX, dy=INIT_DY):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
        self.dx=dx
        self.dy=dy


    def draw(self):
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x + self.r,self.y + self.r,fill = self.color, outline = BG_COLOR)


    def hide(self):
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x + self.r,self.y + self.r,fill = BG_COLOR, outline = BG_COLOR)


    def is_collision(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b)**0.5 <= self.r + ball.r


    def move(self):
        #colliding with walls   
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy  
        #colliding with balls
        for ball in balls:
            if self.is_collision(ball):
               if ball.color != BAD_COLOR: #good ball
                    ball.hide()
                    balls.remove(ball)
                    self.dx = - self.dx
                    self.dy = - self.dy
               else: 
                    ball.hide()
                    del ball
                    canvas.delete("all")
                    canvas.create_text(WIDTH / 2, HEIGHT / 2, text = "You LOSE", font = "Arial" , fill = BAD_COLOR )
                    self.dx = self.dy = 0

        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


def count_bad_balls(balls):
    res = 0
    for ball in balls:
        if ball.color == BAD_COLOR:
            res += 1
    return res

#mouse event
def mouse_click(event):
    global ball
    if event.num == 1:
        if "ball" not in globals():
            ball = Balls(event.x,event.y,R,BL_COLOR)
            ball.draw()
        else: # turn left
            if ball.dx * ball.dy > 0:
                ball.dy = -ball.dy
            else:
                ball.dx = - ball.dx
    elif event.num == 3: # turn right
        if ball.dx * ball.dy > 0: 
            ball.dx = - ball.dx
        else:
            ball.dy = - ball.dy

        ball.hide()

def main():
    if "ball" in globals():
        ball.move()
        # check WIN condition
        if (len(balls) - number_of_bad_balls == 0 ):
            canvas.delete("all")
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text = "You WIN", font = "Arial" , fill = BL_COLOR )
            ball.hide()
    root.after(DELAY,main)


#create list of balls
def create_list_of_balls(number):
    list = []
    while len(list) < number:
        next_ball = Balls(random.choice(range(0,WIDTH)),
                         random.choice(range(0,HEIGHT)),
                         random.choice(range(15,R)),
                         random.choice(COLORS))
        list.append(next_ball)
        next_ball.draw()
    return list

root = Tkinter.Tk()
root.title("Balls")
canvas = Tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
if "ball" in globals():
    del ball
balls = create_list_of_balls(BALLS_INIT_NUMBER)
number_of_bad_balls = count_bad_balls(balls)
main()
root.mainloop()