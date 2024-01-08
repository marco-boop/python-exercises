import turtle

#define constants
#Use capital letters
SQUARE = 4
TRIANGLE = 3
PENTAGON = 5
HEXAGON = 6
OCTAGON = 8

def draw_shape(sides, color):

    turtle.color(color)

    for i in range(0,sides):
        turtle.fd(50)
        turtle.lt(360/sides)
    turtle.fd(75)

turtle.goto(-250,0)

# draw_shape(int(input("How many sides does your shape have >  ")), "blue")
draw_shape(TRIANGLE, "red")
draw_shape(PENTAGON, "green")
draw_shape(HEXAGON,"pink")
draw_shape(OCTAGON,"purple")

delay = input("Press enter to finish.")