#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start
from typing import List
# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 使用双指针法，达到 O(n) 时间复杂度和 O(1) 空间复杂度
        if not height:
            return 0

        n = len(height)
        left, right = 0, n - 1
        
        # left_max: 从左边到 left 指针的最高柱子
        # right_max: 从右边到 right 指针的最高柱子
        left_max, right_max = 0, 0
        
        total_water = 0

        while left < right:
            # 核心逻辑：处理较矮的一边
            if height[left] < height[right]:
                # 如果左边的柱子比 left_max 矮，说明可以蓄水
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                # 移动左指针
                left += 1
            else:
                # 如果右边的柱子比 right_max 矮，说明可以蓄水
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                # 移动右指针
                right -= 1
        
        return total_water

# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [42000,0,40000]\n
# @lcpr case=end

#
