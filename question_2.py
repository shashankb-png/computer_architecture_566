
# Question 2: Rotate Left Without Carry (ROL)

def rotate_left(number, positions, bits=8):
    
    mask = (1 << bits) - 1

    number = number & mask
    positions = positions % bits

    result = ((number << positions) |
              (number >> (bits - positions))) & mask

    return result


binary_number = "11110110"


number = int(binary_number, 2)


positions = 2
result = rotate_left(number, positions)

print("Original binary number:", binary_number)
print("Rotation positions:", positions)
print("Result in binary:", format(result, '08b'))
print("Result in unsigned decimal:", result)
