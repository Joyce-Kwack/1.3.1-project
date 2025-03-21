# layers of the ocean
import turtle as trtl
import random as rand

wn = trtl.Screen()
trtl.screensize(canvwidth = 400, canvheight = 400, bg = "lightblue")

ocean = trtl.Turtle()
setup = ("Helvetica", 12)
fish = []
squid = []

#--------sunlight zone----------
# write instructions
'''ocean.penup()
ocean.goto(0,400)
ocean.write("Press s when you see the stingray to go to the next zone!", font = setup)

# functions
def draw_fish():
    annoying_fish.hideturtle()
    annoying_fish.penup()
    fish_y = rand.randint(-400,400)
    annoying_fish.goto(-1200, fish_y)
    annoying_fish.showturtle()
    bluefish = "fish.gif"
    wn.addshape(bluefish)
    annoying_fish.shape(bluefish)
    wn.tracer(True)
    wn.update()

def info_sunlight():
     ocean.clear()
     ocean.goto(-400,400)
     ocean.write("The sunlight zone is the top layer of the ocean. There is enough sunlight for plants to thrive. Stingrays are an example of the many animals that live in this zone.", font = setup)
     ocean.penup()

# draw coral
ocean.hideturtle()
wn.addshape("coral.gif")
for i in range(15):
    ocean.goto(rand.randint(-1000,1000),rand.randint(-500,-300))
    ocean.shape("coral.gif")
    ocean.stamp()

# draw and move stingray
stingray_image = "actualstingray.gif"
wn.addshape(stingray_image)
stingray = trtl.Turtle()
stingray.penup()
stingray.goto(-1300,0)
stingray.shape(stingray_image)

# draw and move fish and stingray
for i in range(5):
    wn.onkeypress(info_sunlight, "s")
    wn.listen()
    annoying_fish = trtl.Turtle()
    annoying_fish.speed('fastest')
    draw_fish()
    fish.append(annoying_fish)
    while annoying_fish.xcor() < 1200:
        annoying_fish.goto(annoying_fish.xcor() + 10, annoying_fish.ycor())
    if i >= 3: 
        while stingray.xcor() < 1200:
            stingray.goto(stingray.xcor() + 500, stingray.ycor())'''
    
#-----------twilight zone---------------
screen = trtl.Screen()
screen.bgpic("twilight_zone.gif")
ocean.clear()
ocean.penup()
ocean.goto(0,400)
ocean.write("Use the arrow keys to help the whale reach the star")

# draw star
ocean.penup()
ocean.goto(900,-500)
wn.addshape("star.gif")
ocean.shape("star.gif")

# initialize blue whale
whale = trtl.Turtle()
wn.addshape("actualbluewhale.gif")
whale.shape("actualbluewhale.gif")

# whale movement functions
def move_up():
    whale.setheading(90)
    whale.forward(10)
def move_down():
    whale.setheading(270)
    whale.forward(10)
def move_right():
    whale.setheading(0)
    whale.forward(10)
def move_left():
    whale.setheading(180)
    whale.forward(10)
    
# keyboard controls
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.listen()

# set conditions for whale
if whale.ycor() < -450:
    if whale.xcor() > 900:
        ocean.clear()
        ocean.goto(-400,400)
        ocean.write("The twilight zone is the second layer, and it makes up about 20 percent of the ocean's volume. Animals like the vampire squid and the anglerfish live in this zone. ", font = setup)
        ocean.penup()

#---------midnight zone--------------
screen = trtl.Screen()
screen.bgcolor(32/255,58/255,158/255)
ocean.clear()
ocean.penup()
ocean.goto(0,400)
ocean.write("Press m when you see the anglerfish to finish the game!", font = setup)

# functions
def draw_squid():
    annoying_squid.hideturtle()
    annoying_squid.penup()
    squid_x = rand.randint(-400,400)
    annoying_squid.goto(squid_x, -1000)
    annoying_squid.showturtle()
    vampire_squid = "vampire_squid_new.gif"
    wn.addshape(vampire_squid)
    annoying_squid.shape(vampire_squid)
    wn.tracer(True)
    wn.update()

def info_midnight():
     setup = ("Helvetica", 12)
     ocean.clear()
     ocean.goto(-400,400)
     ocean.write("The midnight zone is the third layer, and it is the largest habitat on Earth, making up about 70 percent of the ocean. Animals like the vampire squid and the lanternfish live in this zone. ", font = setup)
     ocean.penup()

# draw and move anglerfish
anglerfish_image = "anglerfish.gif"
wn.addshape(anglerfish_image)
anglerfish = trtl.Turtle()
anglerfish.penup()
anglerfish.goto(0,-2000)
anglerfish.shape(anglerfish_image)

# draw and move squid and lanternfish
for i in range(5):
    wn.onkeypress(info_midnight, "m")
    wn.listen()
    annoying_squid = trtl.Turtle()
    annoying_squid.speed('fastest')
    draw_squid()
    squid.append(annoying_squid)
    while annoying_squid.ycor() < 1200:
        annoying_squid.goto(annoying_squid.xcor(), annoying_squid.ycor() + 10)
    if i >= 3: 
        anglerfish.speed('slow')
        anglerfish.goto(0,700)

wn.listen()
wn.mainloop()