from classes.array import Array
import operations.stuff as stuff
from classes.variable import isfloat
import sys


#  TODO: Mettere la possibilità di dichiarare tutto l'array su una sola riga
#  TODO: Mettere la possibilità di inserire come input l'array

def arr():
    if "->" in stuff.everything[1]:
        array = stuff.everything[1].split("->")
        if not(array[0] in stuff.variables.keys()):
            # Array Declaretion
            stuff.variables[array[0]] = Array(array, [0]*int(array[1]), array[1])
        elif "=" in stuff.everything[1]:
            equals = stuff.everything[1].split("=")
            arrayN = equals[0].split("->")
            if int(arrayN[1]) > int(stuff.variables[arrayN[0]].length) or int(arrayN[1]) < 0:
                raise IndexError("The index of the array that you're trying to assign the value doesn't exist !")
                sys.exit()
            if "->" in stuff.everything[1]:
                if equals[1].isdecimal():
                    stuff.variables[arrayN[0]].value[int(arrayN[1])] = int(equals[1])
                elif isfloat(equals[1]):
                    stuff.variables[arrayN[0]].value[int(arrayN[1])] = float(equals[1])
                else:
                    stuff.variables[arrayN[0]].value[int(arrayN[1])] = equals[1]

