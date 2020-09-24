import math


class Calculator:
    def __init__(self, value):
        self.value = value

    def power(self, *args):
        for degree in args:
            self.value = math.pow(self.value, degree)
        return self

    def root(self, *args):
        for degree in args:
            self.value = math.pow(self.value, 1/degree)
        return self
