#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 解法一：暴力求解(time limit)：
        # n = len(height)
        # total = 0
        # for i in range(n):
        #     leftMax = 0
        #     rightMax = 0
        #     for j in range(i):
        #         leftMax = max(leftMax,height[j])
        #     for k in range(i + 1,n):
        #         rightMax = max(rightMax,height[k])
        #     total += max(min(leftMax,rightMax) - height[i],0)
        # return total
        # 解法二：动态规划：
        # 解法三：双指针法(理解双指针法：1、对于左指针，leftMax一定是其左边的最大值，但是rightMax不一定是其右边的最大值；2、对于右指针，rightMax一定是其右边的最大值，但是leftMax不一定是其左边的最大值)：
        n = len(height)
        left = 0
        right = n - 1
        leftMax = 0
        rightMax = 0
        total = 0
        while left < right:
            if height[left] <= height[right]:
                # 为什么要保证始终都在处理较矮的指针？
                # 含义：这时对于左指针来说，leftmax一定是其左边的最大值，rightmax<=其右边的最大值
                total += max(leftMax - height[left],0) 
                leftMax = max(leftMax,height[left])
                left += 1
                
            else:
                # 含义，这是对于右指针来说，rightmax一定是其右边的最大值，leftmax<=其左边的最大值
                total += max(rightMax - height[right],0)
                rightMax = max(rightMax,height[right])
                right -= 1
                
        return total






# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

