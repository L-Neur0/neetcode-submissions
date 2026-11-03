class Solution:
    def countSubstrings(self, s: str) -> int:
        pals = len(s)

        for i in range(len(s)):
            l, r = i - 1, i + 1
            # odd ones 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pals += 1 
                l -= 1 
                r += 1 
            # even ones 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                    pals += 1 
                    r += 1
                    l -= 1 
               
        return pals