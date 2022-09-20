'''
Given a n*n matrix where all numbers are distinct and distributed
from 1, n^2, find the maximum length path (starting from any cell)
such that all cells along the path are increasing order with a difference of 1.
http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
'''

def maxPath(matrix):

	d = {}
	result = []

	for i, row in enumerate(matrix):
		for j, elem in enumerate(row):

			print (i,j, elem, type(elem))

			if abs(elem - matrix[i+1][j]) ==1:
				result.append(elem)
			elif abs(elem - matrix[i-1][j]) ==1:
					result.append(elem)
			elif abs(elem - matrix[i][j+1]) ==1:
					result.append(elem)
			elif abs(elem - matrix[i][j-1]) ==1:
					result.append(elem)
			else:
				pass

			d[elem] = result

	print (d)


maxPath([[1,2,9], [5,3,8], [4,6,7]])