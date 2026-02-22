#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 分解问题的思路：将原来的问题分解为两个子问题：
        # if root == None:
        #     return 0
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)
        # return max(left_depth, right_depth) + 1

        # 遍历的思路：遍历所有节点，不断更新维护全局变量：
        # 定义全局变量ans：
        ans = 0
        # 定义遍历函数：
        def f(node, cnt):
            # base case：
            if node is None:
                return
            # 每次遍历到一个节点cnt需要+1（cnt含义：当前正在遍历节点所处的深度）：
            cnt +=1
            # 更新全局变量ans：
            nonlocal ans
            ans = max(ans, cnt)
            # 递归调用，先后遍历当前节点的左右节点：
            f(node.left, cnt)
            f(node.right, cnt)
        
        # 执行遍历函数：
        f(root, 0)
        return ans


        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

