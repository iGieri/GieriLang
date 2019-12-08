import operations.stuff as stuff
from classes.variable import Variable

def vo():
    if "=" in stuff.everything[1]:
        operation = stuff.everything[1].split("=")
        if operation[0] in stuff.variables.keys():
            # Here we are checking which operator the coder want to use
            if "+" in operation[1]:
                # Here we create a new instance of Variable overwriting the precedent
                sum = operation[1].split("+")

                totalSum = 0

                for addend in sum:
                    if addend in stuff.variables.keys():
                        if stuff.variables[operation[0]].type == "int":
                            totalSum += int(stuff.variables[addend].value)
                        elif stuff.variables[operation[0]].type == "float":
                            totalSum += float(stuff.variables[addend].value)
                        else:
                            totalSum += stuff.variables[addend].value
                    else:
                        if stuff.variables[operation[0]].type == "int":
                            totalSum += int(addend)
                        elif stuff.variables[operation[0]].type == "float":
                            totalSum += float(addend)
                        else:
                            totalSum += addend

                stuff.variables[operation[0]] = Variable(operation[0], str(totalSum))

