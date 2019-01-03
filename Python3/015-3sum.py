class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i==0 or nums[i]!=nums[i-1]:
                x = nums[i]
                y = 0 - x
                lo = i+1
                hi = len(nums)-1
                while lo<hi:
                    if nums[lo]+nums[hi]==y:
                        res.append([nums[i],nums[lo],nums[hi]])
                        while lo<hi and nums[lo]==nums[lo+1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi-=1
                        lo+=1
                        hi-=1
                    elif nums[lo]+nums[hi]<y:
                        lo+=1
                    else:
                        hi-=1
        return res
