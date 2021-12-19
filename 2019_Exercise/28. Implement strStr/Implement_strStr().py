class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for n in nums:
            if target > n:
                count = count + 1
        return count
    
