class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        
        foundLeft = 0
        foundRight = 0
        
        vow = ["a","e","i", "o","u", "A", "E", "I", "O", "U"]
        
        s = list(s)

        while l < r:
            if s[l] in vow and s[r] in vow:
                s[l],s[r] = s[r], s[l]
                l+=1
                r-=1
            if s[l] not in vow:
                l+=1
            if s[r] not in vow:
                r-=1
                
        return ''.join(s)