class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxAreaValue = 0
        i, j = 0, len(height)-1
        while i<j:
            if min(height[i],height[j])*(j-i) > maxAreaValue:
                maxAreaValue = min(height[i],height[j])*(j-i)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxAreaValue
