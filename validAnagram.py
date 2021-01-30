class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkString = {}
        for i in s:
            if i in checkString:
                checkString[i] += 1
            else:
                checkString[i] = 1
        for i in t:
            if i in checkString:
                checkString[i] -= 1
            else:
                checkString[i] = 1
                
        for key in checkString:
            if checkString[key] != 0:
                return False
        
        return True