#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    x=0
    y=0
    z=0
    for i in range(0,n):
        if s[i]=="U":
            x=x+1
        if (s[i])=="D":
            x=x-1 
        if (x == 0) and ( s[i] == "U"):
            z=z+1
    return z  
   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
