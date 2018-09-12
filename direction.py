# -*- coding: utf-8 -*-
HERE = (0, 0)
N = (0, -1)
NE = (1, -1)
E = (1, 0)
SE = (1, 1)
S = (0, 1)
SW = (-1, 1)
W = (-1, 0)
NW = (-1, -1)
CROSS = (N ,E ,S, W)
CIRCLE = (N, NE, E, SE, S, SW, W, NW)

def opposite(d):
  x, y = d
  return (0 if x == 0 else -x, 0 if y == 0 else -y)
