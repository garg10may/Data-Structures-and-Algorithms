'''
Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing). 
Then doing some arithmetic to calculate the position of each object in the output sequence.
'''


def countingSort( arr, key):

	d = {}

	for i in arr:
		d[i] = 1 + d.get(i, 0)

	countArr = [ d.get(i,0) for i in range(key+1) ]

	for i in range(1,len(countArr)):
		countArr[i] = countArr[i] + countArr[i-1]

	sorted = [ 0 for _ in range(len(arr) + 1) ]

	for i in arr:
		sorted[ countArr[i] ] = i 
		countArr[i] =  countArr[i] -1

	return sorted[1:]

print countingSort( [1,4,1,2,7,5,2], 9)






