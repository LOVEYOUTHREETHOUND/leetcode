#
# @lc app=leetcode.cn id=110 lang=python3
# @lcpr version=30204
#
# [110] 平衡二叉树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 定义内部嵌套功能函数：input根节点：如果当前节点平衡，output对应二叉树的高度；如果当前节点不平衡，return -1：
        def f(node):
            # 边界条件：
            if node is None:
                return 0
            left_height = f(node.left)
            right_height = f(node.right)

            # 如果当前节点不平衡（有三种可能：1、左边节点不平衡；2、右边节点不平衡；3、左右都平衡，但是高度差大于1），返回-1
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            # 递归调用，计算node的左子树与右子树分别的高度、计算、返回结果：
            return max(left_height, right_height) + 1


        # 处理特殊情况： 
        if root is None:
            return True

        return f(root) != -1

        




# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,null,null,4,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

