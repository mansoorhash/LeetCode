class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {"(":")", "{":"}", "[":"]"}
        stack = []
        for p in s:
            if p in pairs:
                stack.append(pairs[p])
            else:
                if not stack or p != stack[-1]:
                    return False
                stack.pop()
        return not stack
            

        