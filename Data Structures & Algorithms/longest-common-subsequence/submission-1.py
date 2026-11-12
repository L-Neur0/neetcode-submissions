class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) # rows
        n = len(text2) # columns 

        prev = [0] * (n + 1) # extra column for empty prefix at the beginning 
        cur = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j-1])
                
            prev, cur = cur, prev 

        return prev[n]

