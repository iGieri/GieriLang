import operations.stuff as stuff
from classes.variable import Variable


def sum(operation):
    if "+" in operation[1]:
        # Here we create a new instance of Variable overwriting the precedent
        sumv = operation[1].split("+")
        totalSum = 0
        for addend in sumv:
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


def difference(operation):
    if "-" in operation[1]:
        # Here we create a new instance of Variable overwriting the precedent
        differencev = operation[1].split("-")
        totalDifference = 0
        for minuend in differencev:
            if minuend in stuff.variables.keys():
                if stuff.variables[operation[0]].type == "int":
                    totalDifference -= int(stuff.variables[minuend].value)
                elif stuff.variables[operation[0]].type == "float":
                    totalDifference -= float(stuff.variables[minuend].value)
                else:
                    totalDifference -= stuff.variables[minuend].value
            else:
                if stuff.variables[operation[0]].type == "int":
                    totalDifference -= int(minuend)
                elif stuff.variables[operation[0]].type == "float":
                    totalDifference -= float(minuend)
                else:
                    totalDifference -= minuend
        stuff.variables[operation[0]] = Variable(operation[0], str(totalDifference))


def multiplication(operation):
    if "*" in operation[1]:
        # Here we create a new instance of Variable overwriting the precedent
        multiplicationv = operation[1].split("*")
        totalMultiplication = 0
        for multiple in multiplicationv:
            if multiple in stuff.variables.keys():
                if stuff.variables[operation[0]].type == "int":
                    totalMultiplication *= int(stuff.variables[multiple].value)
                elif stuff.variables[operation[0]].type == "float":
                    totalMultiplication *= float(stuff.variables[multiple].value)
                else:
                    totalMultiplication *= stuff.variables[multiple].value
            else:
                if stuff.variables[operation[0]].type == "int":
                    totalMultiplication *= int(multiple)
                elif stuff.variables[operation[0]].type == "float":
                    totalMultiplication *= float(multiple)
                else:
                    totalMultiplication *= multiple
        stuff.variables[operation[0]] = Variable(operation[0], str(totalMultiplication))


def division(operation):
    if "/" in operation[1]:
        # Here we create a new instance of Variable overwriting the precedent
        divisionv = operation[1].split("/")
        # for dividend in divisionv:
        if divisionv[0] in stuff.variables.keys() and divisionv[1] in stuff.variables.keys():
            if stuff.variables[operation[0]].type == "int":
                totalDivision = int(stuff.variables[divisionv[0]].value) / int(stuff.variables[divisionv[1]].value)
            elif stuff.variables[operation[0]].type == "float":
                totalDivision = float(stuff.variables[divisionv[0]].value) / float(stuff.variables[divisionv[1]].value)
            else:
                totalDivision = stuff.variables[divisionv[0]].value / stuff.variables[divisionv[1]].value
        elif divisionv[0] in stuff.variables.keys() and not divisionv[1] in stuff.variables.keys():
            if stuff.variables[operation[0]].type == "int":
                totalDivision = int(stuff.variables[divisionv[0]].value) / int(divisionv[1])
            elif stuff.variables[operation[0]].type == "float":
                totalDivision = float(stuff.variables[divisionv[0]].value) / float(divisionv[1])
            else:
                totalDivision = stuff.variables[divisionv[0]].value / divisionv[1]
        elif not divisionv[0] in stuff.variables.keys() and divisionv[1] in stuff.variables.keys():
            if stuff.variables[operation[0]].type == "int":
                totalDivision = int(divisionv[0]) / int(stuff.variables[divisionv[1]].value)
            elif stuff.variables[operation[0]].type == "float":
                totalDivision = float(stuff.variables[divisionv[0]].value) / float(divisionv[1])
            else:
                totalDivision = stuff.variables[divisionv[0]].value / divisionv[1]
        stuff.variables[operation[0]] = Variable(operation[0], str(totalDivision))


def vo():
    if "=" in stuff.everything[1]:
        operation = stuff.everything[1].split("=")
        if operation[0] in stuff.variables.keys():
            # Here we are checking which operator the coder want to use
            # Here we create a new instance of Variable overwriting the precedent
            if "+" in operation[1]:
                sum(operation)
            elif "-" in operation[1]:
                difference(operation)
            elif "*" in operation[1]:
                multiplication(operation)
            elif "/" in operation[1]:
                division(operation)

