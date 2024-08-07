#!/usr/bin/python3
"""This module defines the minOperations function
"""


def minOperations(n):
    """ This function returns the fewest number of operations required
        to create n * 'H' characters. The only allowed operations are:
        Copy all & Paste
    """
    if (n <= 0):
        return 0
    num = n
    divisions = []
    i = 2
    while i < n - 1:
        if num % i == 0:
            divisions.append(i)
            num = num // i
            i = 2
        else:
            i += 1
    if len(divisions) == 0:
        return n
    else:
        return sum(divisions)
