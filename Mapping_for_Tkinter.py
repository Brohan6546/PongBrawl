from tkinter import *
from math import *

class Mapping_for_Tkinter:
    """ class tkinter_mapping to create a mapping between a new math
    coordinate system with (xmin,ymin) at the bottom left (xmax,ymax at the top right)
    and the traditional tkinter coordinate system """
    def __init__(self,xmin,xmax,ymin,ymax,width):
        self.set_xmin(xmin)
        self.set_xmax(xmax)
        self.set_ymin(ymin)
        self.set_ymax(ymax)
        self.set_width(width)
        self.__set_height() #initialize variable __height

    ##### get methods for instance attributes
    def get_xmin(self):
        return self.__xmin
    def get_xmax(self):
        return self.__xmax
    def get_ymin(self):
        return self.__ymin
    def get_ymax(self):
        return self.__ymax
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    
    ##### set methods for instance attributes
    def set_xmin(self, xmin):
        self.__xmin=xmin        
    def set_xmax(self,xmax): #set xmax with property
        while xmax<self.__xmin:
            xmin,xmax=map(float,input("Your xmax is invalid (xmax<=xmin), Re-Enter correct [xmin,xmax]: ").split())
            self.__xmin=xmin
        self.__xmax=xmax
    def set_ymin(self,ymin):
        self.__ymin=ymin
    def set_ymax(self,ymax):  #set ymax with property
        while ymax<=self.__ymin:
            ymin,ymax=map(float,input("Your ymax is invalid (ymax<=ymin), Re-Enter correct [ymin,ymax]: ").split())
            self.__ymin=ymin
        self.__ymax=ymax
    def set_width(self,width):
        self.__width=width
    def __set_height(self): # height is calculated privately and should be an integer
        self.__height=int(self.__width*(self.__ymax-self.__ymin)/(self.__xmax-self.__xmin))
    
    ##### instance methods
        
    #get x math coordinate from i tkinter coordinate     
    def get_x(self,i):
        return self.__xmin + (self.__xmax - self.__xmin) * i / (self.__width-1)

    #get y math coordinate from j tkinter coordinate    
    def get_y(self,j):
        return self.__ymax - (self.__ymax - self.__ymin) * j / (self.__height-1)
    
    #get i tkinter coordinate (int) from x (float)    
    def get_i(self,x):
        return int((x-self.__xmin)*(self.__width-1)/(self.__xmax - self.__xmin))
    
    #get j tkinter coordinate (int) from y (float) 
    def get_j(self,y):
        return int((self.__ymax-y)*(self.__height-1)/(self.__ymax - self.__ymin))

    ## get dimension of Lx
    #def get_Lx(self):
    #    return self.__xmax-self.__xmin
    
    ## get dimension of Ly
    #def get_Ly(self):
    #    return self.__ymax-self.__ymin
    ## str method
    #def __str__(self):
    #    result="Mapping created between x=[%s,%s] y=[%s,%s] math => (%s,%s) tkinter"%(self.__xmin,self.__xmax,self.__ymin,self.__ymax,self.__width,self.__height)
    #    return result

    
    

def main(): 
    """ TESTING MAPPING using FUNCTION PLOTTER """

    #### formula input
    formula=input("Enter math formula (using x variable): ")

    #### coordinate input
    coord=input("Enter xmin,xmax,ymin,ymax (return for default -5,5,-5,5): ")
    if coord=="":
        xmin,xmax=-5,5
        ymin,ymax=-5,5
    else:
        #split the string/create list of string
        xmin,xmax,ymin,ymax=coord.split()

    #### instantiate a mapping
    width=800
    m=Mapping_for_Tkinter(float(xmin),float(xmax),float(ymin),float(ymax),width) 

    #### instantiate a tkinter window 
    window = Tk() 
    canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
    canvas.pack()

    #### create axis
    if m.get_xmin()<0 and m.get_xmax()>0:
        canvas.create_line(m.get_i(0.0),m.get_j(m.get_ymin()),m.get_i(0.0),m.get_j(m.get_ymax()))
    if m.get_ymin()<0 and m.get_ymax()>0:
        canvas.create_line(m.get_i(m.get_xmin()),m.get_j(0.0),m.get_i(m.get_xmax()),m.get_j(0.0))
    
    #### plot function    
    for i in range(width):
        x=m.get_x(i)
        y=eval(formula)
        canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="blue")

    window.mainloop() # wait until the window is closed


if __name__=="__main__":
    main()
