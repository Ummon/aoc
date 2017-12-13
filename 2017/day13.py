#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('day13.input') as f:
    s = [tuple(int(n) for n in l.strip().split(': ')) for l in f.readlines()]

run = lambda s, d, prout: sum((i+d) % (2*(r-1)) == 0 and (prout or i * r) for i, r in s)
r1, r2, c = run(s, 0, False), 0, 1
while c != 0:
    r2, c = r2 + 1, run(s, r2, True)

print("Solutions: [{}] [{}]".format(r1, r2-1))
