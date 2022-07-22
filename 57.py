class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
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

if __name__ == "__main__":
    s,ex, no = Solution(), generate_test_case(),0
    for input1, input2, output in ex:
        no, ans = no+1 , s.insert(input1, input2)
        if ans == output: print("case %d success" % no)
        else:
            print("\033[1;31;40m")
            print("case %d Failed" % no)
            print("\033[0m")
    
