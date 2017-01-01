


def lps( pattern):

	lps = [0]
	i = 0
	j = 1

	while ( j < len(pattern)):
		if pattern[j] == pattern[i]:
			lps.append(1 + i)
			i += 1
			j += 1
		else:
			lps.append(0)
			i = 0 # i pointer resets to search for anoather suffix
			j += 1
	return lps

print lps('AABAACAABAA')








