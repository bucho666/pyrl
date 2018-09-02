import re
import random

class Dice(object):
  def __init__(self, string):
    self._string = string
    match = re.search('(\d+)d(\d+)', string)
    if not match: raise Exception('Dice format error: %s' % string)
    self._number = int(match.group(1))
    self._side = int(match.group(2))
    match = re.search('([\+\-]\d+)$', string)
    self._bonus = int(match.group(1)) if match else 0

  def __str__(self):
    return self._string

  def roll(self):
    roll = sum([random.randint(1, self._side) for n in range(self._number)])
    return roll + self._bonus
