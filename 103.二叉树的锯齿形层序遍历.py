#
# @lc app=leetcode.cn id=103 lang=python3
# @lcpr version=30400
#
# [103] 二叉树的锯齿形层序遍历
#
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (60.79%)
# Likes:    1011
# Dislikes: 0
# Total Accepted:    495K
# Total Submissions: 813.9K
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1]\n[]'
#
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
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
# -100 <= Node.val <= 100
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 分析：本题还是对二叉树进行层序遍历，但是要求对于每一层返回时按照不同的
        # 顺序（第一层从左往右、第二层从右往左、第三层从左往右），
        # 所以最简单的做法是维护一个代表每层中遍历方向的布尔值，按照这个值决定要不要进行局部变量current_level数组的翻转；
        
        # 边界处理：
        if not root:
            return []
        # 使用FIFO队列进行完成：
        q = collections.deque([root])

        # 表示方向的全局布尔值：
        left_to_right = True

        res = []

        # 只要队列还不是空，就一层一层进行遍历：
        while q:
            sz = len(q)
            current_level = []
            for _ in range(sz):
                cur = q.popleft()
                current_level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if not left_to_right:
                current_level  = current_level[::-1]
            
            # 更换每层的遍历顺序：
            left_to_right = not left_to_right

            # 更新res：
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

