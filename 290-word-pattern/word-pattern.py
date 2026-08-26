class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()
        if len(pattern) > len(s_split) or len(pattern) < len(s_split): return False
        h = {}
        for i, key in enumerate(pattern):
            if key not in h and s_split[i] in h.values():
                return False
            elif key in h and h[key] != s_split[i]:
                return False
            h[key] = s_split[i]
            
        return True