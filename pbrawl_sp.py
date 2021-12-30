from racket import Racket
from ball import Ball
from tkinter import *
from Mapping_for_Tkinter import Mapping_for_Tkinter
import random
import time

def single():
    # Create Tk object, Racket and Ball Object with same canvas size as before
    diff = input("\nSelect difficulty!(1 for easy 2 for hard any other key for medium): ")
    if diff == "1":
        v0 = 250
        dv = 50
    elif diff == "3":
        v0 = 450
        dv = 70
    else:
        v0 = 350
        dv = 60
    root = Tk()
    mapping = Mapping_for_Tkinter(-300, 300, -300, 300, 600)
    canvas = Canvas(root, width=mapping.get_width(), height=mapping.get_height(), bg="black")
    r = Racket(mapping, canvas, mapping.get_i(0), mapping.get_j(-295))
    b = Ball(mapping, canvas, mapping.get_i(0), mapping.get_j(mapping.get_ymin()+14), v0, 55)
    # Create ball and racket, bind mouse clicks to racket
    b.create_oval()
    pong = r.create_rectangle()
    canvas.bind("<Left>", lambda e: r.shift_left(pong))
    canvas.bind("<Right>", lambda e: r.shift_right(pong))
    canvas.focus_set()
    canvas.pack()
    t = 0  # real time between event
    t_total = 0  # real total time
    n = 2
    while True:
        # having coordinates of both ball and racket will help program know when rebound off racket occurs
        if n == 2:
            rack = canvas.coords(pong)
            ping = canvas.coords(b.get_ball())
            t = t + 0.01  # real time between events- in second
            t_total = round(t_total + 0.01,2)  # real total time- in second
            side = b.update_xy(t)  # Update ball position and return collision event
            root.update()  # update the graphic (redraw)
            if ping[2] <= rack[2] and rack[0] <= ping[0] and ping[3] >= rack[1]:
                # if ball is on the racket, and in between is right and left edges optional argument from update_xy
                # is called, making the ball bounce off the racket by decreasing the rebound height
                side = b.update_xy(t, True)
            if side == 1:
                # Velocity and theta are increased by 25% and randomized between values respectively
                if b.get_velocity() >= 900:
                    b.set_velocity(850)
                else:
                    b.set_velocity(b.get_velocity()+dv)
                b.set_theta(random.uniform(-160, -20))
            if side != 0:
                # Reinitialize time to make sure update_xy method isn't getting screwed up
                t = 0
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if b.get_y() >= mapping.get_j(mapping.get_ymin()+4):  # stop the simulation if ball touches bottom edge
                print("Game Over! Total time: %s seconds" % t_total)
                n = 1
        else:
            replay = input("\n\nContinue?(Enter for no, any other key for yes): ")
            if replay == "":break
            else:
                n = 2
                t = 0
    print("\nThanks for playing :)")
    root.destroy()




