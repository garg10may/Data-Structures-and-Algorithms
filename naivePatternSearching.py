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
	for i in range( len(s2) -size + 1 ):
		if s2[i : i + size] == s1:
			print 'Pattern found at index %s'%(i)

find("ABABCABAB" ,'ABABDABACDABABCABAB')


#checking by each character, if any character is mismatched be break
#if it's not the count of J should be equal to length of pattern, we check and print
def search(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one
    for i in xrange(N-M+1):

    	status = 1 
        for j in xrange(M):
            if txt[i+j] != pat[j]:
            	status = 0
                break
        if j == M-1 and status != 0: # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print "Pattern found at index " + str(i)

print 
search("ABABCABAB" ,'ABABDABACDABABCABAB')

testString = ''.join([ 'a' for _ in range(1000*100)] ) + 'b'
testPattern = ''.join([ 'a' for _ in range(100*100) ])  + 'b'

search(testPattern, testString)
find(testPattern, testString)
