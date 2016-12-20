

#insertion sort, it's just like you sort a hand of cards


def insertionSort( x ):
	n = len(x)
	for i in range(n):
		for j in range(n):
			if x[i] < x[j]:
				temp = x[i]
				x[j+1:] = x[j:]
				x[j] = temp
	return x

print insertionSort( [9,7,6,15,16,5,10,11])

