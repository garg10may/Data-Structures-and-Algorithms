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
print (totalSteps(10))
print ('No. of calls %s'%(count))

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
print (totalSteps(10))
print ('No. of calls %s'%(count))

#no idea what you are doing in the above solutions
#2nd March 2022, it's clearly a 0/1 knapsack problem

def totalSteps3(coins, amount):
	if amount == 0:
		return 1
	if coins == [] or amount <0:
		return 0
	#take one + not take one i.e 0/1 knapsack
	return totalSteps3(coins, amount- coins[0]) + totalSteps3( coins[1:], amount)

print (totalSteps3([1,2,3], 10))
# lol, output is 14 which is incorrect, I think it's due the fact that person is drunk and 
# can come back also

