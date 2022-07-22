#定义 f(i）跳到i位置的最小数据, 有以下状态方程：
# 1、 f(i) = f(j) +  1  ( num[j] >= i-j )  （从j条过来）或者直接跳转到i。
class Solution:
    def jump_v1(self, nums: List[int]) -> int:
        n = len(nums)
        f = [99999] * (n+1)
        f[0] ,f[1]=0, 0  #从前往后遍历一次就可以
        for i in range(1, n+1):
            x = 0 
            for j in range(1,i):    #从前往后找到一个就break
                if nums[j-1] >= i-j: 
                    x = f[j] + 1
                    break
            f[i] = x
        print(nums)
        print(n)
        print(f)
        return f[n]
    
    def jump_v2(self, nums: List[int]) -> int:
        n = len(nums)
        f = [99999] * (n+1)
        f[0] ,f[1]=0 ,0    #从前往后遍历一次就可以
        for i in range(1, n+1):
            steps = nums[i-1]
            left = i + 1 
            right = i + steps
            if right > n : right = n 
            for k in range(left, right+1):
                f[k] = min(f[k], f[i] + 1)
                
        print(nums)
        print(n)
        print(f)
        return f[n]

    def jump_v3(self, nums:List[int]) -> int:
        right, step,max_windows = 0 , 0 ,0
        if len(nums) ==1 : return 0  #如果只有一个元素，不需要跳跃
        for i  in range(0, len(nums)):
            max_windows = max(max_windows, i + nums[i]) #计算下一个跳跃区间最大右边界,先计算max_windows
            if i == right and i < len(nums)-1:     #最后一个不用跳了
                step += 1   #进入下一个跳跃区间
                right = max_windows
            print("i %d value %d right %d, step %d, max_windows %d " % (i , nums[i],right,step, max_windows))
        return step 

    
    def jump(self, nums: List[int]) -> int:
        return self.jump_v3(nums)
    
    
def generate_test_case():
    examples = list()
    input = [2,3,1,1,4]
    output =2 
    examples.append([input,output])
    return examples

if __name__ == "__main__":
    s = Solution()
    ex = generate_test_case()
    no = 0 
    for input, output in ex:
        no += 1
        ans = s.jump(input)
        if ans == output: print("case %d success" % no)
        else:print("case %d Failed" % no)
