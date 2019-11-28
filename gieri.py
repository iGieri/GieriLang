# Global variables
FILE = "main.gieri"  # Let's define our source code TODO: define this global variable as argument

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
            print(variables[everything[1]])
        else:
            print(everything[1])
    # Code to use variable
    elif everything[0] == "var":
        # Let's Check if it's an empty value
        full = False
        for char in everything[1]:
            if char == "=":
                full = True
        if full:
            var = everything[1].split("=")
            variables[var[0]] = var[1]
        else:
            type = everything[1].split("@")
            try:
                if type[1] == "int":
                    variables[type[0]] = 0
                elif type[1] == "float":
                    variables[type[0]] = 0.0
                elif type[1] == "string":
                    variables[type[0]] = ""
                else:
                    print(f"Error at Line {i}. {type[1]} is not a valid type.")
                    break
            except IndexError:
                print(f"Error at Line {i}. You must declare a valid type or a value of a variable")
                break
    else:
        print(f"Error at Line {i}. {everything[0]} is not a valid operation.")
        break

