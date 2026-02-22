#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30307
#
# [206] 反转链表
#
# https://leetcode.cn/problems/reverse-linked-list/description/
#
# algorithms
# Easy (76.37%)
# Likes:    4060
# Dislikes: 0
# Total Accepted:    2.7M
# Total Submissions: 3.5M
# Testcase Example:  '[1,2,3,4,5]\n[1,2]\n[]'
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 
# 
# 示例 2：
# 
# 输入：head = [1,2]
# 输出：[2,1]
# 
# 
# 示例 3：
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目范围是 [0, 5000]
# -5000 <= Node.val <= 5000
# 
# 
# 
# 
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
# 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # 迭代解法：遍历每一个节点并依次进行翻转：
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # 处理边界：
#         if not head:
#             return head
#         # 因为是单链表数据结构，所以需要定义三个指针：
#         pre = None
#         cur = head
#         nxt = head.next
#         # 遍历所有节点，依次进行翻转：
#         while cur:
#             # 翻转当前节点：
#             cur.next = pre
#             # 更新三个指针状态：
#             pre = cur
#             cur = nxt
#             if nxt:
#                 nxt = nxt.next
#         # 返回：
#         return pre

# 递归解法：
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 该函数【作用】：输入一个链表头节点，该函数将该链表翻转并返回新的头节点：
        # base case:
        if not head or not head.next:
            return head
        # 【当前职责】：因为当前函数输入为head，所有当前（本轮）的职责是1、输入头节点的下一个节点，反转链表并输出新的头节点；2、将head接到末尾；
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

