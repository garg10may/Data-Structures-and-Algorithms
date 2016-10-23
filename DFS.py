from Graph import Node, Edge, Digraph

def printPath(path):
    """Assumes path is a list of nodes"""
    result =''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) -1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest):
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
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None)

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
    sp = search(g, nodes[0], nodes[5])
    print 'Shortest path found by DFS:', printPath(sp)

testSP()