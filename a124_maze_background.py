import turtle as trtl
import random as rand
import time

wn = trtl.Screen()

# background 
wn.bgpic("sky3.gif")

# set variables
number_of_walls = 40
width = 40
pen_color = "white"

# initialize maze turtle
maze = trtl.Turtle()
maze.pencolor(pen_color)
maze.pensize(5)
maze.speed('fastest')

# initialize player turtle
player = trtl.Turtle()
player.shape("turtle")
player.color("white")
wizard_image = "geeked wizard tiny.gif"
wn.addshape(wizard_image)
player.shape(wizard_image)

# initialize star turtle
star = trtl.Turtle()
star.penup()
star.pencolor("white")
star.speed('fastest')

# records number of tries
tries = []

# write text
star.goto(-320,490)
star.write("Escape the maze before it's too late!", font = ("Arial", 24))
star.goto(-320,460)
star.write("You will be teleported every 30 seconds!", font = ("Arial", 20))

# draw the star
star_image = "star1.gif"
wn.addshape(star_image)
star.penup()
star.goto(360,420)
star.shape(star_image)
star.stamp()
wn.update()

# maze functions
def entry():
    maze.penup()
    maze.forward(width)
    maze.pendown()

def extra_wall():
    maze.left(90)
    maze.forward(width)
    maze.penup()
    maze.right(180)
    maze.forward(width)
    maze.left(90)
    maze.pendown()

# draw maze
for i in range (number_of_walls):
    # set more variables
    wall_length = 100 + i*width/2
    if i <= 4:
        maze.penup()
        maze.left(90)
        maze.forward(wall_length)
    elif i >= 36:
        maze.pendown()
        maze.left(90)
        maze.forward(wall_length)
    else:
        maze.pendown()
        maze.left(90)
        rem = i % 3
        if rem==0:
            door = rand.randint(width, wall_length - width * 3)
            maze.forward(door)
            entry()
            barrier1 = rand.randint(width, wall_length - door - width*2)
            maze.forward(barrier1)
            extra_wall()
            maze.forward(wall_length - door - barrier1 - width)
        else:
            barrier = rand.randint(width, wall_length - (width * 3))
            maze.forward(barrier)
            extra_wall()
            door1 = rand.randint(width, wall_length - barrier - width*2)
            maze.forward(door1)
            entry()
            maze.forward(wall_length - barrier - door1 - width)
maze.hideturtle()

# Create goal
goal = trtl.Turtle()
broom_image = "broom.gif"
wn.addshape(broom_image)
goal.shape(broom_image)
goal.penup()
goal.goto(340, -340)  # Exit position


# Teleport player randomly
def teleport_player():
    if player.xcor() > 340:
        print("You escaped the maze!")
        print("It took you", len(tries), "tries!")
    else:
        new_x, new_y = rand.randint(-240, 240), rand.randint(-240, 240)
        player.penup()
        player.goto(new_x, new_y)
        print("🔮 Teleported!") 
        tries.append("try")
        # Schedule the next teleport
        wn.ontimer(teleport_player, 30000)

# Movement functions
def move_up():
    player.setheading(90)
    player.forward(10)
def move_down():
    player.setheading(270)
    player.forward(10)
def move_right():
    player.setheading(0)
    player.forward(10)
def move_left():
    player.setheading(180)
    player.forward(10)
    
# Keyboard controls
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

teleport_player()

trtl.done()

wn.listen()

wn.mainloop()