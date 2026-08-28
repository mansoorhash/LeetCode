class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_i = 0
        t_i = 0

        for c in s:
            s_i += ord(c)

        for c in t:
            t_i += ord(c)
        return chr(t_i-s_i)