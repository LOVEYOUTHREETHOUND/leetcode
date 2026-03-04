#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30400
#
# [70] 爬楼梯
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# algorithms
# Easy (55.57%)
# Likes:    4004
# Dislikes: 0
# Total Accepted:    2.1M
# Total Submissions: 3.8M
# Testcase Example:  '2\n3'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 
# 示例 2：
# 
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
"""
分析：属于动态规划问题，使用dp table进行求解：
1、dp[i]代表什么？
2、状态转移方程？
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始化dp table：dp[i]表示对于i级台阶的方法数目：
        dp = [0] * (n + 1)
        # base case：
        if n <= 2:
            return n
        # 一级台阶有一种到达方式：
        dp[1] = 1
        # 两级台阶有两种到达方式：
        dp[2] = 2
        # 写出状态转移方程：实际上就是斐波那契数列：
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        # 返回：
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

