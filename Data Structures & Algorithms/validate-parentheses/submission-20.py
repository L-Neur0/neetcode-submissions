class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            "{": "}", 
            "[": "]", 
            "(": ")"
        }

        for par in s:
            if par in mp:
                stack.append(par)
            else:
                if stack and par == mp[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False