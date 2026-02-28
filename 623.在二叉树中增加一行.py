#
# @lc app=leetcode.cn id=623 lang=python3
# @lcpr version=30400
#
# [623] 在二叉树中增加一行
#
# https://leetcode.cn/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (60.38%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    57K
# Total Submissions: 94.4K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2\n[4,2,null,3,1]\n1\n3'
#
# 给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。
# 
# 注意，根节点 root 位于深度 1 。
# 
# 加法规则如下:
# 
# 
# 给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur
# 的左子树根和右子树根。
# cur 原来的左子树应该是新的左子树根的左子树。
# cur 原来的右子树应该是新的右子树根的右子树。
# 如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val
# 作为整个原始树的新根，而原始树就是新根的左子树。
# 
# 
# 
# 
# 示例 1:
# 
# 
# 
# 输入: root = [4,2,6,3,1,5], val = 1, depth = 2
# 输出: [4,1,1,2,null,null,6,3,1,5]
# 
# 示例 2:
# 
# 
# 
# 输入: root = [4,2,null,3,1], val = 1, depth = 3
# 输出:  [4,2,null,1,1,3,null,null,1]
# 
# 
# 
# 
# 提示:
# 
# 
# 节点数在 [1, 10^4] 范围内
# 树的深度在 [1, 10^4]范围内
# -100 <= Node.val <= 100
# -10^5 <= val <= 10^5
# 1 <= depth <= the depth of tree + 1
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
1、要求按照既定的加法规则，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根；
    所以直接使用遍历即可；
"""
class Solution:
    def __init__(self):
        # 存储当前节点的深度（根节点的深度为1）：
        self.current_depth = 0
        # 需要添加的那一行的深度：
        self.target_depth = 0
        # 需要添加的值：
        self.target_val = 0
        
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # 如果需要插入行的深度为1，单独处理：
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        # 传参：
        self.target_depth = depth
        self.target_val = val
        # 调用traverse函数：
        self.traverse(root)
        # 返回根节点：
        return root

    def traverse(self, root):
        # base case:
        if not root:
            return
        # 前序位置：刚来到当前节点，需要更新当前节点的深度值：
        self.current_depth += 1
        # 判断当前节点的深度值是否满足对应条件，如果满足需要加上新的一行：
        if self.current_depth == self.target_depth - 1:
            new_left = TreeNode(self.target_val)
            new_right = TreeNode(self.target_val)
            new_left.left = root.left
            new_right.right = root.right
            root.left = new_left
            root.right = new_right

        self.traverse(root.left)
        self.traverse(root.right)

        # 后续位置：即将离开当前节点，需要更新当前节点的深度值：
        self.current_depth -= 1
# @lc code=end



#
# @lcpr case=start
# [4,2,6,3,1,5]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,null,3,1]\n1\n3\n
# @lcpr case=end

#

