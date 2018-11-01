'''
Created on Oct 31, 2018

@author: yash
'''

class Array():

    def searchEle(self,a, x):
        for i in a:
            if i==x:
                return 1
            else:
                
                return 0   
    
    def deleteEle(self, a, z):
        a.remove(z)
        return a

    def insertEle(self,a,y):
        a.insert(1,y)
        return a
        
        

arr=Array()
a=[2,4,1,0,6]
print(arr.searchEle(a,1))
print(arr.insertEle(a,3))
print(arr.deleteEle(a,0))

    
