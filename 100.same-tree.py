#
# @lc app=leetcode.cn id=100 lang=python3
# @lcpr version=30204
#
# [100] 相同的树
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case：比较的两个节点中有空节点：
        if p is None or q is None:
            return p is q
        # 递归调用并返回结果：
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,null,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1]\n[1,1,2]\n
# @lcpr case=end

#

