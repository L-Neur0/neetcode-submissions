class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for p in s:
            if stack and p in mapping and mapping[p] == stack[-1]:
                stack.pop()
            else:
                stack.append(p)

        if not stack:
            return True
        else:
            return False