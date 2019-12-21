from classes.variable import Variable


class Array(Variable):

    def __init__(self, name, value, length):
        super().__init__(name, value)
        self.length = length

    


