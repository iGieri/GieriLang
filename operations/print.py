import operations.stuff as stuff

def printOP():
    if stuff.everything[1] in stuff.variables.keys():
        print(stuff.variables[stuff.everything[1]].value)
    else:
        print(stuff.everything[1])