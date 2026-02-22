#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30204
#
# [713] 乘积小于 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window_product = 1
        left = 0
        ans = 0

        if k <= 1:
            return 0

        # 主循环：
        for right, x in enumerate(nums):
            window_product *= x
            while window_product >= k:
                window_product //= nums[left]
                left += 1
            ans += right - left + 1
        
        return ans

# 1. 时间复杂度：O(n)
# 2. 空间复杂度：O(1)
# 3. 为什么一看到这道题就知道用滑动窗口？：右扩单调不减，左缩单调不增
# 4. 几个问题：
#     1. 需要对k进行怎样的讨论？
#     2. 为什么while循环内不会出现left一直向右越过right的情况？


# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

