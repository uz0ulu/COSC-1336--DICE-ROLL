import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lavender")
wn.title("Dice Game")
a = turtle.Turtle()
b = turtle.Turtle() #1
c = turtle.Turtle() #2
d = turtle.Turtle() #3
e = turtle.Turtle() #4
f = turtle.Turtle() #5
g = turtle.Turtle() #6

# hide turtles
for t in [b, c, d, e, f, g]:
    t.hideturtle()

a.pensize(2)        #dice formation
a.color("black")
for i in range(2):
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)


dots_pos = {
    1:[(50,50)],
    2:[(25,25), (75,75)],
    3:[(25,25), (50,50), (75,75)],
    4:[(25,25),(25,75),(75,75),(75,25)],
    5:[(25,25),(25,75),(50,50),(75,75),(75,25)],
    6:[(25,25),(25,50), (25,75),(75,75),(75,50), (75,25)],
}
def dots(t, positions):
    for i in positions:
        t.penup()
        t.goto(i)
        t.pendown()
        t.dot(10,'red')
#defining 
turtles = {
    1: b,
    2: c,
    3: d,
    4: e,
    5: f,
    6: g,
}



def roll_dice():
    for t in [b, c, d, e, f, g]:
        t.clear()
    result = random.randint(1,6)
    
    dots(turtles[result], dots_pos[result])

    wn.update()
 
def handle_roll(x,y):
    roll_dice()
    
        
wn.onclick(handle_roll)



turtle.done()