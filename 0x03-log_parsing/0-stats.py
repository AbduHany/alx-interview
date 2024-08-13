#!/usr/bin/python3
import sys
import re


def printDict(occurenceDict):
    for key in sorted(occurenceDict.keys()):
        print("{}: {}".format(key, occurenceDict[key]))


count = 1
sum = 0
occurenceDict = {}
try:
    regexPattern = re.compile(
        r'((?:[0-9]{1,3}\.){3}[0-9]{1,3}) -'
        r' \[.+\] "[A-Z]{3} .*" ([0-9]{3})'
        r' ([0-9]*)')
    for line in sys.stdin:
        if re.match(regexPattern, line):
            match = regexPattern.match(line)
            try:
                statusCode = int(match.group(2))
                fileSize = int(match.group(3))
            except Exception:
                continue
            if statusCode not in occurenceDict.keys():
                occurenceDict[statusCode] = 1
            else:
                occurenceDict[statusCode] += 1
            sum += fileSize
            if (count % 10 == 0):
                print("File size: {}".format(sum))
                printDict(occurenceDict)
            count += 1
        else:
            continue
except KeyboardInterrupt:
    print("File size: {}".format(sum))
    printDict(occurenceDict)
