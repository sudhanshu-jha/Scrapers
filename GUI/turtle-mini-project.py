import turtle

# Global Project Settings
background = "black"
shape = "turtle"
speed = 0
color = "green"
start_filled = 60
start_unfilled = -60
triangle_angles = -120

# Different Triangle Sides
side = 30

# Vector Sides
start = 1
end = 3

# Angles to be drawn
specifics = {
    'filled_unit': [start_filled, triangle_angles, triangle_angles, side],
    'unfilled_unit': [start_unfilled, triangle_angles, triangle_angles, side]
}


def drawing():
    # Create a window where action will take place
    window = turtle.Screen()
    window.bgcolor(background)

    # Start the Actual Drawing
    party()

    # Final Graphic
    # final_figure(3)

    # Capture Click Event and Exit
    window.exitonclick()


def party():
    # Create the turtle
    teenage = turtle.Turtle()
    teenage.shape(shape)
    teenage.color(color)
    teenage.speed(speed)

    # Create the 3 different groups
    group(teenage)
    teenage.forward(60)
    teenage.left(60)
    teenage.forward(30)
    group(teenage)
    teenage.left(-60)
    teenage.forward(60)
    teenage.left(-60)
    teenage.forward(60)
    teenage.left(60)
    teenage.forward(30)
    group(teenage)


def group(mutant):
    friends(mutant)
    mutant.left(0)
    mutant.forward(30)
    mutant.left(-180)
    friends(mutant)
    mutant.left(0)
    mutant.forward(30)
    mutant.left(-180)
    friends(mutant)


def friends(ninja):
    unit(ninja, "filled_unit")
    unit(ninja, "unfilled_unit")
    ninja.left(-60)
    ninja.forward(30)
    ninja.left(-180)
    unit(ninja, "filled_unit")
    ninja.left(-120)
    ninja.forward(30)
    ninja.left(-60)
    unit(ninja, "filled_unit")
    ninja.left(-120)
    ninja.forward(30)


def unit(turtle, which):
    # Since start has an assignment in the loop
    global start

    # Only Begin fill if it is a filled_unit
    if which == "filled_unit":
        turtle.begin_fill()

    # Draw the triangle
    while (start <= end):
        turtle.left(specifics[which][start - 1])
        turtle.forward(specifics[which][3])
        start = start + 1

    # Allow the Looping to be restarted next time
    start = 1

    # Only End fill if it is a filled_unit
    if which == "filled_unit":
        turtle.end_fill()

drawing()
