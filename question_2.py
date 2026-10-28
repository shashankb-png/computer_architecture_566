
# Question 2: Rotate Left Without Carry (ROL)

# Function to rotate an 8-bit binary number to the left.
def rotate_left(number, positions, bits=8):
    # Mask to keep the result within 8 bits.
    mask = (1 << bits) - 1

    # Ensure that the number contains only 8 bits.
    number = number & mask

    # Reduce the rotation count to the valid range.
    positions = positions % bits

    # Rotate left and discard bits beyond the 8-bit width.
    result = ((number << positions) |
              (number >> (bits - positions))) & mask

    return result


# Given 8-bit binary number.
binary_number = "11110110"

# Convert the binary string into an integer.
number = int(binary_number, 2)

# Rotate left by 2 positions.
positions = 2
result = rotate_left(number, positions)

# Display the input and output.
print("Original binary number:", binary_number)
print("Rotation positions:", positions)
print("Result in binary:", format(result, '08b'))
print("Result in unsigned decimal:", result)
