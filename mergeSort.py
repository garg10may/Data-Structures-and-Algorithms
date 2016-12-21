#Merge Sort 

#this insert block though right, seems of bad complexity, you aren't using the fact 
#that two lists are already sorted, you should use that to your advantage

def merge( x, y):
	# merge two arrays of sorted lists
	result = []
	i, j = 0,0

	while  i < len(x) and j < len(y):
		if x[i] < y[j]:
			result.append(x[i])
			i +=1
		else:
			result.append(y[j])
			j+=1

	#any of the x or y maybe left, so be need to append as it is
	if i == (len(x)): #i.e. first list was exhausted
		result.extend( y[j:]) #append second list
	else:
		result.extend( x[i:]) #append first

	return result

def mergeSort( x ):

	n = len(x)
	if n == 1:	return x

	return ( merge ( mergeSort( x[ : n/2 ] ),  mergeSort( x[ n/2 :  ]) ) )

print mergeSort( [38, 27, 43, 3, 9, 82, 10]) 




