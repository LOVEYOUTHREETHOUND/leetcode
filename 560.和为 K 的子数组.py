#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30307
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (46.07%)
# Likes:    3019
# Dislikes: 0
# Total Accepted:    967.5K
# Total Submissions: 2.1M
# Testcase Example:  '[1,1,1]\n2\n[1,2,3]\n3'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 
# 子数组是数组中元素的连续非空序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 
# 
# 示例 2：
# 
# 输入：nums = [1,2,3], k = 3
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 构造前缀和数组：
        n = len(nums)
        preSum = [0] * (n + 1)
        ans = 0

        # 构造哈希表（键：前缀和的值；值：前缀和出现的次数）：
        valToCount = {0: 1}
        # 填充前缀和数组，同时更新哈希表并完成对ans的更新：
        for i in range(1, n + 1):
            # 填充前缀和数组：
            preSum[i] = preSum[i - 1] + nums[i - 1]

            # 先检查以当前位置为子数组的结尾时，有没有满足条件的子数组：
            need = preSum[i] - k
            if need in valToCount:
                ans += valToCount[need]


            # 更新哈希表：
            if preSum[i] not in valToCount:
                valToCount[preSum[i]] = 1
            else:
                valToCount[preSum[i]] += 1
                

        # 返回：
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

