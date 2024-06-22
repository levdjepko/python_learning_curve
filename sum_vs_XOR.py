# https://www.hackerrank.com/challenges/three-month-preparation-kit-sum-vs-xor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six
def sumXor(n):    
    binary = bin(n)
    zeros = binary.lstrip('0b').count('0')
    return 2 ** zeros
