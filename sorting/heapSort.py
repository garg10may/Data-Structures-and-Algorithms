
from heap import buildMaxHeap, maxHeapify


#we just need to extract the max element again and again from heap(just build it once)
#to save space we will keep on swapping it with the last, and calling heapify again and again on the reduced heap
def heapSort( arr) :

	n = len(arr) 
	buildMaxHeap(arr)

	for i in reversed(range(n)):
		arr[i], arr[0] = arr[0], arr[i]
		arr = maxHeapify( arr[:i] ) + arr[i:]

	return arr

x = [ 12, 11, 13, 5, 6, 7]
print heapSort(x)
