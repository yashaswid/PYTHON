'''
Created on Nov 1, 2018

@author: yash
'''

class Find():
    
   
    def funcFind(self,li1,li2):
        i=0
        j=0
        li3=[]
        while i<len(li1) and j<len(li2):
            if li1[i]==li2[j]:
                li3.append(li1[i])
                i+=1
                j+=1
            elif li1[i]>li2[j]:
                j+=1
            else :
                i+=1      
        return li3





li1=[1,2,4,6,8,10]
li2=[1,2,6,9,10]
fobj=Find()
print(fobj.funcFind(li1,li2))
