#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
    # If the value of  is less than , no rounding occurs as the result will still be a failing grade.
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i] % 5 > 2:
                # round up the grade to the next multiple of 5
                grades[i] = grades[i]//5 * 5 + 5  # get to the next number that is divisible by 5
    return grades            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
