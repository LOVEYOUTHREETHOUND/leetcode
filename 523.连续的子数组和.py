#
# @lc app=leetcode.cn id=523 lang=python3
# @lcpr version=30307
#
# [523] 连续的子数组和
#
# https://leetcode.cn/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (29.62%)
# Likes:    648
# Dislikes: 0
# Total Accepted:    128.1K
# Total Submissions: 432.3K
# Testcase Example:  '[23,2,4,6,7]\n6\n[23,2,6,4,7]\n6\n[23,2,6,4,7]\n13'
#
# 给你一个整数数组 nums 和一个整数 k ，如果 nums 有一个 好的子数组 返回 true ，否则返回 false：
# 
# 一个 好的子数组 是：
# 
# 
# 长度 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 
# 
# 注意：
# 
# 
# 子数组 是数组中 连续 的部分。
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终 视为 k 的一个倍数。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
# 
# 示例 2：
# 
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
# 
# 
# 示例 3：
# 
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 构建前缀和数组：
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        # 构建哈希表数据结构用于辅助查找（键：除以k的余数；值：对应前缀和数组的索引）：
        modToIndex = {}
        for i in range(n + 1):
            if preSum[i] % k not in modToIndex:
                modToIndex[preSum[i] % k] = i
            else:
                if i - modToIndex[preSum[i] % k] >= 2:
                    return True
                else:
                    continue
            
        # 返回：
        return False
# @lc code=end



#
# @lcpr case=start
# [23,2,4,6,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n13\n
# @lcpr case=end

#

