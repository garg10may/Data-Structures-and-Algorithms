'''
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest
subsequence of a given sequence such that all elements of the subsequence are sorted
in increasing order.

For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6
and LIS is {10, 22, 33, 50, 60, 80}.
'''


def LIS( array):

	rows = len(array)
	cols = len(array)

	# also adding the zeroth row and col
	T = [ [ 0 for j in range(cols+1) ] for i in range(rows+1) ]

	#fill the first row
	for i in range(cols):
		T[1][i] = 1

	#fill the first col
	for j in range(rows):
		T[j][1] = 1


	for i in range(2, rows+1):
		for j in range(2, cols+1):



'''
# Below works for the given test case, but is still wrong. See the second output.
# recursion can be funny. Will try bottom up. 
def LIS(array):

	if len(array) == 1 or len(array) == 0:
		return array

	take = array[0]

	resultTake = []
	resultAlter = []
	resultFinal = []

	withTake = LIS( array[1:] )

	if take < withTake[0]:
		resultTake = [take] + withTake
	else:
		resultNotTake = withTake
		resultAlter = [take]

	if len(withTake) > 1 and take < withTake[1]:
		resultAlter = [take] + withTake[1:]

	if len(resultTake) > len(resultAlter):
		resultFinal.extend(resultTake)
	else:
		resultFinal.extend(resultAlter)

	return resultFinal


print LIS( [10, 22, 9, 33, 21, 50, 41, 60, 80] )
print LIS( [2, 5, 3, 4] ) 
'''