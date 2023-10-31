import  turtle

turtle_screen=turtle.Screen()
turtle_instance=turtle.Turtle()
turtle_screen.bgcolor("black")
turtle_screen.title("Python turtle")
turtle_instance.color("white")
turtle.speed(0)
turtle_color=["red","blue","purple","white","yellow","orange","green"]


for i in range(10):
    turtle_instance.color(turtle_color[i%6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i*2)




turtle.done()