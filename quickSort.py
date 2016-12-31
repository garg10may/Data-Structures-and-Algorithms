'''
https://www.youtube.com/watch?v=aQiWF4E8flQ

Quick sort working on dividing the problem into subtasks. First we choose a pivot,
it can be any element, let's say we choose the last element, then we compare
all the elements, if they are less than pivot we keep them to the left, this is 
done by swapping the element with first element at wall. Above video explains nicely
It's good since it takes only n space, i.e. no more space is required. 
'''


def quickSort( x):

	if len(x) == 0 or len(x) == 1:
		return x  #already sorted

	pivot = len(x)- 1

	wall = 0

	for  currentElement in range(pivot):

		if x[currentElement] <= x[pivot]: 
			#swap to make it left of the wall
			x[currentElement], x[wall] = x[wall], x[currentElement]
			#now move the wall one ahead
			wall += 1

	#once all done, swap the pivot to move it at the wall
	x[pivot], x[wall] = x[wall], x[pivot]

	x = quickSort(x[:wall]) + quickSort(x[wall:])

	return x


print quickSort( [10, 7, 8, 9, 1, 5,1])
			
