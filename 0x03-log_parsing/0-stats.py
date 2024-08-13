#!/usr/bin/python3
"""This module parses a log that's displayed
in stdin and displays its stats.
"""
import sys
import re


def printDict(occurenceDict):
    """ This function prints the dictionary of
        Status code occurences in the parsed log
        in sorted order.
        Args:
            occurenceDict (dict): the dictionary of occurences.
    """
    for key in sorted(occurenceDict.keys()):
        if occurenceDict[key] != 0 and key in [200, 301, 400, 401, 403, 404, 405, 500]:
            print("{}: {}".format(key, occurenceDict[key]))


count = 0
sum = 0
occurenceDict = {}
try:
    regexPattern = re.compile(
        r'((?:[0-9]{1,3}\.){3}[0-9]{1,3}) -'
        r' \[.+\] "[A-Z]{3} .*" ([0-9]{3})'
        r' ([0-9]*)')
    for line in sys.stdin:
        count += 1
        if re.match(regexPattern, line):
            match = regexPattern.match(line)
            try:
                statusCode = int(match.group(2))
                fileSize = int(match.group(3))
            except Exception:
                pass
            if statusCode not in occurenceDict.keys():
                occurenceDict[statusCode] = 1
            else:
                occurenceDict[statusCode] += 1
            sum += fileSize
            if (count % 10 == 0):
                print("File size: {}".format(sum))
                printDict(occurenceDict)
except KeyboardInterrupt:
    print("File size: {}".format(sum))
    printDict(occurenceDict)
    raise
