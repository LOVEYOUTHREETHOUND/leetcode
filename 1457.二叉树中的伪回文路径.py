#
# @lc app=leetcode.cn id=1457 lang=python3
# @lcpr version=30400
#
# [1457] 二叉树中的伪回文路径
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
1、本题要求找出所有路径中满足“回文”要求的路径并进行返回；
2、直接递归遍历找到所有树叶节点的路径，检查其是不是回文路径，如果是就直接加入ans即可；
3、Q：如何判断一个路径是不是回文路径？
"""
class Solution:
    def __init__(self) -> None:
        # 存储当前节点的路径：
        self.current_path = []
        # 存储需要返回的结果：回文路径的个数：
        self.ans = 0
        # counter数组，记录每个数组出现的次数，用于判断当前路径是不是回文路径：
        self.counter = [0] * 9

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # 调用traverse函数更新ans：
        self.traverse(root)
        # 返回：
        return self.ans

    def traverse(self, root):
        # base case：
        if not root:
            return

        # 前序遍历位置：刚来到当前节点，需要更新当前节点对应的路径：
        self.current_path.append(root.val)
        self.counter[root.val - 1] += 1

        # 如果当前遍历到的节点是叶子结点，需要判断当前路径是不是回文路径，并更新ans:
        if not root.left and not root.right:
            # 根据counter数组判断是否是回文路径并更新ans：
            odd = 0
            for i in range(len(self.counter)):
                if self.counter[i] % 2 == 1:
                    # 出现次数为奇数的数字个数：
                    odd += 1
            if odd <= 1:
                self.ans += 1
    
        self.traverse(root.left)
        self.traverse(root.right)
        
        # 后序遍历位置：即将离开当前节点，需要更新当前节点对应的路径：
        self.current_path = self.current_path[:-1]
        self.counter[root.val - 1] -= 1


        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,3,1,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1,1,3,null,null,null,null,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [9]\n
# @lcpr case=end

#

