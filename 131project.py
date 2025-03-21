# layers of the ocean
import turtle as trtl
import random as rand

wn = trtl.Screen()
trtl.screensize(canvwidth = 400, canvheight = 400, bg = "lightblue")

ocean = trtl.Turtle()
fish = []
squid = []

# sunlight zone
ocean.penup()
ocean.goto(0,400)
ocean.write("Press s when you see the stingray to go to the next zone!")
setup = ("Helvetica", 12)

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
            stingray.goto(stingray.xcor() + 500, stingray.ycor())
    
# twilight zone
screen = trtl.Screen()
screen.bgpic("twilight_zone.gif")

ocean.clear()
ocean.penup()
ocean.goto(0,400)
ocean.write("Press t when you see the anglerfish to go to the next zone!", font = setup)

# functions
def draw_squid():
    annoying_squid.hideturtle()
    annoying_squid.penup()
    squid_x = rand.randint(-400,400)
    annoying_squid.goto(squid_x, -1000)
    annoying_squid.showturtle()
    vampire_squid = "vampire_squid.gif"
    wn.addshape(vampire_squid)
    annoying_squid.shape(vampire_squid)
    wn.tracer(True)
    wn.update()

def info_twilight():
     setup = ("Helvetica", 12)
     ocean.clear()
     ocean.goto(-400,400)
     ocean.write("The twilight zone is the second layer, and it makes up about 20 percent of the ocean's volume. Animals like the vampire squid and the anglerfish live in this zone. ", font = setup)
     ocean.penup()

# draw and move anglerfish
anglerfish_image = "anglerfish.gif"
wn.addshape(anglerfish_image)
anglerfish = trtl.Turtle()
anglerfish.penup()
anglerfish.goto(0,-2000)
anglerfish.shape(anglerfish_image)

# draw and move squid and anglerfish
for i in range(5):
    wn.onkeypress(info_twilight, "t")
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

# midnight zone


wn.listen()
wn.mainloop()