#
# @lc app=leetcode.cn id=958 lang=python3
# @lcpr version=30400
#
# [958] 二叉树的完全性检验
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 还是使用二叉树的层序遍历进行解决：
        # 充分必要条件：只要出现了一个null，那么之后都不应该出现null；
        # 边界处理：
        if not root:
            return True
        # 使用FIFO队列进行二叉树的层序遍历：
        q = collections.deque([root])
        reached_null = False
        # 只要队列不为空，就进行层序遍历：
        while q:
            # pop当前节点：
            cur = q.popleft()
            # apend当前节点的左右孩子：
            if cur:
                q.append(cur.left)
                q.append(cur.right)
            # 处理逻辑：
            if not cur and not reached_null:
                reached_null = True
                continue
            if reached_null and cur:
                return False

        # 返回：
        return True

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,null,7]\n
# @lcpr case=end

#

