#!/usr/bin/python

import sys

sumTotal = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSum = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", sumTotal
        oldKey = thisKey;
        sumTotal = 0

    oldKey = thisKey
    sumTotal += int(thisSum)

if oldKey != None:
    print oldKey, "\t", sumTotal



