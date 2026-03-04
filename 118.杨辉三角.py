#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30400
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# algorithms
# Easy (78.04%)
# Likes:    1339
# Dislikes: 0
# Total Accepted:    805.6K
# Total Submissions: 1M
# Testcase Example:  '5\n1'
#
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 
# 
# 示例 2:
# 
# 输入: numRows = 1
# 输出: [[1]]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= numRows <= 30
# 
# 
#

# @lc code=start
"""
分析：属于动态规划问题，使用dp table进行求解：
1、dp[i - 1][j - 1]代表什么：代表第i行第j列的数值；
2、应该如何进行dp table的初始化：每行的开头和结尾的那个数都是1；
3、如何进行状态转义：每个数都等于其左上角的数和右上角的数的和；
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 初始化dp table：
        dp = []
        # 填充杨辉三角：
        for i in range(numRows):# i对应的那一行数目应该是i + 1个；
            # 创建当前行：
            row = [1] * (i + 1)
            # 填充当前行除了开头与结尾的位置：
            for j in range(1, i):
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]

            dp.append(row)

        # 返回：
        return dp

# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

