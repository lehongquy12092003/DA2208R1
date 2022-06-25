import turtle

t = turtle.Turtle()
d = 0
while True:
    t.fd(d)
    t.lt(10)
    d+=0.1
    if d > 30:
        break
    
