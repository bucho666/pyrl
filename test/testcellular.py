import unittest
from cellular import Cellular

class TestCellular(unittest.TestCase):
  def testInitializeAllAlive(self):
    cellular = Cellular((3, 3)).initialize(100)
    for line in cellular.lines:
      self.assertTrue(all(line))

  def testInitializeAllDead(self):
    cellular = Cellular((3, 3)).initialize(0)
    for line in cellular.lines:
      self.assertTrue(all([not cell for cell in line]))

  def testCountAliveNeighbours(self):
    cellular = Cellular((3, 3)).initialize(100)
    self.assertTrue(all([cellular.countLiveNeighbours(c) == 8 for c in cellular]))
    cellular = Cellular((3, 3)).initialize(0)
    self.assertEqual(cellular.countLiveNeighbours((0, 0)), 5)
    self.assertEqual(cellular.countLiveNeighbours((1, 0)), 3)
    self.assertEqual(cellular.countLiveNeighbours((2, 0)), 5)
    self.assertEqual(cellular.countLiveNeighbours((0, 1)), 3)
    self.assertEqual(cellular.countLiveNeighbours((1, 1)), 0)
    self.assertEqual(cellular.countLiveNeighbours((2, 1)), 3)
    self.assertEqual(cellular.countLiveNeighbours((0, 2)), 5)
    self.assertEqual(cellular.countLiveNeighbours((1, 2)), 3)
    self.assertEqual(cellular.countLiveNeighbours((2, 2)), 5)


