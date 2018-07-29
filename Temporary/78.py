class Solution(object):
    def backtrack(self, final_list, temp_list, nums, start):
        final_list.append(list(temp_list))
        for i in range(start, len(nums)):
            temp_list.append(nums[i])
            self.backtrack(final_list, temp_list, nums, i+1)
            del temp_list[-1]

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final_list = []
        self.backtrack(final_list, [], nums, 0)
        return final_list
