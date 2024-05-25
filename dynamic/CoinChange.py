# -*- coding: utf-8 -*-
'''
Given a value N, if we want to make change for N cents,
and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions:
{1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, there are five solutions:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
This is same as finding partitions of a number, just now the arr would hold all the numbers upto that integer
'''

#This code I found on some website, though not very intuitive as I would approach a 
#include and not include problem, there's extra varaiable to keep track of coinsLeft
def count( coins, coinsLeft, amount):

    # we have reached a recursive loop where whole amount has been exhausted, hence solution exists
    if (amount == 0):
        return 1

    # say 2,2,2 for 5, at last iteration amount left would have been -1 there this solution is not feasible
    if (amount < 0):
        return 0

    #amount is left, but there are no coins left 
    if (coinsLeft <= 0 and amount >= 1):
        return 0

    # not including a coin + including a coin, best is form a tree for a simple case
    # when not including, the possible coins to use are now 1 less, but whole amount would be left
    # when including, all coins can be used, but amount got less. 
    return count( coins, coinsLeft-1, amount) + count( coins, coinsLeft, amount - coins[coinsLeft-1] )


arr = [2, 4,7]
m = len(arr)
amount = 50

#print count(arr, len(arr), amount)


#Same as we approach a knapsack problem
def count( coins, amount):

    global numCalls
    numCalls +=1

    if amount == 0:
        return 1 
    if coins == [] or amount <0:
        return 0
    return count( coins, amount-coins[0]) + count( coins[1:], amount)

global numCalls
numCalls = 0
print (count(arr, amount))
print ('No. of calls %s'%(numCalls))

#using DP now
def count(coins, amount, d={}):

    global numCalls
    numCalls += 1
    try:
        return d[(coins, amount)]
    except:
        if amount == 0:
            return 1 
        if coins == () or amount <0:
            return 0

        #this line is most important to understand, Total = take a coin + not take a coin
        d[(coins, amount)] = count( coins, amount-coins[0]) + count( coins[1:], amount)
        return d[(coins, amount)] 

print 
numCalls = 0
print (count(tuple(arr), amount))
print ('No. of calls %s'%(numCalls))

#using pure DP, this is also knowns as bottom up since we are calculating starting for 0,1,2 and reaching higher values
# very effective also able to calculate partitions for 10000. 
# not possible with even with DP recursion
# After 5 year I have no idea why this code is doing, found the below video
# https://www.youtube.com/watch?v=_fgjrs570YE&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=16
# after thinking about it for a while got it, so always note down, it's no use if you forget
# Bottom up DP requires you to see how the recursion was precisely building the complete solution i.e. what kind of 
# subproblems were being created and how they filled the base case hence it's somewhat difficult to write bottom up DP. 
# In Top down (recursion with memoization) you have to write a backtrack solution (which is still hard) and see the state of backtrack solution. 
# Time complexities wise bottom up DP is better since in Top down it requires function calls and therefore implicit stack formation. 
def count( coins, amount):

    row = len(coins)
    col = amount

    T = [ [ 0 for j in range(col+1) ] for i in range(row) ]

    #make first column as 1
    for i in range(row):
        T[i][0] = 1   

    for i in range(row):
        for j in range(1, col + 1):
            if j >= coins[i]:
                T[i][j] = T[i-1][j] + T[i][j - coins[i]]
            else:
                T[i][j] = T[i-1][j]
    return T[i][j]

print 
arr = [2,4,7]
amount = 50
print (count(arr, amount))