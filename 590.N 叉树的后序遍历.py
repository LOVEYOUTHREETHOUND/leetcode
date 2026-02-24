#
# @lc app=leetcode.cn id=590 lang=python3
# @lcpr version=30400
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 本题要求返回多叉树的后序遍历结果，使用递归遍历进行完成；
        # 实现递归函数：
        res = []
        def traverse(node):
            # base case 处理：
            if not node:
                return
            # 递归遍历所有子节点：
            for child in node.children:
                traverse(child)
            # 后序位置收集节点值：
            res.append(node.val)
        # 调用递归函数、返回：
        traverse(root)
        return res

        
# @lc code=end



#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#

