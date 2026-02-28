#
# @lc app=leetcode.cn id=129 lang=python3
# @lcpr version=30400
#
# [129] 求根节点到叶节点数字之和
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
1、要求所有叶子节点所对应的数字的和，所以使用遍历进行解决；
2、路径对应的数字是前后拼接而成的，所以使用str数据类型进行存储；
"""
class Solution:
    def __init__(self) -> None:
        # 当前路径对应的数字：
        self.current_num = ""
        # 需要返回的结果：一个整数：
        self.ans = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 调用traverse函数更新ans：
        self.traverse(root)
        # 返回：
        return self.ans
    
    # traverse函数：
    # 函数定义：输入root，递归遍历二叉树并更新ans：
    def traverse(self, root):
        # base case:
        if not root:
            return
        # 前序遍历位置：刚来到当前节点，更新当前节点对应路径对应的数字：
        self.current_num += str(root.val)
        # 如果是叶子结点，需要更新ans：
        if not root.left and not root.right:
            self.ans += int(self.current_num)
        self.traverse(root.left)
        self.traverse(root.right)
        # 后续遍历位置：即将离开当前节点，更新当前节点对应路径对应的数字：
        self.current_num = self.current_num[:-1]


# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,0,5,1]\n
# @lcpr case=end

#

