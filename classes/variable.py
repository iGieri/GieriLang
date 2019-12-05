def isfloat(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.type = self.findType()

    def findType(self):
        if str(self.value).isdecimal():
            return "int"
        elif isfloat(str(self.value)):
            return "float"
        else:
            return "string"
    def setValue(self):
        if self.type == "int":
            self.value = int(self.value)
        elif self.type == "float":
            self.value = float(self.value)
        else:
            self.value

