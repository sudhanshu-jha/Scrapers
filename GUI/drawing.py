import turtle


def drawing():
    # Create a window where action will take place
    window = turtle.Screen()
    window.bgcolor("black")

    # Call the Draw Shape for each object
    draw_shape("square", "green", "arrow", 1)
    draw_shape("circle", "purple", "turtle", 3)
    draw_shape("triangle", "blue", "circle", 6)

    # Capture Click Event and Exit
    window.exitonclick()


def draw_shape(format, color, shape, speed):

    # Create the turtle
    generic_turtle = turtle.Turtle()
    generic_turtle.shape(shape)
    generic_turtle.color(color)
    generic_turtle.speed(speed)

    if (format == "square"):
        start = 1
        while (start <= 4):
            generic_turtle.forward(100)
            generic_turtle.right(90)
            start = start + 1

    elif (format == "circle"):
        generic_turtle.circle(60)

    elif (format == "triangle"):
        start = 1
        while (start <= 3):
            generic_turtle.forward(100)
            generic_turtle.right(120)
            start = start + 1

    else:
        print("Unrecognized Format")

drawing()
