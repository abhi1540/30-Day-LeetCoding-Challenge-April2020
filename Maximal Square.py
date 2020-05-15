class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if len(matrix) == 0:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[None]*(n+1) for i in range(m+1)] 
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0 
                
        for i in range(1,m+1):
            for j in range(1,n+1):    
                if matrix[i-1][j-1] == "0":
                    dp[i][j] = 0
                elif matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        maxval = 0
        for i in range(m+1):
            for j in range(n+1):
                if dp[i][j] > maxval:
                    maxval = dp[i][j]
                    
        return maxval ** 2