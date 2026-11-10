class Solution:
    def longestPalindrome(self, s: str) -> str:
        # need to find the center
        max_pal = ""
        if len(s)<2:
            return s

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (r - l + 1) > len(max_pal):
                    max_pal = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (r - l + 1) > len(max_pal):
                    max_pal = s[l:r+1]
                l -= 1
                r += 1

        return max_pal


