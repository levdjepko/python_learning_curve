#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    
    # format the string
    # from AM/PM format to military time
    hour=int(s[:2])
    timeOfDay=s[8:]
    
        
    if timeOfDay == 'PM':
        if hour != 12:  # 12 pm = 12:00
            hour+=12 
    if timeOfDay == 'AM' and hour == 12:
        hour-=12     
    # handle the missing 0 from a single digit times  
    if len(str(hour)) == 1:
        adjustedHour='0'+str(hour)   
    else:
        adjustedHour =str(hour)
               
    newTime=str(adjustedHour)+s[2:8]
    return newTime
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
