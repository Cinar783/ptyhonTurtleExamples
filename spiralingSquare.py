import turtle

drawing_board=turtle.Screen()
turtle_instance=turtle.Turtle();
n=5

for i in range(n*4):
    turtle_instance.forward(i*20)
    turtle_instance.left(90)

turtle.done()


