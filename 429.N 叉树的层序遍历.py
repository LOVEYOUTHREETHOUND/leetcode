#
# @lc app=leetcode.cn id=429 lang=python3
# @lcpr version=30400
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 分析：本题要求返回多叉树的层序遍历结果，使用层序遍历组织为一层一层的结果；
        # 处理边界：
        if not root:
            return []
        # 使用FIFO队列实现层序遍历：
        q = collections.deque([root])
        res = []
        # 只要队列不为空，就一直进行遍历：
        while q:
            # 当前层个数：
            sz = len(q)
            # 记录当前层节点：
            current_level = []
            for _ in range(sz):
                # pop当前节点：
                cur = q.popleft()
                current_level.append(cur.val)
                # 加入其他节点：
                for child in cur.children:
                    q.append(child)
            res.append(current_level)
        # 返回：
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

