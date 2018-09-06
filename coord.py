import math

def sum(*coords):
  x, y = 0, 0
  for tx, ty in coords:
    x += tx
    y += ty
  return (x, y)

def sub(*coords):
  x, y = coords[0]
  for tx, ty in coords[1:]:
    x -= tx
    y -= ty
  return (x, y)

def line(start, end):
  (sx, sy), (ex, ey) = start, end
  dx, dy = abs(ex - sx), abs(ey - sy)
  ix, iy = 1 if sx < ex else -1, 1 if sy < ey else -1
  x, y, error = sx, sy, dx - dy
  while True:
    error2 = error * 2
    if error2 > -dy:
      error -= dy
      x += ix
    if error2 < dx:
      error += dx
      y += iy
    if x == ex and y == ey: break
    yield (x, y)
