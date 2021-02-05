class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] in inter:
                continue
            else:
                inter[nums1[i]] = 1
        
        for i in range(len(nums2)):
            if nums2[i] in inter:
                res.append(nums2[i])
                del inter[nums2[i]]
            else:
                continue
        return res