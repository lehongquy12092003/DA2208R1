import turtle
def nhamouoc(a,b,c,d,e,f,g,h):
    t = turtle.Turtle()
    turtle.bgcolor("green")
    t.penup()
    t.goto(-400,-100)
    t.pendown()
    t.color("deepskyblue")
    t.begin_fill()
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)
    t.end_fill()

    t.penup()
    t.goto(-320,225)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    t.penup()
    t.goto(200,200)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.penup()
    t.goto(200,240)
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.penup()
    t.goto(230,215)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.penup()
    t.goto(180,225)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()


    t.penup()
    t.goto(-100,-100)
    t.pendown()
    t.pensize(3)
    t.color("chocolate","orange")
    t.begin_fill()

    for i in range(4):
        t.fd(c)
        t.lt(90)
    t.end_fill()

    t.penup()
    t.goto(20,130)
    t.pendown()
    t.color("brown","firebrick")
    t.begin_fill()
    for i in range(2):
        t.fd(d)
        t.lt(90)
        t.fd(e)
        t.lt(90)
    t.end_fill()

    t.penup()
    t.goto(-127, 70)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.fd(f)
        t.lt(120)
    t.end_fill()

    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color("black","white")
    t.begin_fill()

    for i in range(4):
        t.fd(g)
        t.lt(90)
    t.end_fill()

    t.penup()
    t.goto(0,25)
    t.pendown()
    t.color("black")
    t.fd(g)

    t.penup()
    t.goto(25,0)
    t.pendown()
    t.lt(90)
    t.fd(g)
#
    t.penup()
    t.goto(-80,0)
    t.pendown()
    t.rt(90)
    t.color("black","white")
    t.begin_fill()

    for i in range(4):
        t.fd(g)
        t.lt(90)
    t.end_fill()

    t.penup()
    t.goto(-80,25)
    t.pendown()
    t.color("black")
    t.fd(50)

    t.penup()
    t.goto(-55,0)
    t.pendown()
    t.lt(90)
    t.fd(g)

    t.penup()
    t.goto(-40,-97)
    t.pendown()
    t.rt(90)
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.fd(g)
        t.lt(90)
        t.fd(h)
        t.lt(90)
    t.end_fill()   
    
    t.penup()
    t.goto(-30,-60)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
nhamouoc(800,500,170,40,100,225,50,80)














