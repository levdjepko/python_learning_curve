# This is a password checker app
# Its length is at least 6
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+


def minimumNumber(n, password):
    
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    has_special_character = has_uppercase = has_lowercase = has_number = padding = 0
    
    for i in range(len(password)):
        if password[i] in special_characters:
            print("special")
            has_special_character = 1
        if password[i] in upper_case:
            print("uppercase")
            has_uppercase = 1
        if password[i] in lower_case:
            print("lowercase")
            has_lowercase = 1
        if password[i] in numbers:
            print("number")
            has_number = 1
    # Add required symbols to the pasword
    addition = 4 - (has_special_character + has_uppercase + has_lowercase + has_number)
    
    # If the password is still too short, pad it with some more symbols
    if len(password) + addition < 6:
        padding = 6 - len(password) - addition
        
    return (addition + padding)
