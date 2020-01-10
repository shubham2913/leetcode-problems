class Solution:
    def myAtoi(self, str):
        if len(str)==0 :
            return 0
        i=0
        for i in range(len(str)) :
            if str[i]!=" " :
                break
        if i==len(str) :
            return 0
        int_list=['0','1','2','3','4','5','6','7','8','9']
        if str[i]!='+' and str[i]!='-' and str[i] not in int_list :
            return 0
        minus_flag=0
        plus_flag=0
        if str[i]=="-" :
            i+=1
            minus_flag=1
        elif str[i]=="+" :
            i+=1
            plus_flag=1
        j=i
        while j < len(str) :
            if str[j] not in int_list :
                break
            j+=1
        if j==i :
            return 0
        if minus_flag==1 :
            if -1*int(str[i:j]) < -2**31 :
                return -2**31
            else :
                return -1*int(str[i:j])
        else :
            if int(str[i:j]) > 2**31-1 :
                return 2**31-1
            else :
                return int(str[i:j])