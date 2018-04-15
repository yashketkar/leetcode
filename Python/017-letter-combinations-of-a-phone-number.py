class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        keypad = {'1':[''], '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z'], '0':['']}
        options = list(keypad[digits[0]])
        if len(digits)>1:
            for d in range(1,len(digits)):
                new_options = []
                for i in options:
                    for j in keypad[digits[d]]:
                        new_options.append(i+j)
                options=new_options
        return options
