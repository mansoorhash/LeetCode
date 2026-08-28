class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and s[l].lower() not in vowels: l +=1
            while l < r and s[r].lower() not in vowels: r -=1

            if l < r:
                s[l], s[r] = s[r], s[l]
                r -= 1
                l +=1
        return "".join(s)




