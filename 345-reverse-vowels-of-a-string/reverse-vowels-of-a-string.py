class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        l = 0
        r = len(s)-1
        while l < r:
            left_c = s[l].lower()
            if left_c in vowels:
                while s[r].lower() not in vowels:
                    r -= 1
                if l > r: break
                move_c = s[r]
                s[r] = s[l]
                s[l] = move_c
                r -= 1
            l += 1
        return "".join(s)




