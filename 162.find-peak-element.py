#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30204
#
# [162] 寻找峰值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2 # [left, right]
        while left <= right:
            M = (left + right) // 2
            if nums[M] < nums[M + 1]:
                left = M + 1
            else:
                right = M - 1
        return left
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#

