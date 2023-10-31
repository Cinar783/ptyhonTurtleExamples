import  turtle

turtle_screen=turtle.Screen()
turtle_instance=turtle.Turtle()


def turtle_function (size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size=size-5


turtle_function(150)
turtle_function(130)
turtle_function(110)
turtle_function(90)
turtle_function(70)
turtle_function(50)
turtle_function(30)
turtle_function(10)



turtle.done()
