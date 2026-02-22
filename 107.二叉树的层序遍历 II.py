#
# @lc app=leetcode.cn id=107 lang=python3
# @lcpr version=30400
#
# [107] 二叉树的层序遍历 II
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Medium (75.56%)
# Likes:    854
# Dislikes: 0
# Total Accepted:    419.4K
# Total Submissions: 555K
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1]\n[]'
#
# 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 
# 
# 示例 1：
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[15,7],[9,20],[3]]
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 分析：本题还是二叉树的层序遍历，还是要求一层一层地对二叉树进行层序遍历并分层分组进行返回，但是要求从下到上进行返回，所以只需要将结果翻转即可；
        # 边界处理：
        if not root:
            return []
        # 使用FIFO队列进行完成：
        q = collections.deque([root])

        res = []        
        # 只要队列还不为空，就一层一层进行处理：
        while q:
            # 当前层的节点个数：
            sz = len(q)
            # 重置局部变量用于存储当前层节点的值：
            current_level = []
            # 处理当前节点：
            for _ in range(sz):
                # 取到当前节点：
                cur = q.popleft()
                current_level.append(cur.val)
                # 处理当前节点的左右孩子：
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # 处理完一层之后使用局部变量更新res：
            res.append(current_level)
        # 返回：
        return res[::-1]
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

