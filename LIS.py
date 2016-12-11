'''
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest
subsequence of a given sequence such that all elements of the subsequence are sorted
in increasing order.

For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6
and LIS is {10, 22, 33, 50, 60, 80}.
'''


#below is awfully wrong, I thought all combinations given take and not take option
# and I would choose one with the max length
def LIS(array):

	if len(array) == 1 or len(array) == 0:
		return array

	take = array[0]

	resultTake = []
	resultNotTake = []
	resultFinal = []

	withTake = LIS( array[1:] )

	if take < withTake[0]:
		resultTake = [take] + withTake
	else:
		resultTake = withTake

	withNotTake = LIS( array[1:])

	resultNotTake = withNotTake

	if len(resultTake) > len(resultNotTake):
		resultFinal.extend(resultTake)
	else:
		resultFinal.extend(resultNotTake)

	return resultFinal


print LIS( [10,22,9,33])
