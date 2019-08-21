import math

class RpnCalculator:
    def __init__(self):
        self.values = []

    def push(self, *args):
        for arg in args:
            self.values.append(arg)

    def pop(self):
        return self.values.pop()

    def result(self):
        return self.values[-1]

    def stack(self):
        return self.values

    def clear(self):
        self.values.clear()

    def add(self):
        i = self.values.pop()
        j = self.values.pop()
        r = i + j
        self.values.append(r)

    def sub(self):
        i = self.values.pop()
        j = self.values.pop()
        r = j - i
        self.values.append(r)

    def mul(self):
        i = self.values.pop()
        j = self.values.pop()
        r = i*j
        self.values.append(r)

    def div(self):
        i = self.values.pop()
        j = self.values.pop()
        r = j / i
        self.values.append(r)

    def sqrt(self):
        i = self.values.pop()
        r = math.sqrt(i)
        self.values.append(r)
