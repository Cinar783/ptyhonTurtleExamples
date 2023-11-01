import turtle

drawing_board=turtle.Screen()
turtle_instance=turtle.Turtle()

def turtle_forfard():
    turtle_instance.forward(100)

def turtle_lef():
    turtle_instance.setheading(turtle_instance.heading()-10)
    #turtle_instance.left(10)

def turtle_rıght():
    turtle_instance.setheading(turtle_instance.heading()+10)
    #turtle_instance.right(10)

def clear_screen():
    turtle_instance.clear()

def turtle_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()


def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

turtle.listen()
turtle.onkey(fun=turtle_forfard,key='space')
turtle.onkey(fun=turtle_lef,key='Down')
turtle.onkey(fun=turtle_rıght,key="Up")
turtle.onkey(fun=clear_screen,key="c")
turtle.onkey(fun=turtle_home,key="h")
turtle.onkey(fun=turtle_pen_up,key="z")
turtle.onkey(fun=turtle_pen_down,key="x")

turtle.mainloop()