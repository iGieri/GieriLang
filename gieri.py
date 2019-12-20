"""
GieriLang Interpreter,

Written by Federico Gerardi aka Gieri

MIT License
"""


import sys

from classes.operation import Operation  # Let's import the classe for operations
from operations.print import printOP  # Let's import print function
from operations.comment import comment  # Let's import comment function
from operations.var import var  # Let's import var function
from operations import stuff  # Module for changing data with other files
from operations.vo import vo  # Let's import vo function
from operations.if_function import if_function  # Let's import if function
from operations.input import input_function  # Let's import input function

# Global variable
try:
    FILE = sys.argv[1]  # Let's define our source code
except:
    FILE = "main.gieri"

# In this part we are reading the file
codeFile = open(FILE, "r")
code = codeFile.read()
codeFile.close()

lines = code.split("\n")  # We are splitting the lines of our source code in an array

i = 0  # Init of the i variable

stuff.numOfCondition = 0

stuff.numOfElse = 0

stuff.nIf = 0

stuff.nElse = 0

stuff.ifFlag = False

stuff.elseFlag = True

stuff.lines = lines

variables = {}  # The register of all variable

operations = [
    Operation("//", lambda: comment()),
    Operation("print", lambda: printOP()),
    Operation("var", lambda: var()),
    Operation("vo", lambda: vo()),
    Operation("if", lambda: if_function()),
    Operation("input", lambda: input_function()),
]



# In this for we are reading line per line all the source code
for line in lines:
    i += 1
    everything = line.split(":")  # We are splitting the kind of operation from the operation

    stuff.everything = everything
    stuff.variables = variables

    if (stuff.ifFlag and stuff.numOfCondition < stuff.nIf) or ((not stuff.elseFlag) and stuff.numOfElse < stuff.nElse):
        stuff.numOfCondition += 1
        continue

    for operation in operations:
        operation.start(everything)
