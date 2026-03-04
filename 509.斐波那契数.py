#
# @lc app=leetcode.cn id=509 lang=python3
# @lcpr version=30400
#
# [509] 斐波那契数
#
# https://leetcode.cn/problems/fibonacci-number/description/
#
# algorithms
# Easy (65.59%)
# Likes:    889
# Dislikes: 0
# Total Accepted:    927.7K
# Total Submissions: 1.4M
# Testcase Example:  '2\n3\n4'
#
# 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# 
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 
# 
# 给定 n ，请计算 F(n) 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
# 
# 
# 示例 2：
# 
# 输入：n = 3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
# 
# 
# 示例 3：
# 
# 输入：n = 4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 30
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.memo = []

    def fib(self, n: int) -> int:
        # 调用dp函数，返回结果：
        self.memo = [-1] * (n + 1)
        return self.dp(n)
    
    def dp(self, n: int) -> int:
        # 函数定义：输入一个整数n，递归计算所有节点的数值并将其存入memo中：
        # base case:
        if n == 0 or n == 1:
            return n
        # 如果之前计算过，就直接返回：
        if self.memo[n] != -1:
            return self.memo[n]
        # 递归计算并存入memo中：
        self.memo[n] = self.dp(n - 1) + self.dp(n - 2)
        return self.memo[n]
        
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

