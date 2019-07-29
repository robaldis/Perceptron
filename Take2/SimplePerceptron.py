import Perceptron as per
import Training
import pygame
import numpy


WIDTH = 500
HEIGHT = 500
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

P = None
Points = list()


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perceptron Training")
clock = pygame.time.Clock()


def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def make_points(amount):
    for i in range (amount):
        Points.append(Training.Point())

def show_point(point, colour, size):
    px = round(mapFromTo(point.x, -1, 1, 0 , WIDTH))
    py = round(mapFromTo(point.y, -1, 1, HEIGHT, 0))
    pygame.draw.circle(game_display, colour, (px, py), size)

def writeFile(text):    # Write weights to file
    textFile = open("weights.txt", "r+")
    old = textFile.read()
    textFile.seek(0)
    textFile.write(text + old)
    textFile.close()

def train_network():
    meanError = 0

    # for all the points train the network
    for point in Points:
        inputs = [point.x,point.y, point.b]  # Inputs for the network
        guess = P.guess(inputs) # Guess what the value should be

        # Train the network and get the error of the point
        meanError += numpy.absolute(P.train(inputs, point.label))   # get all the error values in a positive value

        if(guess == point.label):   # If it guessed right
            show_point(point, GREEN, 3)
        else:
            show_point(point, RED, 3)

    # Print the mean error to the console
    meanError = meanError / 2
    print("This is the mean error {0}".format(meanError))

    if (meanError == 0): # If it guessed all the points correctly
        text = "{0},{1},{2}\n".format(P.weights[0],P.weights[1],P.weights[2])
        print("The error is\n \t\t{0}\n and the Weights are\n\t\t 1:{1}\n\t\t 2:{2}\n\t\t 3:{3}".format(meanError,P.weights[0],P.weights[1], P.weights[2]))
        writeFile(text)
        quit()
        pygame.quit()

def draw():
    game_display.fill((100,100,100))

    # Show the points on the screen
    for point in Points:
        if (point.label == 1):
            show_point(point, BLACK, 6)
        else:
            show_point(point, WHITE, 6)

    # Train the network
    train_network()
    linex1, liney1, linex2, liney2 = Training.line()
    linex1 = mapFromTo  (linex1, -1, 1, 0, WIDTH)
    linex2 = mapFromTo  (linex2, -1, 1, 0,WIDTH)
    liney1 = mapFromTo  (liney1, -1, 1, HEIGHT, 0)
    liney2 = mapFromTo  (liney2, -1, 1, HEIGHT, 0)
    pygame.draw.line(game_display,BLACK, (linex1,liney1),(linex2,liney2),4)
    #pygame.draw.line(game_display,BLACK, (0,800),(800, 0),4)


    x1 = -1
    y1 = P.guessY(x1)
    x2 = 1
    y2 = P.guessY(x2)
    x1 = mapFromTo  (x1, -1, 1, 0, WIDTH)
    x2 = mapFromTo  (x2, -1, 1, 0,WIDTH)
    y1 = mapFromTo  (y1, -1, 1, HEIGHT, 0)
    y2 = mapFromTo  (y2, -1, 1, HEIGHT, 0)
    pygame.draw.line(game_display,BLACK, (x1,y1),(x2,y2),4)


    # Update the screen
    pygame.display.update()

def main():
    global P
    make_points(500)    # Make 100 points
    P = per.Perceptron(3, 0.0001)
    # Loop until we press quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Draw to the canvas
        draw()
        # Keep the refresh rate to 60
        clock.tick(5)

# Start the program if it is the main prokgram
if (__name__ == "__main__"):
    main()
