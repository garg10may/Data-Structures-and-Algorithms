
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue as queue
import os

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def bfs(g, start):
	start = g.getVertex(start)
#	start.setPred(None)
	q = queue()
	q.enqueue(start)

	while (q.size() > 0):
		s = q.dequeue()
		for i in s.getConnections():
			if (i.getColor() == 'white'):
				i.setColor('gray')
				i.setPred(s)
				q.enqueue(i)
		s.setColor('black')

def traverse(g, x):
	s = g.getVertex(x)
	while ( s.getPred()):
		print s.getId()
		s = s.getPred()
	print s.getId()

os.chdir(r'C:\Users\garg10may\Desktop')
g = buildGraph('unixdict.txt')
bfs(g, 'luck')
traverse(g, 'sage')

