#
# @lc app=leetcode.cn id=1022 lang=python3
# @lcpr version=30400
#
# [1022] 从根到叶的二进制数之和
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
1、要求找出所有叶子节点的路径对应的二进制数对应的数字并返回所有路径的和；
2、如何进行二进制数的加减？
"""
class Solution:
    def __init__(self) -> None:
        # 存储当前遍历到的节点对应路径对应的二进制数值：
        self.current_path = 0
        # 存储需要返回的结果（所有路径对应二进制数的和）：
        self.ans = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 调用traverse函数：
        self.traverse(root)
        # 返回：
        return self.ans
    
        
    def traverse(self, root):
        # base case：
        if not root:
            return
        # 前序位置：刚到达节点，需要更新当前路径对应的二进制数值：
        self.current_path = self.current_path << 1 | root.val
        self.traverse(root.left)
        self.traverse(root.right)
        # 如果是叶子结点，需要更新ans：
        if not root.left and not root.right:
            self.ans = self.ans + self.current_path
        # 后续位置：即将离开节点，需要更新当前路径对应的二进制数值：
        self.current_path = self.current_path >> 1

# @lc code=end



#
# @lcpr case=start
# [1,0,1,0,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

