#
# @lc app=leetcode.cn id=257 lang=python3
# @lcpr version=30400
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from cgitb import reset


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 分析：要求返回所有根节点到叶子结点的路径，
        # 首先考虑使用遍历找到二叉树中所有的叶子结点，找到叶子结点之后更新res；
        # 通过遍历更新结果
        self.traverse(root)
        # 返回：
        return self.res
     
    # init出全局变量：
    def __init__(self):
        # 当前遍历到的节点的路径：
        self.current_path = []
        # 需要返回的结果：所有叶子结点对应的路径：
        self.res = []

    # traverse函数：
    # 函数定义：从根节点出发遍历二叉树同时维护当前路径以及更新res：
    def traverse(self, root):
        # base case:
        if not root:
            return 
        
        # 如果是叶子结点，更新res：
        if not root.left and not root.right:
            # 前序遍历位置：刚来到叶子节点，需要更新当前路径：
            self.current_path.append(str(root.val))
            # 因为当前遍历节点是叶子结点，所以需要更新res：
            self.res.append('->'.join(self.current_path))
            # 后续遍历位置：即将离开叶子结点，需要更新当前路径，供下一步使用：
            self.current_path.pop()
            return

        # 前序遍历位置：刚来到当前节点，更新当前路径；
        self.current_path.append(str(root.val))
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序遍历位置：即将离开当前节点，更新当前位置；
        self.current_path.pop()



# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

