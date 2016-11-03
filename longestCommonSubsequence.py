#Given two strings find the longest common subsequence between them, the sequence should be continuous
# abcd 1abcd1 --> abcd
# abcd 1ab1c1 --> ab 


#recursion with dp
def LCS(s1, s2, d = {}):
    try:
        return d[(s1,s2)]
    except:
        if s2.find(s1) != -1:
            d[(s1,s2)] = s1
            return s1
        if s1 == '':
            d[(s1,s2)] = ''
            return ''
        result1 = LCS(s1[1:], s2)
        result2 = LCS(s1[:-1], s2)
        if len(result1) > len(result2):
            return result1
        else:
            return result2

print LCS('tanmayanganaabcdef', "elepltanmabananaakjlkjkojhanbcorangejant")

#recursion 
def LCS(s1, s2):
    if s2.find(s1) != -1:
        return s1
    if s1 == '':
        return ''
    result1 = LCS(s1[1:], s2)
    result2 = LCS(s1[:-1], s2)
    if len(result1) > len(result2):
        return result1
    else:
        return result2

print LCS('tanmayorandaabcdef', "elepltanmabananaakjlkjkojhanbcorangejant")

#The problem remains same, now the sequence 
# Need not be continuous
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


print LCS2('tanmayorandaabcdef', "anmabannbcorangej")

#DP solution, also need to find out the sequence
#this is wrong
def LCS3( s1, s2):
    row = len(s1)
    col = len(s2)
    T = [ [ 0 for _ in range(col)] for _ in range(row)  ]
    for i in (range(1,row)):
        for j in range( 1,col):
            if s1[i-1] == s2[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max( T[i-1][j], 
                               T[i][j-1] )
    return T

T =  LCS3('tanmayorandaabcdef', "anmabannbcorangej")
print T[-1][-1]

def constructSequence(T, s1):
    result=''
    i = len(T) -1 #row
    j = len(T[0]) -1 #col
    print i, j
    while i >= 0 and j >= 0:
        print i, j        
        if T[i][j] == T[i-1][j-1] +1:
            result += s1[i]
        i -= 1
        j -= 1
    return result[::-1]

print constructSequence(T, 'tanmayorandaabcdef')

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