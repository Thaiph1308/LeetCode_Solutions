coins = [1,3,5,2]
amount = 11
mem = {}
MAX = float('inf')
# def top_down(coins,amount):
#     if (amount < 0):
#         return MAX
#     if (amount == 0):
#         return 0
#     if (amount) not in mem:   
#         min_amount = [] 
#         for i in coins:
#             a = top_down(coins,amount-i)
#             b = a+1 if a != -1 else MAX
#             print(b)
#             min_amount.append(b)
#         if min(min_amount) == float('inf'):
#             mem[amount] = -1
#         else:
#             mem[amount] = min(min_amount)
#         print("amount = {}, with i = {}, so min_amount = {}, mem= {}".format(amount,i,min_amount,mem))
#     return mem[amount]

def bottom_up(coins,amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 
    count = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            count = count + 1
            dp[x] = min(dp[x], dp[x - coin] + 1)
    print(dp)
    print(count)
    return dp[amount] if dp[amount] != float('inf') else -1 

print(bottom_up(coins,amount))