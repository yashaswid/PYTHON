'''
Created on Nov 1, 2018

@author: yash
'''

class nonRepeat():
    def nonRepeat(self,s):
        temp=100;
        k=0
        
        dic={}
        for i in s:
            if i in dic:
                dic[i]=dic[i]+1
        
            else:
                dic[i]=1
        print(dic)
                
        for key,value in dic.items():
            if value<temp:
                temp=value
                k=key;
                continue
        return k
    
obj=nonRepeat() 
s="aaccggdeacd"
print(obj.nonRepeat(s))