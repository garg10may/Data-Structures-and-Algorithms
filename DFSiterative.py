from Graph import Node, Edge, Digraph

def printPath(path):
    """Assumes path is a list of nodes"""
    result =''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) -1:
            result = result + '->'
    return result


#it's same as BFS, just we pop from the end and keep on adding, but we would have to check for shortest from all iterations. It's DFS right right
#so BFS is best for finding shortest, since iterations are not wasted
#Also DFS have benefit of less memory requirement, but here you are giving it up also. So twice bad. 
def DFS(graph, start, end, shortest):
    """Assumes graph is a digraph; start and end are nodes;
       path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) !=0:
        tmpPath = pathQueue.pop()
        print ('Current DFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            if shortest == None or len(tmpPath) < len(shortest):
                shortest = tmpPath
        else:                  
            for child in graph.childrenOf(lastNode):
                if child not in tmpPath:
                    pathQueue.append(tmpPath + [child])
    return shortest



def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, None)

def testSP():
    nodes = []
    for  name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)


    g.addEdge(Edge(nodes[0], nodes[5]))
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
    sp = search(g, nodes[0], nodes[5])
    print 'Shortest path found by DFS:', printPath(sp)

testSP()