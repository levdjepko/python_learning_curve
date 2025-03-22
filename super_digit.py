def superDigit(n):
    # find a super-digit which is a sum of all digits in a number
    # do it recursively    
        
    result = n
    while result >= 10:
        result = sum(int(digit) for digit in str(result))
    return result
