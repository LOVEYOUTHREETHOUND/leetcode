#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30400
#
# [322] 零钱兑换
#

# @lc code=start
"""
分析：本题属于动态规划问题，直接使用dp table进行自底向上的穷举：
1、dp table的定义是什么？
2、dp[0]是什么？
3、应该如何进行状态转移？
""" 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 定义dp table：dp[i]表示凑足i元需要的硬币数目：
        dp = [amount + 1] * (amount + 1)
        # 初始化dp[0]:凑足零元需要0个硬币：
        dp[0] = 0
        # 自底向上进行状态转移：
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        # 返回：
        return -1 if dp[amount] == amount + 1 else dp[amount]
# @lc code=end



#
# @lcpr case=start
# [1,2,5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

