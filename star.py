import turtle
turtle.color("blue")
turtle.speed(15)



def star(t, size):
    for i in range(5):
       turtle.forward(size)
       t.right(144)

def starspiral():
 size=1
 for i in range(60):
   star(turtle,size)
   size=size+5
turtle.forward(10)
turtle.right(5)

starspiral()
turtle.penup()
turtle.forward(280)
turtle.pendown()


starspiral()
turtle.penup()
turtle.backward(200)
turtle.pendown()

starspiral
for i in range(30):
    star(turtle,size)
    size=size+5
    turtle.forward(1)
    turtle.right(10)
turtle.exitonclick()