#
# @lc app=leetcode.cn id=525 lang=python3
# @lcpr version=30307
#
# [525] 连续数组
#
# https://leetcode.cn/problems/contiguous-array/description/
#
# algorithms
# Medium (55.81%)
# Likes:    821
# Dislikes: 0
# Total Accepted:    99.5K
# Total Submissions: 178.2K
# Testcase Example:  '[0,1]\n[0,1,0]\n[0,1,1,1,1,1,0,0,0]'
#
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [0,1]
# 输出：2
# 说明：[0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
# 
# 示例 2：
# 
# 输入：nums = [0,1,0]
# 输出：2
# 说明：[0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。
# 
# 示例 3：
# 
# 输入：nums = [0,1,1,1,1,1,0,0,0]
# 输出：6
# 解释：[1,1,1,0,0,0] 是具有相同数量 0 和 1 的最长连续子数组。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] 不是 0 就是 1
# 
# 
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 构建前缀和数组（将0替换为-1）：
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + (-1 if nums[i - 1] == 0 else 1)
        # 找一段最大的滑动窗口，是的两个端点对应的前缀和一样（寻找方法：使用哈希表进行辅助判断）：
        preSumValue_to_preSumIndex = {}
        ans = 0
        for i in range(n + 1):
            # 如果对应前缀和的值还未出现，就将其添加到哈希记录表中：
            if preSum[i] not in preSumValue_to_preSumIndex:
                preSumValue_to_preSumIndex[preSum[i]] = i
            # 如果对应的前缀和值已经出现，说明已经找到一段合适的数组，不要更新哈希表，更新ans值：
            else:
                ans = max(ans, i - preSumValue_to_preSumIndex[preSum[i]])

        # 返回：
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,1,1,0,0,0]\n
# @lcpr case=end

#

