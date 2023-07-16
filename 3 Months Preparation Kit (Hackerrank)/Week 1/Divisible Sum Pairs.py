#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n, k, ar):
    # Write your code here
    sorted_arr = sorted(ar)
    count = 0
    for i in range(len(sorted_arr) - 1):
        temp_arr = [(j + sorted_arr[i]) % k for j in sorted_arr[i + 1 :]]
        count += temp_arr.count(0)
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
