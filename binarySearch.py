



def binarySearch( numbers, number, index=0 ):
	#prints the index of the number in the list of numbers

	size = len(numbers)

	if size==1 and numbers==number:
		return index
	else:
		return -1

	if size % 2 == 0:
		index = size /2 
	else:
		index = (size/2) + 1

	mid = numbers[index - 1]
	if mid == number:
		return index
	elif number > mid:
		#right search
		index += binarySearch( numbers[index:], number, index) 
	else:
		#left search
		index += binarySearch( numbers[:index], number, index) 
	return index


print binarySearch( [4], 4)