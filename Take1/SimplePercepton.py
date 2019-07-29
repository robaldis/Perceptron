from tkinter import *
import random as rnd
import numpy


#SUM [x0*w0 =x1*w1]

#ACTIVATION     => SIGN(n)
#   FUNTION     N > 0 = 1
#               N < 0 = -1
# Setting up global variables
p = 0
points = list()
inputs = list()
inputs = list()
window = Tk()

# Setting up the window
window.title("Graph")
# Setting up the canvas H-400 W-400
canvas = Canvas(window, width=400, height=400, background="grey")
canvas.pack()

#CODE
def makePoints():
    global p
    # Make all the points and add them to an array
    for i in range(1000):
        points.append(Point())
    p = Perceptron()


# The activation function
def sign(n):
    if (n>= 0):
        return 1
    else:
        return -1



def main():
    makePoints()
    window.after(0,train())



def train():
    meanError = 0
    count = 0

    canvas.delete("all")    #Deletes all of the things on the screen

    line = canvas.create_line(0, 0, 400, 400, width = 2)    #Creates a line to see where it is calssifying

    # Show all the points
    for i in range(len(points)):
        points[i].show()

    # for all the points train the network
    for i in range(len(points)):
        inputs = [points[i].x,points[i].y, 1]  # Inputs for the network
        count += 1

        guess = p.guess(inputs) # Guess what the value should be

        meanError += numpy.absolute(p.train(inputs, points[i].label))   # get all the error values in a positive value

        if(guess == points[i].label):   # If it guessed right
            canvas.create_oval(points[i].x - 3,points[i].y - 3,points[i].x + 3,points[i].y + 3, fill = "blue")

    print("This is the mean error {0}".format(meanError))
    meanError = (meanError / count) / 2

    if (meanError == 0): # If it guessed all the points correctly
        text = "{0},{1}\n".format(p.weights[0],p.weights[1])
        print("The error is\n \t\t{0}\n and the Weights are\n\t\t 1:{1}\n\t\t 2:{2}".format(meanError,p.weights[0],p.weights[1]))
        writeFile(text)
        window.destroy()
    else:
        window.after(2000,train) # If wrong keep going

def writeFile(text):    # Write weights to file
    textFile = open("weights.txt", "r+")
    old = textFile.read()
    textFile.seek(0)
    textFile.write(text + old)
    textFile.close()

class Point(object):
    x = 0
    y = 0
    label = 0

    # __init__
    # Starts up every time that you make a new object
    # this sets up the object and all the variables
    # StartUp code
    def __init__(self):
        self.x = rnd.randint(0 ,400)
        self.y = rnd.randint(0 ,400)

        # give each point a label
        #depending on where it is on the grid
        if (self.x > self.y):
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
        canvas.create_oval(self.x-3,self.y-3,self.x+3,self.y+3,fill = colour)



class Perceptron(object):
#Variables
    weights = list()
    lr = 0.1

    def __init__(self):
        #init weights randomly
        for i in range(1):
            #self.weights.append(rnd.random())
            self.weights.append(0)
            self.weights.append(0)


        self.lr = 0.0001


    def guess(self,inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i]*self.weights[i]
        output = sign(sum)
        return output

    # Tune all the weights
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        #print(error)
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.lr

        return error


window.after(0, main)
window.mainloop()
