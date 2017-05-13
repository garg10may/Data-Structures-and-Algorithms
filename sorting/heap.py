#Building a heap
	# O(n/2) calls to maxHeapify
	# each of which takes O(lg n)
	# Complexity: O(n/2 *logn) = O(log n)
	# ok so on perfunctory analysis it looks O(nlogn) but it's O(n) only, you would have to do math, 
	# since not each of the nodes are going logn level. You just have to remember it's O(n)
	#http://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity

# O(logn), since the height of heap is logn, at max logn calls can take place
# our aim is to look at one (parent, children) and make the max of them as parent
# and if parent was not already the max elemnt, search recursively for the path

#make a tree, that will give clear intution to the logic 
def maxHeapify( arr, i=0):

	n = len(arr)
	largest = i #initializing first element as root
	l = 2*i + 1 #left
	r = 2*i + 2 #right

	if ( l < n and arr[l] > arr[largest] ):
		largest = l

	if ( r < n and arr[r] > arr[largest] ):
		largest = r

	if ( largest != i ):
		arr[i], arr[largest] = arr[largest], arr[i]

		maxHeapify( arr, largest)
		
	return arr 

def buildMaxHeap( arr):
	for i in reversed(range(len(arr)/2)):
		arr = maxHeapify( arr, i)
	return arr


if __name__ == '__main__':
	a = [ 3,5,1,2,6,8 ]
	print buildMaxHeap(a)