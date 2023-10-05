import struct

def decimal_or_float_to_binary_32bit(number):
    # Check if the input is a valid number
    try:
        number = float(number)
    except ValueError:
        return "Invalid input: Not a number"

    # Pack the float as a 32-bit binary string
    binary_representation = struct.pack('f', number)

    # Unpack the binary string to get the 32-bit integer representation
    int_representation = struct.unpack('I', binary_representation)[0]

    # Convert the integer to a binary string with leading zeros
    binary_string = format(int_representation, '032b')

    return binary_string

# Test cases
print(decimal_or_float_to_binary_32bit(1))         # Integer
print(decimal_or_float_to_binary_32bit(-1))    # Positive float
print(decimal_or_float_to_binary_32bit(3.7))   # Negative float



