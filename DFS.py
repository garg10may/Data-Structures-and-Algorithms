from Graph import Node, Edge, Digraph

def printPath(path):
    """Assumes path is a list of nodes"""
    result =''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) -1:
            result = result + '->'
    return result

#DFS1 --> To find the shortest path between 2 nodes, there's no concept of shortest without end
#DFS2 --> To find the longest path of all paths. 
#Essentially one has to understand how the recursive nature is working, different comparisons can always be made
def DFS1(graph, start, end, path=[], shortest=None):
    """Assumes graph is a digraph; start and end are nodes;
       path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    print 'Current DFS path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS1(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def DFS2(graph, start, path=[], maxPath=[]):
    path = path + [start]
    print 'Current DFS path: %s'%(printPath(path))
    if graph.childrenOf(start) == [] :
        return path
    else:
        for child in graph.childrenOf(start):
            if child not in path:
                newPath = DFS2(graph, child, path, maxPath)
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
    shortest = DFS1(g, nodes[0], nodes[5])
    longest = DFS2(g, nodes[0])

    print 'Shortest path found by DFS:', printPath(shortest)
    print 'Longest path found by DFS:', printPath(longest)

testSP()