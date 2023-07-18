import turtle as tr
#-window-----------
win = tr.Screen()
win.title("The Artist's Turtle V_0.8")
win.bgcolor("Black")
win.setup(1000,600)
#-Turtle_Object----
T = tr.Turtle()
T.color("Cyan")
T.speed(0)

a = 20 

#-Funcs-----------
def T_up():
    y = T.ycor()
    y += a
    T.sety(y)

def T_down():
    y = T.ycor()
    y -= a
    T.sety(y)

def T_right():
    x = T.xcor()
    x += a
    T.setx(x)

def T_left():
    x = T.xcor()
    x -= a
    T.setx(x)

def T_penup():
    T.penup()

def T_pendown():
    T.pendown()
#------------------
win.listen()
win.onkeypress(T_up,"z")     # ↑
win.onkeypress(T_down,"s")   # ↓
win.onkeypress(T_right,"d")  # →
win.onkeypress(T_left,"q")   # ←
win.onkeypress(T_penup,"0")
win.onkeypress(T_pendown,"1")
#------------------
while True:
    win.update()