class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        s_c = Counter(s)
        
        for l in t:
            if l not in s_c or s_c[l] == 0:
                return l
            s_c[l] -= 1
        return ""
            
