#
# @lc app=leetcode.cn id=971 lang=python3
# @lcpr version=30400
#
# [971] 翻转二叉树以匹配先序遍历
#
# https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/description/
#
# algorithms
# Medium (49.30%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    16.3K
# Total Submissions: 33K
# Testcase Example:  '[1,2]\n[2,1]\n[1,2,3]\n[1,3,2]\n[1,2,3]\n[1,2,3]'
#
# 给你一棵二叉树的根节点 root ，树中有 n 个节点，每个节点都有一个不同于其他节点且处于 1 到 n 之间的值。
# 
# 另给你一个由 n 个值组成的行程序列 voyage ，表示 预期 的二叉树 先序遍历 结果。
# 
# 通过交换节点的左右子树，可以 翻转 该二叉树中的任意节点。例，翻转节点 1 的效果如下：
# 
# 请翻转 最少 的树中节点，使二叉树的 先序遍历 与预期的遍历行程 voyage 相匹配 。 
# 
# 如果可以，则返回 翻转的 所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 [-1]。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [1,2], voyage = [2,1]
# 输出：[-1]
# 解释：翻转节点无法令先序遍历匹配预期行程。
# 
# 
# 示例 2：
# 
# 输入：root = [1,2,3], voyage = [1,3,2]
# 输出：[1]
# 解释：交换节点 2 和 3 来翻转节点 1 ，先序遍历可以匹配预期行程。
# 
# 示例 3：
# 
# 输入：root = [1,2,3], voyage = [1,2,3]
# 输出：[]
# 解释：先序遍历已经匹配预期行程，所以不需要翻转节点。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数目为 n
# n == voyage.length
# 1 <= n <= 100
# 1 <= Node.val, voyage[i] <= n
# 树中的所有值 互不相同
# voyage 中的所有值 互不相同
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
"""
分析：
1、本题要求按照已经给定的前序遍历结果整理已有二叉树；如果能够整理，就返回所有反转过的节点列表；如果不能，就返回列表-1；
2、Q:要想使二叉树符合某个前序遍历结果，应该怎样进行翻转整理？
"""
class Solution:
    def __init__(self):
        # 存储是否整理成功：
        self.can_flip = True
        # 存储翻转过的节点的列表：
        self.res = []
        # 存储当前遍历到的节点的位置：
        self.loc = 0

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        # 调用traverse函数：
        self.traverse(root, voyage)
        # 根据是否整理成功进行不同返回：
        if self.can_flip:
            return self.res
        else:
            return [-1]


    def traverse(self, root, voyage):
        # base case：
        if not root:
            return
        # 前序位置：刚来到节点，需要1、更新当前节点位置；2、比较当前节点值是否符合预期，如果不符合预期，不能继续整理，赋值为False并返回；如果符合预期，需要看左孩子是不是一样，左孩子不符合预期的话就左右子树进行翻转；
        self.loc += 1
        if root.val != voyage[self.loc - 1]:
            self.can_flip = False
            return
        if root.left and root.left.val != voyage[self.loc]:
            self.res.append(root.val)
            root.left, root.right = root.right, root.left

        self.traverse(root.left, voyage)
        self.traverse(root.right, voyage)


# @lc code=end



#
# @lcpr case=start
# [1,2]\n[2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

#

