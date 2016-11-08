from Graph import Node, Edge, Digraph

def printPath(path):
    """Assumes path is a list of nodes"""
    result =''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) -1:
            result = result + '->'
    return result

def DFS(graph, start, path=[], maxPath=[]):
    path = path + [start]
    print 'Current DFS path: %s'%(printPath(path))
    if graph.childrenOf(start) == [] :
        return path
    else:
        for child in graph.childrenOf(start):
            if child not in path:
                newPath = DFS(graph, child, path, maxPath)
                if len(newPath) > len(maxPath):
                    maxPath = newPath
    return maxPath

def testSP():
    nodes = []
    for  name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    g.addEdge(Edge(nodes[0], nodes[4]))
    g.addEdge(Edge(nodes[4], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[5]))
    sp = DFS(g, nodes[0])
    print 'Longest path found by DFS:', printPath(sp)

testSP()