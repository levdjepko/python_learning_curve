#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    '''
    # Given the scores for a season, determine the number of times 
    # Maria breaks her records for most and least points scored during the season.
    '''
    min_count = max_count = 0
    max_score = min_score = scores[0]
    
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            # new high record
            max_count += 1
            max_score = scores[i]
        elif scores[i] < min_score:
            # new low record
            min_count += 1
            min_score = scores[i]
    return [max_count, min_count]       
