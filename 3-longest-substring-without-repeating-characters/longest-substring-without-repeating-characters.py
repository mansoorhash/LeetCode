class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        last = {}
        best = 0
        for i, c in enumerate(s):
            if c in last and last[c] >= left: left = last[c] + 1
            last[c]=i
            if i - left + 1 > best: best = i - left + 1
        return best