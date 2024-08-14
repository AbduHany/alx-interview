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
        if occurenceDict[key] != 0:
            print("{}: {}".format(key, occurenceDict[key]))


count = 0
sum = 0
occurenceDict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
try:
    regexPattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.+?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$')  # noqa
    for line in sys.stdin:
        count += 1
        string = line[:-1]
        if re.match(regexPattern, line):
            match = regexPattern.match(line)
            try:
                statusCode = match.group(3)
                fileSize = int(match.group(4))
            except Exception:
                pass
            if statusCode in occurenceDict.keys():
                occurenceDict[statusCode] += 1
                sum += fileSize
            if (count % 10 == 0):
                print("File size: {}".format(sum))
                printDict(occurenceDict)
except KeyboardInterrupt:
    print("File size: {}".format(sum))
    printDict(occurenceDict)
    raise
