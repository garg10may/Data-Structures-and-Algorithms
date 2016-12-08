'''
Given a value N, if we want to make change for N cents,
and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions:
{1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, there are five solutions:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
'''

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


    # Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
amount = 10
print(count(arr, len(arr), amount))
 
# This code is contributed by Bhavya Jain