#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30400
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 分析：因为要求对题给二叉树进行原地处理，所以不能使用1、对二叉树进行前序遍历；2、根据前序遍历结果构造链表；的解法；
        # 所以使用“分治”进行解决；

        # 给出函数定义：输入一个根节点，就将该根节点对应的二叉树按照前序遍历结果转变为链表；
        # 边界处理：
        if not root:
            return
        # 分治左孩子与右孩子：
        self.flatten(root.left)
        self.flatten(root.right)
        # 将结果合并：
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right
# @lc code=end



#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

