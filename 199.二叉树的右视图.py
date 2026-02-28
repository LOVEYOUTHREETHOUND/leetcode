#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30400
#
# [199] 二叉树的右视图
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
1、要求返回二叉树的每一层的最右边的值，所以对二叉树进行层序遍历并将每层的最后一个数组成结果即可；
2、从右到左对二叉树进行层序遍历可以进一步提高效率（？）
"""
import collections
class Solution:
    def __init__(self) -> None:
        # 当前层的所有节点：
        self.currrent_level = []
        # 需要返回的结果：
        self.res = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 对二叉树进行层序遍历并更新结果：
        self.traverse(root)
        # 返回：
        return self.res
    
    # 层序遍历函数：
    def traverse(self, root):
        # 边界处理：
        if not root:
            return
        # 使用FIFO队列进行层序遍历：
        q = collections.deque([root])
        # 只要队列不为空，就一层一层进行遍历：
        while q:
            sz = len(q)
            self.currrent_level = []
            for _ in range(sz):
                cur = q.popleft()
                self.currrent_level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            self.res.append(self.currrent_level[-1])
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

