def insert( listOfElements, element):
	#insert element in list in sorted order where list is already sorted
	status = 0 
	for i in range(len(listOfElements)):
		if element < listOfElements[i] :
			status = 1 
			listOfElements.insert( i, element )
			break
	if status ==0:
		listOfElements.append(element)
	return listOfElements


def merge( x, y):
	# merge two arrays of sorted lists

	result = []
	#add the first element
	if x[0] < y[0]:
		result.extend( [ x[0], y[0] ] )
	else:
		result.extend( [ y[0], x[0] ] )

	for i in range(1, max(len(x), len(y))):
		try:
			result = insert( result, x[i] ) 
		except:
			pass
		try:
			result = insert( result, y[i] ) 
		except:
			pass
	return result


def mergeSort( x ):
	if len(x) == 1:
		return x
	n = len(x)
	return ( merge ( mergeSort( x[ : n/2 ] ),  mergeSort( x[ n/2 :  ]) ) )

print mergeSort( [38, 27, 43, 3, 9, 82, 10])




