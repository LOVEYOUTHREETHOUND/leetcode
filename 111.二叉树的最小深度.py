#
# @lc app=leetcode.cn id=111 lang=python3
# @lcpr version=30400
#
# [111] 二叉树的最小深度
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 二叉树的最小深度是从根节点到叶子结点的最短路径上面的节点数；
        # 所以只需要使用层序遍历找出第一个叶子结点，从根节点到该节点的路径就是该二叉树的最小深度；
        # 处理边界：
        if not root:
            return 0
        # 使用FIFO队列进行二叉树的层序遍历：
        q = collections.deque([root])
        depth = 1 # 队列中已经有一个根节点了，所以将当前高度初始化为1
        # 队列不为空时，就一层一层进行层序遍历并1、找第一个出现的叶子节点；2、维护当前深度；
        while q:
            # 当前遍历到的层的节点个数：
            sz = len(q)
            for _ in range(sz):
                # pop节点：
                cur = q.popleft()
                # 加入左右孩子：
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                # 如果是叶子节点，直接return：
                if not cur.left and not cur.right:
                    return depth
            # for循环之后一层二叉树已经遍历完成，需要更新depth：
            depth += 1
        # 返回:
        return depth
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,null,3,null,4,null,5,null,6]\n
# @lcpr case=end

#

