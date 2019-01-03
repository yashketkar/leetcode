class Solution:
    def backtrack(self, final_list, mod_list, og_list, start):
        for i in range(start, len(og_list)):
            if og_list[i].isalpha() and not og_list[i].istitle():
                mod_list2 = mod_list[:]
                mod_list2[i]=mod_list2[i].upper()
                final_list.append(mod_list2)
                self.backtrack(final_list, mod_list2, og_list, i+1)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S.lower()
        final_list = [list(S)]
        self.backtrack(final_list, list(S), list(S), 0)
        result = [''.join(s) for s in final_list]
        return result
