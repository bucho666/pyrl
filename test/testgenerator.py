# -*- coding: utf-8 -*-
from generator import RoomSizeRange
from size import Size
import unittest

class TestGenerator(unittest.TestCase):
  def testRoomSizeRangeProperty(self):
    rsr = RoomSizeRange(Size(1, 3), Size(5, 7))
    self.assertEqual(rsr.minWidth, 1)
    self.assertEqual(rsr.minHeight, 3)
    self.assertEqual(rsr.maxWidth, 5)
    self.assertEqual(rsr.maxHeight, 7)
    self.assertEqual(rsr.min, Size(1, 3))
    self.assertEqual(rsr.max, Size(5, 7))

  def testRoomSizeRangeRandomSize(self):
    rsr = RoomSizeRange(Size(1, 3), Size(5, 7))
    rooms = [rsr.randomSize() for c in range(100)]
    self.assertTrue(any([room.width == 1 for room in rooms]))
    self.assertTrue(any([room.width == 3 for room in rooms]))
    self.assertTrue(any([room.width == 5 for room in rooms]))
    self.assertTrue(any([room.height == 3 for room in rooms]))
    self.assertTrue(any([room.height == 5 for room in rooms]))
    self.assertTrue(any([room.height == 7 for room in rooms]))
    self.assertTrue(all([room.width != 2 for room in rooms]))
    self.assertTrue(all([room.width != 4 for room in rooms]))
    self.assertTrue(all([room.height != 4 for room in rooms]))
    self.assertTrue(all([room.height != 6 for room in rooms]))

  def testRoomSizeRangeRandomSizeSameSize(self):
    rsr = RoomSizeRange(Size(1, 3), Size(1, 3))
    rooms = [rsr.randomSize() for c in range(100)]
    self.assertTrue(all([room == Size(1, 3) for room in rooms]))

