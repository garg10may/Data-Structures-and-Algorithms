'''
Given a distance 'dist', count total number of ways to cover the distance with 1,2 and 3 steps. 
'''


#Top down
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
print totalSteps(10)
print 'No. of calls %s'%(count)

def totalSteps(n):

	global count
	count += 1

	d= {}
	d[0] = 1
	d[1] = 1
	d[2] = 2

	for i in range(3,n+1):
		d[i] = d[i-1] + d[i-2] + d[i-3]


	return d[n]

count  =0
print totalSteps(10)
print 'No. of calls %s'%(count)
