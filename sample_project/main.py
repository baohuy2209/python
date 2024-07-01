from file.router.complex_number import Complex_number
from operation import Operation

if __name__ == "__main__":
    op = Operation(5, 6)
    print(op.addition())
    print(op.subtraction())
    complex_number1 = Complex_number(3, 4)
    complex_number2 = Complex_number(4, 5)
    complex_number1.addition(complex_number2)
