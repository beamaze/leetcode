class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnaDict = {}
        res = []
        
        for i in range((len(s)-len(s)%10)):
            
            sequence = s[i:i+10]
            
            if sequence in dnaDict:
                if dnaDict[sequence] >= 2:
                    continue
                else:
                    res.append(sequence)
                dnaDict[sequence] += 1
            
            else:
                dnaDict[sequence] = 1
        return res