#!/usr/bin/env python3
#-*- coding: utf-8 -*-

print("Spreadsheet: ")
s = []
while True:
    l = input()
    if not l:
        break
    s.append([int(d) for d in l.split('\t')])

r1, r2 = sum([max(d) - min(d) for d in s]), 0
for l in s:
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            c = l[i], l[i+j+1]
            x, y = max(c), min(c)
            r2 += x % y == 0 and x // y

print("Solutions: [{}] [{}]".format(r1, r2))
