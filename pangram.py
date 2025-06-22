import math
import os
import random
import re
import sys


def pangrams(s):
    # Create a dictionary of the letters in the input string
    dict = []
    
    for char in s:
        if char.lower() not in dict and char.lower() != ' ':
            dict.append(char.lower())
            
    if len(dict) >= 26:
        return ("pangram")
    else:
        return ("not pangram")
