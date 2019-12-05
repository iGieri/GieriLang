# TODO: Trasformare le operazioni in classi

from classes.variable import Variable  # Let's import the class for variable

# Global variables
FILE = "main.gieri"  # Let's define our source code TODO: definire questa variabile globale come argomento del programma

# In this part we are reading the file
codeFile = open(FILE, "r")
code = codeFile.read()
codeFile.close()

lines = code.split("\n")  # We are splitting the lines of our source code in an array

i = 0  # Init of the i variable

variables = {}  # The register of all variable

# In this for we are reading line per line all the source code
for line in lines:
    i += 1
    everything = line.split(":")  # We are splitting the kind of operation from the operation
    # Code to define comments with: //:
    if everything[0] == "//" or everything[0] == "":
        continue
    # Code to define print function
    elif everything[0] == "print":
        if everything[1] in variables.keys():
            print(variables[everything[1]].value)
        else:
            print(everything[1])
    # Code to use variable
    elif everything[0] == "var":
        # Let's Check if it's an empty value
        full = False
        if "=" in everything[1]:
            full = True
        if full:
            # if it's a full variable we create a new instance of Variable class with the value after =
            var = everything[1].split("=")
            variables[var[0]] = Variable(var[0], var[1])

        else:
            # else we are defining only the type of the Variable
            type = everything[1].split("@")
            try:
                if type[1] == "int":
                    variables[type[0]] = Variable(type[0], "0")
                elif type[1] == "float":
                    variables[type[0]] = Variable(type[0], "0.0")
                elif type[1] == "string":
                    variables[type[0]] = Variable(type[0], "")
                else:
                    print(f"Error at Line {i}. {type[1]} is not a valid type.")
                    break
            except IndexError:
                print(f"Error at Line {i}. You must declare a valid type or a value of a variable")
                break
    
    # Here we are introducing the concept of operations between Variables
    elif everything[0] == "vo":
        # Now we are checking if all the code is OK
        if "=" in everything[1]:
            operation = everything[1].split("=")
            if operation[0] in variables.keys():
                # Here we are checking which operator the coder want to use
                if "+" in operation[1]:
                    # Here we create a new instance of Variable overwriting the precendt
                    sum = operation[1].split("+")
                    if variables[operation[0]].type == "int":
                        variables[operation[0]] = Variable(operation[0], str(int(sum[0]) + int(sum[1])))
                    elif variables[operation[0]].type == "float":
                        variables[operation[0]] = Variable(operation[0], str(float(sum[0]) + float(sum[1])))
                    else:
                        variables[operation[0]] = Variable(operation[0], str(sum[0] + sum[1]))

        else:
            print(f"Error at Line {i}. You must use = for variable assignament")
            break
    else:
        print(f"Error at Line {i}. {everything[0]} is not a valid operation.")
        break

