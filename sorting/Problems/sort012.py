'''
Write a program to sort an array of 0's,1's and 2's in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, First line is number of elements in array 'N' and second its values.

Output: 
Print the sorted array of 0's, 1's and 2's.

Constraints: 

1 <= T <= 100
1 <= N <= 100
0 <= arr[i] <= 2

Example:

Input :

2
5
0 2 1 2 0
3
0 1 0
 

Output:

0 0 1 2 2
0 0 1
'''

testCases = int(raw_input())

for i in range(testCases):

	arrayLength = int(raw_input())

	arr = map(int, raw_input().split(' ') )

	arr.sort()

	' '.join(map(str, arr))