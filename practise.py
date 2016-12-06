
from itertools import combinations

# item, weight, and value
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

def all_combinations(items):
	return ( comb for r in range(1,len(items)+1)
                for comb in combinations(items,r)
                )

def KS_Brute_force(items, maxWeight, d={}):
	result = 0

	if items ==
	for combination in all_combinations(items):
		value = 0
		weight = 0
		for item in combination:
			try:
				value = d[combination][0]
				weight = d[combination][1]
				break
			value += getValue(item)
			weight += getWeight(item)
		d[combination] = value, weight
		if value > result and weight <=maxWeight:
			result = value
			answer = combination
	return result, answer

print KS_Brute_force(items, 400)
