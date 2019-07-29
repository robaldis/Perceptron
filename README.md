# Perceptron
Perceptron machine learning algorithm to categories data on a 2D graph.
It takes X and Y coordinates that have been categorised to be above the line or bellow the line. The perceptron will then the a guess
where it thinks the line is and gets the error on how accurate it is and changes the weights to make it correct.

## what's here
1. take 1 was my first attempt to make a perceptron, it used tkinter to show the window so if you are using it you need tkinter installed.
it is all in one file and it is a bit confusing

2. take 2 was a refactoring of the code to make it work with pygames as well as separating out the training class and the perceptron class

## usage
To use the python program you need to run the SimplePerceptron.py file and watch it run
make sure that pygames is installed before you run.

To change the direction of the line go into Training.py and at the top in f(x) function change the return to any formula for a line,
the graph is mapped out between -1 and 1 so DON'T have anything bigger than + 1 at the end of the return otherwise you wont see the line
```python
# Correct
def f(x):
  return 3 * x + 0.5
# Incorrect
def f(x):
  return 3* x + 2
```
