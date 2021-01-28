class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        
        curSum = 0
        maxSum = 0
        
        while i < j:
            curSum = (j - i)* min(height[i], height[j])
            maxSum = max(curSum, maxSum)
            
            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
                
        return maxSum
            