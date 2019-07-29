# Perceptron
Perceptron machine learning algoorithm to catogarise data on a 2D graph.
It takes X and Y coordinates that have been catagorised to be above the line or bellow the line. The perceptron will then tae a guess
where it thinks the line is and gets the error on how accurate it is and changes the weights to make it correct.

## usage
To use the python program you need to run the SimplePerceptron.py file and watch it run
make sure that pygames is installed before you run.

To cahnge the direction of the line go into Training.py and at the top in f(x) function cahnge the return to any fomula for a line,
the graph is mapped out between -1 and 1 so DON'T have anything bigger than + 1 at the end of the return otherwise you wont see the line
```python
# Correct
def f(x):
  return 3 * x + 0.5
# Incorrect
def f(x):
  return 3* x + 2
```

