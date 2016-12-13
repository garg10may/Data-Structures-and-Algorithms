# remember '^' : is exclusive-or (bitwise) not power operator

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