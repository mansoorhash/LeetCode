class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        from collections import Counter
        h = Counter(s)
        last_seen = float('inf')
        for i in range(len(s)):
            if h[s[i]] == 1 and i < last_seen:
                last_seen = i
        return last_seen if last_seen != float('inf') else -1


