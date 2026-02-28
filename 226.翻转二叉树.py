#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30400
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from operator import invert


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 分析：对于二叉树相关问题，分别思考能否从“遍历”以及“分解问题”两个层面去解决问题：
        # 遍历：递归遍历每个节点，遍历到每个节点时，交换其左右子树的位置就可以了；
        # 分治：给出函数定义，根据定义分治完成；

        # “遍历”解法：
        # # base case处理：
        # if not root:
        #     return None
        # # 前序交换左右节点：
        # root.left, root.right = root.right, root.left
        # # 递归处理左右子树：
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # # 返回：
     
# @lc code=end   # return root

        # “分治”解法：
        # 函数定义：输入一个根节点，函数将该根节点对应的树进行翻转并返回根节点；
        # 所以分治为：
        # 1、翻转根节点左子树，返回的是root的左孩子；
        # 2、翻转根节点的右子树，返回的是root的右孩子；
        # 3、交换根节点的左右孩子，完成整个树的翻转；

        # 边界处理：
        if not root:
            return None

        # 翻转左右子树：
        left_done = self.invertTree(root.left)
        right_done = self.invertTree(root.right)

        # 交换根节点的左右孩子：
        root.left = right_done
        root.right = left_done

        # 返回：
        return root



#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

