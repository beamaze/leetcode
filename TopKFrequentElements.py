class Solution:
    def topKFrequent(self, nums, k: int):
        index = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in index:
                index[nums[i]] += 1
            else:
                index[nums[i]] = 1
        for i in range(k):
            curMax = max(index, key=index.get)
            res.append(curMax)
            del index[curMax]
        return res