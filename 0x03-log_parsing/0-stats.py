#!/usr/bin/env python3
"""
a script that reads stdin line by line and compute metrics
"""
import sys
import re


if __name__ == "__main__":
    regex = (
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
            r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
            )

    line = sys.stdin.readline()
    numberOfLines = 0
    validStatus = ['200', '301', '400', '401', '403', '404', '405', '500']
    pattern = re.compile(r" [0-5]{3} ")
    statusList = {status: 0 for status in validStatus}
    totalSize = []
    sizePattern = re.compile("[0-9]{1,}$")

    while line:
        if re.match(regex, line):
            numberOfLines += 1
            key = pattern.search(line).group().strip()
            if key in validStatus:
                statusList[key] += 1

            size_match = sizePattern.search(line)
            if size_match:
                totalSize.append(int(size_match.group()))
        else:
            print("not march")

        if numberOfLines == 10:
            print("File size:", sum(totalSize))

            for statusCode, number in statusList.items():
                if number == 0:
                    continue
                print(f"{statusCode}: {number}")
            numberOfLines = 0
        line = sys.stdin.readline()
