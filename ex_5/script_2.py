from script_1 import Complex

cmp_1 = Complex(12, 4)
cmp_2 = Complex(2, 44)

equation = input("Enter complex equation: ")
complex_1 = Complex(complex(equation.split(" ")[0]).real, complex(equation.split(" ")[0]).imag)
complex_2 = Complex(complex(equation.split(" ")[2]).real, complex(equation.split(" ")[2]).imag)

if equation.split(" ")[1] == "+":
    Complex.add(complex_1, complex_2).show_complex()
elif equation.split(" ")[1] == "-":
    Complex.subtract(complex_1, complex_2).show_complex()
elif equation.split(" ")[1] == "*":
    Complex.multiply(complex_1, complex_2).show_complex()
elif equation.split(" ")[1] == "/":
    Complex.divide(complex_1, complex_2).show_complex()
else:
    print("Incorrect format of equation")
