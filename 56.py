from ast import In
from distutils.errors import LibError
from heapq import merge
import re
from typing import List


class Solution:
    def merge(self, intervals:List[List[Int]]) ->List[List[Int]]:
        intervals.sort(key=lambda x:x[0])
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1]) #这里result始终都是最后一个数
        return result