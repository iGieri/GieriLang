import operations.stuff as stuff
from classes.variable import Variable

def vo():
    if "=" in stuff.everything[1]:
        operation = stuff.everything[1].split("=")
        if operation[0] in stuff.variables.keys():
            # Here we are checking which operator the coder want to use
            if "+" in operation[1]:
                # Here we create a new instance of Variable overwriting the precendt
                sum = operation[1].split("+")
                if stuff.variables[operation[0]].type == "int":
                    stuff.variables[operation[0]] = Variable(operation[0], str(int(sum[0]) + int(sum[1])))
                elif stuff.variables[operation[0]].type == "float":
                    stuff.variables[operation[0]] = Variable(operation[0], str(float(sum[0]) + float(sum[1])))
                else:
                    stuff.variables[operation[0]] = Variable(operation[0], str(sum[0] + sum[1]))