import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:  # Odd numbers
        print("Weird")
    elif 2 <= n <= 5:  # Even numbers in [2, 5]
        print("Not Weird")
    elif 6 <= n <= 20:  # Even numbers in [6, 20]
        print("Weird")
    else:  # Even numbers greater than 20
        print("Not Weird")