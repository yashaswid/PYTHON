'''
Created on Nov 2, 2018

@author: yash
'''



def sea(li,fi,first,last):
    
    mid=(first+last)//2
    if li[mid]==fi:
        print(mid)
    elif fi<li[mid]:
        return sea(li,fi,0,mid-1)
    else:
        return sea(li,fi,mid+1,last)
    
    
li=[1,2,3,4,5,6]
fi=5
first=0
ans = sea(li,fi,first,len(li)-1)   
    
    
    
    
    
    

