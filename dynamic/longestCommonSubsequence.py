# -*- coding: utf-8 -*-

# Given two strings find the longest common subsequence between them
# abcd 1abcd1 --> abcd
# abcd 1ab1c1 --> abc

# this is still wrong
def LCS2(s1, s2):

    index1 = 0
    largest = ""
    while index1 != len(s1):
        index2 = 0
        result = ""
        for i in s1[index1:]:
            new = s2[index2:]
            if new.find(i) != -1:  # it exists
                index2 += new.index(i) + 1
                result += i
        if len(result) > len(largest):
            largest = result
        index1 += 1
    return largest


print(LCS2("xxxaXpplexxx", "yyyapplXeyyy"))  # output should be apple but getting pple

# DP solution, also need to find out the sequence
# this is wrong
def LCS3(s1, s2):
    row = len(s1) + 1
    col = len(s2) + 1
    T = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(1, row):
        for j in range(1, col):
            if s1[i - 1] == s2[j - 1]:
                T[i][j] = 1 + T[i - 1][j - 1]
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    return T


T = LCS3("xxxapplexxx", "yyyappleyyy")
print()
print("Using bottom up")
print(T[-1][-1])

# this is still wrong, will solve for later
def constructSequence(T, s1):
    result = ""
    i = len(T) - 1  # row
    j = len(T[0]) - 1  # col
    while i >= 0 and j >= 0:
        if T[i][j] == T[i][j - 1] + 1:  # from above
            result += s1[i]
            i -= 1
            j -= s1[i] + 1
        elif T[i][j] == T[i][j - 1]:
            i -= 1
            j = j
    print(result)
    return result[::-1]


print(constructSequence(T, "appleorangekiwibanan"))
print()

# recursive solution for the same, highly inefficent
def lcs_recursive_helper(sequence1, sequence2, index1, index2):
    if (index1 == len(sequence1)) or (index2 == len(sequence2)):
        return 0

    if sequence1[index1] == sequence2[index2]:
        return 1 + lcs_recursive_helper(sequence1, sequence2, index1 + 1, index2 + 1)

    return max(
        lcs_recursive_helper(sequence1, sequence2, index1 + 1, index2),
        lcs_recursive_helper(sequence1, sequence2, index1, index2 + 1),
    )


def longest_common_subsequence_recursive(sequence1, sequence2):
    return lcs_recursive_helper(sequence1, sequence2, 0, 0)


print(lcs_recursive_helper("xxxapplexxx", "yyyappleyyy", 0, 0))


# These should be memorized, once muscle memory is there, it can solve complex
global result
result = []
# 18th Sep, 2022, this is incorrect and not working
def LCS(s1, s2, d={}):

    try:
        return d[(s1, s2)]

    except:

        if len(s1) == 0 or len(s2) == 0:
            return 0

        # if last characters match
        if s1[-1] == s2[-1]:
            d[(s1, s2)] = LCS(s1[:-1], s2[:-1])
            return 1 + d[(s1, s2)]

        else:
            # if don't match, two options, which would cover all scenario
            d[(s1, s2)] = max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))
            # print(d)
            return d[(s1, s2)]


# two options take last from s1 not s2 and
print(LCS("xxxapplexxx", "yyyappleyyy"))
# print(''.join(result))


def LCS(s1, s2):
    # create a 2D array to store the results
    T = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                T[i][j] = 1 + T[i - 1][j - 1]
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    return T


print(LCS("xxxapplexxx", "yyyappleyyy"))


# 19th Sep, 2022
# print longest common subsequence, finding the sequence itself not just the length
# the below solution looks so easy but try to get a gist of it
# and Github Copilot wrote it better than me, I was going for a verbose solution
# and trying to pass result in the function itself and later realized that copilot
# has written it right.
#        return max(LCS(s1[1:], s2), LCS(s1, s2[1:]), key=len) , this is the main gist
# you have to visualize how this generates all the permutations which will be used again and again
# just like knapsack problem, you have to visualize the recursion tree and then you will get it
# and even if you get the hang of it, understanding how and what to return where is also important.
# And below link has been suggested by Copilot, AI is going to rule the world
# https://www.youtube.com/watch?v=NnD96abizww
# and  also uncomment print(s1,s2) line than you will understand very high number of recursions
# take place not just 100


def LCS(s1, s2):
    # print(s1, s2)
    if len(s1) == 0 or len(s2) == 0:
        return ""
    elif s1[0] == s2[0]:
        return s1[0] + LCS(s1[1:], s2[1:])
    else:
        return max(LCS(s1[1:], s2), LCS(s1, s2[1:]), key=len)


print(LCS("xxapXplex", "yyappOleyy"))
# print(LCS("appleorange", "appleorange"))

def LCS(s1, s2, result=[]):
    if len(s1) == 0 or len(s2) == 0:
        return result
    elif s1[0] == s2[0]:
        result.append(s1[0])
        return LCS(s1[1:], s2[1:], result)
    else:
        #see how you have made copy of the result. recursive loop will append to same result
        # because the result is passed by reference
        return max(LCS(s1[1:], s2, result.copy()), LCS(s1, s2[1:], result), key=len)
print(LCS("xxapXplex", "yyappOleyy"))

# 20th Sep, 2022
# solving LCS iteratively
# this is working, I was like if I am able to think on paper why I am not able 
# to convert the same in code, iteratively using multiple pointers, tracking where
# am I and using while loops etc. this is working. But yes recursion is best 
# given we can clearly see the same problem is getting repeated
# outer loop is like recursion only, but inner also we have to keep track where
# am I, reset start from here etc. so best is to use recursion

import collections
def LCS(s1, s2):
    result = collections.defaultdict(list)
    while s1:
        outer = 0
        inner = 0
        temp_result = ""
        inner_position = 0

        while outer< len(s1)-1:
            if inner == len(s2):
                outer += 1
                if inner_position:
                    inner = inner_position
                else:
                    inner = 0
            if (s1[outer] == s2[inner]):
                temp_result += s1[outer]
                outer += 1
                inner += 1
                inner_position = inner # to keep track where I left off
            else:
                inner += 1

        result[s1[0]].append(temp_result)
        s1 = s1[1:]
    return result

print(LCS("xapXplexki11w1i0", "yappOley9jki3lwni"))
