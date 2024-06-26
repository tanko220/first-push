def binary_to_decimal(binary_num):
    decimal_num = 0
    power = len(binary_num) - 1
    
    for digit in binary_num:
        # Multiply the digit by 2 raised to the power of its position
        decimal_num += int(digit) * (2 ** power)
        power -= 1
    
    return decimal_num

# Example usage
binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)
print("Decimal representation:", decimal_number)
