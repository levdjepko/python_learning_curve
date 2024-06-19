def is_power_of_two(n):
    # check if the number is 0 to begin with
    # if not, then check that bitwise & is exacly 0
    # because any power of 2 has exactly one 1 in binary representation, and ...
    # same number -1 is all 1's but the set bit
    return (n != 0) and (n & (n-1) == 0)
    
def counterGame(n):
    # we have to substract the next lowest power of 2
    # and then we get to a point where the number is reduced to 1 by dividing it on 2
    moves = 0
    while n != 1:
        exponent = math.log2(n)
        if exponent.is_integer():
            n = n/2
        else:
            n = n - 2 ** int(exponent)
        moves += 1
    if moves % 2 == 0:
        return 'Richard'
    else:
        return 'Louise'   
