import types

class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        """Default method that prints the name of the strategy being used"""
        print("{} is used.".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))

# Creating default strategy
s0 = Strategy()
# Executing default strategy
s0.execute()

# First variation of default strategy
s1 = Strategy(strategy_one)
s1.name = "Strategy 1"
s1.execute()

# Second variation
s2 = Strategy(strategy_two)
s2.name = "Strategy 2"
s2.execute()
