import numpy
import random as rnd


# The activation function
def sign(n):
    if (n>= 0):
        return 1
    else:
        return -1


class Perceptron(object):
#Variables
    weights = list()

    def __init__(self,numWeights=3,lr=0.1):
        #init weights randomly
        for i in range((numWeights)):
            self.weights.append(rnd.random())
        self.lr = lr


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

    def guessY(self, x):
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]



        return -(w2/w1) - (w0/w1) * x
