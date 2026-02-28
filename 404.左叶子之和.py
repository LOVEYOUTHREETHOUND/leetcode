#
# @lc app=leetcode.cn id=404 lang=python3
# @lcpr version=30400
#
# [404] 左叶子之和
#
# https://leetcode.cn/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (64.09%)
# Likes:    800
# Dislikes: 0
# Total Accepted:    402.8K
# Total Submissions: 628.2K
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1]'
#
# 给定二叉树的根节点 root ，返回所有左叶子之和。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入: root = [3,9,20,null,null,15,7] 
# 输出: 24 
# 解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 
# 
# 示例 2:
# 
# 输入: root = [1]
# 输出: 0
# 
# 
# 
# 
# 提示:
# 
# 
# 节点数在 [1, 1000] 范围内
# -1000 <= Node.val <= 1000
# 
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
分析：
1、题目要求返回所有左叶子之和，只需要使用遍历，更新结果即可；
"""
class Solution:
    def __init__(self):
        # 存储所有左节点的和：
        self.ans = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 调用travers函数：
        self.traverse(root)
        # 返回：
        return self.ans

    def traverse(self, root):
        # base case：
        if not root:
            return

        # 前序遍历位置，需要看看root有没有左节点且左节点是不是叶子节点，如果是，需要更新结果：
        if root.left and not root.left.left and not root.left.right:
            self.ans += root.left.val

        self.traverse(root.left)
        self.traverse(root.right)
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

