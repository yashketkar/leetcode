class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
            if dict.get(target-num, -1) == -1:
                dict[num] = i
            elif i!=dict.get(target-num, -1):
                return [dict.get(target-num, -1), i]
