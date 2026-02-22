#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30307
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (49.29%)
# Likes:    2747
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.8M
# Testcase Example:  '[100,4,200,1,3,2]\n[0,3,7,2,5,8,4,6,0,1]\n[1,0,1,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
# 示例 2：
# 
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 
# 
# 示例 3：
# 
# 输入：nums = [1,0,1,2]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 将数组nums转为集合方便查找（用途：去重、判存在）：
        set_nums = set(nums)
        # 遍历集合中每个元素，查找是否是连续序列的第一个元素，从而更新序列长度：
        res = 0
        for num in set_nums:
            # 如果num不是序列开头（等价于：num-1在set中），就跳过本次循环：
            if num - 1 in set_nums:
                continue
            # num是序列开头，就一直查找到不连续为止：
            current_length = 1
            while num + 1 in set_nums:
                current_length += 1
                num += 1 
            res = max(current_length, res)
        # 返回：
        return res
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#

