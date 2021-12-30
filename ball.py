from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time

class Ball:
    def __init__(self,mapping,canvas,x0,y0,velocity, theta):
        # use get and set methods to make attributes private
        self.set_mapping(mapping)
        self.set_canvas(canvas)
        self.set_x0(x0)
        self.set_y0(y0)
        self.set_velocity(velocity)
        self.set_theta(theta)

    def get_mapping(self):
        return self.__mapping

    def get_canvas(self):
        return self.__canvas

    def get_x0(self):
        return self.__x0

    def get_y0(self):
        return self.__y0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_velocity(self):
        return self.__velocity

    def get_theta(self):
        return self.__theta

    def get_ball(self):
        return self.__ball

    def set_mapping(self, mapping):
        self.__mapping = mapping

    def set_canvas(self, canvas):
        self.__canvas = canvas

    # x0,v0,velocity and theta are used in calculations so must make them into float from string
    def set_x0(self, x0):
        self.__x0 = float(x0)

    def set_y0(self, y0):
        self.__y0 = float(y0)

    def set_velocity(self,velocity):
        self.__velocity = float(velocity)

    def set_theta(self,theta):
        # Turn given angle in degree to radian and float
        self.__theta = -float(theta)*(math.pi/180)

    def create_oval(self):
        # The -4 and +4 on x and y makes them the center of the ball and with radius 4
        self.__ball = self.__canvas.create_oval(self.__x0-4, self.__y0-4, self.__x0+4, self.__y0+4, fill="green")

    def update_xy(self, t, ymin=None):
        self.__x = self.__x0 + (self.__velocity * math.cos(self.__theta) * float(t))
        self.__y = self.__y0 + (self.__velocity * math.sin(self.__theta) * float(t))
        # Get the new x and y coordinates using second kinematics equation
        # Move the ball to new location, again with the -4 and +4 on respective coordinates
        self.__canvas.coords(self.__ball, self.__x -4, self.__y-4, self.__x+4, self.__y+4)
        if ymin is True:  # Deals with when the lower bound is higher to show ball bouncing off racket in game 1 and 2
            if self.__y >= self.__mapping.get_j(self.__mapping.get_ymin()+10):
                self.__theta = -self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("2")
            elif self.__y <= self.__mapping.get_j(self.__mapping.get_ymax()-4):
                self.__theta = -self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("1")
            elif self.__x <= self.__mapping.get_i(self.__mapping.get_xmin()+4):
                self.__theta = math.pi - self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("3")
            elif self.__x >= self.__mapping.get_i(self.__mapping.get_xmax()-4):
                self.__theta = math.pi - self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("4")
            else:
                return int("0")
        elif ymin is False:  # Deals with when top racket in game 2 needs to be rebounded off top screen instead of low
            if self.__y >= self.__mapping.get_j(self.__mapping.get_ymin()+4):
                self.__theta = -self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("2")
            elif self.__y <= self.__mapping.get_j(self.__mapping.get_ymax()-10):
                self.__theta = -self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("1")
            elif self.__x <= self.__mapping.get_i(self.__mapping.get_xmin()+4):
                self.__theta = math.pi-self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("3")
            elif self.__x >= self.__mapping.get_i(self.__mapping.get_xmax()-4):
                self.__theta = math.pi - self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("4")
            else:
                return int("0")
        else:  # original code for ball.py where ball rebounds off edges of screen
            if self.__y >= self.__mapping.get_j(self.__mapping.get_ymin()+4):
                self.__theta = -self.__theta  # Makes angle its negative counterpart to initiate rebound
                self.__x0 = self.__x  # Reinitialize x0 and y0 to x and y values when ball hit the edge
                self.__y0 = self.__y
                return int("2")  # return specific number value when rebounded to help with edge specific game change
                # bottom edge
            elif self.__y <= self.__mapping.get_j(self.__mapping.get_ymax()-4):
                self.__theta = -self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("1")
                # top edge
            elif self.__x <= self.__mapping.get_i(self.__mapping.get_xmin()+4):
                self.__theta = math.pi-self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("3")
                # left edge
            elif self.__x >= self.__mapping.get_i(self.__mapping.get_xmax()-4):
                self.__theta = math.pi - self.__theta
                self.__x0 = self.__x
                self.__y0 = self.__y
                return int("4")
            else:  # if no edge has been touched yet, method returns 0
                return int("0")


def main():
        mapping = Mapping_for_Tkinter(-300, 300, -300, 300, 600)
        root = Tk()
        canvas = Canvas(root, width= mapping.get_width(), height=mapping.get_height(), bg="white")
        parameters = input("Enter velocity  theta (return for default: 500 pixels/s and 30 degrees): ")
        if parameters == "":  # Default values if "enter" on keyboard is inputted
            v = 500
            theta = 30
        else:
            v, theta = parameters.split()
        canvas.pack()
        b = Ball(mapping, canvas, mapping.get_i(0), mapping.get_j(0), v, theta)
        # Create object of class Ball in center of canvas
        b.create_oval()  # Create the ball by calling the method
        t = 0  # real time between event
        t_total = 0  # real total time
        count = 0  # rebound_total=0
        while True:
            t = t+0.01  # real time between events- in second
            t_total = t_total+0.01  # real total time- in second
            side = b.update_xy(t)  # Update ball position and return collision event
            root.update()   # update the graphic (redraw)
            if side != 0:
                count = count+1  # increment the number of rebounds
                t = 0  # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if count == 10: break  # stop the simulation
        print("Total time: %ss" % t_total)
        canvas.pack()
        root.mainloop()


if __name__ == "__main__":
    main()

