#(C) 2022. https://blog.naver.com/gmail2012 all rights reserved.

import turtle as t
import numpy as np
import sys
import math

Angle = 1/7
c = 500
c_move = 50
b_move = 50
a_move = 50
num_size = 30

def draw_x(z, x_len):
    x = t.xcor()-(z*Angle)
    t.up()
    t.goto(x, z*Angle)
    t.down()
    t.setheading(0)
    t.fd(z*Angle)
    t.up()
    t.goto(x, z*Angle)
    t.down()
    t.setheading(270)
    t.fd(z*Angle)
    t.up()
    t.goto(x+(z*Angle), 0)
    t.down()

    t.goto(x_len/2, 0)
    t.up()
    t.goto(t.xcor(), t.ycor()-a_move)
    t.write("%d"%x_len, False, "center", ("",num_size))
    t.goto(t.xcor(), t.ycor()+a_move)
    t.down()
    t.goto(0,0)

def draw_arc(x, i):
    t.down()
    t.goto(t.xcor()+(x*Angle), 0)
    t.setheading(90)
    t.color("red")
    t.circle(x*Angle, 90-i)
    t.up()
    t.goto(t.xcor()-((x*Angle)+20), 0)
    t.write("%g'"%(90-i), False, "center", ("",25))
    t.color("black")

t.ht()
t.speed(0)
t.speed()
t.pensize(3)
t.title("(C) 2022. https://blog.naver.com/gmail2012 all rights reserved.");
t.setup(width=.999, height=.99)

def Loop(i):
    t.home()
    t.clear()

    t.down()
    t.setheading(90)
    t.right(i)
    t.fd(c/2)
    t.up()
    t.goto(t.xcor()-c_move, t.ycor())
    t.write("%d"%c, False, "center", ("",num_size))
    t.goto(t.xcor()+c_move, t.ycor())
    t.down()
    t.fd(c/2)

    t.setheading(270)
    b = t.ycor()
    a = t.xcor()
    t.goto(t.xcor(), int(np.round(b))*2/5)
    t.up()
    t.goto(t.xcor()+b_move, t.ycor())
    t.write("%d"%int(np.round(b)), False, "center", ("",num_size))
    t.goto(t.xcor()-b_move, t.ycor())
    t.down()
    t.goto(t.xcor(), 0)

    if int(np.round(a)) >= int(np.round(b)):  
        draw_x(int(np.round(b)), int(np.round(a)))
        draw_arc(int(np.round(b)), i)
    else:
        draw_x(int(np.round(a)), int(np.round(a)))
        draw_arc(int(np.round(a)), i)

    t.up()
    t.goto(-750, 250)
    t.write("sin(x)\n----  =  %g\n   x"%(math.sin(math.radians(90-i))/math.radians(90-i)), False, "left", ("",25))
    t.goto(-750, 50)
    t.write("tan(x)\n----  =  %g\n   x"%(math.tan(math.radians(90-i))/math.radians(90-i)), False, "left", ("",25))
    t.goto(-750, -150)
    t.write("cos(x)\n----  =  %g\n   x"%(math.cos(math.radians(90-i))/math.radians(90-i)), False, "left", ("",25))
    t.home()

while 1:
    n = t.numinput("Degree", "Enter Degree (0 ~ 89)", minval=0.000000000001, maxval=89)

    if n != None:
        Loop(90 - n)
    else:
        t.bye()
        sys.exit(0)

t.mainloop()