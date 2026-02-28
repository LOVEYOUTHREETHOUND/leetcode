#
# @lc app=leetcode.cn id=654 lang=python3
# @lcpr version=30400
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 分析：该题可以分为两步：1、找到值最大的作为根节点；2、递归构建所需要的二叉树；
        # 实现构造所需二叉树的build函数：
        # 函数定义：输入数组以及起始索引、结束索引，就构造所需要的二叉树并返回根节点：
        def build(nums: List[int], lo: int, hi: int) -> Optional[TreeNode]:
            # base case：
            if lo > hi:
                return None
            # 找到数组对应部分的最大值：
            max_val = float('-inf')
            max_index = -1
            for i in range(lo, hi + 1):
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_index = i
            # 根据找到的最大值构造根节点：
            root = TreeNode(max_val)
            # 递归构造左右孩子：
            root.left = build(nums, lo, max_index - 1)
            root.right = build(nums, max_index + 1, hi)
            return root
        # 调用构造函数：
        return build(nums, 0, len(nums) - 1)

# @lc code=end



#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#

