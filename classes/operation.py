import operations.stuff as stuff

class Operation:
    def __init__(self, name, function):
        self.name = name
        self.function = lambda: function()
    def start(self, everything):
        if everything[0] == self.name:
            stuff.commandFlag = True
            self.function()
        else:
            stuff.commandFlag = False

