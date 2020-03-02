"""
GieriLang Interpreter,

Written by Federico Gerardi aka Gieri

MIT License
"""

#  TODO Rimettere gli errori - Work In Progress

import sys  # System Library
import platform  # OS Library

from classes.operation import Operation  # Let's import the classe for operations
from operations.print import printOP  # Let's import print function
from operations.comment import comment  # Let's import comment function
from operations.var import var  # Let's import var function
from operations import stuff  # Module for changing data with other files
from operations.vo import vo  # Let's import vo function
from operations.if_function import if_function  # Let's import if function
from operations.input import input_function  # Let's import input function
from operations.arr import arr  # Let's import the array declaretion function
from operations.for_function import for_function  # Let's import for function
from operations.nothing import nothing  # Let's import the nothing function

VERSION = "0.1-alpha"
OS = platform.system()

# Global variable
try:
    FILE = sys.argv[1]  # Let's define our source code
except:
    print(f"GieriLang Interpreter Version: {VERSION} on {OS}")
    sys.exit()

# In this part we are reading the file
try:
    codeFile = open(FILE, "r")
    code = codeFile.read()
    codeFile.close()
except FileNotFoundError:
    raise FileNotFoundError("This file doesn't exist !")

lines = code.split("\n")  # We are splitting the lines of our source code in an array

i = 0  # Init of the i variable

definitveElseFlag = False

stuff.isElse = False

stuff.numOfCondition = 0

stuff.numOfElse = 0

stuff.nIf = 0

stuff.nElse = 0

stuff.ifFlag = False

stuff.elseFlag = False

stuff.lines = lines

stuff.commandFlag = True

variables = {}  # The register of all variable

operations = [
    Operation("", lambda: nothing()),
    Operation("//", lambda: comment()),
    Operation("print", lambda: printOP()),
    Operation("var", lambda: var()),
    Operation("vo", lambda: vo()),
    Operation("if", lambda: if_function()),
    Operation("input", lambda: input_function()),
    Operation("arr", lambda: arr()),
    Operation("for", lambda: for_function())
]

# In this for we are reading line per line all the source code
for line in lines:
    i += 1
    everything = line.split(":")  # We are splitting the kind of operation from the operation

    stuff.everything = everything
    stuff.variables = variables

    if stuff.ifFlag and stuff.numOfCondition < stuff.nIf:
        stuff.numOfCondition += 1
        continue

    if (not stuff.ifFlag) and stuff.numOfCondition < stuff.nIf:
        stuff.numOfCondition += 1
        definitveElseFlag = True
        pass
    elif not stuff.numOfCondition < stuff.nIf and stuff.isElse and definitveElseFlag:
            stuff.elseFlag = True

    if stuff.elseFlag and stuff.numOfElse < stuff.nElse:
        stuff.numOfElse += 1
        continue

    for operation in operations:
        operation.start(everything)
        if not stuff.commandFlag:
            break

    if stuff.commandFlag:
        raise Exception(f"The operation you wrote in line {i} doesn't exist !")

