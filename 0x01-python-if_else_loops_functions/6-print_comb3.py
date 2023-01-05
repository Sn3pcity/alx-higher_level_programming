#!/usr/bin/python3
for s in range(0, 9):
    for j in range(s + 1, 10):
        if s == 8:
            print("{:d}{:d}".format(s, j))
            break
        print("{:d}{:d}".format(s, j), end=", ")
