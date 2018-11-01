'''
Created on Oct 31, 2018

@author: yash
'''
li1=[1,1,2,3,3,4,5,5,5]
dic={}
temp=0
k=0
for i in range(0,len(li1)):
    if li1[i] in dic:
        dic[li1[i]]= dic[li1[i]]+1
    else:
        dic[li1[i]]=1
for key,value in dic.items():
    if value>temp:
        temp=value
        k=key
print(" %d is repeated %d times" %(k,temp))

        
        