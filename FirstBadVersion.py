# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        
        while l < r:
            mid = l + (r-l)//2
            
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return r