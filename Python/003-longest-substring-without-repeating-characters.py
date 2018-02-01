class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        maxLength = 0
        i = 0
        for j in range(len(s)):
            if seen.get(s[j], -1) != -1:
                i = max(seen[s[j]], i)
            maxLength = max(maxLength, j - i + 1)
            seen[s[j]] = j+1
        return maxLength
