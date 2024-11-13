class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack and push the string we encounter
        stack = []
        parentheses = ['(', ')', '[', ']', '{', '}']
        for char in s:
            # check each character in a string
            if char in parentheses and char in ['(', '[', '{']:
                # opening brackets
                stack.append(char)
            elif char in parentheses and char in [')', '}', ']'] and len(stack) > 0:
                # closing bracket - check the top one on the stack
                pair_to_match = stack.pop()
                if (pair_to_match == '(' and char != ')') or (pair_to_match == '[' and char != ']') or (pair_to_match == '{' and char != '}'):
                    return False
            else:
                return False        
        # if at this point we pushed and popped each character in correct order, the string is a valid code
        if len(stack) == 0:
            return True
        return False                
