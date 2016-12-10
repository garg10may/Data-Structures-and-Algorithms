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


arr = [1, 2, 3,4,5,6,7,8,9]
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
print count(arr, amount)
print 'No. of calls %s'%(numCalls)

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

        d[(coins, amount)] = count( coins, amount-coins[0]) + count( coins[1:], amount)
        return d[(coins, amount)] 

print 
numCalls = 0
print count(tuple(arr), amount)
print 'No. of calls %s'%(numCalls)

#using pure DP
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
arr = [1,2,3,4,5,6,7,8,9]
amount = 50
from pprint import pprint 
pprint (count(arr, amount))