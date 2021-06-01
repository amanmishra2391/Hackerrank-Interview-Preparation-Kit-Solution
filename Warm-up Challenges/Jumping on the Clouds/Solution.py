#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    J=0
    while i<len(c)-1:
        if (i+2)==len(c):
            return J+1
        elif c[i+2]==0:
            i+=2
        else :
            i+=1
        J+=1 
    return J
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
