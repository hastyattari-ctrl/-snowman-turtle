import turtle
from turtle import Screen,Turtle 
w1=turtle.Screen() 
w1.setup(500,500)

t1=turtle.Turtle()
t2=turtle.Turtle() 
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()
t7=turtle.Turtle()
t8=turtle.Turtle()
t9=turtle.Turtle()



t1.speed(0)
t2.speed(0) 
t3.speed(0)
t4.speed(0)
t5.speed(0)
t6.speed(0)
t7.speed(0)
t8.speed(0)
t9.speed(0)





t1.circle(30)
t1.penup()
t1.goto(0,-100)
t1.pendown()
t1.hideturtle()
t1.circle(50)

t1.penup()
t1.goto(-20,-115)
t1.fillcolor("black")
t1.begin_fill()
t1.pendown()
t1.circle(10)
t1.end_fill()

t1.penup()
t1.goto(20,-115)
t1.fillcolor("black")
t1.begin_fill()
t1.pendown()
t1.circle(10)
t1.end_fill()

t1.penup()
t1.goto(-58,-55)
t1.fillcolor("black")
t1.begin_fill()
t1.pendown()
t1.circle(10)
t1.end_fill()

t1.penup()
t1.goto(58,-55)
t1.fillcolor("black")
t1.begin_fill()
t1.pendown()
t1.circle(10)
t1.end_fill()


t2.penup()
t2.shape("triangle")
t2.shapesize(stretch_wid=3, stretch_len=3)
t2.color("orange")
t2.left(80)
t2.goto(6,65)

t3.penup()
t3.goto(-16,39)
t3.hideturtle()
t3.dot(10,"black")

t4.penup()
t4.goto(12,39)
t4.hideturtle()
t4.dot(10,"black")

t8.penup()
t8.hideturtle()
t8.goto(-1,28)
t8.dot(5,"black")

t9.penup()
t9.goto(-13,20)
t9.hideturtle()
t9.pendown()
t9.right(90)

t9.circle(10,180)
t9.end_fill()





t5.penup()
t5.goto(0,-23)
t5.dot(10,"black")
t5.goto(0,-45)
t5.dot(10,"black")
t5.goto(0,-65)
t5.hideturtle()
t5.dot(10,"black")


t6.penup()
t6.shape("triangle")
t6.shapesize(stretch_wid=1, stretch_len=1)
t6.color("red")
t6.goto(-12,0)

t7.shape("triangle")
t7.shapesize(stretch_wid=1, stretch_len=1)
t7.color("red")
t7.left(180)
t7.goto(14,0)



import random


screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Snowfall with Turtle")
screen.tracer(0)  


snowflakes = []

for _ in range(50):
    flake = turtle.Turtle()
    flake.shape("circle")
    flake.color("white")
    flake.penup()
    flake.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(100, 300)
    flake.goto(x, y)
    snowflakes.append(flake)


def snowfall():
    for flake in snowflakes:
        y = flake.ycor()
        y -= random.randint(1, 5)
        if y < -300:
            y = random.randint(100, 300)
            x = random.randint(-300, 300)
            flake.goto(x, y)
        else:
            flake.sety(y)
    screen.update()
    screen.ontimer(snowfall, 50) 


snowfall()
screen.mainloop()



