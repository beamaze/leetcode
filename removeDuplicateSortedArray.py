class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[count] < nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1