import unittest
from cellular import Cellular
from size import Size
from coord import Coord

class TestCellular(unittest.TestCase):
  def testInitializeAllAlive(self):
    cellular = Cellular(Size(3, 3)).initialize(100)
    for line in cellular.lines:
      self.assertTrue(all(line))

  def testInitializeAllDead(self):
    cellular = Cellular(Size(3, 3)).initialize(0)
    for line in cellular.lines:
      self.assertTrue(all([not cell for cell in line]))

  def testCountAliveNeighbours(self):
    cellular = Cellular(Size(3, 3)).initialize(100)
    self.assertTrue(all([cellular.countLiveNeighbours(c) == 8 for c in cellular]))
    cellular = Cellular(Size(3, 3)).initialize(0)
    self.assertEqual(cellular.countLiveNeighbours(Coord(0, 0)), 5)
    self.assertEqual(cellular.countLiveNeighbours(Coord(1, 0)), 3)
    self.assertEqual(cellular.countLiveNeighbours(Coord(2, 0)), 5)
    self.assertEqual(cellular.countLiveNeighbours(Coord(0, 1)), 3)
    self.assertEqual(cellular.countLiveNeighbours(Coord(1, 1)), 0)
    self.assertEqual(cellular.countLiveNeighbours(Coord(2, 1)), 3)
    self.assertEqual(cellular.countLiveNeighbours(Coord(0, 2)), 5)
    self.assertEqual(cellular.countLiveNeighbours(Coord(1, 2)), 3)
    self.assertEqual(cellular.countLiveNeighbours(Coord(2, 2)), 5)


