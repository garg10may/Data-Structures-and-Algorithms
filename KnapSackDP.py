# item, weight, value
itemsList = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )

items = [ x[0] for x in itemsList]

def getWeight(item):
    index = items.index(item)
    weight = itemsList[index][1]
    return weight
def getValue(item):
    index = items.index(item)
    value = itemsList[index][2]
    return value

#using recusion and dynamic programming, a very significant improvement due to D.P.

def maxVal(toConsider, avail, memo={}):
    try:
        result = memo[(toConsider, avail)]
    except:
        if toConsider == () or avail == 0:
            result = (0,())
        elif getWeight(toConsider[0][0]) > avail:
            result = maxVal(toConsider[1:], avail, memo)
        else:
            nextItem = toConsider[0]
            withVal, withToTake = maxVal(toConsider[1:], avail - getWeight(nextItem[0]), memo)
            withVal += getValue(nextItem[0])
            withoutVal, withoutToTake = maxVal(toConsider[1:], avail, memo)
            if withVal > withoutVal:
                result = (withVal, withToTake + (nextItem,))
            else:
                result = (withoutVal, withoutToTake)
        memo[(toConsider, avail)] = result
    return result

print maxVal(itemsList,400)


