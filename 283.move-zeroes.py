#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #解法一：快慢指针
        # slow = 0
        # for fast in range(len(nums)):
        #     if nums[fast] != 0:
        #         nums[slow] = nums[fast]
        #         slow += 1
        # for i in range(slow,len(nums)):
        #     nums[i] = 0
        # return nums



# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

