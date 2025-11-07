import math
import os
import random
import re
import sys

def twoArrays(k, A, B):
    # Permute the arrays A and B to get the sums of each pair A[i] + B[i] >= k if that's possible
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        # the arrays A and B are the same size
        # get the sums
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'         

