class Addition:
    def __init__(self, f, s):              # parameterized constructor
        self.first = f
        self.second = s

    def calculate(self):
        print(self.first + self.second)

obj = Addition(1000, 2000)                         # Invoking parameterized constructor
obj.calculate()                        # perform addition
