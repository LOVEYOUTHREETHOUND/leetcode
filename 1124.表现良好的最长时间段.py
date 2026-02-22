#
# @lc app=leetcode.cn id=1124 lang=python3
# @lcpr version=30307
#
# [1124] 表现良好的最长时间段
#
# https://leetcode.cn/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (41.91%)
# Likes:    590
# Dislikes: 0
# Total Accepted:    59K
# Total Submissions: 140.8K
# Testcase Example:  '[9,9,6,0,6,6,9]\n[6,6,6]'
#
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 
# 请你返回「表现良好时间段」的最大长度。
# 
# 
# 
# 示例 1：
# 
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 
# 示例 2：
# 
# 输入：hours = [6,6,6]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= hours.length <= 10^4
# 0 <= hours[i] <= 16
# 
# 
#

# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 根据hours初始化前缀和数组（劳累记为1，不劳累记为-1）：
        n = len(hours)
        preSum = [0] * (n + 1)
        # 创建哈希表（键：前缀和的值；值：值对应的最早的前缀和的数组索引）：
        valToIndex = {0: 0}
        ans = 0
        # 填充前缀和数组：
        for i in range(1, n + 1):
            # 计算当前索引对应的前缀和：
            preSum[i] = preSum[i - 1] + (1 if hours[i - 1] > 8 else -1)
            # 更新哈希表：
            if preSum[i] not in valToIndex:
                valToIndex[preSum[i]] = i
            else:
                pass
        
            # 查找是否有对应满足条件（比当前前缀和小，因为presum变化是连续的，所以只需找 preSum[i] - 1）的已出现的前缀和：
            if preSum[i] > 0:
                ans = i
            else:
                need = preSum[i] - 1
                if need in valToIndex:
                    ans = max(i - valToIndex[need], ans)
        
        # 返回：
        return ans
# @lc code=end



#
# @lcpr case=start
# [9,9,6,0,6,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,6]\n
# @lcpr case=end

#

