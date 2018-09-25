import turtle


def drawing():
    # Create a window where action will take place
    window = turtle.Screen()
    window.bgcolor("black")

    angle = 0
    while (angle <= 360):
        draw_square("blue", "circle", 3, angle)
        angle = angle + 10

    # Capture Click Event and Exit
    window.exitonclick()


def draw_square(color, shape, speed, angle):

    # Create the turtle
    generic_turtle = turtle.Turtle()
    generic_turtle.shape(shape)
    generic_turtle.color(color)
    generic_turtle.speed(speed)
    generic_turtle.right(angle)

    # Draw the Square
    start = 1
    while (start <= 4):
        generic_turtle.forward(100)
        generic_turtle.right(90)
        start = start + 1

drawing()
