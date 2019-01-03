class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        longest = 1
        current = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current += 1
                if longest < current:
                    longest = current
            else:
                current = 1
        return longest
