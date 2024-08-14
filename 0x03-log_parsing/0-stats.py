#!/usr/bin/python3
"""This module parses a log that's displayed
in stdin and displays its stats.
"""
import sys
import re


def printDict(occurenceDict):
    """ This function prints the dictionary of
        Status code occurrences in the parsed log
        in sorted order.
        Args:
            occurenceDict (dict): the dictionary of occurrences.
    """
    for key in sorted(occurenceDict.keys()):
        if occurenceDict[key] != 0:
            print("{}: {}".format(key, occurenceDict[key]))


count = 0
total_size = 0
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
    regexPattern = re.compile(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.+?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'  # noqa
    )
    for line in sys.stdin:
        match = regexPattern.match(line)
        if match:
            count += 1
            statusCode = match.group(3)
            fileSize = int(match.group(4))

            if statusCode in occurenceDict:
                occurenceDict[statusCode] += 1
                total_size += fileSize

            if count % 10 == 0:
                print("File size: {}".format(total_size))
                printDict(occurenceDict)

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    printDict(occurenceDict)
