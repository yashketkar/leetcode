class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            sor = ''.join(sorted(s))
            if sor in dic:
                dic[sor].append(s)
            else:
                dic[sor] = [s]
        return dic.values()
