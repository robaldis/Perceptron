import random

# The activation function
def sign(n):
    if (n>= 0):
        return 1
    else:
        return -1

class Perceptron(object):
#Variables
    weights = list()

    def __init__(self):
        #init weights randomly
        for i in range(len(self.weights)):
            self.weights[i] = random.random()


    def guess(self,inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i]*self.weights[i]
        output = sign(sum)
        return output
