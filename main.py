import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

#square
turtle.instance = turtle.Turtle()  # Create a new Turtle object
#for i in range(4):
   # turtle.instance.forward(100)
   # turtle.instance.left(90)



#star
#for i in range(5):
   # turtle.instance.left(144)
   # turtle.instance.forward(200)

#polygon
num_sides=5
angle=360.0/num_sides
side_length=100
for i in range(num_sides):
    turtle.instance.left(angle)
    turtle.instance.forward(side_length)

turtle.done()