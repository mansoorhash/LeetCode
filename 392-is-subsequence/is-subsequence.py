class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        s_point = 0
        t_point = 0

        while t_point < len(t):
            if s[s_point] == t[t_point]:
                s_point += 1
                if s_point == len(s): 
                    return True

            t_point += 1
        
        return False