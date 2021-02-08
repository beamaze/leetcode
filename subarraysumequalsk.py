from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSumDict = defaultdict(int)
        count = 0
        curSum = 0
        curSumDict[0] = 1
        
        for i in nums:
            curSum += i
            count += curSumDict[curSum - k]
            curSumDict[curSum] += 1
            
        return count