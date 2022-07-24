#todo: 还有一些bug
import numpy as np
class Solution:

    def randomPartition(self, nums: List[int], l:int, h:int) ->int :
        if h > l :
            pivot = np.random.randint(l,h)    # 核心思想是把pivot的位置空出来，然后用快速排序进行交换
            nums[h], nums[pivot] = nums[pivot], nums[h]
            pivot = h 
            x, h = nums[pivot] , h-1
            while l < h :                       # 核心思想应该是 i和j进行交换
                while nums[l] < x : l = l  + 1 
                while nums[h] > x : h = h  - 1 
                if l < h: nums[h], nums[l] = nums[l], nums[h]
                nums[l],nums[pivot] = nums[pivot], nums[l]
            return l
        else:
            return 0

    def quickSelect(self, nums:List[int],l:int,h:int,index:int ):   # quick是一个递归查找
        q = self.randomPartition(nums, l,h)
        if q == index:
            return nums[q]
        elif q < index:
            return self.quickSelect(nums,q+1,h,index)
        else:
            return self.quickSelect(nums,l,q-1,index)
    
  
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k == 1 :
            return nums[0] 
        else:
            return self.quickSelect(nums,0, len(nums)-1, len(nums)-k)

