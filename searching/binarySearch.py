
#binary search using recursion. 
def binarySearch( numbers, number, index=0 ):
	#prints the index of the number in the list of numbers

	size = len(numbers)

    #there is no need for base condition
	'''
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
	'''
	if size % 2 == 0:
		index = (size /2) - 1 
	else:
		index = (size/2)  


	try:
		mid = numbers[index]
		if mid == number:
			return index
		elif number > mid:
			#right search
			return binarySearch( numbers[index+1:], number, index) + 1
		else:
			#left search
			return  binarySearch( numbers[:index], number, index) 
	except:
		pass


print (binarySearch( [5,10,20,30,40,60,73,80,90], 20))




