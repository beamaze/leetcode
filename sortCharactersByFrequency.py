class Solution:
    def frequencySort(self, s: str) -> str:
        
        from collections import Counter
        
        c = Counter(s)
        
        heap = [ (-v, k) for k, v in c.items()]
        
        heapq.heapify(heap)
        
        res = []
        
        while heap:
            v, k = heapq.heappop(heap)
            res += [k]* -v
        return ''.join(res)