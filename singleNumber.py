class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i, val in enumerate(nums):
            if val in dic:
                del dic[val]
            else:
                dic[val] = i
        
        count = list(dic)
        
        return count[0]