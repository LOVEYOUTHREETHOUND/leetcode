#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30400
#
# [102] 二叉树的层序遍历
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (70.51%)
# Likes:    2249
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 2.2M
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1]\n[]'
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 
# 
# 示例 2：
# 
# 输入：root = [1]
# 输出：[[1]]
# 
# 
# 示例 3：
# 
# 输入：root = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
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
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 二叉树的层序遍历：要求分组进行层序遍历：
        # 边界处理：
        if not root:
            return []
        # 使用deque（FIFO队列）进行实现：
        q = collections.deque([root])  # 先放入根节点；

        res = []

        # 只要队列还不为空，就一层一层进行处理并进行记录：
        while q:
            # 当前层的节点个数：
            sz = len(q)
            # 定义局部变量，记录当前层节点值：
            current_level = []
            for _ in range(sz):
                # 弹出第一个节点：
                cur = q.popleft()
                # 记录第一个节点：
                current_level.append(cur.val)
                # 处理第一个节点的左右孩子：
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # 处理完一层之后，使用局部变量更新res：
            res.append(current_level)
        # 返回：
        return res
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

