#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30400
#
# [300] 最长递增子序列
#
# https://leetcode.cn/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (58.31%)
# Likes:    4177
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 2.5M
# Testcase Example:  '[10,9,2,5,3,7,101,18]\n[0,1,0,3,2,3]\n[7,7,7,7,7,7,7]'
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
# 的子序列。
# 
# 
# 示例 1：
# 
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 
# 
# 示例 2：
# 
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 
# 
# 示例 3：
# 
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
# 
# 
#

# @lc code=start
"""
分析：一维动态规划问题，使用一维dp table进行求解；
1、dp[i]是什么含义：表示以nums[i]结尾的子数组中最长严格递增子序列的长度；
2、如何初始化基础值：dp[0] = 1;
3、如何进行状态转移：如果 nums[j] < nums[i]，说明 nums[i] 可以接在 j 结尾的递增序列后面。
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 初始化dp table,初始化dp table的基础值：
        n = len(nums)
        dp = [1] * n
        # 根据状态转移公式填充dp table：
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # 返回：
        return max(dp)
# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#

