#!/usr/bin/python3
"""This module parses a log that's displayed
in stdin and displays its stats.
"""
import sys
import re


def printDict(totalSize, occurenceDict):
    """ This function prints the dictionary of
        Status code occurences in the parsed log
        in sorted order.
        Args:
            occurenceDict (dict): the dictionary of occurences.
    """
    print("File size: {}".format(totalSize))
    for key in sorted(occurenceDict.keys()):
        if occurenceDict[key] != 0:
            print("{}: {}".format(key, occurenceDict[key]))


count = 0
totalSize = 0
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
        match = regexPattern.match(line)
        try:
            statusCode = match.group(3)
            fileSize = int(match.group(4))
            if fileSize:
                totalSize += fileSize
            if statusCode and statusCode in occurenceDict.keys():
                occurenceDict[statusCode] += 1
            if (count % 10 == 0):
                printDict(totalSize, occurenceDict)
        except Exception as e:
            print(e)
            continue
except KeyboardInterrupt:
    print("File size: {}".format(totalSize))
    printDict(occurenceDict)
    raise
