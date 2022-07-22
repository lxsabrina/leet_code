import unittest


class Solution:
    def insert_v1(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x:x[0])
        print(intervals)
        print(newInterval)
        ans = list()
        ans.append(intervals[0])
        print(ans)
        for interval in intervals[1:]:
            print("get interval")
            print(interval)
            if interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1]  = max(interval[1], ans[-1][1])
        return ans

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]: 
        #参考【代码随想录】的解决方案：https://leetcode.cn/problems/insert-interval/solution/57-cha-ru-qu-jian-mo-ni-cha-ru-xiang-jie-by-carlsu/
        index ,ans  = 0, list()
        #第一步，找到要合并区间，停止条件: x > newInterval[0] 
        print(intervals)
        print(newInterval)
        while index < len(intervals) and  intervals[index][1] < newInterval[0]:    #先插入y之前的位置
            ans.append(intervals[index])
            index += 1
        print("after step1 index %d" % index)
        #第二步，找到合并区间，停止条件: y > newInterval[1] ,否则都在区间中
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:   #合并区间
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index +=1
        ans.append(newInterval)
        print("after step2 index %d" % index)
        #第三步：合并之后的区间
        while index<len(intervals): 
            ans.append(intervals[index])
            index += 1
        print("after step3 index %d" % index)  
        print(ans)     
        return ans

def generate_test_case():
    examples = list()
    
    input1,input2,output= [[1,3],[6,9]],[2,5],[[1,5],[6,9]]
    #examples.append([input1,input2, output])

    input1,input2,output= [[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8],[[1,2],[3,10],[12,16]]
    examples.append([input1,input2, output])

    input1,input2,output= [],[5,7],[[5,7]]
    #examples.append([input1,input2, output])

    input1,input2,output= [[1,5]], [2,3], [[1,5]]
    examples.append([input1,input2, output])

    input1,input2,output=[[1,5]],[2,7],[[1,7]]
    #examples.append([input1,input2, output])
    return examples

class Test(unittest.TestCase):
    def Test1(self):
        print("runnning")
        s = Solution()
        #input1,input2,output= [[1,3],[6,9]],[2,5],[[1,5],[6,9]]
        input1,input2,output= [[1,3],[6,9]],[2,5],[[1,5],[6,10]]
        ans = s.insert(input1, input2)
        assert(ans == output)
'''        
if __name__ == "__main__":
    s,ex, no = Solution(), generate_test_case(),0
    for input1, input2, output in ex:
        no, ans = no+1 , s.insert(input1, input2)
        if ans == output: print("case %d success" % no)
        else:
            print("\033[1;31;40m")
            print("case %d Failed" % no)
            print("\033[0m")
'''
if __name__ == "__main__":
    unittest.main()
    
