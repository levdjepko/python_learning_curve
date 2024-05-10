#!/bin/python3

import math
import os
import random
import re
import sys



def matchingStrings(strings, queries):
    # There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
    counted_instances = [0] * len(queries)   # we will use this array to track the counts of occurences
    for i in range(len(queries)):
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                counted_instances[i] += 1
    return counted_instances            
            
