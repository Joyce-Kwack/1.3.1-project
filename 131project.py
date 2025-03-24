import turtle as trtl
import random as rand
import time
import subprocess

# Correctly formatted path using raw string (to handle backslashes)
sound_file_path = r"H:\CSP\1_3_1\exampleaudio.wav"

# Run the subprocess to play the sound
subprocess.run(['start', sound_file_path], shell=True)

# Create the main screen and make it fullscreen
wn = trtl.Screen()

# Set the window to fullscreen
wn._root.attributes('-fullscreen', True)
wn.bgcolor("lightblue")

ocean = trtl.Turtle()
setup = ("Helvetica", 28)
fish = []
squid = []

#--------sunlight zone----------
# write instructions
username = input("What is your name?:")
print("Hello",username,", this card is about the first three layers of the ocean. Follow the instructions on the screen to continue!")
ocean.hideturtle()
ocean.penup()
ocean.goto(0,400)
ocean.showturtle()
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
     ocean.write("The sunlight zone is the top layer of the ocean. There is enough sunlight for plants to thrive. Stingrays are an example of the many animals that live in this zone.", font = ("Helvetica",12))
     ocean.penup()

# draw coral
ocean.hideturtle()
wn.addshape("coral.gif")
for i in range(15):
    ocean.speed('fastest')
    ocean.goto(rand.randint(-1000,1000),rand.randint(-500,-300))
    ocean.shape("coral.gif")
    ocean.stamp()

# draw and move stingray
stingray_image = "actualstingray.gif"
wn.addshape(stingray_image)
stingray = trtl.Turtle()
stingray.penup()
stingray.hideturtle()
stingray.goto(-1300,0)
stingray.showturtle()
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
    
#-----------twilight zone---------------
wn.bgcolor(132/255,172/255,245/255)
ocean.speed('normal')
ocean.clear()
ocean.penup()
ocean.goto(0,400)
ocean.write("Get whale soon!", font = setup)
ocean.goto(0,360)
ocean.write("Blue whales are able to dive into the twilight zone to find food.", font = ("Helvetica",12))

# initialize blue whale
whale = trtl.Turtle()
whale.hideturtle()
whale.penup()
whale.goto(1000,0)
whale.showturtle()
wn.addshape("actualbluewhale.gif")
whale.shape("actualbluewhale.gif")

# move blue whale
while whale.xcor() > -1300:
    whale.goto(whale.xcor()-20,0)
time.sleep(10)
whale.hideturtle()
wn.clear()

#---------midnight zone--------------
wn.bgcolor(32/255,58/255,158/255)
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

# ending
time.sleep(5)
print("Congratulations", username,"! You have reached the end of the card :)")

wn.listen()
wn.mainloop()
