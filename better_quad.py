# Redo the quadratic equation solver, but account for imaginary solutions.
import math

a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

discriminant = b * b - 4 * a * c
if discriminant == 0:  (#Condition   == is a comparison operators one = means to assign a variable to something)
    # One solution: -b/2a
    x1 = -b / (2 * a)
    print("There is one solution: x = {0}".format(x1))
elif discriminant < 0:
    # No real solutions    #elif stands for else if try the next elif statement 
    print("There are no real solutions.")
else:
    # Two solutions
    discr_sqrt = math.sqrt(discriminant)
    x1 = (-b + discr_sqrt) / (2 * a)
    x2 = (-b - discr_sqrt) / (2 * a)
    print("There are two solutions: x1 = {0}, x2 = {1}".format(x1, x2))

    >= greater than or equal to 0
    (Read assignment 2)

