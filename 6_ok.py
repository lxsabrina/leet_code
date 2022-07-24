import numpy as np
class Solution:
    def convert(self, s:str, numRows:int) -> str:
        if len(s) <= 2 or numRows ==1 : return s  #case "AB" ,1 ;"ABC",1
        ans = ["" for x in range(numRows)]
        i, flag = 0 , -1
        for c in s:
            ans[i]  += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(ans)
