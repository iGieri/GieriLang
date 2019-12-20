import operations.stuff as stuff


def if_function():
    stuff.isElse = False
    if "->" in stuff.everything[1]:
        condition = stuff.everything[1].split("->")
        if "," in condition[1]:
            elsenum = condition[1].split(",")
            stuff.isElse = True
            stuff.nElse = int(elsenum[1])
        if stuff.isElse:
            stuff.nIf = int(elsenum[0])
        else:
            stuff.nIf = int(condition[1])
        if "==" in condition[0]:
            equals = condition[0].split("==")
            if ((equals[0] in stuff.variables.keys()) and (equals[1] in stuff.variables.keys())) and (stuff.variables[equals[0]].value == stuff.variables[equals[1]].value):
                return 0
            elif (equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value == float(equals[1])):
                return 0
            elif (not equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (float(equals[0]) == stuff.variables[equals[1]].value):
                return 0
            elif (not equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (float(equals[0]) == float(equals[1])):
                return 0
            else:
                stuff.ifFlag = True
        elif ">=" in condition[0]:
            equals = condition[0].split(">=")
            if (equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value >= stuff.variables[equals[1]].value):
                return 0
            elif (equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value >= float(equals[1])):
                return 0
            elif (not equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (float(equals[0]) >= stuff.variables[equals[1]].value):
                return 0
            elif (not equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (float(equals[0]) >= float(equals[1])):
                return 0
            else:
                stuff.ifFlag = True
        elif "<=" in condition[0]:
            equals = condition[0].split("<=")
            if (equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value <= stuff.variables[equals[1]].value):
                return 0
            elif (equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value <= float(equals[1])):
                return 0
            elif (not equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (float(equals[0]) <= stuff.variables[equals[1]].value):
                return 0
            elif (not equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (float(equals[0]) <= float(equals[1])):
                return 0
            else:
                stuff.ifFlag = True
        elif ">" in condition[0]:
            equals = condition[0].split(">")
            if (equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value > stuff.variables[equals[1]].value):
                return 0
            elif (equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value > float(equals[1])):
                return 0
            elif (not equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (float(equals[0]) > stuff.variables[equals[1]].value):
                return 0
            elif (not equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (float(equals[0]) > float(equals[1])):
                return 0
            else:
                stuff.ifFlag = True
        elif "<" in condition[0]:
            equals = condition[0].split("<")
            if (equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value < stuff.variables[equals[1]].value):
                return 0
            elif (equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value < float(equals[1])):
                return 0
            elif (not equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (float(equals[0]) < stuff.variables[equals[1]].value):
                return 0
            elif (not equals[0] in stuff.variables.keys() and not equals[1] in stuff.variables.keys()) and (float(equals[0]) < float(equals[1])):
                return 0
            else:
                stuff.ifFlag = True
