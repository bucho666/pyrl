# -*- coding: utf-8 -*-
from maze import RoomSizeRange
from maze import Maze
import unittest

class TestMaze(unittest.TestCase):
  def testRoomSizeRangeProperty(self):
    rsr = RoomSizeRange((1, 3), (5, 7))
    self.assertEqual(rsr.minWidth, 1)
    self.assertEqual(rsr.minHeight, 3)
    self.assertEqual(rsr.maxWidth, 5)
    self.assertEqual(rsr.maxHeight, 7)
    self.assertEqual(rsr.min, (1, 3))
    self.assertEqual(rsr.max, (5, 7))

  def testRoomSizeRangeRandomSize(self):
    rsr = RoomSizeRange((1, 3), (5, 7))
    rooms = [rsr.randomSize() for c in range(100)]
    self.assertTrue(any([w == 1 for (w, h) in rooms]))
    self.assertTrue(any([w == 3 for (w, h) in rooms]))
    self.assertTrue(any([w == 5 for (w, h) in rooms]))
    self.assertTrue(any([h == 3 for (w, h) in rooms]))
    self.assertTrue(any([h == 5 for (w, h) in rooms]))
    self.assertTrue(any([h == 7 for (w, h) in rooms]))
    self.assertTrue(all([w != 2 for (w, h) in rooms]))
    self.assertTrue(all([w != 4 for (w, h) in rooms]))
    self.assertTrue(all([h != 4 for (w, h) in rooms]))
    self.assertTrue(all([h != 6 for (w, h) in rooms]))

  def testRoomSizeRangeRandomSizeSameSize(self):
    rsr = RoomSizeRange((1, 3), (1, 3))
    rooms = [rsr.randomSize() for c in range(100)]
    self.assertTrue(all([room == (1, 3) for room in rooms]))

  def testSplitLineIsOdd(self):
    g = Maze((79, 21)).generate()
    for area in g.area:
      self.assertTrue(all([x % 2 == 0 or y % 2 == 0 for (x, y) in area.frame]))
