
#binary search using recursion. 
def binarySearch( numbers, number, index=0 ):
	#prints the index of the number in the list of numbers

	size = len(numbers)

	if size==2:
		if number == numbers[0]:
			return 0
		elif number == numbers[1]:
			return 1
		else:
			return -999999

	if size==1:
		if number == numbers[0]:
			return 0
		else:
			return -9999999

	if size % 2 == 0:
		index = (size /2) - 1 
	else:
		index = (size/2)  

	mid = numbers[index]
	if mid == number:
		return index
	elif number > mid:
		#right search
		index += binarySearch( numbers[index+1:], number, index) + 1
	else:
		#left search
		index = binarySearch( numbers[:index], number, index) 
	return index


print binarySearch( [10,40,60,73,80,90], 90)




