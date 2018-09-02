import direction

class Node(object):
  def __init__(self, parent, cost, coord, goal):
    self._parent = parent
    self._cost = cost
    self._coord = coord
    self._heuristicCost = self._calculateCost(goal)

  def __eq__(self, other):
    return  self.coord == other.coord

  def __iter__(self):
    route = []
    n = self._parent
    while(n):
      route.append(n.coord)
      n = n.parent
    route.pop()
    route.reverse()
    for c in route:
      yield c

  @property
  def coord(self):
    return self._coord

  @property
  def around(self):
    return [self._coord + d for d in direction.AROUND]

  @property
  def cost(self):
    return self._cost

  @property
  def parent(self):
    return self._parent

  def score(self):
    return self._cost + self._heuristicCost

  def _calculateCost(self, goal):
    diff = goal - self._coord
    return max(abs(diff.x), abs(diff.y))

class AStar(object):
  def __init__(self, costAt):
    self._costAt = costAt

  def compute(self, start, goal):
    nodes, opens, closes = [Node(None, 0, start, goal)], set(), set()
    opens.add(start)
    while(nodes):
      n = nodes.pop(0)
      if n.coord == goal: return n
      closes.add(n.coord)
      opens.remove(n.coord)
      for c in n.around:
        if c in closes or c in opens: continue
        nodes.append(Node(n, n.cost + self._costAt(c), c, goal))
        opens.add(c)
      nodes.sort(key=Node.score)

if __name__ == '__main__':
  from demo.astardemo import AStarDemo
  AStarDemo().run()
