
#select smallest at each loop and keep on adding


def selectionSort( x ):

	for i in range(len(x)):			
		for j in range(len(x)):
			if x[i] < x[j]:
				x[i], x[j] = x[j], x[i]
	return x 

print selectionSort([64, 25, 12, 22, 11])