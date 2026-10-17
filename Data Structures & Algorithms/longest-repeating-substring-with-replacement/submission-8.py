class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res= 0 

        l = 0 
        for r in range(len(s)):
            # add one visit 
            count[s[r]] = 1 + count.get(s[r], 0)
            # when diff > k, not valid window, reset l go on by one. 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 
                l += 1
            res = max(res, r - l + 1)
        return res