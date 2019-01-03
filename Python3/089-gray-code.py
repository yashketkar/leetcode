class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [0]
        for i in range(n):
            results += [x | (1 << i) for x in reversed(results)]
        return results
