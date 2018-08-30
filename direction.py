# -*- coding: utf-8 -*-
from coord import Coord

HERE = Coord(0, 0)
N = Coord(0, -1)
NE = Coord(1, -1)
E = Coord(1, 0)
SE = Coord(1, 1)
S = Coord(0, 1)
SW = Coord(-1, 1)
W = Coord(-1, 0)
NW = Coord(-1, -1)
CROSS = (N ,E ,S, W)
AROUND = (N, NE, E, SE, S, SW, W, NW)
