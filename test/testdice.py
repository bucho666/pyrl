import unittest
from dice import Dice

class TestDice(unittest.TestCase):
  def testRoll(self):
    self.rollTest(Dice('2d6'), 2, 12)
    self.rollTest(Dice('2d6+2'), 4, 14)
    self.rollTest(Dice('2d6-3'), -1, 9)

  def testString(self):
    self.stringTest('2d6')
    self.stringTest('2d6+2')
    self.stringTest('2d6-3')

  def rollTest(self, dice, low, high):
    result = [dice.roll() for c in range(255)]
    for r in range(low, high + 1):
      self.assertTrue(r in result)
    self.assertFalse(low - 1 in result)
    self.assertFalse(high + 1 in result)

  def stringTest(self, string):
    self.assertEqual(str(Dice(string)), string)
