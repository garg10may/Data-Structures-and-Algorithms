

#backtracking method, 
# we swap a with each character, in first iteration we swap with a itself
# likewise in second we swap with b, now once done, we revert it back and then 
# in third iteration swap it with c
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


#we take each character one by one, and then find all the permutations of remaining
# the trick is in s[:i] + s[i+1]:len(s)], this removes the ith character in each iteration
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
# to check for how that splitting of character is working
s = 'abcd'
for i in range(len(s)):
	print s[0:i] + s[i + 1 : len(s)]







