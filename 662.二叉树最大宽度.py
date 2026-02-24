#
# @lc app=leetcode.cn id=662 lang=python3
# @lcpr version=30400
#
# [662] 二叉树最大宽度
#
# https://leetcode.cn/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (45.40%)
# Likes:    720
# Dislikes: 0
# Total Accepted:    141.2K
# Total Submissions: 310.7K
# Testcase Example:  '[1,3,2,5,3,null,9]\n[1,3,2,5,null,null,9,6,null,7]\n[1,3,2,5]'
#
# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。
# 
# 树的 最大宽度 是所有层中最大的 宽度 。
# 
# 
# 
# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null
# 节点，这些 null 节点也计入长度。
# 
# 题目数据保证答案将会在  32 位 带符号整数范围内。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [1,3,2,5,3,null,9]
# 输出：4
# 解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。
# 
# 
# 示例 2：
# 
# 输入：root = [1,3,2,5,null,null,9,6,null,7]
# 输出：7
# 解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。
# 
# 
# 示例 3：
# 
# 输入：root = [1,3,2,5]
# 输出：2
# 解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目范围是 [1, 3000]
# -100 <= Node.val <= 100
# 
# 
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
from typing import AnyStr
import collections

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 本题实际上还是使用二叉树的层序遍历进行解题，但是因为徐亚比较得到最大宽度，
        # 所以在FIFO队列中进行节点存储时，需要同时存储一个节点在满二叉树中的索引值；
        # 边界处理：
        if not root:
            return 0
        # 使用FIFO队列进行二叉树层序遍历：
        q = collections.deque([(root, 1)])
        ans = 0
        # 队列不为空时，就一层一层进行处理（计算宽度）：
        while q:
            # 当前层的节点个数：
            sz = len(q)
            left = 0
            right = 0
            for i in range(sz):
                # pop第一个节点：
                cur_node, cur_idx = q.popleft()
                # 处理第一个节点的左右孩子：
                if cur_node.left:
                    q.append((cur_node.left, 2 * cur_idx))
                if cur_node.right:
                    q.append((cur_node.right, 2 * cur_idx + 1))
                # 记录第一个节点以及最后一个节点的索引值：
                if i == 0:
                    left = cur_idx
                if i == sz - 1:
                    right = cur_idx
            # 计算宽度,更新结果：
            ans = max(ans, right - left + 1)

        # 返回：
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,5,null,null,9,6,null,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,5]\n
# @lcpr case=end

#

