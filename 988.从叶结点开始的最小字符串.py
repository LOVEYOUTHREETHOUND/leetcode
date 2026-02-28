#
# @lc app=leetcode.cn id=988 lang=python3
# @lcpr version=30400
#
# [988] 从叶结点开始的最小字符串
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
1、通过遍历解决；
2、二叉树节点存储的是0-25，怎么将其转化为小写字母a-z？
3、怎么比较两个字符串的字典序大小？
"""
class Solution:
    def __init__(self) -> None:
        # 遍历到的当前节点对应的路径：
        self.current_path = ""
        # 需要返回的字典序最小的路径：
        self.ans = None

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # 调用递归函数：
        self.traverse(root)
        # 返回：
        return self.ans
    
    def traverse(self, root):
        # base case:
        if not root:
            return
        # 前序位置：刚来到当前节点，需要更新当前路径：
        self.current_path = chr(ord("a") + root.val) + self.current_path
        # 如果是叶子结点，需要比较字典序看看要不要更新ans：
        if not root.left and not root.right:
            # 先处理 ans 还未初始化的情况，再比较字典序
            if self.ans is None or self.current_path < self.ans:
                self.ans = self.current_path
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置：即将离开当前节点，需要更新当前路径：
        self.current_path = self.current_path[1:]
# @lc code=end



#
# @lcpr case=start
# [0,1,2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [25,1,3,1,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,null,1,0,null,0]\n
# @lcpr case=end

#

