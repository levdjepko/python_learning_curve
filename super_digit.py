def superDigit(n, k):
    # find a super-digit which is a sum of all digits in a number
    # do it recursively
    # first, create a string by concatenating the string N K times:
        
    result = sum(int(digit) for digit in str(n)) * k
    while result >= 10:
        result = sum(int(digit) for digit in str(result))
    return result
