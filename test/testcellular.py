import unittest
from cellular import Cellular

class TestCellular(unittest.TestCase):
  def testInitializeAllAlive(self):
    cellular = Cellular((3, 3)).initialize(100)
    self.assertEqual(len([ alive for alive in cellular ]), 9)

  def testInitializeAllDead(self):
    cellular = Cellular((3, 3)).initialize(0)
    self.assertEqual(len([ alive for alive in cellular ]), 0)

  def testCountAliveNeighbours(self):
    cellular = Cellular((3, 3)).initialize(100)
    self.assertEqual(cellular.countLiveNeighbours((0, 0)), 3)
    self.assertEqual(cellular.countLiveNeighbours((1, 0)), 5)
    self.assertEqual(cellular.countLiveNeighbours((2, 0)), 3)
    self.assertEqual(cellular.countLiveNeighbours((0, 1)), 5)
    self.assertEqual(cellular.countLiveNeighbours((1, 1)), 8)
    self.assertEqual(cellular.countLiveNeighbours((2, 1)), 5)
    self.assertEqual(cellular.countLiveNeighbours((0, 2)), 3)
    self.assertEqual(cellular.countLiveNeighbours((1, 2)), 5)
    self.assertEqual(cellular.countLiveNeighbours((2, 2)), 3)
