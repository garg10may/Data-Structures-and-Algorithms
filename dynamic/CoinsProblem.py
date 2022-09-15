# Find the minimum number of coins needed to furnish change for a given amount.
# The amount of respective changes are infinite.
# For example [25,5,1,10,21],63 would need only 3, 21 coins.


def recMC(coinValueList, change, d):
    global coins
    result = []
    if change in d:
        return d[change]
    else:
        if change in coinValueList:
            d[change] = 1
            return 1
        else:
            for i in [c for c in coinValueList if c <= change]:
                numCoins = 1 + recMC(coinValueList, change - i, d)
                result.append(numCoins)
            d[change] = min(result)
            return min(result)


print("starting")
print(recMC([25, 5, 1, 10, 21], 63, {}))
print("end")


def recDC(coinValueList, change, knownResults, knownCoins):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif change in knownResults:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults, knownCoins)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
                knownCoins[change] = i
    return minCoins


knownCoins = [0] * 65
print(recDC([25, 5, 10, 1, 21], 63, {}, knownCoins))
print(knownCoins)

print("-" * 80)


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)


main()
