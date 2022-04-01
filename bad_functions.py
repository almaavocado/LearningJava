# Some good functions are good. Some are bad. We want to write good functions.

def absolute_value(value, is_negative):
    if is_negative:
        return -value
    return value

# Why is is_negative a parameter? Is it necessary?
# Good functions take only the parameters that are necessary
# to make their calculation or decision.


def power(base, exponent):
    return exponent ** base

# Good functions use give meaningful names to parameters,
# and use them in the way they are named.


def maximum(num1, num2):
    if num1 > num2:
        print("The max is", num1)
    else:
        print("The max is", num2)

# Good functions RETURN the values they calculate,
# they don't print them. Don't print in functions, except in rare
# circumstances:
#       - the function's purpose is to gather input from the user
#       - the function's purpose is to display information to the user
# Such functions will generally have names that reflect their purpose,
# like "get_gunpowder" or "print_menu".


def minimum(num1, num2):
    num1 = float(input("Please enter a positive number"))
    while num1 <= 0:
        num1 = float(input("Please enter a positive number"))

    print("OK, let's find the min of those numbers!")
    if num1 < num2:
        return num1
    return num2


    
