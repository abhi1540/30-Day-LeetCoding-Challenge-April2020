class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        cost = [[None]*(n+1) for i in range(m+1)] 

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    cost[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    cost[i][j] = cost[i-1][j-1] + 1
                else:
                    cost[i][j] = max(cost[i-1][j], cost[i][j-1])
        return cost[m][n]