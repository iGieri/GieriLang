
def isfloat(element):
    """
    This function check if a string is convertable to float
    """
    try:
        float(element)
        return True
    except ValueError:
        return False

class Variable:
    """
    This class define a new variable
    """
    def __init__(self, name, value):
        self.name = name
        temp = value
        self.type = self.findType(temp)
        self.value = self.setValue(temp)

    def findType(self, value):
        """
        This method return the type of variable
        """
        if str(value).isdecimal():
            return "int"
        elif isfloat(str(value)):
            return "float"
        else:
            return "string"
    
    def setValue(self, value):
        """
        This method return the value of variable converted in the correct type
        """
        if self.type == "int":
            return int(value)
        elif self.type == "float":
            return float(value)
        else:
            return str(value)
