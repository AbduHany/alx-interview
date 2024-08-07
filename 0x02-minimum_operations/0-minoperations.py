#!/usr/bin/python3
"""This module defines the minOperations function
"""


def minOperations(n):
    """ This function returns the fewest number of operations required
        to create n * 'H' characters. The only allowed operations are:
        Copy all & Paste
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
