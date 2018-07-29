class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        keypad = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        succ = []
        for k in keypad[digits[0]]:
            succ.append(k)
        digits = digits[1:]
        while digits:
            news = []
            for s in succ:
                for l in keypad[digits[0]]:
                    news.append(s+l)
            succ = news
            digits = digits[1:]
        return succ
