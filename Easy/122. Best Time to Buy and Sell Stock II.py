#prices = [7,1,5,3,6,4,2,1,5,6,7]
prices = [1,2,3,4,5]
class Solution:
    # def up(self,prices,n):
    #     if (prices[n+1] > prices[n]):
    #         return True
    #     else:
    #         return False
    # def down(self,prices,n):
    #     if (prices[n+1] < prices[n]):
    #         return True
    #     else:
    #         return False
    # def maxProfit(self,prices):
    #     _min = 99999
    #     _max = 0
    #     _profit = 0
    #     _act = ['None']*(len(prices))
    #     for i in range(len(prices)-1):
    #         if (self.up(prices,i)):
    #             _act[i] = 'UP'
    #         if (self.down(prices,i)):
    #             _act[i] = 'DOWN'
    #     for i in range(len(_act)):
    #         if (_act[i] == "UP") and ((_max == -1) or (i == 0)):
    #             _max = i
    #         if (_act[i] == "DOWN" or _act[i] == 'None') and (_max > -1):
    #             _min = i
    #             #print(_min,_max)
    #             _profit = _profit + prices[_min] - prices[_max]
    #             print(_max,_min,prices[_min],prices[_max],_profit)
    #             _max = -1 
    #     print(_act,_profit)
    #     return _profit    
#ver 2
    def larger(self,prices,n):
        if (n == len(prices)-1):
            return None
        if (prices[n+1] > prices[n]):
            return True
        else:
            return False
    def maxProfit(self,prices):
        _min = 99999
        _max = 0
        _profit = 0
        for i in range(len(prices)):
            if (self.larger(prices,i) == True) and ((_max ==-1) or (i == 0)):
                _max = i 
            if (self.larger(prices,i) == False or self.larger(prices,i) == None) and (_max > -1):
                _min = i
                _profit = _profit + prices[_min] - prices[_max]
                #print(_max,_min,prices[_max],prices[_min],_profit)
                _max = -1
        return _profit

a = Solution()
print(a.maxProfit(prices))      