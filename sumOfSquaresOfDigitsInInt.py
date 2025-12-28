def sum_of_square_digits(n):
    # The input 'n' is a positive integer.
    # Convert the integer 'n' to a string to iterate over the digits.
    # For each digit, convert it back to an integer and calculate its square.
    # Add the square to a running total.
    # Return the total.
    number_as_string = str(n)
    result = 0
    for i in range(len(number_as_string)):
        result += int(number_as_string[i]) ** 2
    return result    

n = int(input())
print(sum_of_square_digits(n))
