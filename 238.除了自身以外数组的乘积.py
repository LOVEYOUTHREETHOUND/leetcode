#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30307
#
# [238] 除了自身以外数组的乘积
#
# https://leetcode.cn/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (77.94%)
# Likes:    2181
# Dislikes: 0
# Total Accepted:    895.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4]\n[-1,1,0,-3,3]'
#
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。
# 
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 
# 示例 2:
# 
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 输入 保证 数组 answer[i] 在  32 位 整数范围内
# 
# 
# 
# 
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 根据已知nums数组构造前缀积数组：
        n = len(nums)
        preProduct = [1] * n
        for i in range(1, n):
            preProduct[i] = preProduct[i - 1] * nums[i - 1]
        # 构造后缀积数组（也就是从右到左的“前缀积”数组）：
        sufProduct = [1] * n
        for i in range(n - 2, -1, -1):
            sufProduct[i] = sufProduct[i + 1] * nums[i + 1]
        # 遍历数组，构建结果数组：
        answer = [0] * n
        for i in range(n):
            answer[i] = preProduct[i] * sufProduct[i]
        # 返回：
        return answer

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

