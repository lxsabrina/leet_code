#solution https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
import numpy as np
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        copy = copy.deepcopy(nums)
        tmp = np.zeros(n)
        return self.reversePairs(copy, 0, n-1, tmp)


    # nums[left..right] 计算逆序对个数并且排序
    def reversePairs(self,nums,left, right, tmp) -> int:
        if left == right: return 0
        mid = (left + (right-left))//2
        if nums[mid] <= nums[mid+1]: return leftPairs + rightPairs 
        leftPairs = self.reversePairs(nums, left, mid, tmp)
        rightPairs = self.reversePairs(nums, mid+1, right, tmp)
        crossPairs = self.mergeAndCount(nums, left, mid, right,tmp)
        return leftPairs + rightPairs + crossPairs

    # nums[left...mid] 有序，nums[left ...mid] 有序
    def mergeAndCount(self, nums, left, right, tmp)-> int: #计算逆序数的个数就在合并过程中。先划分，再合并。(后调用的方法先执行，方法栈 后进先出)
        tmp[left:right] = nums[left:right]   #辅助数组上比较大小，否则nums被重写，无法比较。
        i ,j ,count, k = left,  mid+1,0, left
        while k <= right:
            if i == mid+1:
                nums[k] = tmp[j]
                j +=1
            elif j == right+1:
                nums[k] = tmp[i]
                i +=1
            elif tmp[i] <= tmp[j]: 
                nums[k] = tmp[i]
                i +=1
            else:
                nums[k] = tmp[j]
                j +=1
                count += (mid -i +1)
        return count


