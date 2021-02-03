class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        
        for i in range(len(T)):
            
            while stack and T[stack[-1]] < T[i]:
                cur = stack.pop()
                res[cur] = i - cur
            
            stack.append(i)
        
        
        return res