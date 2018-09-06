# -*- coding: utf-8 -*-
import parentpath
from size import Size
from cellular import Cellular

if __name__ == '__main__':
  cellular = Cellular(Size(80, 20)).initialize(40).update(5, 3, 5).connect()
  for line in cellular.lines:
    print(''.join(['#' if c else '.' for c in line]))
