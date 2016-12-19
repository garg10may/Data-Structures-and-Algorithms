


def find_permutations( x ):

	n = len(x)
	a = list(x)

	def permute( a, l, r):

		if l == r:
			print ''.join(a),

		else:
			for i in range(l, r+1):
				a[l], a[i] = a[i], a[l]
				permute(a, l+1, r)
				a[l], a[i] = a[i], a[l]

	permute(a, 0, n-1)

def getPermutation(s, prefix=''):
        if len(s) == 0:
                print prefix,
        for i in range(len(s)):
                getPermutation(s[0:i] + s[i + 1 : len(s)], prefix + s[i] )



find_permutations('abc')

print
print 
getPermutation('abc')

print 
print
s = 'abcd'
for i in range(len(s)):
	print s[0:i] + s[i + 1 : len(s)]







