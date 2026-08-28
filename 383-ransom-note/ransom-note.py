class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r_l = Counter(ransomNote)
        m_l = Counter(magazine)
        
        for c, num in r_l.items():
            if c not in m_l:
                return False
            if num > m_l[c]:
                return False
        return True

