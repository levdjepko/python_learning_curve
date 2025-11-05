import random


def rand7():
    return random.randint(1, 7)


def rand5():
    # implement function Random-5 or simulate a 5-sided die using an existing 7-sided die
    #
    result = rand7()
    
    while result > 5:
        result = rand7()

    return result


print('Rolling 5-sided die...')
print(rand5())
