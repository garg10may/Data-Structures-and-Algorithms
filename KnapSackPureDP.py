#item, weight, value
sampleList = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )


class item(object):

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def getDensity(self):
        return float(self.value)/float(self.weight)

    def __str__(self):
        return '%s has value of %s and weight of %s and density of %s'%(self.name, self.value, self.weight, self.getDensity())

class itemList(object):

    def __init__(self):
        self.itemList = []

    def add(self, item):
        self.itemList.append(item)

    def __str__(self):
        temp = []
        for i in self.itemList:
            temp.append(i.getName())
        return str(temp)

def buildItems(sample):
    temp = itemList()
    for i in sample:
        temp.add(item(i[0], i[2], i[1]))
    return temp.itemList

sample1 = buildItems(sampleList)

def pureDynamicKS(items, maxWeight):

    temp = []
    for i in items:
        temp.append( (i, i.weight, i.value))

    items = sorted( temp, key=lambda x:x[1])
    rows = len(items)
    cols = maxWeight

    global numCalls

    T = [ [0 for j in range(cols)] for i in range(rows)]

    for i, item in enumerate(items):
        for j in range(cols):
            if j< item[0].weight:
                T[i][j] = T[i-1][j]
                numCalls +=1
            else:
                T[i][j] = max(
                            (  item[0].value + T[i-1][j-item[0].weight]   ), 
                               T[i-1][j]
                             )
                numCalls +=1
    return T[rows-1][cols-1]

numCalls = 0
print pureDynamicKS(sample1, 400)
print 'No. of calls %s'%(numCalls)