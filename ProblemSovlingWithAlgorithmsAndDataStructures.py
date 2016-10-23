

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

a = itemList()
a.add(item('a', 6, 3))
a.add(item('b', 7, 3))
a.add(item('c', 8, 2))
a.add(item('d', 9, 5))

def greedyKS(itemList, maxWeight):
    items = []
    for i in itemList:
        items.append((i, i.getDensity()))

    items = sorted(items, reverse=True, key=lambda x:x[1])

    totalValue = 0
    selected = ''
    for i in items:
        if i[0].getWeight() <= maxWeight:
            selected += i[0].getName() + ' '
            weightLeft = maxWeight - i[0].getWeight()
            totalValue += i[0].getValue()
            maxWeight = weightLeft

    return (selected, totalValue)

#print greedyKS(a.itemList, 10)

def subsets(items):    
    from itertools import combinations
    temp = []
    for i in range(1,len(items) + 1):
        temp += combinations(items, i)
    return temp

def bruteForceKS( itemList, maxWeight):
    value = 0
    for i in subsets(itemList):
        totalValue = reduce(lambda x, y : x + y, [x.getValue() for x in i])
        totalWeight = reduce(lambda x, y : x + y, [x.getWeight() for x in i])
        if totalWeight <= maxWeight and totalValue > value:
            selected = [ x.getName() for x in i]
            value = totalValue

    return (selected, value)

#print bruteForceKS(a.itemList, 10)

sampleList = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )

def buildItems(sample):
    temp = itemList()
    for i in sample:
        temp.add(item(i[0], i[2], i[1]))
    return temp.itemList

sample1 = buildItems(sampleList)
#print bruteForceKS(sample1,400)
#print greedyKS(sample1, 400)

def totalValue(items):
    try:
        value = reduce(lambda x,y: x+y, [ i.getValue() for i in items])
        return value
    except:
        return 0

def recursionKS(items, avail):

    if items == [] or avail == 0:
        result =  [], 0
    elif items[0].getWeight() <= avail:
        including, valueTake = recursionKS(items[1:], avail - items[0].getWeight())
        valueTake += items[0].getValue()
        notincluding, valueNotTake = recursionKS(items[1:], avail)
        if valueTake > valueNotTake:
            including.append(items[0])
            result =  including, valueTake
        else:
            result =  notincluding, valueNotTake
    else:
        result =  recursionKS( items[1:], avail)
    return result

#selected, value = recursionKS(sample1, 400)
#print value, map(lambda x: x.getName(), selected)

def maxVal(toConsider, avail, memo={}):
    try:
        result = memo[(len(toConsider), avail)]
    except:
        if toConsider == [] or avail == 0:
            result = (0,[])
        elif toConsider[0].getWeight() > avail:
            result = maxVal(toConsider[1:], avail, memo)
        else:
            nextItem = toConsider[0]
            withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight(), memo)
            withVal += nextItem.getValue()
            withoutVal, withoutToTake = maxVal(toConsider[1:], avail, memo)
            if withVal > withoutVal:
                #withToTake.append(nextItem) this is still ambigious why this small change is resulting in such absurd answer. Need to debug properly, 
                #therefore I say, recursion is so difficult, you just don't see things as they are supposed to be :P
                result = (withVal, withToTake + [nextItem])
            else:
                result = (withoutVal, withoutToTake)
        memo[(len(toConsider), avail)] = result
    return result

#alue, selected = maxVal(sample1, 400)
#print value, map(lambda x: x.getName(), selected)


def pureDynamicKS(items, maxWeight):

    temp = []
    for i in items:
        temp.append( (i, i.weight, i.value))

    items = sorted( temp, key=lambda x:x[1])
    print items
    rows = len(items)
    cols = maxWeight

    T = [ [0 for j in range(cols)] for i in range(rows)]

    for i, item in enumerate(items):
        for j in range(cols):
            if j< item[0].weight:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(
                            (  item[0].value + T[i-1][j-item[0].weight]   ), 
                               T[i-1][j]
                             )
    print T[rows-1][cols-1]

pureDynamicKS(a.itemList, 10)