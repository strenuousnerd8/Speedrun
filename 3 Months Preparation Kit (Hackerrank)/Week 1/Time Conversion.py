#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    meridian = s[-2:]
    time = s[:-2]
    if time[:2] == str(12):
        if meridian == "AM":
            return "00" + time[2:]
        else:
            return time
    elif time[:2] != str(12) and meridian == "AM":
        return time
    return str(int(time[:2]) + 12) + time[2:]


if __name__ == "__main__":

    s = input()

    result = timeConversion(s)

    print(result + "\n")
