

#insertion sort, it's just like you sort a hand of cards


def insert( listOfElements, element):
	#insert element in list in sorted order where list is already sorted
	print listOfElements, element
	status = 0 
	for i in range(len(listOfElements)):
		if element < listOfElements[i] :
			status = 1 
			listOfElements.insert( i, element )
			break
	if status ==0:
		listOfElements.append(element)
	return listOfElements


def insertionSort( x ):
	n = len(x)
	for i in range(n):
		insert( x, x.pop())

	return x

print insertionSort( [9,7,6,15,16,5,10,11])

