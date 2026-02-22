#
# @lc app=leetcode.cn id=1314 lang=python3
# @lcpr version=30307
#
# [1314] 矩阵区域和
#
# https://leetcode.cn/problems/matrix-block-sum/description/
#
# algorithms
# Medium (73.93%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    36.8K
# Total Submissions: 49.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1\n[[1,2,3],[4,5,6],[7,8,9]]\n2'
#
# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素
# mat[r][c] 的和： 
# 
# 
# i - k <= r <= i + k, 
# j - k <= c <= j + k 且
# (r, c) 在矩阵内。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# 示例 2：
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n, k <= 100
# 1 <= mat[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # 根据已知矩阵mat构建前缀和矩阵：
        # 矩阵行数m、列数n：
        m = len(mat)
        n = len(mat[0])
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        # 填充前缀和矩阵：
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + mat[i - 1][j - 1]
        # 构建结果矩阵：
        answer = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 因为k是固定的，所以需要处理四个角的越界问题：
                leftUpperX = max(0, j - k)
                leftBottomX = max(0, j - k)
                leftUpperY = max(0, i - k)
                rightUpperY = max(0, i - k)
                rightUpperX = min(n - 1,j + k)
                rightBottomX = min(n - 1,j + k)
                rightBottomY = min(m - 1,i + k)
                leftBottomY = min(m - 1,i + k)
                answer[i][j] = preSum[rightBottomY + 1][rightBottomX + 1] - preSum[leftBottomY + 1][leftBottomX] - preSum[rightUpperY][rightUpperX + 1] + preSum[leftUpperY][leftUpperX]
        # 返回：
        return answer
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n2\n
# @lcpr case=end

#

