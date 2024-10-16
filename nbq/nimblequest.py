# ---- imports ----
import turtle as t
import time
import random
wn = t.Screen()
framedelay = 0.1


# ---- counter test ----
counter =  t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-860,440)
counter.pendown()
timer2 = 1
timer = 3
repeatrate = 20
counter_interval = 2
counter_interval2 = 800000
timer_up = False
global changeDir
changeDir = False

#---- img
lanB = "lancer_back.gif"
lanB2 = "lancer_back2.gif"
lanB3 = "lancer_back3.gif"
lanR = "lancer_right.gif"
lanR2 = "lancer_right2.gif"
lanR3 = "lancer_right3.gif"
lanL = "lancer_left.gif"
lanL2 = "lancer_left2.gif"
lanL3 = "lancer_left3.gif"
lanF = "lancer_front.gif"
lanF2 = "lancer_front2.gif"
lanF3 = "lancer_front3.gif"

wn.addshape(lanB)
wn.addshape(lanB2)
wn.addshape(lanB3)
wn.addshape(lanR)
wn.addshape(lanR2)
wn.addshape(lanR3)
wn.addshape(lanL)
wn.addshape(lanL2)
wn.addshape(lanL3)
wn.addshape(lanF)
wn.addshape(lanF2)
wn.addshape(lanF3)

# ---- knight img ----
kniF = "knight_front.gif"

wn.addshape(kniF)

# ---- knight ----
knight = t.Turtle()
knight.penup()
knight.goto(200,200)
knight.shape(kniF)
wn.update()
# ---- lancer ----
lancer = t.Turtle()
lancer.penup()
lancer.goto(0,0)
lancer.shape(lanB)
wn.update()

#---- func img
def boundary(lancer):
  if (((400 - abs(lancer.xcor())) < 125) | ((400 - abs(lancer.ycor())) < 125)):
    print("hit boundary")
    lancer.hideturtle()
    lancer.penup()
  return True

def check(prevheading):
  if(prevheading == lancer.heading()):
    return True
  else:
    return False

def checking(img1,img2,img3,x):
  global timer
  global heading
  heading = 90
  timer = 3
  while(timer > -1):
    if timer == 0:
      lancer.shape(img2)
      wn.update()
      timer -= 1
    else:
      if timer == 3:
        lancer.shape(img3)
        wn.update()
      elif timer == 2:
        lancer.shape(img2)
        wn.update()
      else:
        lancer.shape(img1)
        wn.update()
      timer -= 1
    boundary(lancer)
    hitbox()
    time.sleep(0.1)
    lancer.forward(6)
    


#---- func mov
def up():
  if(lancer.heading == 90):
    checking(lanB,lanB2,lanB3,up)
  else:
    lancer.setheading(90)
    checking(lanB,lanB2,lanB3,up)
def down():
  if(lancer.heading == 270):
    checking(lanF,lanF2,lanF3,down)
  else:
    lancer.setheading(270)
    checking(lanF,lanF2,lanF3,down)
def left():
  if(lancer.heading == 180):
    checking(lanL,lanL2,lanL3,left)
  else:
    lancer.setheading(180)
    checking(lanL,lanL2,lanL3,left)
def right():
  if repeating:
    wn.ontimer(right,repeatrate)
    if(lancer.heading == 0):
      checking(lanR,lanR2,lanR3,right)
    else:
      lancer.setheading(0)
      checking(lanR,lanR2,lanR3,right)

def start_repeat(func):
    global repeating

    repeating = True

    func()

def stop_repeat():
    global repeating

    repeating = False

repeating = False

# Tell the program which functions go with which keys
wn.onkeypress(lambda: start_repeat(left), 'Left')
wn.onkeyrelease(stop_repeat, 'Left')

wn.onkeypress(lambda: start_repeat(right), 'Right')
wn.onkeyrelease(stop_repeat, 'Right')

# ---- lancer hp ----

def hitbox():
  global hp 
  hp = 200
  if (lancer.xcor()) - knight.xcor() < 25 :
    if (lancer.ycor()) - knight.ycor() < 25 :
      hp = hp - 50
      print(hp)
    counter.getscreen().ontimer(hitbox, counter_interval2)
# ---- screen ----


wn.setup(800,800)
wn.bgpic("map.png")
while True:
  wn.listen()
  wn.onkeypress(up, "w")
  wn.onkeypress(down, "s")
  wn.onkeypress(left, "a")
  wn.onkeypress(right, "d")
  time.sleep(0.2)
  wn.mainloop()

