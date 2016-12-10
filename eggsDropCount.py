
'''
#You have to take care of very very small things in recursion or the answer would be nowhere near expected. 
#Here you can't define minDrop as global, try to understand why
def dropCount( eggs, floors):

	global minDrop	

	if eggs ==1 or floors ==0 or floors ==1:
		return floors

	for i in range( 1, floors+1 ):
		result = ( max(dropCount( eggs-1, i-1) ,
		               dropCount( eggs, floors - i) ))
		if result < minDrop:
			minDrop = result

	return (minDrop + 1)

global minDrop
#we need to ensure that first value taken in minimum so defined minDrop as max value
minDrop = 99999999
print dropCount( 2, 10)
'''


#Without DP just for floors=100 no result was there even in 10 mins, with DP blink 0.1 secs.
def dropCount( eggs, floors, d = {}):

	try:
		return d[(eggs, floors)] 
	except:		
		if eggs ==1 or floors ==0 or floors ==1:
			return floors

		minDrop = 99999999
		for i in range( 1, floors+1 ):
			result = ( max(dropCount( eggs-1, i-1) ,
			               dropCount( eggs, floors - i) ))
			if result < minDrop:
				minDrop = result

		d[(eggs, floors)] = minDrop + 1 
		return (minDrop + 1)


print dropCount( 2, 100) 


# Bottom up, DP, can calculate even for (2, 10000), not possible with top down DP 
def dropCount( eggs, floors):

	rows = eggs
	cols = floors

	# always add zeroth row and col so that calculation is synchronized, otherwise confusion
	T = [ [ 0 for j in range(cols+1)] for i in range(rows+1)]

	#fill first col
	for j in range(1,cols+1):
		T[1][j] = j 

	#fill first row 
	for i in range(1,rows+1):
		T[i][1] = 1 

	for eggs in range(2, rows+1):
		for floors in range(2, cols+1):


			if ( eggs > floors ) :
				T[eggs][floors] = T[eggs-1][floors]
			else:
				minCount = 999999999
				for option in range(1, floors+1):
					result =  1 + max( T[eggs-1][option-1] , T[eggs][floors-option] )
					if result < minCount:
						minCount = result
				T[eggs][floors] = minCount

	return T[eggs][floors]


print dropCount( 2, 10000)

















