class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        i = 0
        while i<len(str) and str[i]==' ':
            i+=1
        x = i+1 if i<len(str) and str[i] in ['+','-'] else i
        j=0
        for j in range(x, len(str)):
            if not str[j].isdigit():
                j-=1
                break
        if j<0:
            return 0
        if str[x:j+1].isdigit():
            if int(str[i:j+1]) < -2147483648:
                return -2147483648
            elif int(str[i:j+1]) > 2147483647:
                return 2147483647
            else:
                return int(str[i:j+1])
        return 0
