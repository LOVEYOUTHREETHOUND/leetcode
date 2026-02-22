#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30307
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (54.77%)
# Likes:    2064
# Dislikes: 0
# Total Accepted:    913.6K
# Total Submissions: 1.7M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n[[1,2,3,4],[5,6,7,8],[9,10,11,12]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 矩阵行数,列数,上下左右边界:
        m = len(matrix)
        n = len(matrix[0])
        # 边界含义:边界上的是还没有被取到的最外围元素:
        upper = 0
        lower = m - 1
        left = 0
        right = n - 1
        ans = []
        # 顺时针取值并不断压缩边界:
        while len(ans) < m * n:
            # 第一条线:从左到右遍历取值:
            if upper <= lower:
                for j in range(left, right + 1):
                    ans.append(matrix[upper][j])
                upper += 1
            # 第二条线:从上到下遍历取值:
            if right >= left:
                for i in range(upper, lower + 1):
                    ans.append(matrix[i][right])
                right -= 1
            # 第三条线:从右到左遍历取值:
            if upper <= lower:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[lower][j])
                lower -= 1
            # 第四条线:从下到上遍历取值:
            if left <= right:
                for i in range(lower, upper - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        # 返回: 
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

