class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        right = 0
        last = {}
        best = 0
        for i, c in enumerate(s):
            if c in last and last[c] >= left: left = last[c] + 1
            last[c]=i
            right = i
            if right - left + 1 > best: best = right - left + 1
        return best