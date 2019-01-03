class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = []
        for i in range(26):
            counts.append([0,0])
        for i in range(len(s)):
            counts[ord(s[i])-97][0] += 1
            if not counts[ord(s[i])-97][1]:
                counts[ord(s[i])-97][1] = i
        answer = len(s)
        for x in counts:
            if x[0]==1 and x[1]<answer:
                answer = x[1]
        if answer == len(s):
            return -1
        else:
            return answer
