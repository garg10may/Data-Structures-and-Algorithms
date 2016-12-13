'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], 
write a function search(char pat[], char txt[])
that prints all occurrences of pat[] in txt[].
You may assume that n > m.
'''


# This looks fine, worst case ~O(2nm) , O((m+m) * (n-m+1))
# m+m --> for slicing and comparision
# n-m+1 --> number of times the loop will
def find(s1, s2):
	size = len(s1)
	index = 0 
	while ( index <= len(s2)):
		if s2[index : index + size] == s1:
			print 'Pattern found at index %s'%(index)
			index += size
		else:
			index += 1

find('AABA', "AABAACAADAABAAABAA")
print 
find('AAAA', 'BAAAAAAAAAAAAAAAAAB')
print 
find("ABABCABAB" ,'ABABDABACDABABCABAB')
print '*'*80


#Found on geeks for geeks, not sure what they are trying to achieve
# Python program for Naive Pattern Searching
# this is also wrong since for second test, it doesn't continue where it left off
# though this is subjective
def search(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one
    for i in xrange(N-M+1):
 
        # For current index i, check for pattern match
        for j in xrange(M):
            if txt[i+j] != pat[j]:
                break
        if j == M-1: # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print "Pattern found at index " + str(i)

print 
search('AABA', "AABAACAADAABAAABAA")
print 
search('AAAA', 'BAAAAAAAAAAAAAAAAAB')
print 
search("ABABCABAB" ,'ABABDABACDABABCABAB')

'''
# looks simple and good, but fails in second case, where it should continue
# from if left off
def find(s1, s2):
	size = len(s1)
	for i in range( len(s2) ):
		s2[i : i + size] == s1
			print 'Pattern found at index %s'%(i)

#find('AABA', "AABAACAADAABAAABAA")
print 
#find('AAAAA', 'AAAAAAAAAAAAAAAAAAAA')
print
'''