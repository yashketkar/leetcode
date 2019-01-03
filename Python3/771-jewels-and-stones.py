class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {}
        for j in J:
            dic[j]=1
        return sum(map(lambda x: x in dic, S))
