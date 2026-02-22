#
# @lc app=leetcode.cn id=304 lang=python3
# @lcpr version=30307
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 需要根据已经给定的矩阵（二维数组）初始化前缀和数组：
        # 前缀和数组含义：当前位置左上角的面积（不包含当前位置所在行列的所有左上角数据点之和）：
        # 计算矩阵行数m、列数n：
        m = len(matrix)
        n = len(matrix[0])
        # 初始化前缀和矩阵：
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        # 填充前缀和矩阵（一行一行进行填充）：
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.preSum[i][j] = self.preSum[i - 1][j] + self.preSum[i][j - 1] + matrix[i - 1][j - 1] - self.preSum[i - 1][j - 1]





    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - self.preSum[row1][col2 + 1] + self.preSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end



#
# @lcpr case=start
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]\n
# @lcpr case=end

#

