#
# @lc app=leetcode.cn id=145 lang=python3
# @lcpr version=30400
#
# [145] 二叉树的后序遍历
#
# https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (77.84%)
# Likes:    1269
# Dislikes: 0
# Total Accepted:    979.6K
# Total Submissions: 1.3M
# Testcase Example:  '[1,null,2,3]\n[1,2,3,4,5,null,8,null,null,6,7,9]\n[]\n[1]'
#
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 
# 输出：[3,2,1]
# 
# 解释：
# 
# 
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3,4,5,null,8,null,null,6,7,9]
# 
# 输出：[4,6,7,5,2,9,8,3,1]
# 
# 解释：
# 
# 
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 
# 输出：[]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1]
# 
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 实现后序遍历函数：1、处理当前节点；2、处理左子树；3、处理右子树；4、记录；
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            res.append(node.val)
        # 先从root节点进行处理：
        res = []
        traverse(root)
        # 返回：
        return res
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,null,8,null,null,6,7,9]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

