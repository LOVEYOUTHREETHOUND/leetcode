#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30400
#
# [279] 完全平方数
#
# https://leetcode.cn/problems/perfect-squares/description/
#
# algorithms
# Medium (68.37%)
# Likes:    2300
# Dislikes: 0
# Total Accepted:    881.6K
# Total Submissions: 1.3M
# Testcase Example:  '12\n13'
#
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
# 不是。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4
# 
# 示例 2：
# 
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^4
# 
# 
#

# @lc code=start
"""
分析：本题可以拆分，求最值，所以属于动态规划问题，使用一维dp table进行求解：
1、dp[i]是什么含义：表示和为i的完全平方数的最少数目；
2、如何对dp table进行初始化：dp0 = 0；
3、如何进行状态转移：dp[i] = min(dp[i], dp[i - j * j] + 1)；
"""
class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化dp table:
        dp = [float("inf")] * (n + 1)
        # 初始化基础值：
        dp[0] = 0
        # 根据状态转移公式进行dp table的填充：
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        # 返回：
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#

