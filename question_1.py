
# Question 1: Signed Binary Arithmetic Using 2's Complement


def to_binary(number, bits=8):
    return format(number & ((1 << bits) - 1), f'0{bits}b')

def binary_arithmetic(a, b, operator, bits=8):
   
    binary_a = to_binary(a, bits)
    binary_b = to_binary(b, bits)


    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    else:
        print("Invalid operator")
        return

   
    minimum = -(1 << (bits - 1))
    maximum = (1 << (bits - 1)) - 1

   
    overflow = result < minimum or result > maximum

    print("\nOperand A (decimal):", a)
    print("Operand A (binary) :", binary_a)
    print("Operand B (decimal):", b)
    print("Operand B (binary) :", binary_b)

    print("\nOperation:", a, operator, b)
    print("Result (decimal):", result)
    print("Result (binary) :", to_binary(result, bits))

    if overflow:
        print("Arithmetic overflow: YES")
        print("The result cannot be represented in", bits, "bits.")
    else:
        print("Arithmetic overflow: NO")



print("EXPRESSION (a): 35 - (+29)")
binary_arithmetic(35, 29, '-', 8)


print("\nEXPRESSION (b): (-35) - (-12)")
binary_arithmetic(-35, -12, '-', 8)
