#Given two strings find the longest common subsequence between them, the sequence should be continuous
# abcd 1abcd1 --> abcd
# abcd 1ab1c1 --> ab 

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

def LCS(s1, s2, d = {}):
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


print LCS2('tanmayorandaabcdef', "anmabananaakjlkjkojhanbcorangej")

def LCS3( s1, s2):
    row = len(s1)
    col = len(s2)
    T = [ [ 0 for i in range(col)] for j in range(row)  ]
    for i in (range(1,row)):
        for j in range( 1,col):
            if s1[i-1] == s2[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max( T[i-1][j], 
                               T[i][j-1] )
    return T

T =  LCS3('tanmayorandaabcdef', "anmabananaakjlkjkojhanbcorangej")
print T[-1][-1]

