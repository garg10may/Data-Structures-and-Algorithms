'''
Given a number n, print following pattern without using any loop.

Input: n = 16
Output: 16, 11, 6, 1, -4, 1, 6, 11, 16

Input: n = 10
Output: 10, 5, 0, 5, 10
'''

n = 16 
count = 1
while count != 5:
	print n, 
	n -= 5 
	count +=1 
count = 1
while count != 6:
	print n, 
	n += 5
	count +=1 

