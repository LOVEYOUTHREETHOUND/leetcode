#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30307
#
# [59] 螺旋矩阵 II
#
# https://leetcode.cn/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (69.80%)
# Likes:    1528
# Dislikes: 0
# Total Accepted:    601K
# Total Submissions: 861.2K
# Testcase Example:  '3\n1'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 20
# 
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 结果矩阵大小已经确定.先定义上下左右边界:
        # 上下左右边界的本质含义:边界上还没有被遍历到(也就是说填写元素是应该按照四个边界进行顺时针填写):
        upper = 0
        lower = n - 1
        left = 0
        right = n - 1 
        num = 1
        matrix = [[0] * n for _ in range(n)]

        # num小于n*n的条件下,顺时针遍历进行填写:
        while num <= n * n:
            # 填写上边界:
            if upper <= lower:
                for j in range(left, right + 1):
                    matrix[upper][j] = num
                    num += 1
                upper += 1
            # 填写右边界:
            if right >= left:
                for i in range(upper, lower + 1):
                    matrix[i][right] = num
                    num += 1
                right -= 1
            # 填写下边界:
            if lower >= upper:
                for j in range(right, left - 1, -1):
                    matrix[lower][j] = num
                    num += 1
                lower -= 1
            # 填写左边界:
            if left <= right:
                for i in range(lower, upper - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        # 返回:
        return matrix
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

