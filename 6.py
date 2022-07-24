#超时
import numpy as np
class Solution:
    def convert(self, s:str, numRows:int) -> str:
        i,j,k,n = 0, 0, 0, len(s)
        #print(s)
        #print(n)
        numCols =  numRows * n 
        #print(numRows)
        #print(numCols)
        array = np.full((numRows,numRows * n ),'')
        while k < n:
            for i in range(0, numRows):
                if k < n :
                    array[i][j] = s[k]
                    #print("11  i %d j %d k %d" %(i,j,k))
                    k = k + 1
            for t in range(1, numRows-1):
                if k < n:
                    j = j + 1 
                    array[numRows-t-1][j] = s[k]
                    #print("22  j %d j %d k %d" %(j,j,k))
                    k  = k + 1
            j = j + 1
            
        result = ""
        for i in range(0, numRows):
            for j in range(0, numCols):
                if array[i][j] != '':
                    result += array[i][j]
        return result

        #https://www.bilibili.com/video/av626554294/
    



                    
            