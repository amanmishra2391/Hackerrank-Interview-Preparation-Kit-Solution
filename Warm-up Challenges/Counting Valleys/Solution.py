#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    V=0
    S=1
    D=False
    for i in range(n):
        if s[i]=='U' :
            if S==1:
                D=False
            S+=1   
        elif s[i]=="D":
            if S==1:
                D=True
            S-=1
        if S==1 and D:
            V+=1
            D=False
    return V
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
