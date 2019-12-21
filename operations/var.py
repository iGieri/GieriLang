from classes.variable import Variable
import operations.stuff as stuff

def var():
    # Let's Check if it's an empty value
    full = False
    if "=" in stuff.everything[1]:
        full = True
    if full:
        # if it's a full variable we create a new instance of Variable class with the value after =
        var = stuff.everything[1].split("=")
        stuff.variables[var[0]] = Variable(var[0], var[1])

    else:
        # else we are defining only the type of the Variable
        type = stuff.everything[1].split("@")
        if type[1] == "int":
            stuff.variables[type[0]] = Variable(type[0], "0")
        elif type[1] == "float":
            stuff.variables[type[0]] = Variable(type[0], "0.0")
        elif type[1] == "string":
            stuff.variables[type[0]] = Variable(type[0], "")
