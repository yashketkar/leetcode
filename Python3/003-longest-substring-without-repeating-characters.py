class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        longest = 0
        seen = {}
        for j in range(len(s)):
            if s[j] in seen:
                 i = max(seen[s[j]],i)
            longest = max(longest, j-i+1)
            seen[s[j]] = j+1
        return longest
