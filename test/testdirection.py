# -*- coding: utf-8 -*-
import unittest
import direction

class TestDirection(unittest.TestCase):
  def testOpposite(self):
    self.assertEqual(direction.opposite(direction.N), direction.S)
    self.assertEqual(direction.opposite(direction.S), direction.N)
    self.assertEqual(direction.opposite(direction.E), direction.W)
    self.assertEqual(direction.opposite(direction.W), direction.E)
    self.assertEqual(direction.opposite(direction.NW), direction.SE)
    self.assertEqual(direction.opposite(direction.SE), direction.NW)
    self.assertEqual(direction.opposite(direction.NE), direction.SW)
    self.assertEqual(direction.opposite(direction.SW), direction.NE)
