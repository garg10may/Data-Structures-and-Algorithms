

# O(logn), since the height of heap is logn, at max logn calls can take place
# our aim is to look at one (parent, children) and make the max of them as parent
# and if parent was not already the max elemnt, search recursively for the path 
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

def buildMaxHeap( arr):

	#calling each element once and then recursively buidling that binary tree
	# nlogn --> n for number of calls, logn for each call
	for i in reversed(range(len(arr)/2)):
		maxHeapify( arr, i)
		print arr
	return arr


a = [ 3,5,1,2,6,8 ]
print buildMaxHeap(a)

