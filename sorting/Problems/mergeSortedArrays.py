'''
You have to merge the two sorted arrays into one sorted array (in non-increasing order)

Input:
First line contains an integer T, denoting the number of test cases.
First line of each test case contains two space separated integers X and Y, denoting the size of the two sorted arrays.
Second line of each test case contains X space separated integers, denoting the first sorted array P.
Third line of each test case contains Y space separated integers, denoting the second array Q.

Output:
For each test case, print (X + Y) space separated integer representing the merged array.


Constraints:
1 <= T <= 100
1 <= X, Y <= 5*104
0 <= Pi, Qi <= 109

Example:

INPUT:
1
4 5
7 5 3 1
9 8 6 2 0

OUTPUT:
9 8 7 6 5 3 2 1 0
'''

def merge( arr1, arr2):

	x = len(arr1)
	y = len(arr2)

	i,j = 0, 0

	result = []

	while i < x and j < y:

		if arr1[i] > arr2[j]:
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1

	#any of the array might be left, check for that
	if j==y:
		result.extend(arr1[i:])
	else:
		result.extend(arr2[j:])

	return result


result = merge( [10,9,8,6,2,0], [1] )

print result