class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        parts = s.replace("-","").upper()
        r = len(parts)
        res = []
        while r > 0:
            l = max(0,r-k)
            res.append(parts[l:r])
            r = l
        return "-".join(reversed(res))
