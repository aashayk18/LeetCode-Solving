class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        maximal transactions allowed is K = 2
        """
        
        # 1. init
        n = len(prices)
        T = [[[0] * 2 for _ in range(3)] for _ in range(n+1)]
        
        # no stock
        for k in range(3):
            T[0][k][0] = 0
            T[0][k][1] = float("-inf")
        
        # no transaction
        for i in range(n+1):
            T[i][0][0] = 0
            T[i][0][1] = float("-inf")
            
        # 2. dp update
        for i in range(1, n+1):
            for k in range(1, 3):
                T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i-1])
                T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i-1])
        
        # 3. return
        return T[-1][2][0]
            
