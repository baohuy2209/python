class Complex_number:
    def __init__(self, a, b):
        self.real = a
        self.virtual = b

    def addition(self, complex_number2):
        self.real += complex_number2.real
        self.virtual += complex_number2.virtual
        print("Result: " + str(self.real) + " + " + str(self.virtual) + "i")
