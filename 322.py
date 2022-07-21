#递归直观解决方案 解体思路：解方程   x1 * w1 + x2 * w2 + ... = amount, 要求x1+x2+x3..最小，转化成不同coin的子数据问题，
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0 :return 0
        if len(coins) == 1 : return amount//coins[0] if amount % coins[0] == 0 else -1
        coins,ans  = sorted(coins), 99999
        cur_coin = coins.pop() 
        for k in range(amount//cur_coin,-1,-1):
            sub_amount = amount -k * cur_coin
            if self.coinChange(coins,sub_amount) != -1:
                ans = min(ans, self.coinChange(coins,sub_amount)+k) #注意，递归函数输入值应该是local这一点要注意
                print("amount %d sub_amount %d  k %d cur_coin %d ans %d" %(amount, sub_amount,k, cur_coin,ans))
        if ans == 99999: ans = -1       #找不到
        return int(ans)

#动态规划解法
import numpy as np 
class Solution:
    def coinChange(self, coins: List[int], amount:int) ->int:
        m = len(coins)
        dp = np.full((amount+1, m+1),-1)
        for a in range(1, amount+1):
            if a % coins[0] == 0: dp[a][1] = a //coins[0]
            else: dp[a][1] = -1
        for a  in range(1, amount+1):
            for j in range(1, m+1):
                cur_coin = coins[j-1]
                ans = 9999
                for k in range(a//cur_coin,-1,-1):
                    if dp[a-k*cur_coin][j-1] !=-1:
                        ans = min(ans, dp[a-k*cur_coin][j-1] + k)
                if ans == 9999: ans = -1
                dp[a][j] = ans
        print(dp[amount][m])
