from racket import Racket
from ball import Ball
from tkinter import *
from Mapping_for_Tkinter import Mapping_for_Tkinter
import random
import time


def multi():
    # create Tk Object, Canvas, both objects of class racket and the object of class ball
    root = Tk()
    v0 = 350
    mapping = Mapping_for_Tkinter(-300, 300, -300, 300, 600)
    canvas = Canvas(root, width= mapping.get_width(), height=mapping.get_height(), bg="grey")
    r1 = Racket(mapping, canvas, mapping.get_i(0), mapping.get_j(mapping.get_ymin()+5))  # bottom racket
    r2 = Racket(mapping, canvas, mapping.get_i(0), mapping.get_j(mapping.get_ymax()-5))  # top racket
    b = Ball(mapping, canvas, mapping.get_i(0), mapping.get_j(mapping.get_ymin()+14), v0, 45)
    # create both rackets and ball
    b.create_oval()
    pong = r1.create_rectangle()
    pong2 = r2.create_rectangle()
    canvas.pack()
    t = 0  # real time between event
    t_total = 0  # real total time
    score_top = 0
    score_bottom = 0
    firstto = input("First to (press enter for first to 3): ")
    if firstto == "":
        firstto = 3
    else:
        firstto = int(firstto)

    i = 2 #used to reset while loop to play another match
    while True:
        # once again use coords method to make conditionals easy
        if i == 2:
            canvas.pack()
            canvas.focus_set()
            rack = canvas.coords(pong)
            rack2 = canvas.coords(pong2)
            ping = canvas.coords(b.get_ball())
            t = t + 0.01  # real time between events- in second
            t_total = t_total + 0.01  # real total time- in second
            side = b.update_xy(t)  # Update ball position and return collision event
            root.update()  # update the graphic (redraw)

            if ping[2] <= rack[2] and rack[0] <= ping[0] and ping[3] >= rack[1]:  # when bottom racket is struck
                side = b.update_xy(t, True)
            if ping[2] <= rack2[2] and rack2[0] <= ping[0] and ping[3] >= rack2[1]:  # when top racket is struck
                side = b.update_xy(t, False)
            if side == 1:  # when top edge is struck, color of activated racket, theta, and binding change to racket1
                r1.activate(pong)
                r2.deactivate(pong2)
                canvas.bind("<Left>", lambda e: r1.shift_left(pong))
                canvas.bind("<Right>", lambda e: r1.shift_right(pong))
                b.set_theta(random.uniform(-160, -20))
                b.set_velocity(50 + b.get_velocity())
            if side == 2:  # when bottom edge is struck, color of activated racket, theta, and binding change to racket2
                r2.activate(pong2)
                r1.deactivate(pong)
                canvas.bind("<a>", lambda e: r2.shift_left(pong2))
                canvas.bind("<d>", lambda e: r2.shift_right(pong2))
                b.set_theta(random.uniform(20, 160))
                b.set_velocity(50 + b.get_velocity())
            if side != 0:  # reinitialize time just like in ball.py
                t = 0
            if b.get_velocity() > 650:
                b.set_velocity(600)
            time.sleep(0.01)  # wait 0.01 second (simulation time)

            #conditionals that read when ball is missed, changes and prints score, breaks if limit is reached


            if b.get_y() >= mapping.get_j(mapping.get_ymin()+4):
                score_top += 1
                b.set_velocity(v0)
                if score_bottom < score_top < firstto:
                    print("Top Player leads %s - %s" % (score_top, score_bottom))
                elif score_top < score_bottom:
                    print("Bottom Player leads %s - %s" % (score_bottom, score_top))
                elif score_top == score_bottom:
                    print("Series Tied %s - %s" % (score_top, score_bottom))
                if score_top == firstto:
                    print("====================Top Player wins %s - %s!===================" % (score_top, score_bottom))
                    i = 1
            elif b.get_y() <= mapping.get_j(mapping.get_ymax()-4):
                score_bottom += 1
                b.set_velocity(v0)
                if score_top < score_bottom < firstto:
                    print("Bottom Player leads %s - %s" % (score_bottom, score_top))
                elif score_bottom < score_top:
                    print("Top Player leads %s - %s" % (score_top, score_bottom))
                elif score_top == score_bottom:
                    print("Series Tied %s - %s" % (score_top, score_bottom))
                if score_bottom == firstto:
                    print("====================Bottom Player wins %s - %s!====================" % (score_bottom, score_top))
                    i = 1
        else:
            reset = input("\n\nPlay again?(Enter for no, any other key for yes): ")
            if reset == "": break
            else:
                i = 2
                score_bottom = 0
                score_top = 0
    print("Thanks for Playing :)")
    root.destroy()




