# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spot_color="#4d4699"
spot_size=5
spot_shape="circle"
score=0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000
timer_up = False
wn=trtl.Screen()
wn.bgcolor("#dedbff")
color = ["#fa9687", "#fad687", "#bdfa87", "#87fabf", "#87e5fa", "#f687fa", "#fa87c6", "#c087fa"]

#-----initialize turtle-----
spot=trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)
spot.color(spot_color)
score_writer=trtl.Turtle()
counter = trtl.Turtle()

#-----game functions--------
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Timers up", font = font_setup)
        timer_up = True
        spot.hideturtle() 
    else: 
        counter.write("Timer: " + str(timer), font = font_setup)
        timer -=1
        counter.getscreen().ontimer(countdown, counter_interval)

def update_score():
    global score
    score+=1
    score_writer.clear()
    print(score_writer.write(score, font=font_setup))

def change_position():
    spot.penup()
    new_xpos= rand.randint(-200,-200)
    new_ypos= rand.randint(-150,150)
    spot.goto(new_xpos,new_ypos)
    spot.pendown()
    update_score()

def change_color():
    spot_color = rand.choice(color)
    spot.color(spot_color)
    spot.stamp()
    spot.color("#4d4699")

def spot_clicked(x,y):
    global spot_size
    spot.penup()
    spot.hideturtle()
    change_position()
    change_color()
    spot.showturtle()
    spot_size = spot_size/1.2
    spot.turtlesize(spot_size)
    spot.pendown()
    if timer_up==True:
        spot.hideturtle()

#-----events----------------

score_writer.penup()
counter.penup()
score_writer.goto(200,150)
counter.goto(200, 120)
score_writer.pendown()
counter.pendown()
spot.onclick(spot_clicked)

wn.ontimer(countdown, counter_interval)
wn.mainloop()
