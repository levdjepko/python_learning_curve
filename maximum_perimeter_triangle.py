def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    return_triangle = []
    # A triangle always has three sides, and the sum of any two of them should be longer than the third side
    # thus, we just need to find the three longest values, and sum of any two of which is larger than the third
    for i in range(len(sticks) - 2):
        a = sticks[i]
        b = sticks[i + 1]
        c = sticks[i + 2]
        if a + b > c and a + c > b and b + c > a:
            return_triangle = [c, b, a]
            return return_triangle
    return [-1]    
                
