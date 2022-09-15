#15th Sep, 2022
#Graph

class Node(object):
    def __init__(self, name):
        self.name = name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

class Graph(object):

  def __init__(self) -> None:
    self.nodes = []
    self.edges = []

  def addNode(self, name):
    self.nodes.append(Node(name))

  def addEdge(self, src, dest):
    self.edges.append(Edge(src, dest))

  def addWeightedEdge(self, src, dest, weight):
    self.edges.append(WeightedEdge(src, dest, weight))

  def getNodes(self):
    return self.nodes
  
  def getEdges(self):
    return self.edges