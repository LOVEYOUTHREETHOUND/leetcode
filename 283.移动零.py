#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30307
#
# [283] 移动零
#
# https://leetcode.cn/problems/move-zeroes/description/
#
# algorithms
# Easy (63.89%)
# Likes:    2813
# Dislikes: 0
# Total Accepted:    2.2M
# Total Submissions: 3.4M
# Testcase Example:  '[0,1,0,3,12]\n[0]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 
# 示例 2:
# 
# 输入: nums = [0]
# 输出: [0]
# 
# 
# 
# 提示:
# 
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# 
# 进阶：你能尽量减少完成的操作次数吗？
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 初始化快慢指针：
        fast, slow = 0, 0
        n = len(nums)
        # 遍历并执行对应读写操作：
        while fast <= n - 1:
            # 如果fast指针读到的元素不是0，就将其移动到数组的前端：
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # 将末尾所有元素全部赋值为0：
        for i in range(slow, n):
            nums[i] = 0
        # 返回：
        # 本题只需原地修改，无需返回值
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

