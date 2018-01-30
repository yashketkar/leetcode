class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num==0:
            return ["0:00"]
        n_hours = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for n in range(12):
            n_hours[bin(n).count("1")].append(n)
        n_minutes = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for n in range(60):
            n_minutes[bin(n).count("1")].append(n)
        i = 0
        j = num
        output = []
        while i<=num and i<4:
            for h in n_hours[i]:
                for m in n_minutes[j]:
                    output.append(str(h)+":"+str(format(m, '02d')))
            i+=1
            j-=1
        return output