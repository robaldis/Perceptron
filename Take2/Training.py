import random as rnd

def f(x):
    return 9 * x

def line():
    x1 = -1
    y1 = f(x1)
    x2 = 1
    y2 = f(x2)
    return x1,y1,x2,y2

class Point(object):
    x = 0
    y = 0
    label = 0

    # __init__
    # Starts up every time that you make a new object
    # this sets up the object and all the variables
    # StartUp code
    def __init__(self):
        self.x = rnd.uniform(-1.0 ,1.0)
        self.y = rnd.uniform(-1.0 ,1.0)
        self.b = 1

        # give each point a label
        #depending on where it is on the grid
        if (f(self.x) > self.y):
            self.label = 1
        else:
            self.label = -1

    # Show the point on the canvas
    def show(self):
        # change the colour depending on the label
        if (self.label == 1):
            colour = "red"      # Red = Top
        else:
            colour = "green"    # Green = Bottom

        # Create an oval at each of the points, size 6
        #return(self.x-3,self.y-3,self.x+3,self.y+3,fill = colour)
