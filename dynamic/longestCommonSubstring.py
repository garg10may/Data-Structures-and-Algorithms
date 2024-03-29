#Given two strings find the longest common substring between them
# abcd 1abcd1 --> abcd
# abcd 1ab1c1 --> ab 

#recursion with dp
#Comlexity 2^len(s1)
def LCS(s1, s2, d = {}):
    global numCalls
    numCalls +=1
    try:
        return d[s1]
    except:
        if s2.find(s1) != -1: #substring present
            d[s1] = s1
            return s1
        if s1 == '':
            d[s1] = ''
            return ''
        result1 = LCS(s1[1:], s2, d)
        result2 = LCS(s1[:-1], s2, d)
        if len(result1) > len(result2):
            return result1
        else:
            return result2
numCalls = 0
print (LCS('banannaorangekiwiapple', 'appleorangepomengranate'))
print ('Number of calls %s'%(numCalls))

#recursion 
#Complexity 2^len(s1 or s2, whichever is lower)
def LCS2(s1, s2):
    global numCalls
    numCalls += 1
    if len(s1) > len(s2):
        s1,s2 = s2,s1 #to increase efficency, complexity is dependant on the length of S1
    if s2.find(s1) != -1: #string is there
        return s1
    if s1 == '':
        return ''
    result1 = LCS(s1[1:], s2)
    result2 = LCS(s1[:-1], s2)
    if len(result1) > len(result2):
        return result1
    else:
        return result2

numCalls = 0
print
print (LCS2('banannaorangekiwiapple', 'appleorangepomengranate'))
print ('Number of calls %s'%(numCalls))
#try this without the len(s1) > len(s2) condition, it should take few secs
numCalls = 0
print
print (LCS2('appleorangepomengranateExtraLengthAddedButSameNoOfCalls','banannaorangekiwiapple'))
print ('Number of calls %s'%(numCalls))

#recursion
#highly inefficient, found on some website, my computer not able to run it
#also it only calculates the length, not sure what they are tyring to do
def longest_common_string_recursive_helper(str1, str2, pos1, pos2, check_equal):
    if pos1 == -1 or pos2 == -1:
        return 0

    if check_equal:
        if str1[pos1] == str2[pos2]:
            return 1 + longest_common_string_recursive_helper(str1, str2, pos1 - 1, pos2 - 1, True)
        else:
            return 0

    longest = 0     # start (again) to find the longest from the current positions
    if str1[pos1] == str2[pos2]:
        longest = 1 + longest_common_string_recursive_helper(str1, str2, pos1 - 1, pos2 - 1, True)

    return max(longest,
               longest_common_string_recursive_helper(str1, str2, pos1, pos2 - 1, False),
               longest_common_string_recursive_helper(str1, str2, pos1 - 1, pos2, False))


def longest_common_substring_recursive(str1, str2):
    return longest_common_string_recursive_helper(str1, str2, len(str1) - 1, len(str2) - 1, False)


#print longest_common_substring_recursive('banannaorangekiwi', 'appleorangepomengranate')

#DP, matrix method, O(s1 * s2)
def LCS3(s1,s2):
    row = len(s1) + 1 
    col = len(s2) + 1
    maxLength = 0
    T = [ [ 0 for _ in range(col)] for _ in range(row)  ]

    for i in (range(1,row)):
        for j in range( 1,col):
            if s1[i-1] == s2[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
                maxLength = max(maxLength, T[i][j])

    for i, row in enumerate(T):
        for value in row:
            if value == maxLength:
                index = i
                break
    subString = s1[:index][-maxLength:]
    return subString

print() 
print (LCS3('banannaorangekiwip', 'appleorangepomengranate'))