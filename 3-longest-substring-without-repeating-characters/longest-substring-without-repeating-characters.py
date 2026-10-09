class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        best = 0
        l = 0
        h = {}
        for r in range(len(s)):
            if s[r] in h and h[s[r]] >= l:
                l = h[s[r]] + 1
            h[s[r]] = r
            best = max(best, r-l+1)
        return best