#
# @lc app=leetcode.cn id=398 lang=python3
# @lcpr version=30307
#
# [398] 随机数索引
#
# https://leetcode.cn/problems/random-pick-index/description/
#
# algorithms
# Medium (68.23%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    65K
# Total Submissions: 95.3K
# Testcase Example:  '["Solution","pick","pick","pick"]\n[[[1,2,3,3,3]],[3],[1],[3]]'
#
# 给你一个可能含有 重复元素 的整数数组 nums ，请你随机输出给定的目标数字 target 的索引。你可以假设给定的数字一定存在于数组中。
# 
# 实现 Solution 类：
# 
# 
# Solution(int[] nums) 用数组 nums 初始化对象。
# int pick(int target) 从 nums 中选出一个满足 nums[i] == target 的随机索引 i
# 。如果存在多个有效的索引，则每个索引的返回概率应当相等。
# 
# 
# 
# 
# 示例：
# 
# 输入
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# 输出
# [null, 4, 0, 2]
# 
# 解释
# Solution solution = new Solution([1, 2, 3, 3, 3]);
# solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
# solution.pick(1); // 返回 0 。因为只有 nums[0] 等于 1 。
# solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
# 
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# target 是 nums 中的一个整数
# 最多调用 pick 函数 10^4 次
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        # 使用哈希表记录每个数值对应的所有索引列表
        # 键：数值 val，值：[索引1, 索引2, ...]
        self.val_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.val_to_indices[num].append(i)
        
        # 初始化随机数生成器
        self.rng = random.Random()

    def pick(self, target: int) -> int:
        # 直接从对应的索引列表中随机选一个
        # random.choice 的时间复杂度为 O(1)
        indices = self.val_to_indices[target]
        return self.rng.choice(indices)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end



#
# @lcpr case=start
# ["Solution","pick","pick","pick"]\n[[[1,2,3,3,3]],[3],[1],[3]]\n
# @lcpr case=end

#

