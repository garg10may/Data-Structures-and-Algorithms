'''
Given a distance 'dist', count total number of ways to cover the distance with 1,2 and 3 steps. 
'''



def totalSteps(n, d= {}):

	global count
	count +=1

	try:
		return d[n]
	except:
		if n < 0:
			return 0
		if n == 0:
			return 1

		else:
			d[n] = (totalSteps(n-1) + totalSteps(n-2) + totalSteps(n-3) )
			return d[n]


count = 0
print totalSteps(500)
print 'No. of calls %s'%(count)