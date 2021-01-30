class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevDiff = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in prevDiff:
                prevDiff[temp].append(i)
            else:
                prevDiff[temp] = [i]
                
        return prevDiff.values()