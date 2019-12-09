import operations.stuff as stuff

def if_function():
    if "->" in stuff.everything[1]:
        condition = stuff.everything[1].split("->")
        if "==" in condition[0]:
            equals = condition[0].split("==")
            if (equals[0] in stuff.variables.keys() and equals[1] in stuff.variables.keys()) and (stuff.variables[equals[0]].value == stuff.variables[equals[1]].value):
                return 0
            else:
                if stuff.numOfCondition < int(condition[1]):
                    stuff.ifFlag = True
                else:
                    stuff.ifFlag = False
                    return 0
                stuff.numOfCondition = stuff.numOfCondition + 1

