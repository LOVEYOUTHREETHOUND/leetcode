#
# @lc app=leetcode.cn id=1094 lang=python3
# @lcpr version=30307
#
# [1094] 拼车
#
# https://leetcode.cn/problems/car-pooling/description/
#
# algorithms
# Medium (53.80%)
# Likes:    443
# Dislikes: 0
# Total Accepted:    132.5K
# Total Submissions: 246.4K
# Testcase Example:  '[[2,1,5],[3,3,7]]\n4\n[[2,1,5],[3,3,7]]\n5'
#
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
# 
# 给定整数 capacity 和一个数组 trips ,  trips[i] = [numPassengersi, fromi, toi] 表示第 i
# 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
# 
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
# 
# 
# 
# 示例 1：
# 
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
# 
# 
# 示例 2：
# 
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 构建车站数组（含义：单行程上每个车站车上对应的人数）：
        stops = [0] * 1001
        # 根据车站数组初始化/构建差分数组：
        diff = [0] * 1001
        # 根据已知条件（三元组数组trips）调整差分数组：
        for trip in trips:
            i = trip[1]
            j = trip[2]
            diff[i] += trip[0]
            diff[j] -= trip[0]
        # 根据调整之后的差分数组更新stops数组：
        for i in range(1001):
            if i == 0:
                stops[i] = diff[i]
            else:
                stops[i] = stops[i - 1] + diff[i]
            
            if stops[i] > capacity:
                return False
        
        return True
        
# @lc code=end



#
# @lcpr case=start
# [[2,1,5],[3,3,7]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,5],[3,3,7]]\n5\n
# @lcpr case=end

#

