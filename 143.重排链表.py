#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30307
#
# [143] 重排链表
#
# https://leetcode.cn/problems/reorder-list/description/
#
# algorithms
# Medium (67.80%)
# Likes:    1652
# Dislikes: 0
# Total Accepted:    415.7K
# Total Submissions: 612.9K
# Testcase Example:  '[1,2,3,4]\n[1,2,3,4,5]'
#
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# 请将其重新排列后变为：
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 
# 示例 2：
# 
# 
# 
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
# 
# 
# 
# 提示：
# 
# 
# 链表的长度范围为 [1, 5 * 10^4]
# 1 <= node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 使用栈对链表元素进行存储:
        stk = []
        # 将链表反序存入栈中:
        p = head
        while p:
            stk.append(p)
            p = p.next
        # 双指针法:按照题给要求"穿针引线"重新连接链表:
        p = head
        while p:
            lastNode = stk.pop()
            next_node = p.next
            if p.next == lastNode or p == lastNode:
                lastNode.next = None
                break
            # 穿针引线:
            p.next = lastNode
            lastNode.next = next_node
            p = next_node



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

