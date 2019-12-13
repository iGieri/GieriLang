import operations.stuff as stuff
from classes.variable import Variable


def input_function():
    if stuff.everything[1] in stuff.variables.keys():
        stuff.variables[stuff.everything[1]] = Variable(stuff.everything[1], input())
    else:
        print("Input Error")