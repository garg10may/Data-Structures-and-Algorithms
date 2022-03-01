# -*- coding: utf-8 -*-

#Given two strings find the longest common subsequence between them
# abcd 1abcd1 --> abcd
# abcd 1ab1c1 --> abc

# this is still wrong
def LCS2(s1, s2):

    index1 = 0
    largest = ""
    while index1 != len(s1):
        index2 = 0   
        result = ''        
        for i in s1[index1:]:
            new = s2[index2:]
            if new.find(i) != -1: #it exists
                index2 += new.index(i) + 1
                result += i
        if len(result) > len(largest):
            largest = result
        index1 += 1
    return largest


print LCS2('appleorangekiwi', 'plumorangetomato')

#DP solution, also need to find out the sequence
#this is wrong
def LCS3( s1, s2):
    row = len(s1) + 1
    col = len(s2) + 1
    T = [ [ 0 for _ in range(col)] for _ in range(row)  ]
    for i in (range(1,row)):
        for j in range( 1,col):
            if s1[i-1] == s2[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max( T[i-1][j], 
                               T[i][j-1] )
    return T

T =  LCS3('appleorangekiwibanan', 'xxxxorangekiwixxxx')
print
print 'Using bottom up'
print T[-1][-1]

#this is still wrong, will solve for later
def constructSequence(T, s1):
    result=''
    i = len(T) -1 #row
    j = len(T[0]) -1 #col
    while i >= 0 and j >= 0:       
        if T[i][j] == T[i][j-1] +1: #from above
            result += s1[i]
            i -= 1
            j -= s1[i] + 1
        elif T[i][j] == T[i][j-1]:
            i -= 1
            j = j
    print result
    return result[::-1]

print constructSequence(T, 'appleorangekiwibanan' )
print

#recursive solution for the same, highly inefficent
def lcs_recursive_helper(sequence1, sequence2, index1, index2):
    if (index1 == len(sequence1)) or (index2 == len(sequence2)):
        return 0

    if sequence1[index1] == sequence2[index2]:
        return 1 + lcs_recursive_helper(sequence1, sequence2, index1 + 1, index2 + 1)

    return max(lcs_recursive_helper(sequence1, sequence2, index1 + 1, index2),
               lcs_recursive_helper(sequence1, sequence2, index1, index2 + 1))


def longest_common_subsequence_recursive(sequence1, sequence2):
    return lcs_recursive_helper(sequence1, sequence2, 0, 0)


print lcs_recursive_helper('tanmayorand', "anmabananaaan", 0, 0)


#These should be memorized, once muscle memory is there, it can solve complex
def LCS(s1,s2, d = {}):

    try:
        return d[(s1,s2)]

    except:

        if len(s1)==0 or len(s2)==0:
            return 0

        # if last characters match
        if s1[-1] == s2[-1]:
            d[(s1,s2)] = LCS( s1[:-1], s2[:-1])
            return 1 + d[(s1,s2)]

        else:
            # if don't match, two options, which would cover all scenario
            d[(s1,s2)] = max( LCS( s1[:-1], s2), LCS( s1, s2[:-1]))
            return d[(s1,s2)]


#two options take last from s1 not s2 and 
print LCS( 'appleorangekiwibanan', 'xxxxorangekiwixxxx')