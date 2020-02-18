cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
def minCostClimbingStairs(cost):
    f1,f2 = 0,0
    for i in range(len(cost)):
        f1,f2 = min(f1,f2) + cost[i], f1
    return min(f1,f2)

print(minCostClimbingStairs(cost))