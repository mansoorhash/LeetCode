class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        m_l = Counter(magazine)
        
        for c in ransomNote:
            if c not in m_l:
                return False
            if m_l[c] == 0:
                return False
            m_l[c] -= 1
        return True

