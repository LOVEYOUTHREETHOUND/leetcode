#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 暴力求解(复杂度太高，无法pass):
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         current_area = (j-i)*min(height[i],height[j])
        #         max_area = max(max_area,current_area)
        # return max_area

        # 双指针法(实际上是贪心)：
        left = 0
        right = len(height)-1
        max_area = (right-left) * min(height[left],height[right])
        while left <= right:
            if height[left] < height[right]:
                left += 1
                current_area = (right-left) * min(height[left],height[right])
                max_area = max(max_area,current_area)
            else:
                right -= 1
                current_area = (right-left) * min(height[left],height[right])
                max_area = max(max_area,current_area)
        return max_area
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

