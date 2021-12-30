from Mapping_for_Tkinter import *
from tkinter import *


class Racket:
    def __init__(self, mapping,canvas, x, y):
        self.set_mapping(mapping)
        self.set_canvas(canvas)
        self.set_x(x)
        self.set_y(y)
    # Use get and set methods to get private attributes like in mapping for tkinter
    def get_mapping(self):
        return self.__mapping

    def get_canvas(self):
        return self.__canvas

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_mapping(self,mapping):
        self.__mapping = mapping

    def set_canvas(self, canvas):
        self.__canvas = canvas

    def set_x(self, x):
        self.__x = x

    def set_y(self,y):
        self.__y = y

    def create_rectangle(self):
        rack = self.__canvas.create_rectangle(self.__x-30,self.__y-5,self.__x+30,self.__y+5,fill="red")
        return rack

    # used in game 2 to signify which racket can be controlled
    def activate(self, rack):
        return self.__canvas.itemconfig(rack, fill="black")

    def deactivate(self, rack):
        return self.__canvas.itemconfig(rack, fill="white")

    def shift_left(self,rack):
        # uses coords method to get and compare left and right side of racket to window bounds, stop if there
        points = self.__canvas.coords(rack)
        if points[0] > self.__mapping.get_i(-300):
            self.__canvas.move(rack, -30, 0)

    def shift_right(self,rack):
        points = self.__canvas.coords(rack)
        if points[2] < self.__mapping.get_i(300):
            self.__canvas.move(rack, 30, 0)
def main():
    m = Mapping_for_Tkinter(-300,300,-300,300,600) # get new mapping with tkinter window
    root = Tk()
    c = Canvas(root, width=m.get_width(), height=m.get_height(), bg="white")  # create canvas window
    r = Racket(m,c, m.get_i(0), m.get_j(-300))  # create object of class Racket using external mapping
    pong = r.create_rectangle()  # Create racket
    c.bind("<Left>", lambda e: r.shift_left(pong))  # bind left and right mouse buttons to methods that move racket
    c.bind("<Right>",lambda e: r.shift_right(pong))
    c.focus_set()
    c.pack()
    root.mainloop()


if __name__=="__main__":
    main()


