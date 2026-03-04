#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30400
#
# [198] 打家劫舍
#
# https://leetcode.cn/problems/house-robber/description/
#
# algorithms
# Medium (56.28%)
# Likes:    3462
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,3,1]\n[2,7,9,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2：
# 
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#

# @lc code=start
"""
分析：本题是一维动态规划问题，使用dp table进行解题；
1、dp[i]含义是什么：表示前i间房所能偷到的最大金额；
2、怎么初始化dp table：dp[0] = 0; dp[1] = nums[0];
3、怎么进行状态转移：如何转移到dp[i + 1]:对于第i间房，要么偷，要么不偷；
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 初始化dp table：
        n = len(nums)
        dp = [0] * (n + 1)
        # 初始化基础值：
        dp[0] = 0
        dp[1] = nums[0]
        # 根据状态转移公式填充dp table：
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # 返回：
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

