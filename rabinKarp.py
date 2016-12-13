#Rabin karp algorithm for string searching 
# remember '^' : is exclusive-or (bitwise) not power operator in python

'''
The algorithm for rolling hash user here is as below. Pattern : 'abc', Text : 'abcd'
Consider 'abc' it's hash value is calcualted using formula a*x^0 + b*x^1 + c*x^2, where x is prime
Now when we need to roll( i.e. find hash of 'bcd'), which should be b*x^0 + c*x^1 + d*x^2, 
instead of calculating it whole , we just subract first character value and add next character value. 
Value of first character would be a*X^0 --> a, so we subract a and divide by prime so that new position becomes
b*x^0 + c*x^1, now we need to add next character, which would be 'd'*x^(patternLength-1), so here 'd'*x^2 so it becomes
b*x^0 + c*x^1 + d*x^2, which is what we need. It's O(1) so very useful for long strings. 

Note:
Here it's recommended to use high value of text characters, therefore use ASCII value for text not just 0,1,2
Also use prime number greater than 100, so that the hash function is good and less collisions are there
'''

def hashValue(pattern, prime):
	value = 0
	for index, char in enumerate(pattern): 
		value += ord(char) * (pow(prime,index))
	return value


def find(pattern , text):

	prime = 3
	m = len(pattern)
	n = len(text)
	p = hashValue(pattern, prime)
	t = hashValue(text[:m], prime)

	for i in range(n-m+1):

		#if hashes are equal
		if p == t:
			#check for each character, since two different strings can have same hash
			for j in range(m):
				if text[i + j] != pattern[j]:
					break

			if j == m-1:
				print 'Pattern found at index %s'%(i)

		#calculate rolling hash
		if i < n-m: # i.e. still some text of lenth m is left
			 t = ((t - ord(text[i])) / prime) +  (ord(text[i + m]) * (pow(prime, (m - 1))))

find('abc', '***abc***111***abc***')