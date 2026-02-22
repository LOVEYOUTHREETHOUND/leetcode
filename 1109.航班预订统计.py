#
# @lc app=leetcode.cn id=1109 lang=python3
# @lcpr version=30307
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 初始化航班数组：
        nums = [0] * n
        # 初始化差分数组：
        diff = [0] * n
        for i in range(1, n):
            diff[i] = nums[i] - nums[i - 1]

        # 根据bookings对差分数组进行增减处理：
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            diff[i] += booking[2]
            if j + 1 < n:
                diff[j + 1] -= booking[2]

        # 根据处理之后的差分数组以及原航班数组nums还原answer数组：
        answer = [0] * n
        for i in range(n):
            if i == 0:
                answer[i] = diff[i]
            else:
                answer[i] = answer[i - 1] + diff[i]

        return answer
        





#
# @lcpr case=start
# [[1,2,10],[2,3,20],[2,5,25]]\n5\n
# @lcpr case=end

# @lc code=end


# @lcpr case=start
# [[1,2,10],[2,2,15]]\n2\n
# @lcpr case=end

# @lc code=end




