#https://www.youtube.com/watch?v=aQiWF4E8flQ


def quickSort( x):

	high = len(x)

	pivot = high

	j = low

	for  i in range( high):

		if x[i] < pivot: 
			#swap to make it left of the wall
			x[i], x[j] = x[j], x[i]
			
