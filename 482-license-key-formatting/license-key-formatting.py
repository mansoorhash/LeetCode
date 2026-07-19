class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        parts = s.split('-')
        clean = ''.join(parts).upper()
        r = len(clean) - 1
        res = []
        while r > 0:
            k_size = min(k, len(clean))
            res.insert(0,clean[-k_size:])
            
            clean = clean[:-k_size]
            r -= k_size
        if clean:
            res.insert(0, clean)
        return "-".join(res)
