#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30204
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 定义isSymmetric内部功能函数：比较两个二叉树是否对称：
        def f(p, q):
            # 边界条件：遍历到空节点：
            if p is None or q is None:
                return p is q
            # 递归调用并返回比较结果：
            return p.val == q.val and f(p.left, q.right) and f(p.right, q.left)

        # 调用以上定义的函数，传入参数为根节点的左节点与右节点（根节点处已经满足轴对称条件）：
        return f(root.left, root.right)

# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

