def check_palindrome(s, d={}):

	try:
		return d[s]
	except:
		if len(s)==0 or len(s)==1:
			return True

		if s[0]==s[-1]:
			if check_palindrome(s[1:-1]):
				d[s] = True
				return True
			else:
				d[s] = False
				return False
		else:
			d[s] = False
			return False

def f(s):

	global longest

	if check_palindrome(s):
		if len(s) > longest[0]:
			longest = (len(s), s)

	if len(s)==0 or len(s)==1:
		pass
	else:
		f(s[1:])
		f(s[:-1])

	return longest

longest = (0,'')
print f('+++678976aba---')

l = ['a','b',1,2,'sap',3,'d']
l = filter(lambda x: type(x)==str, l)
print(l.index('sap'))
