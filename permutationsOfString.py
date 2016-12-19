


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




find_permutations('apple')










