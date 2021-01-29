class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevDiff = {}
        start = 0
        sum = 0
        
        for i in range(len(s)):
            if s[i] in prevDiff and start <= prevDiff[s[i]]:
                start = prevDiff[s[i]]+1
            else:
                sum = max(sum, i-start + 1)
            
            prevDiff[s[i]] = i
            
        return sum