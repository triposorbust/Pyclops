#!/usr/bin/env python

from sys import argv,path
import src.pyclops.core as pyclops

def main(filename):
    with open(filename, 'r') as f:
        points = [tuple(map(int, l.split())) for l in f if not l.strip() == ""]
        pair,d = pyclops.closest_pair(points)
    p,q = pair
    print("(x1,y1) = ({0},{1})".format(p[0],p[1]))
    print("(x2,y2) = ({0},{1})".format(q[0],q[1]))
    print("distance = {0}".format(d))
    return

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage:\n% python main.py <input-filename>")
        exit(1)
    main(argv[1])
