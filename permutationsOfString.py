#For a given string find all the permutations of that string 

#backtracking method, 
# we swap a with each character, in first iteration we swap with a itself
# likewise in second we swap with b, now once done, we revert it back and then 
# in third iteration swap it with c
def find_permutations( x ):
	n = len(x)
	a = list(x)
	def permute( a, l, r):
		if l == r:
			print ''.join(a)
		else:
			for i in range(l, r+1):
				a[l], a[i] = a[i], a[l]
				permute(a, l+1, r)
				a[l], a[i] = a[i], a[l]
	permute(a, 0, n-1)


#we take each character one by one, and then find all the permutations of remaining
# the trick is in s[:i] + s[i+1]:len(s)], this removes the ith character in each iteration
# this is intiutive, like we remove a from abcd, now after a, their should be b, or c, or d. 
# So now we remove b, now after ab, there should be c or d, we remove c, now after abc, ........
def getPermutation(s, prefix=''):
        if len(s) == 0:
                print prefix
        for i in range(len(s)):
                getPermutation(s[0:i] + s[i + 1 : len(s)], prefix + s[i] )

find_permutations('abc')
print
 
getPermutation('abc')
print 

# to get a feel of how that splitting of character is working
s = 'abcd'
for i in range(len(s)):
	print s[:i] ,  s[i + 1 : len(s)]



# this will merge character at all positions for all strings in the stringList
def mergeChar( char, stringList):
	result = []
	for string in stringList:
		for i in range(len(string) + 1):
			result.append(string[:i] + char + string[i : len(string)])
	return result

#this is also intutive, for 'bc' we have just 'bc' and 'cb' and for 'abc', if I insert a in bc and cb i.e.
# abc, bac, bca
# acb, cab, cba, I would have all the combinations
def all_permutations(string):
	if len(string) == 1:
		return [string]
	return mergeChar( string[0], all_permutations(string[1:]) )

print 
print all_permutations('abc')














