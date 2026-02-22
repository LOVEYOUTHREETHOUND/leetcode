#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 初始化：
        left = 0
        window_sum = 0
        ans = float('inf')
        # 主循环:
        for right, x in enumerate(nums):
            window_sum += x
            # 左指针不断右移至不满足条件(大于等于target)，更新滑动窗口内：
            while window_sum >= target:
                # 更新满足条件的数组最小长度：
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans


# 1. 时间复杂度是O(n)：
#     right指针一共走n次，left指针最多走n次（不会回退）。
# 2. 空间复杂度是O(1)：
#     只用了几个变量。
# 3. 为什么这道题可以使用滑动窗口（同向双指针）？
#     因为 nums[i] 全是正数，窗口和随右扩单调不减，随左缩单调不增，能保证不漏解且 O(n)。
            
                

# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

