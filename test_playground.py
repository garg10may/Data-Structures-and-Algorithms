

def find_coins(coins, sum):
  if len(c?
  if sum ==0:
    return 1
  elif sum <0:
    return 0
  else:
    ways = find_coins(coins[1:], sum) + find_coins(coins, sum-coins[0])
    # ways = find_coins(coins[1:], sum) + find_coins(coins[1:], sum-coins[0]) 
  
  return ways


print(find_coins([1,2,3,4,5,6,7,8,9,10], 10))

