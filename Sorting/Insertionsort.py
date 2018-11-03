'''
Created on Nov 3, 2018

@author: yash
'''

def insertionsortpgm(seq):
    for i in range(1,len(seq)):
        max1=seq[i]
        while i > 0 and  seq[i-1]>max1:
            seq[i]=seq[(i-1)]
            i=i-1
        seq[i]=max1
        
        
seq=[2,6,7,3,5]
insertionsortpgm(seq)
print(seq)
