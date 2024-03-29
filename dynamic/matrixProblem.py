# one of the easiest problem on dynamic programming

'''
Find the number of unique paths in a matrix, given that you can 
only move down or right. i.e. count the number of paths from top left
to bottom right.
'''

#Top down
def numberOfPaths( m, n, d={} ):
	try:
		return d[(m,n)]
	except:			
		if m==1 or n==1: # this works since if I reach the last column or row there is only
			return 1		# one way to reach the end
		d[(m,n)] =  numberOfPaths( m-1, n) + numberOfPaths( m, n-1)
		return d[ (m,n) ]

print (numberOfPaths( 10, 10))


#Bottom up
def numberOfPaths( m, n ):

	T = [ [ 0 for _ in range(n)] for _ in range(m) ]

	#initializing first row as 1
	T[0] = [1 for _ in range(n)]

	#initialize first column as 1
	for i in range(m):
		T[i][0] = 1

	for i in range(1,m):
		for j in range(1,n):
			T[i][j] = T[i - 1][j] + T[i][j - 1]

	return  T[n-1][m-1]

print (numberOfPaths(10,10))