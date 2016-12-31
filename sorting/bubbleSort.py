

# simplest, run two loops keep on comparing and swapping, worst also



def bubbleSort( x ):

	for i in range(len(x)):

		for j in range(len(x) -i-1):

			if x[j] > x[j+1]:
				#swap
				x[j], x[j+1] = x[j+1], x[j]

	return x


print bubbleSort( [90,89,1,5,4,8,2])